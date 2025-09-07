import os
import sys
import platform
import openai

KEYS_FILE = "keys.txt"
HISTORY_FILE = "history.txt"

# Charger toutes les clés
if not os.path.exists(KEYS_FILE):
    print("Erreur : keys.txt introuvable.")
    exit(1)

with open(KEYS_FILE, "r") as f:
    keys = [line.strip() for line in f if line.strip()]

if not keys:
    print("Erreur : aucune clé valide dans keys.txt.")
    exit(1)

current_key_index = 0
openai.api_key = keys[current_key_index]

# Menu hacker style
def banner():
    print("="*50)
    print("=== GPT Ultra Interactive - trhacknon ===")
    print("="*50)
    print(f"Systeme : {platform.system()} | Cle active : #{current_key_index + 1}")
    print("Commandes : exit, switch_key, switch_model, history\n")

# Initial model
model = "gpt-4"

def switch_key():
    global current_key_index, keys
    current_key_index = (current_key_index + 1) % len(keys)
    openai.api_key = keys[current_key_index]
    print(f"\n[+] Cle active changee. Utilisation de la cle #{current_key_index + 1}\n")

def switch_model():
    global model
    model = "gpt-5" if model == "gpt-4" else "gpt-4"
    print(f"\n[+] Model change : {model}\n")

def chat(prompt):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        answer = response.choices[0].message.content.strip()
        # Sauvegarde dans l'historique
        with open(HISTORY_FILE, "a", encoding="utf-8") as f:
            f.write(f"Vous : {prompt}\nGPT ({model}) : {answer}\n\n")
        return answer
    except Exception as e:
        return f"Erreur GPT : {e}"

# Boucle principale
banner()
while True:
    prompt = input("Vous : ")
    cmd = prompt.lower()
    if cmd in ["exit", "quit"]:
        break
    elif cmd == "switch_key":
        switch_key()
        continue
    elif cmd == "switch_model":
        switch_model()
        continue
    elif cmd == "history":
        if os.path.exists(HISTORY_FILE):
            with open(HISTORY_FILE, "r", encoding="utf-8") as f:
                print("\n=== Historique ===\n")
                print(f.read())
                print("=== Fin historique ===\n")
        else:
            print("Historique vide.\n")
        continue
    answer = chat(prompt)
    print(f"GPT ({model}) : {answer}\n")
