from Joueur import Joueur
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from Propriete import Propriete


class JoueurHumain(Joueur):
    """Joueur humain qui lance les dés"""
    
    def __init__(self, nom: str, argent_initial: int = 1500):
        super().__init__(nom, argent_initial)
    
    def peut_lancer_des(self) -> bool:
        return True
    
    def est_humain(self) -> bool:
        return True
    
    def demander_decision_achat(self, propriete: 'Propriete') -> bool:
        return self.argent >= propriete.prix
    
    def demander_decision_construction(self, propriete: 'Propriete') -> bool:
        from Terrain import Terrain
        if isinstance(propriete, Terrain):
            return self.argent >= propriete.prix_maison * 2
        return False
