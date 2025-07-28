Guide d'utilisation
==================

jokepy peut être utilisé de deux façons : comme module Python ou via l'interface en ligne de commande (CLI).

🐍 Utilisation comme module Python
----------------------------------

Import basique
~~~~~~~~~~~~~~

.. code-block:: python

   from jokepy import get_random_joke, get_all_categories, get_jokes_count

Génération de blagues aléatoires
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Blague aléatoire (toutes catégories)
   joke = get_random_joke()
   print(joke)
   # "Pourquoi les plongeurs plongent-ils toujours en arrière ?"

   # Blague d'une catégorie spécifique
   sport_joke = get_random_joke("sport")
   print(sport_joke)

Gestion des catégories
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Lister toutes les catégories disponibles
   categories = get_all_categories()
   print(categories)
   # ['sport', 'travail', 'animaux', 'école']

   # Compter les blagues
   total = get_jokes_count()
   print(f"Total: {total} blagues")

   # Compter par catégorie
   sport_count = get_jokes_count("sport")
   print(f"Sport: {sport_count} blagues")

Gestion des erreurs
~~~~~~~~~~~~~~~~~~

.. code-block:: python

   try:
       joke = get_random_joke("categorie_inexistante")
   except ValueError as e:
       print(f"Erreur: {e}")
       # Affiche les catégories disponibles

Exemple complet
~~~~~~~~~~~~~~

.. code-block:: python

   from jokepy import get_random_joke, get_all_categories, get_jokes_count

   def afficher_menu():
       """Affiche un menu interactif de blagues."""
       print("🎭 Générateur de blagues")
       print("=" * 30)
       
       categories = get_all_categories()
       
       print("Catégories disponibles:")
       for i, cat in enumerate(categories, 1):
           count = get_jokes_count(cat)
           print(f"  {i}. {cat.title()} ({count} blagues)")
       
       print(f"  0. Aléatoire ({get_jokes_count()} blagues)")
       print()
       
       choix = input("Choisissez une catégorie (0-{}): ".format(len(categories)))
       
       try:
           if choix == "0":
               joke = get_random_joke()
           else:
               category = categories[int(choix) - 1]
               joke = get_random_joke(category)
           
           print(f"\n🎭 {joke}\n")
       except (ValueError, IndexError):
           print("❌ Choix invalide")

   if __name__ == "__main__":
       afficher_menu()

💻 Utilisation en ligne de commande (CLI)
-----------------------------------------

Commandes de base
~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Afficher une blague aléatoire
   jokepy

   # Afficher l'aide
   jokepy --help

   # Afficher la version
   jokepy --version

Blagues par catégorie
~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Blague de sport
   jokepy -c sport
   jokepy --category sport

   # Blague de travail
   jokepy -c travail

   # Blague sur les animaux
   jokepy -c animaux

   # Blague d'école
   jokepy -c école

Gestion des catégories
~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Lister toutes les catégories
   jokepy --list-categories

   # Compter toutes les blagues
   jokepy --count

   # Compter les blagues d'une catégorie
   jokepy --count sport

Exemples pratiques
~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Script pour blague quotidienne
   #!/bin/bash
   echo "🌅 Blague du jour:"
   jokepy

   # Blague aléatoire dans un alias
   alias blague="jokepy"

   # Intégration dans un prompt
   echo "Astuce du jour: $(jokepy -c travail)"

🔧 Intégration dans d'autres projets
-----------------------------------

Serveur web simple
~~~~~~~~~~~~~~~~~

.. code-block:: python

   from flask import Flask, jsonify
   from jokepy import get_random_joke, get_all_categories

   app = Flask(__name__)

   @app.route('/joke')
   def random_joke():
       return jsonify({"joke": get_random_joke()})

   @app.route('/joke/<category>')
   def category_joke(category):
       try:
           joke = get_random_joke(category)
           return jsonify({"joke": joke, "category": category})
       except ValueError:
           return jsonify({"error": "Catégorie invalide"}), 400

   @app.route('/categories')
   def categories():
       return jsonify({"categories": get_all_categories()})

Bot Discord/Telegram
~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   # Exemple pour Discord.py
   import discord
   from jokepy import get_random_joke

   @bot.command()
   async def blague(ctx, category=None):
       try:
           joke = get_random_joke(category)
           await ctx.send(f"🎭 {joke}")
       except ValueError:
           await ctx.send("❌ Catégorie invalide")

🎨 Cas d'usage avancés
---------------------

Générateur de blagues personnalisées
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   import random
   from jokepy import get_random_joke

   def blague_avec_nom(nom):
       """Personnalise une blague avec un nom."""
       joke = get_random_joke()
       # Logique de personnalisation...
       return f"Salut {nom}! {joke}"

Système de favoris
~~~~~~~~~~~~~~~~

.. code-block:: python

   import json
   from jokepy import get_random_joke

   class FavoriteJokes:
       def __init__(self, filename="favorites.json"):
           self.filename = filename
           self.favorites = self._load()
       
       def _load(self):
           try:
               with open(self.filename, 'r') as f:
                   return json.load(f)
           except FileNotFoundError:
               return []
       
       def add_favorite(self, joke):
           if joke not in self.favorites:
               self.favorites.append(joke)
               self._save()
       
       def _save(self):
           with open(self.filename, 'w') as f:
               json.dump(self.favorites, f, indent=2)

🚨 Bonnes pratiques
------------------

1. **Gestion d'erreurs** : Toujours encapsuler dans try/except
2. **Catégories valides** : Vérifier avec ``get_all_categories()``
3. **Performance** : Mettre en cache les catégories si usage intensif
4. **Localisation** : Toutes les blagues sont en français
