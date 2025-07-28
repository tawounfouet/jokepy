#!/bin/bash

# Script d'installation rapide pour le développement
# Usage: ./setup_dev.sh

set -e  # Arrêter en cas d'erreur

echo "🚀 Configuration de l'environnement de développement pour jokepy..."

# Vérifier Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 n'est pas installé"
    exit 1
fi

echo "✅ Python trouvé: $(python3 --version)"

# Créer l'environnement virtuel
if [ ! -d "venv" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv venv
else
    echo "✅ Environnement virtuel déjà existant"
fi

# Activer l'environnement virtuel
echo "🔧 Activation de l'environnement virtuel..."
source venv/bin/activate

# Mettre à jour pip
echo "⬆️ Mise à jour de pip..."
pip install --upgrade pip

# Installer le package en mode développement
echo "📚 Installation du package en mode développement..."
pip install -e ".[dev,docs]"

# Configurer pre-commit
echo "🔐 Configuration de pre-commit..."
pre-commit install

# Lancer les tests pour vérifier
echo "🧪 Lancement des tests..."
pytest

echo ""
echo "✅ Configuration terminée !"
echo ""
echo "Pour activer l'environnement virtuel :"
echo "  source venv/bin/activate"
echo ""
echo "Commandes utiles :"
echo "  make test       # Lancer les tests"
echo "  make lint       # Vérifier le code"
echo "  make format     # Formatter le code"
echo "  jokepy          # Tester le CLI"
echo ""
