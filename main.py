from biblioteque import Bibliotheque

b = Bibliotheque()

ADMIN_PASSWORD = "admin123"   # tu peux changer le mot de passe ici

def menu_principal():
    print("\n=== MENU PRINCIPAL ===")
    print("1. Mode utilisateur")
    print("2. Mode administrateur")
    print("0. Quitter")

def menu_utilisateur():
    print("\n=== MENU UTILISATEUR ===")
    print("1. Emprunter une ressource")
    print("2. Rendre une ressource")
    print("3. Afficher les ressources")
    print("0. Retour")

def menu_admin():
    print("\n=== MENU ADMINISTRATEUR ===")
    print("1. Ajouter un utilisateur")
    print("2. Ajouter une ressource")
    print("3. Supprimer un utilisateur")
    print("4. Supprimer une ressource")
    print("5. Voir la liste des utilisateurs")
    print("6. Voir la liste des ressources")
    print("0. Retour")

# ------------------------------
# BOUCLE PRINCIPALE
# ------------------------------

while True:
    menu_principal()
    choix = input("Choisissez une option : ")

    # --- MODE UTILISATEUR ---
    if choix == "1":
        while True:
            menu_utilisateur()
            c = input("Choix : ")

            if c == "1":
                utilisateur = input("Nom de l'utilisateur : ")
                identifiant = int(input("ID de la ressource : "))
                try:
                    b.emprunter(utilisateur, identifiant)
                    print("Emprunt réussi.")
                except Exception as e:
                    print("Erreur :", e)

            elif c == "2":
                identifiant = int(input("ID de la ressource : "))
                try:
                    b.rendre(identifiant)
                    print("Ressource rendue.")
                except Exception as e:
                    print("Erreur :", e)

            elif c == "3":
                b.afficher()

            elif c == "0":
                break

            else:
                print("Choix invalide.")

    # --- MODE ADMIN ---
    elif choix == "2":
        mdp = input("Mot de passe admin : ")
        if mdp != ADMIN_PASSWORD:
            print("Mot de passe incorrect.")
            continue

        while True:
            menu_admin()
            c = input("Choix : ")

            if c == "1":
                nom = input("Nom de l'utilisateur : ")
                b.ajouter_utilisateur(nom)
                print(f"Utilisateur '{nom}' ajouté.")

            elif c == "2":
                identifiant = int(input("ID de la ressource : "))
                nom = input("Nom de la ressource : ")
                b.ajouter_ressource(identifiant, nom)
                print("Ressource ajoutée.")

            elif c == "3":
                nom = input("Nom de l'utilisateur à supprimer : ")
                if nom in b.utilisateurs:
                    b.utilisateurs.remove(nom)
                    b.sauvegarder()
                    print("Utilisateur supprimé.")
                else:
                    print("Utilisateur introuvable.")

            elif c == "4":
                identifiant = int(input("ID de la ressource à supprimer : "))
                if identifiant in b.ressources:
                    del b.ressources[identifiant]
                    b.sauvegarder()
                    print("Ressource supprimée.")
                else:
                    print("Ressource introuvable.")

            elif c == "5":
                print("\n--- Liste des utilisateurs ---")
                for u in b.utilisateurs:
                    print("-", u)

            elif c == "6":
                b.afficher()

            elif c == "0":
                break

            else:
                print("Choix invalide.")

    # --- QUITTER ---
    elif choix == "0":
        print("Au revoir.")
        break

    else:
        print("Choix invalide.")