Référence API
=============

Cette page contient la documentation complète de l'API jokepy.

Module principal
---------------

.. automodule:: jokepy
   :members:
   :undoc-members:
   :show-inheritance:

Module generator
---------------

.. automodule:: jokepy.generator
   :members:
   :undoc-members:
   :show-inheritance:

Fonctions principales
--------------------

get_random_joke
~~~~~~~~~~~~~~

.. autofunction:: jokepy.get_random_joke

Exemple d'utilisation :

.. code-block:: python

   from jokepy import get_random_joke
   
   # Blague aléatoire
   joke = get_random_joke()
   print(joke)
   
   # Blague d'une catégorie spécifique
   sport_joke = get_random_joke("sport")
   print(sport_joke)

get_all_categories
~~~~~~~~~~~~~~~~~

.. autofunction:: jokepy.get_all_categories

Exemple d'utilisation :

.. code-block:: python

   from jokepy import get_all_categories
   
   categories = get_all_categories()
   print("Catégories disponibles:", categories)
   # ['sport', 'travail', 'animaux', 'école']

get_jokes_count
~~~~~~~~~~~~~~

.. autofunction:: jokepy.get_jokes_count

Exemple d'utilisation :

.. code-block:: python

   from jokepy import get_jokes_count
   
   # Nombre total de blagues
   total = get_jokes_count()
   print(f"Total: {total} blagues")
   
   # Nombre de blagues par catégorie
   sport_count = get_jokes_count("sport")
   print(f"Sport: {sport_count} blagues")

Constantes
---------

JOKES
~~~~~

.. autodata:: jokepy.generator.JOKES
   :annotation: List[str]

Liste de toutes les blagues disponibles.

JOKES_BY_CATEGORY
~~~~~~~~~~~~~~~~

.. autodata:: jokepy.generator.JOKES_BY_CATEGORY
   :annotation: Dict[str, List[str]]

Dictionnaire organisant les blagues par catégorie.

Structure :

.. code-block:: python

   {
       "sport": ["blague sport 1", "blague sport 2"],
       "travail": ["blague travail 1", "blague travail 2"],
       "animaux": ["blague animaux 1", "blague animaux 2"],
       "école": ["blague école 1"]
   }

Exceptions
---------

ValueError
~~~~~~~~~

Levée quand une catégorie invalide est fournie aux fonctions ``get_random_joke()`` ou ``get_jokes_count()``.

.. code-block:: python

   try:
       joke = get_random_joke("categorie_inexistante")
   except ValueError as e:
       print(f"Erreur: {e}")
       # Affiche: "Catégorie 'categorie_inexistante' inconnue. Catégories disponibles: sport, travail, animaux, école"

Types
-----

Les annotations de type utilisées dans jokepy :

.. code-block:: python

   from typing import Dict, List, Optional
   
   # Type pour une blague
   Joke = str
   
   # Type pour une catégorie
   Category = str
   
   # Type pour le dictionnaire de blagues
   JokeDict = Dict[str, List[str]]

CLI Reference
------------

Point d'entrée principal
~~~~~~~~~~~~~~~~~~~~~~~

.. automodule:: jokepy.__main__
   :members:
   :undoc-members:

La fonction ``main()`` est le point d'entrée du CLI et gère tous les arguments de ligne de commande.

Arguments disponibles :

* ``-c, --category`` : Spécifier une catégorie
* ``--list-categories`` : Lister toutes les catégories
* ``--count`` : Afficher le nombre de blagues
* ``--version`` : Afficher la version
* ``--help`` : Afficher l'aide

Exemples complets
----------------

Script d'exemple complet
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   """
   Exemple complet d'utilisation de jokepy
   """
   
   from jokepy import get_random_joke, get_all_categories, get_jokes_count
   import random
   
   
   class JokeManager:
       """Gestionnaire de blagues avec fonctionnalités avancées."""
       
       def __init__(self):
           self.categories = get_all_categories()
           self.history = []
       
       def get_joke(self, category=None, avoid_repeats=True):
           """Obtient une blague en évitant les répétitions."""
           max_attempts = 10
           attempts = 0
           
           while attempts < max_attempts:
               joke = get_random_joke(category)
               if not avoid_repeats or joke not in self.history:
                   self.history.append(joke)
                   # Garder seulement les 50 dernières blagues
                   if len(self.history) > 50:
                       self.history.pop(0)
                   return joke
               attempts += 1
           
           # Si on n'arrive pas à éviter les répétitions, retourner quand même
           return get_random_joke(category)
       
       def get_stats(self):
           """Retourne des statistiques sur les blagues."""
           stats = {
               'total': get_jokes_count(),
               'by_category': {},
               'categories': len(self.categories)
           }
           
           for cat in self.categories:
               stats['by_category'][cat] = get_jokes_count(cat)
           
           return stats
       
       def random_category_joke(self):
           """Retourne une blague d'une catégorie aléatoire."""
           category = random.choice(self.categories)
           joke = self.get_joke(category)
           return joke, category
   
   
   def demo():
       """Démonstration des fonctionnalités."""
       manager = JokeManager()
       
       print("🎭 Démonstration de jokepy")
       print("=" * 40)
       
       # Statistiques
       stats = manager.get_stats()
       print(f"📊 Total: {stats['total']} blagues")
       print(f"📁 Catégories: {stats['categories']}")
       
       for cat, count in stats['by_category'].items():
           print(f"   • {cat}: {count} blagues")
       
       print()
       
       # Blagues par catégorie
       for category in manager.categories:
           joke = manager.get_joke(category)
           print(f"🏷️  {category.title()}: {joke}")
           print()
       
       # Blague aléatoire
       joke, cat = manager.random_category_joke()
       print(f"🎲 Aléatoire ({cat}): {joke}")
   
   
   if __name__ == "__main__":
       demo()

Intégration avec FastAPI
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: python

   from fastapi import FastAPI, HTTPException
   from pydantic import BaseModel
   from jokepy import get_random_joke, get_all_categories, get_jokes_count
   
   app = FastAPI(title="Jokepy API", description="API de blagues en français")
   
   class JokeResponse(BaseModel):
       joke: str
       category: str = None
   
   class StatsResponse(BaseModel):
       total: int
       categories: dict
   
   @app.get("/joke", response_model=JokeResponse)
   def random_joke():
       """Retourne une blague aléatoire."""
       return JokeResponse(joke=get_random_joke())
   
   @app.get("/joke/{category}", response_model=JokeResponse)
   def category_joke(category: str):
       """Retourne une blague d'une catégorie spécifique."""
       try:
           joke = get_random_joke(category)
           return JokeResponse(joke=joke, category=category)
       except ValueError:
           raise HTTPException(status_code=404, detail="Catégorie non trouvée")
   
   @app.get("/categories")
   def list_categories():
       """Liste toutes les catégories disponibles."""
       return get_all_categories()
   
   @app.get("/stats", response_model=StatsResponse)
   def get_stats():
       """Retourne des statistiques sur les blagues."""
       categories = get_all_categories()
       category_counts = {cat: get_jokes_count(cat) for cat in categories}
       
       return StatsResponse(
           total=get_jokes_count(),
           categories=category_counts
       )
