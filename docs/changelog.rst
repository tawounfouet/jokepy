Changelog
=========

Toutes les modifications notables de ce projet sont documentées dans ce fichier.

Le format est basé sur `Keep a Changelog <https://keepachangelog.com/en/1.0.0/>`_,
et ce projet adhère au `Versioning Sémantique <https://semver.org/spec/v2.0.0.html>`_.

[Non publié]
------------

Ajouté
~~~~~~
- Support des catégories de blagues
- CLI avec options avancées (``--list-categories``, ``--count``)
- Tests complets avec pytest et couverture
- Configuration des outils de développement (black, flake8, mypy, isort)
- Documentation complète avec Sphinx
- Workflow GitHub Actions pour CI/CD
- Pre-commit hooks pour la qualité du code
- Scripts d'installation automatisée
- Guide de contribution détaillé

Modifié
~~~~~~~
- Structure du projet modernisée avec ``pyproject.toml``
- API enrichie avec ``get_all_categories()`` et ``get_jokes_count()``
- CLI amélioré avec gestion des erreurs et emojis
- Documentation README complètement réécrite

[0.1.0] - 2025-07-28
--------------------

Ajouté
~~~~~~
- Générateur de blagues aléatoires basique
- Fonction ``get_random_joke()`` principale
- Interface en ligne de commande simple
- Structure de package moderne avec ``pyproject.toml``
- Tests de base avec pytest
- Configuration initiale du projet
- Licence MIT
- README basique

Technique
~~~~~~~~~
- Support Python 3.8+
- Installation via pip
- Point d'entrée CLI configuré
- Type hints basiques
