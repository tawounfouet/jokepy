Contribution
============

Merci de votre intérêt pour contribuer à jokepy ! 🎉

🚀 Mise en route rapide
----------------------

1. **Fork** le projet sur GitHub
2. **Clonez** votre fork localement
3. **Configurez** l'environnement de développement
4. **Créez** une branche pour votre contribution
5. **Développez** et testez vos modifications
6. **Soumettez** une Pull Request

📋 Guide détaillé
----------------

Configuration de l'environnement
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Cloner votre fork
   git clone https://github.com/VOTRE_USERNAME/jokepy.git
   cd jokepy

   # Créer un environnement virtuel
   python -m venv venv
   source venv/bin/activate  # macOS/Linux
   # venv\Scripts\activate   # Windows

   # Installer en mode développement
   pip install -e ".[dev,docs]"

   # Configurer pre-commit
   pre-commit install

   # Configurer le remote upstream
   git remote add upstream https://github.com/yourusername/jokepy.git

Workflow de développement
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Synchroniser avec upstream
   git fetch upstream
   git checkout main
   git merge upstream/main

   # Créer une branche pour votre feature
   git checkout -b feature/ma-nouvelle-fonctionnalite

   # Développer...
   # Tester...

   # Committer (pre-commit se lance automatiquement)
   git add .
   git commit -m "feat: ajouter nouvelle fonctionnalité"

   # Pousser vers votre fork
   git push origin feature/ma-nouvelle-fonctionnalite

🧪 Tests et qualité
------------------

Lancer les tests
~~~~~~~~~~~~~~~

.. code-block:: bash

   # Tests complets
   make test
   # ou
   pytest

   # Tests avec couverture
   pytest --cov=jokepy --cov-report=html

   # Tests sur plusieurs versions Python
   tox

Vérifications de qualité
~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   # Formatage automatique
   make format
   # ou
   black src tests
   isort src tests

   # Vérifications
   make lint
   # ou
   flake8 src tests
   isort --check-only src tests
   black --check src tests

   # Vérification des types
   make type-check
   # ou
   mypy src

📝 Types de contributions
------------------------

🐛 Correction de bugs
~~~~~~~~~~~~~~~~~~~

1. Vérifiez qu'un issue n'existe pas déjà
2. Créez un issue décrivant le bug
3. Créez une branche `fix/description-du-bug`
4. Ajoutez un test reproduisant le bug
5. Corrigez le bug
6. Vérifiez que le test passe
7. Soumettez une PR

✨ Nouvelles fonctionnalités
~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Créez un issue pour discuter de la fonctionnalité
2. Attendez l'approbation des mainteneurs
3. Créez une branche `feature/description-fonctionnalite`
4. Développez la fonctionnalité
5. Ajoutez des tests complets
6. Mettez à jour la documentation
7. Soumettez une PR

📚 Documentation
~~~~~~~~~~~~~~~

1. Améliorations du README
2. Ajouts à la documentation Sphinx
3. Exemples d'utilisation
4. Corrections de typos

🎭 Nouvelles blagues
~~~~~~~~~~~~~~~~~~

Pour ajouter de nouvelles blagues :

1. Modifiez ``src/jokepy/generator.py``
2. Ajoutez à ``JOKES`` et ``JOKES_BY_CATEGORY``
3. Respectez le style existant
4. Assurez-vous que les blagues sont appropriées
5. Ajoutez des tests si nécessaire

.. code-block:: python

   # Exemple d'ajout dans generator.py
   JOKES = [
       # ... blagues existantes ...
       "Votre nouvelle blague ici !",
   ]

   JOKES_BY_CATEGORY = {
       "sport": [
           # ... blagues existantes ...
           "Nouvelle blague de sport !",
       ],
       # ... autres catégories ...
   }

🔍 Processus de review
--------------------

Critères d'acceptation
~~~~~~~~~~~~~~~~~~~~~

- ✅ Tests passent sur toutes les versions Python supportées
- ✅ Couverture de code maintenue ou améliorée
- ✅ Code formaté avec Black et isort
- ✅ Pas d'erreurs de lint (flake8, mypy)
- ✅ Documentation mise à jour si nécessaire
- ✅ Commit messages suivent les conventions

Format des commit messages
~~~~~~~~~~~~~~~~~~~~~~~~~

Nous suivons la convention `Conventional Commits <https://www.conventionalcommits.org/>`_ :

.. code-block::

   type(scope): description

   [corps optionnel]

   [footer optionnel]

Types acceptés :

- ``feat``: nouvelle fonctionnalité
- ``fix``: correction de bug
- ``docs``: documentation uniquement
- ``style``: formatting, missing semi colons, etc
- ``refactor``: refactoring du code
- ``test``: ajout/modification de tests
- ``chore``: maintenance, dépendances, etc

Exemples :

.. code-block::

   feat(generator): ajouter support pour nouvelles catégories
   fix(cli): corriger affichage des caractères spéciaux
   docs(api): améliorer documentation de get_random_joke
   test(generator): ajouter tests pour cas limites

📋 Checklist PR
---------------

Avant de soumettre votre Pull Request, vérifiez :

- [ ] Tests ajoutés/modifiés et tous passent
- [ ] Documentation mise à jour
- [ ] Code formaté (``make format``)
- [ ] Pas d'erreurs de lint (``make lint``)
- [ ] Types vérifiés (``make type-check``)
- [ ] Commit messages suivent les conventions
- [ ] CHANGELOG.md mis à jour si nécessaire
- [ ] Description PR claire et détaillée

🏷️ Standards du code
-------------------

Style de code
~~~~~~~~~~~~

- Suivre PEP 8 (vérifié par flake8)
- Formatage automatique avec Black
- Tri des imports avec isort
- Ligne maximale : 88 caractères

Docstrings
~~~~~~~~~

Utiliser le format Google :

.. code-block:: python

   def ma_fonction(param1: str, param2: int = 0) -> str:
       """
       Description courte de la fonction.

       Description plus détaillée si nécessaire.

       Args:
           param1: Description du premier paramètre.
           param2: Description du second paramètre.

       Returns:
           Description de ce qui est retourné.

       Raises:
           ValueError: Quand param1 est vide.

       Examples:
           >>> ma_fonction("test", 42)
           "résultat"
       """
       # Implementation...

Type hints
~~~~~~~~~~

Toujours utiliser les type hints :

.. code-block:: python

   from typing import Dict, List, Optional

   def ma_fonction(
       items: List[str], 
       mapping: Dict[str, int], 
       optional_param: Optional[bool] = None
   ) -> str:
       # Implementation...

🚨 Guidelines spécifiques
------------------------

Blagues appropriées
~~~~~~~~~~~~~~~~~

- Humor familial uniquement
- Pas de contenu offensant
- Éviter les références datées
- Privilégier les jeux de mots universels

Tests robustes
~~~~~~~~~~~~~

- Tester les cas normaux ET les cas d'erreur
- Utiliser des fixtures pytest si nécessaire
- Tests déterministes (attention au random)
- Couverture > 90%

Performance
~~~~~~~~~~

- Éviter les opérations coûteuses inutiles
- Optimiser pour la fréquence d'usage commune
- Profiler si nécessaire avec cProfile

🤝 Communauté
------------

- Soyez respectueux et bienveillants
- Aidez les nouveaux contributeurs
- Participez aux discussions dans les issues
- Partagez vos cas d'usage

📞 Contact
---------

- **Issues GitHub** : Pour bugs et features
- **Discussions** : Pour questions générales
- **Email** : thomas.awounfouet@example.com

Merci de contribuer à jokepy ! 🎭✨
