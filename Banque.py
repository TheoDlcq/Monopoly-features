from Joueur import Joueur
from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Propriete import Propriete


class Banque(Joueur):
    """Banque du jeu - Singleton, ne lance pas les dés"""
    
    _instance: Optional['Banque'] = None
    
    def __init__(self, argent_initial: int = 100000000):
        super().__init__("Banque", argent_initial)
        self.en_prison = False
        self.est_en_faillite = False
    
    @classmethod
    def get_instance(cls) -> 'Banque':
        if cls._instance is None:
            cls._instance = Banque()
        return cls._instance
    
    @classmethod
    def reset_instance(cls) -> None:
        cls._instance = None
    
    def peut_lancer_des(self) -> bool:
        return False
    
    def est_humain(self) -> bool:
        return False
    
    def est_banque(self) -> bool:
        return True
    
    def deplacer(self, nombre_cases: int, plateau_taille: int = 40) -> bool:
        return False
    
    def aller_en_prison(self) -> None:
        pass
    
    def sortir_de_prison(self) -> None:
        pass
    
    def declarer_faillite(self, creancier: Optional['Joueur'] = None) -> None:
        pass
    
    def vendre_propriete(self, propriete: 'Propriete', acheteur: 'Joueur') -> bool:
        if propriete.proprietaire != self or acheteur.argent < propriete.prix:
            return False
        acheteur.payer(propriete.prix, self)
        propriete.proprietaire = acheteur
        if propriete in self.proprietes:
            self.proprietes.remove(propriete)
        acheteur.proprietes.append(propriete)
        return True
    
    def encaisser(self, montant: int, payeur: Optional['Joueur'] = None) -> None:
        self.recevoir(montant)
    
    def decaisser(self, montant: int, beneficiaire: 'Joueur') -> bool:
        if montant <= 0:
            return False
        self.argent -= montant
        beneficiaire.recevoir(montant)
        return True
    
    def initialiser_proprietes(self, proprietes: List['Propriete']) -> None:
        for propriete in proprietes:
            propriete.proprietaire = self
            if propriete not in self.proprietes:
                self.proprietes.append(propriete)
    
    def possede_quartier_complet(self, couleur: str) -> bool:
        return False
    
    def __str__(self) -> str:
        return f"Banque: {self.argent}€, {len(self.proprietes)} propriétés"
