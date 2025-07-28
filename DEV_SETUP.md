# Guide de développement - Environnement virtuel

## 🔧 Configuration de l'environnement de développement

### 1. Créer un environnement virtuel

```bash
# Avec venv (recommandé)
python -m venv venv

# Ou avec virtualenv
virtualenv venv

# Ou avec conda
conda create -n jokepy-dev python=3.11
```

### 2. Activer l'environnement virtuel

```bash
# Sur macOS/Linux
source venv/bin/activate

# Sur Windows
venv\Scripts\activate

# Avec conda
conda activate jokepy-dev
```

### 3. Installer le package en mode développement

```bash
# Installation complète avec dépendances de dev
pip install -e ".[dev,docs]"

# Ou utiliser le Makefile
make dev-install
```

### 4. Vérifier l'installation

```bash
# Vérifier que le package est installé
pip list | grep jokepy

# Tester le CLI
jokepy --help

# Lancer les tests
pytest
```

### 5. Désactiver l'environnement

```bash
# Pour tous les environnements
deactivate

# Avec conda
conda deactivate
```

## 📋 Workflow complet de développement

```bash
# 1. Cloner le projet
git clone https://github.com/yourusername/jokepy.git
cd jokepy

# 2. Créer et activer l'environnement virtuel
python3.11 -m venv .venv
source .venv/bin/activate  # macOS/Linux

# 3. Installer en mode dev
make dev-install

# 4. Configurer pre-commit
pre-commit install

# 5. Développer et tester
make test
make lint
make format

# 6. Avant de committer
make lint  # Vérifications
git add .
git commit -m "feat: nouvelle fonctionnalité"
```

## 🚨 Pourquoi l'environnement virtuel est essentiel ?

1. **Isolation** : Évite les conflits entre projets
2. **Reproductibilité** : Garantit le même environnement partout
3. **Propreté** : Ne pollue pas l'installation Python système
4. **Sécurité** : Contrôle total sur les dépendances
5. **Collaboration** : Facilite le travail en équipe
