from Propriete import Propriete
from Case import Case
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Joueur import Joueur
    from Quartier import Quartier
    from Monopoly import Monopoly


class Terrain(Propriete):
    """Propriété constructible avec loyers différenciés"""
    
    def __init__(self, nom: str, position: int, prix: int, loyers: List[int], couleur: str, quartier: Optional['Quartier'] = None):
        # Initialiser Case directement pour éviter le conflit avec a_hotel
        Case.__init__(self, nom, position)
        self.prix = prix
        self.loyer_base = loyers[0] if loyers else 0
        self.couleur = couleur
        self.proprietaire = None
        self.hypothequee = False
        
        self.loyers = loyers  # [nu, 1 maison, 2 maisons, 3 maisons, 4 maisons, hôtel]
        self.nb_maisons = 0
        self._a_hotel = False
        self.quartier: Optional['Quartier'] = quartier
        if quartier:
            quartier.ajouter_propriete(self)
    
    @property
    def a_hotel(self) -> bool:
        return self._a_hotel
    
    @a_hotel.setter
    def a_hotel(self, value: bool):
        self._a_hotel = value
    
    @property
    def prix_maison(self) -> int:
        if self.quartier:
            return self.quartier.prix_maison
        return 0
    
    def calculer_loyer(self) -> int:
        if self.hypothequee or not self.proprietaire:
            return 0
        if self.a_hotel:
            return self.loyers[5] if len(self.loyers) > 5 else self.loyers[-1]
        elif self.nb_maisons > 0:
            return self.loyers[self.nb_maisons] if len(self.loyers) > self.nb_maisons else self.loyers[-1]
        else:
            if self.quartier and self.quartier.posseder_quartier(self.proprietaire):
                return self.loyers[0] * 2
            return self.loyers[0]
    
    def peut_construire(self, joueur: 'Joueur') -> bool:
        if self.proprietaire != joueur or joueur.est_en_faillite:
            return False
        if joueur.argent < self.prix_maison:
            return False
        if not self.quartier or not self.quartier.posseder_quartier(joueur):
            return False
        if self.hypothequee or self.a_hotel:
            return False
        # Construction équilibrée
        if self.quartier:
            def nb_constructions(p):
                return 5 if p.a_hotel else p.nb_maisons
            nb_min = min([nb_constructions(p) for p in self.quartier.proprietes])
            if nb_constructions(self) > nb_min:
                return False
        return True
    
    def construire_maison(self, joueur: 'Joueur') -> bool:
        if not self.peut_construire(joueur) or self.nb_maisons >= 4:
            return False
        if joueur.argent < self.prix_maison:
            return False
        joueur.payer(self.prix_maison)
        self.nb_maisons += 1
        return True
    
    def construire_hotel(self, joueur: 'Joueur') -> bool:
        if not self.peut_construire(joueur) or self.nb_maisons != 4:
            return False
        if joueur.argent < self.prix_maison:
            return False
        joueur.payer(self.prix_maison)
        self.nb_maisons = 0
        self.a_hotel = True
        return True
    
    def vendre_maison(self) -> int:
        """Retourne moitié du prix"""
        if self.a_hotel:
            self.a_hotel = False
            self.nb_maisons = 4
            return self.prix_maison // 2
        if self.nb_maisons <= 0:
            return 0
        self.nb_maisons -= 1
        return self.prix_maison // 2
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        if self.proprietaire is None:
            if joueur.argent >= self.prix:
                decision = jeu.strategie.decider_achat(joueur, self)
                if decision:
                    joueur.acheter_propriete(self)
                    print(f"  → {joueur.nom} achète {self.nom} pour {self.prix}€")
                else:
                    print(f"  → {joueur.nom} refuse d'acheter {self.nom}")
            else:
                print(f"  → {joueur.nom} n'a pas assez d'argent pour {self.nom}")
        elif self.proprietaire != joueur:
            loyer = self.calculer_loyer()
            if loyer > 0:
                print(f"  → {joueur.nom} paie {loyer}€ de loyer à {self.proprietaire.nom}")
                joueur.payer(loyer, self.proprietaire)
                if hasattr(jeu, 'stats'):
                    jeu.stats.enregistrer_loyer(self, loyer)
    
    def __str__(self):
        info = f"{self.nom} ({self.couleur})"
        if self.proprietaire:
            info += f" - {self.proprietaire.nom}"
            if self.a_hotel:
                info += " [H]"
            elif self.nb_maisons > 0:
                info += f" [{self.nb_maisons}M]"
        return info
