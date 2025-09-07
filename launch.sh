#!/bin/bash
echo "=== GPT Ultra Interactive - trhacknon ==="
echo

# Vérifie Python
if ! command -v python3 &> /dev/null
then
    echo "Python n'est pas installe. Installez-le avant."
    exit
fi

# Vérifie keys.txt
if [ ! -f keys.txt ]; then
    echo "Aucun fichier keys.txt trouve. Creez le fichier avec vos cles OpenAI, une par ligne."
    exit
fi

python3 gpt.py
