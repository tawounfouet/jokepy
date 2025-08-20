# jokepy 🎭

[![Tests](https://github.com/tawounfouet/jokepy/workflows/Tests/badge.svg)](https://github.com/tawounfouet/jokepy/actions)
[![Coverage](https://img.shields.io/badge/coverage-98%25-brightgreen.svg)](https://github.com/tawounfouet/jokepy)
[![Code Quality](https://img.shields.io/badge/code%20style-black-black.svg)](https://github.com/psf/black)
[![PyPI version](https://badge.fury.io/py/jokepy.svg)](https://badge.fury.io/py/jokepy)
[![Python versions](https://img.shields.io/pypi/pyversions/jokepy.svg)](https://pypi.org/project/jokepy/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Mini package humour pour générer des blagues aléatoires en français.

## 🚀 Installation

### Depuis PyPI (recommandé)
```bash
pip install jokepy
```

### Depuis les sources
```bash
git clone https://github.com/tawounfouet/jokepy.git
cd jokepy
pip install -e .
```

## 📖 Utilisation

### En tant que module Python

```python
from jokepy import get_random_joke, get_all_categories, get_jokes_count

# Blague aléatoire
print(get_random_joke())
# "Pourquoi les plongeurs plongent-ils toujours en arrière ? Parce que sinon ils tombent dans le bateau !"

# Blague par catégorie
print(get_random_joke("sport"))

# Lister les catégories
print(get_all_categories())
# ['animaux', 'humour', 'sport', 'travail', 'école']

# Compter les blagues
print(get_jokes_count())  # Total
print(get_jokes_count("sport"))  # Par catégorie
```

### Interface en ligne de commande (CLI)

```bash
# Blague aléatoire
jokepy

# Plusieurs blagues
jokepy -n 3

# Blague par catégorie
jokepy -c sport
jokepy -c humour -n 2

# Lister les catégories
jokepy --list-categories

# Compter les blagues
jokepy --count
jokepy --count sport

# Aide
jokepy --help
```

## 🎯 Fonctionnalités

- ✅ Génération de blagues aléatoires
- ✅ Support des catégories (sport, travail, animaux, école, humour)
- ✅ Interface en ligne de commande intuitive avec options avancées
- ✅ Support pour plusieurs blagues à la fois (-n option)
- ✅ API Python simple et claire
- ✅ Type hints complets avec py.typed
- ✅ Tests exhaustifs (98% de couverture)
- ✅ Documentation complète
- ✅ Code formaté avec Black et validé avec flake8/mypy

## 🏗️ Développement

### Prérequis
- Python 3.8+
- Git

### Configuration initiale

```bash
# 1. Cloner le repository
git clone https://github.com/tawounfouet/jokepy.git
cd jokepy

# 2. Créer un environnement virtuel (ESSENTIEL !)
python -m venv venv

# 3. Activer l'environnement virtuel
# Sur macOS/Linux :
source venv/bin/activate
# Sur Windows :
# venv\Scripts\activate

# 4. Installer en mode développement
make dev-install
# ou manuellement :
pip install -e ".[dev,docs]"
pre-commit install
```

> **⚠️ Important** : Toujours utiliser un environnement virtuel pour éviter les conflits de dépendances !

### Tests

```bash
# Lancer tous les tests
make test
# ou
pytest

# Tests avec couverture
pytest --cov=jokepy

# Tests sur plusieurs versions Python
tox
```

### Outils de qualité

```bash
# Formatage du code
make format
# ou
black src tests
isort src tests

# Vérification du style
make lint
# ou
flake8 src tests

# Vérification des types
make type-check
# ou
mypy src
```

## 📁 Structure du projet

```
jokepy/
│
├── src/
│   └── jokepy/
│       ├── __init__.py          # API publique
│       ├── __main__.py          # Point d'entrée CLI
│       ├── generator.py         # Logique métier
│       └── py.typed            # Support des types
│
├── tests/
│   ├── __init__.py
│   └── test_generator.py       # Tests unitaires
│
├── docs/
│   ├── conf.py                 # Configuration Sphinx
│   ├── index.rst              # Page d'accueil
│   └── api.rst                # Documentation API
│
├── .github/
│   └── workflows/
│       ├── tests.yml           # CI/CD
│       └── publish.yml         # Publication PyPI
│
├── pyproject.toml              # Configuration moderne
├── tox.ini                     # Tests multi-versions
├── Makefile                    # Tâches automatisées
├── .pre-commit-config.yaml     # Hooks Git
├── .gitignore
├── LICENSE
├── CHANGELOG.md
└── README.md
```

## 🤝 Contribution

Les contributions sont les bienvenues ! Pour contribuer :

1. Fork le projet
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/amazing-feature`)
3. Committez vos changements (`git commit -m 'Add amazing feature'`)
4. Pushez vers la branche (`git push origin feature/amazing-feature`)
5. Ouvrez une Pull Request

### Guidelines

- Respectez les conventions PEP 8
- Ajoutez des tests pour vos nouvelles fonctionnalités
- Mettez à jour la documentation si nécessaire
- Vérifiez que tous les tests passent

## 📊 Documentation

La documentation complète est disponible sur [Read the Docs](https://jokepy.readthedocs.io) ou peut être construite localement :

```bash
# Construire la documentation
make docs
# ou
cd docs && make html

# Ouvrir la documentation
open docs/_build/html/index.html
```

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 🎉 Remerciements

- Merci à tous les contributeurs
- Inspiré par la joie de partager de l'humour en français
