from Propriete import Propriete
from Case import Case
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Joueur import Joueur


class Gare(Propriete):
    """Gare - loyer selon nb de gares possédées"""
    
    LOYERS_GARES = {1: 25, 2: 50, 3: 100, 4: 200}
    
    def __init__(self, nom: str, position: int):
        Case.__init__(self, nom, position)
        self.prix = 200
        self.loyer_base = 25
        self.couleur = "gare"
        self.proprietaire = None
        self.nb_maisons = 0
        self._a_hotel = False
        self.prix_maison = 0
        self.hypothequee = False
    
    @property
    def a_hotel(self) -> bool:
        return self._a_hotel
    
    @a_hotel.setter
    def a_hotel(self, value: bool):
        self._a_hotel = value
    
    def calculer_loyer(self) -> int:
        if self.hypothequee or not self.proprietaire:
            return 0
        nb_gares = sum(1 for p in self.proprietaire.proprietes if isinstance(p, Gare))
        return self.LOYERS_GARES.get(nb_gares, 25)
    
    def peut_construire(self, joueur: 'Joueur') -> bool:
        return False
    
    def __str__(self):
        info = f"{self.nom} (Gare)"
        if self.proprietaire:
            info += f" - {self.proprietaire.nom}"
        if self.hypothequee:
            info += " [HYPOTHÉQUÉE]"
        return info
