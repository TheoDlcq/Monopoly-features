# Pour installer le connecteur mysql, dans la fenetre terminal :
# python -m pip install --user mysql-connector-python
import mysql.connector

from Terrain import Terrain
from Gare import Gare
from Compagnie import Compagnie
from Quartier import Quartier

class DB:
    @classmethod
    def connexionBase(cls):
        mydb = mysql.connector.connect(
          host="localhost",
          user="monopoly_user",
          password="Azerty$",
          database = "monopoly"
        )
        return mydb

# TABLE PROPRIETES -------------------------------------------------------

# Liste des proprietes. donnée de classe
    __Proprietes = []
    __Quartiers = {}
    
    @classmethod
    def get_quartiers(cls):
        """Retourne les quartiers créés."""
        if not cls.__Quartiers:
            cls.__Quartiers = Quartier.creer_quartiers_standard()
        return cls.__Quartiers
    
    @classmethod
    def get_proprietes(cls):
        if cls.__Proprietes == []:
            # S'assurer que les quartiers sont créés
            quartiers = cls.get_quartiers()
            
            maConnexion = cls.connexionBase()
            monCurseur = maConnexion.cursor(dictionary=True)
 
            # Requête mise à jour pour récupérer les 6 loyers différenciés
            monCurseur.execute("""
                SELECT position,
                       nom,
                       type_propriete_code,
                       prix_achat,
                       loyer_base,
                       loyer_1_maison,
                       loyer_2_maisons,
                       loyer_3_maisons,
                       loyer_4_maisons,
                       loyer_hotel,
                       couleur,
                       prix_maison
                FROM   v_proprietes;""")
            mesResultats = monCurseur.fetchall()

            for r in mesResultats:
                p = None
                if r["type_propriete_code"] == "propriete":           
                    # Construire la liste des loyers différenciés
                    loyers = [
                        int(r["loyer_base"]),
                        int(r.get("loyer_1_maison", r["loyer_base"] * 5)),
                        int(r.get("loyer_2_maisons", r["loyer_base"] * 15)),
                        int(r.get("loyer_3_maisons", r["loyer_base"] * 45)),
                        int(r.get("loyer_4_maisons", r["loyer_base"] * 80)),
                        int(r.get("loyer_hotel", r["loyer_base"] * 100))
                    ]
                    
                    # Récupérer le quartier correspondant
                    quartier = quartiers.get(r["couleur"])
                    
                    # Créer un Terrain avec les loyers différenciés
                    p = Terrain(
                        r["nom"], 
                        int(r["position"]), 
                        int(r["prix_achat"]), 
                        loyers, 
                        r["couleur"],
                        quartier
                    )
                elif r["type_propriete_code"] == "gare":
                    # Créer une Gare
                    p = Gare(r["nom"], int(r["position"]))
                elif r["type_propriete_code"] == "compagnie":
                    # Créer une Compagnie
                    p = Compagnie(r["nom"], int(r["position"]))

                if p is not None:
                    cls.__Proprietes.append(p)
            
        return cls.__Proprietes
    
    @classmethod
    def reset(cls):
        """Réinitialise les données (utile pour les tests)."""
        cls.__Proprietes = []
        cls.__Quartiers = {}
        Quartier.reset_quartiers()
    
# test
if __name__ == '__main__':
    for p in DB.get_proprietes():
        print(f"{p.position} : ({p.couleur}) {p.nom} - prix d'achat : {p.prix}€")
        if isinstance(p, Terrain):
            print(f"   Loyers: {p.loyers}")
            if p.quartier:
                print(f"   Quartier: {p.quartier}")



        
