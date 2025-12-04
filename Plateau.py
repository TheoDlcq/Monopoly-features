from Propriete import Propriete
from Terrain import Terrain
from Case import Case
from CaseSpeciale import CaseSpeciale
from Gare import Gare
from Compagnie import Compagnie 
from Global import TypeCase
from typing import List
from db import DB


class Plateau:
    """Plateau de 40 cases"""
    
    def __init__(self):
        self.cases: List['Case'] = []
        self._creer_plateau()
    
    def _creer_plateau(self):
        # Propriétés depuis la DB
        for p in DB.get_proprietes():
            self.cases.append(p)

        # Cases spéciales
        self.cases.append(CaseSpeciale("Départ", 0, TypeCase.DEPART, 200))
        self.cases.append(CaseSpeciale("Caisse de Communauté", 2, TypeCase.CAISSE_COMMUNAUTE))
        self.cases.append(CaseSpeciale("Impôts sur le revenu", 4, TypeCase.TAXE, 200))
        self.cases.append(CaseSpeciale("Chance", 7, TypeCase.CHANCE))
        self.cases.append(CaseSpeciale("Prison / Simple visite", 10, TypeCase.PRISON))
        self.cases.append(CaseSpeciale("Caisse de Communauté", 17, TypeCase.CAISSE_COMMUNAUTE))
        self.cases.append(CaseSpeciale("Parc Gratuit", 20, TypeCase.PARC_GRATUIT))
        self.cases.append(CaseSpeciale("Chance", 22, TypeCase.CHANCE))
        self.cases.append(CaseSpeciale("Allez en prison", 30, TypeCase.ALLER_PRISON))
        self.cases.append(CaseSpeciale("Caisse de Communauté", 33, TypeCase.CAISSE_COMMUNAUTE))
        self.cases.append(CaseSpeciale("Chance", 36, TypeCase.CHANCE))
        self.cases.append(CaseSpeciale("Taxe de luxe", 38, TypeCase.TAXE, 100))
    
        self.cases.sort(key=lambda x: x.position)
    
    def get_case(self, position: int) -> Case:
        return self.cases[position % len(self.cases)]
    
    def afficher_plateau(self):
        print("\n" + "="*60)
        print("PLATEAU DE MONOPOLY")
        print("="*60)
        for case in self.cases:
            info = f"{case.position:2}. {case.nom}"
            if isinstance(case, Terrain):
                info += f" ({case.couleur})"
                if case.quartier:
                    info += f" - Maison: {case.prix_maison}€"
            print(info)

    
if __name__ == "__main__":
    plateau = Plateau()
    assert len(plateau.cases) == 40, "Le plateau doit avoir 40 cases"
    assert isinstance(plateau.cases[0], CaseSpeciale), "La case 0 est la case de départ"
    assert isinstance(plateau.cases[5], Gare), "La case 5 est une gare"
    assert plateau.cases[39].nom == "Rue de la Paix", "La case 39 est Rue de la Paix"
    
    for case in plateau.cases:
        if isinstance(case, Terrain):
            assert hasattr(case, 'loyers'), f"Le terrain {case.nom} doit avoir des loyers"
            assert len(case.loyers) == 6, f"Le terrain {case.nom} doit avoir 6 loyers"
            assert case.quartier is not None, f"Le terrain {case.nom} doit appartenir à un quartier"
            print(f"Terrain {case.nom}: loyers = {case.loyers}")