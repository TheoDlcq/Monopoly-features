from typing import List, Optional, TYPE_CHECKING

if TYPE_CHECKING:
    from Terrain import Terrain
    from Joueur import Joueur


class Quartier:
    """Groupe de propriétés de même couleur"""
    
    _quartiers: dict[str, 'Quartier'] = {}
    
    def __init__(self, couleur: str, prix_maison: int):
        self.couleur = couleur
        self.prix_maison = prix_maison
        self.proprietes: List['Terrain'] = []
        Quartier._quartiers[couleur] = self
    
    def ajouter_propriete(self, propriete: 'Terrain') -> None:
        if propriete not in self.proprietes:
            self.proprietes.append(propriete)
            propriete.quartier = self
    
    def posseder_quartier(self, joueur: 'Joueur') -> bool:
        """Retourne True si joueur possède toutes les propriétés"""
        if not self.proprietes:
            return False
        for propriete in self.proprietes:
            if propriete.proprietaire != joueur:
                return False
        return True
    
    def get_nb_proprietes(self) -> int:
        return len(self.proprietes)
    
    @classmethod
    def get_quartier(cls, couleur: str) -> Optional['Quartier']:
        return cls._quartiers.get(couleur)
    
    @classmethod
    def get_tous_quartiers(cls) -> dict[str, 'Quartier']:
        return cls._quartiers
    
    @classmethod
    def reset_quartiers(cls) -> None:
        cls._quartiers = {}
    
    @classmethod
    def creer_quartiers_standard(cls) -> dict[str, 'Quartier']:
        """Crée les 8 quartiers du Monopoly"""
        cls.reset_quartiers()
        quartiers_config = {
            "marron": 50, "bleu_clair": 50, "rose": 100, "orange": 100,
            "rouge": 150, "jaune": 150, "vert": 200, "bleu_fonce": 200
        }
        for couleur, prix_maison in quartiers_config.items():
            Quartier(couleur, prix_maison)
        return cls._quartiers
    
    def __str__(self) -> str:
        return f"Quartier {self.couleur} ({len(self.proprietes)} propriétés, maison: {self.prix_maison}€)"
    
    def __repr__(self) -> str:
        return f"Quartier('{self.couleur}', {self.prix_maison})"
