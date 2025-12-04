from Propriete import Propriete
from Case import Case
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Joueur import Joueur
    from Monopoly import Monopoly


class Compagnie(Propriete):
    """Compagnie - loyer = dés × (4 ou 10)"""
    
    def __init__(self, nom: str, position: int):
        Case.__init__(self, nom, position)
        self.prix = 150
        self.loyer_base = 0
        self.couleur = "compagnie"
        self.proprietaire = None
        self.nb_maisons = 0
        self._a_hotel = False
        self.prix_maison = 0
        self.hypothequee = False
        self.dernier_lancer_des = 0
    
    @property
    def a_hotel(self) -> bool:
        return self._a_hotel
    
    @a_hotel.setter
    def a_hotel(self, value: bool):
        self._a_hotel = value
    
    def calculer_loyer(self) -> int:
        if self.hypothequee or not self.proprietaire:
            return 0
        nb_compagnies = sum(1 for p in self.proprietaire.proprietes if isinstance(p, Compagnie))
        multiplicateur = 4 if nb_compagnies == 1 else 10
        return multiplicateur * self.dernier_lancer_des
    
    def action(self, joueur: 'Joueur', jeu: 'Monopoly'):
        self.dernier_lancer_des = jeu.dernier_total_des
        super().action(joueur, jeu)
    
    def peut_construire(self, joueur: 'Joueur') -> bool:
        return False
    
    def __str__(self):
        info = f"{self.nom} (Compagnie)"
        if self.proprietaire:
            info += f" - {self.proprietaire.nom}"
        if self.hypothequee:
            info += " [HYPOTHÉQUÉE]"
        return info
