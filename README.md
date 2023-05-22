# 🎮🧭🏠 Pygamon - Aventure

## Description

Pygamon - Aventure est un jeu 2D simple écrit en Python avec l'utilisation de la bibliothèque Pygame. <br>

## **Le jeu a été créé principalement pour découvrir le fonctionnement des jeux 2D.**

## Code Structure

- Le script principal (`main.py`) initialise le jeu et le lance.
- Le fichier `game.py` contient la classe `Game` qui gère l'état du jeu, la carte, le joueur, les mouvements du joueur et les collisions.
- Le fichier `player.py` contient la classe `Player` qui gère l'apparence du joueur, le mouvement et les collisions.

## Comment lancer le jeu

1. Assurez-vous d'avoir Python 3.x installé sur votre machine.
2. Installez Pygame, PyTMX, et PyScroll si vous ne l'avez pas déjà fait :
    ```bash
    pip install pygame pytmx pyscroll
    ```
3. Clonez ce dépôt sur votre machine locale.
4. Exécutez `main.py` pour lancer le jeu.

## Structure du code

Le jeu est composé de trois fichiers Python principaux : `main.py`, `game.py`, et `player.py`.

### main.py

`main.py` est le point d'entrée du jeu. Il importe Pygame et la classe Game, initialise Pygame, crée une instance de Game, et lance le jeu.

### game.py

`game.py` contient la logique principale du jeu. La classe `Game` gère l'état du jeu, notamment la carte du jeu, la position du joueur et les collisions. Elle utilise les bibliothèques PyTMX et PyScroll pour charger et dessiner la carte à partir d'un fichier .tmx, et la classe `Player` pour gérer le joueur.

La classe `Game` contient plusieurs méthodes pour gérer les différentes parties du jeu :

- `__init__` : initialise l'écran de jeu, charge la carte du monde, crée le joueur, et prépare les collisions.
- `switch_house` et `switch_world` : ces méthodes sont utilisées pour passer d'un monde à un autre (du monde extérieur à l'intérieur d'une maison, par exemple).
- `update` : cette méthode est appelée à chaque tour de la boucle principale du jeu. Elle vérifie les collisions, met à jour la position du joueur, et change de monde si nécessaire.
- `run` : cette méthode contient la boucle principale du jeu, qui gère l'entrée du joueur et rafraîchit l'écran.
- `handle_input` : cette méthode est appelée à chaque tour de la boucle principale pour gérer les entrées du joueur.

### player.py

`player.py` contient la classe `Player`, qui gère le personnage du joueur. Le joueur a une position, une vitesse, une apparence (qui est gérée par une sprite sheet), et des méthodes pour se déplacer dans les quatre directions.

## Auteur

Ce jeu a été créé par [ranki].
