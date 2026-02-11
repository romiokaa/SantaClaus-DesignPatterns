# Santa Claus Gift System 🎅

Projet d'implémentation de Design Patterns en Python.

## Patterns utilisés :
* **Facade** : `SantaClausFacade` centralise la logique.
* **Factory** : `GiftFactory` pour la création des produits.
* **Decorator** : Pour l'emballage (Papier, Ruban, Message).
* **Observer** : Le `Workshop` notifie les `Elfes`.
* **Strategy** : Différents modes de livraison (Drone, Sleigh, Reindeer).
* **Command** : `GiftOrderCommand` pour encapsuler les commandes.

## Lancement
```bash
python main.py
