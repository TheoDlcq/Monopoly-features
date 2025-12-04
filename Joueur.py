from Global import *
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Propriete import Propriete
    from Quartier import Quartier


class Joueur:
    """Représente un joueur de Monopoly"""
    
    def __init__(self, nom: str, argent_initial: int = 1500):
        self.nom = nom
        self.argent = argent_initial
        self.position = 0
        self.proprietes: List['Propriete'] = []
        self.en_prison = False
        self.tours_en_prison = 0
        self.cartes_liberte = 0
        self.est_en_faillite = False
        self.doubles_consecutifs = 0
    
    def deplacer(self, nombre_cases: int, plateau_taille: int = 40):
        ancienne_position = self.position
        self.position = (self.position + nombre_cases) % plateau_taille
        if ancienne_position > self.position and ancienne_position != 0:
            self.recevoir(ARGENT_PASSAGE_DEPART)
            print(f"  → {self.nom} passe par la case Départ (+{ARGENT_PASSAGE_DEPART}€)")
            return True
        return False
    
    def aller_en_prison(self):
        self.en_prison = True
        self.tours_en_prison = 0
        self.position = 10
        self.doubles_consecutifs = 0
    
    def sortir_de_prison(self):
        self.en_prison = False
        self.tours_en_prison = 0

    def payer(self, montant: int, beneficiaire: Optional['Joueur'] = None):
        if montant <= 0:
            return
        if self.argent >= montant:
            self.argent -= montant
            if beneficiaire:
                beneficiaire.recevoir(montant)
        else:
            print(f"    {self.nom} n'a pas assez d'argent! (a {self.argent}€, doit {montant}€)")
            self.declarer_faillite(beneficiaire)
    
    def recevoir(self, montant: int):
        if montant > 0:
            self.argent += montant
    
    def acheter_propriete(self, propriete: 'Propriete') -> bool:
        if propriete.proprietaire is not None or self.argent < propriete.prix:
            return False
        self.argent -= propriete.prix
        propriete.proprietaire = self
        self.proprietes.append(propriete)
        return True
    
    def possede_quartier_complet(self, couleur: str) -> bool:
        if couleur in ["gare", "compagnie"]:
            return False
        from Quartier import Quartier
        quartier = Quartier.get_quartier(couleur)
        if quartier:
            return quartier.posseder_quartier(self)
        # Fallback
        nb_par_couleur = {
            "marron": 2, "bleu_clair": 3, "rose": 3, "orange": 3, "rouge": 3,
            "jaune": 3, "vert": 3, "bleu_fonce": 2
        }
        props = [p for p in self.proprietes if hasattr(p, 'couleur') and p.couleur == couleur]
        return len(props) >= nb_par_couleur.get(couleur, 3)

    def declarer_faillite(self, creancier: Optional['Joueur'] = None):
        print(f"{self.nom} fait FAILLITE!")
        self.est_en_faillite = True
        for propriete in self.proprietes:
            if creancier:
                propriete.proprietaire = creancier
                creancier.proprietes.append(propriete)
                print(f"     → {propriete.nom} transférée à {creancier.nom}")
            else:
                from Banque import Banque
                banque = Banque.get_instance()
                propriete.proprietaire = banque
                banque.proprietes.append(propriete)
                from Terrain import Terrain
                if isinstance(propriete, Terrain):
                    propriete.nb_maisons = 0
                propriete.hypothequee = False
        self.proprietes.clear()
        self.argent = 0
    
    def calculer_valeur_totale(self) -> int:
        from Terrain import Terrain
        valeur = self.argent
        for prop in self.proprietes:
            valeur += prop.prix
            if isinstance(prop, Terrain):
                valeur += prop.nb_maisons * prop.prix_maison
        return valeur
    
    def peut_lancer_des(self) -> bool:
        return True
    
    def est_humain(self) -> bool:
        return False
    
    def est_banque(self) -> bool:
        return False
    
    def __str__(self):
        status = f"{self.nom}: {self.argent}€"
        if self.en_prison:
            status += " [PRISON]"
        if self.est_en_faillite:
            status += " [FAILLITE]"
        return status
