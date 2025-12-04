# Monopoly

Jeu de Monopoly en Python avec base de données MySQL.

## Structure

### Classes principales
- **Joueur** - Joueur de base avec gestion argent, déplacements, prison
- **JoueurHumain** - Joueur humain (hérite de Joueur)
- **Banque** - Singleton gérant les transactions (hérite de Joueur)

### Propriétés
- **Propriete** - Classe parente des propriétés achetables
- **Terrain** - Propriété constructible avec loyers différenciés (6 valeurs)
- **Gare** - Loyer selon le nombre de gares possédées
- **Compagnie** - Loyer = dés × multiplicateur

### Organisation
- **Quartier** - Groupe les terrains par couleur, définit le prix des maisons
- **Plateau** - 40 cases (propriétés + cases spéciales)
- **Monopoly** - Moteur de jeu principal

## Base de données

```bash
# Installer le connecteur
pip install mysql-connector-python

# Exécuter le script SQL pour les loyers différenciés
mysql -u monopoly_user -p monopoly < update_loyers.sql
```

## Lancer une partie

```python
from Monopoly import Monopoly

jeu = Monopoly(["Alice", "Bob"])
jeu.jouer_partie()
```

## IA disponibles
- `IAAgressive` - Achète tout, construit max
- `IAConservative` - Prudente avec l'argent
- `IAStrategique` - Équilibrée