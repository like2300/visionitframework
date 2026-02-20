#!/bin/bash
# Lancer l'application desktop test_final

cd "$(dirname "$0")"

echo "=============================================="
echo "🚀 Lancement de test_final"
echo "=============================================="

# Activer l'environnement virtuel
if [ -d "../venv" ]; then
    source ../venv/bin/activate
elif [ -d "venv" ]; then
    source venv/bin/activate
fi

# Vérifier les dépendances
echo "⏳ Vérification des dépendances..."
pip install -q -r package.txt

# Lancer l'application
echo ""
echo "🖥️  Ouverture de la fenêtre desktop..."
echo ""
python main.py
