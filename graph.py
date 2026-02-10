import customtkinter as ctk
from biblioteque import Bibliotheque

# ============================
#   CONFIGURATION
# ============================

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

b = Bibliotheque()
ADMIN_PASSWORD = "admin123"


# ============================
#   FENÊTRE PRINCIPALE
# ============================

app = ctk.CTk()
app.title("Gestion de Bibliothèque")
app.geometry("500x450")


# ============================
#   FONCTIONS UTILISATEUR
# ============================

def fenetre_emprunter():
    win = ctk.CTkToplevel(app)
    win.title("Emprunter une ressource")
    win.geometry("350x250")

    ctk.CTkLabel(win, text="Nom utilisateur :").pack(pady=5)
    entry_user = ctk.CTkEntry(win)
    entry_user.pack()

    ctk.CTkLabel(win, text="ID ressource :").pack(pady=5)
    entry_id = ctk.CTkEntry(win)
    entry_id.pack()

    def valider():
        try:
            utilisateur = entry_user.get()
            identifiant = entry_id.get()
            b.emprunter(utilisateur, identifiant)
            ctk.CTkLabel(win, text="Emprunt réussi !", text_color="green").pack(pady=10)
        except Exception as e:
            ctk.CTkLabel(win, text=f"Erreur : {e}", text_color="red").pack(pady=10)

    ctk.CTkButton(win, text="Valider", command=valider).pack(pady=15)


def fenetre_rendre():
    win = ctk.CTkToplevel(app)
    win.title("Rendre une ressource")
    win.geometry("350x200")

    ctk.CTkLabel(win, text="ID ressource :").pack(pady=5)
    entry_id = ctk.CTkEntry(win)
    entry_id.pack()

    def valider():
        try:
            identifiant = entry_id.get()
            b.rendre(identifiant)
            ctk.CTkLabel(win, text="Ressource rendue !", text_color="green").pack(pady=10)
        except Exception as e:
            ctk.CTkLabel(win, text=f"Erreur : {e}", text_color="red").pack(pady=10)

    ctk.CTkButton(win, text="Valider", command=valider).pack(pady=15)


def fenetre_afficher():
    win = ctk.CTkToplevel(app)
    win.title("Liste des ressources")
    win.geometry("500x400")

    text = ctk.CTkTextbox(win, width=480, height=350)
    text.pack(pady=10)

    for identifiant, data in b.ressources.items():
        etat = "Disponible" if data["disponible"] else f"Emprunté par {data['emprunteur']}"
        text.insert("end", f"{identifiant} : {data['nom']} — {etat}\n")


# ============================
#   FONCTIONS ADMIN
# ============================

def fenetre_admin():
    win = ctk.CTkToplevel(app)
    win.title("Mode Administrateur")
    win.geometry("400x500")

    def check_password():
        if entry_mdp.get() != ADMIN_PASSWORD:
            lbl_result.configure(text="Mot de passe incorrect", text_color="red")
        else:
            lbl_result.configure(text="Accès autorisé", text_color="green")
            afficher_menu_admin()

    ctk.CTkLabel(win, text="Mot de passe admin :").pack(pady=5)
    entry_mdp = ctk.CTkEntry(win, show="*")
    entry_mdp.pack()

    ctk.CTkButton(win, text="Valider", command=check_password).pack(pady=10)
    lbl_result = ctk.CTkLabel(win, text="")
    lbl_result.pack()

    def afficher_menu_admin():
        frame = ctk.CTkFrame(win)
        frame.pack(pady=20)

        ctk.CTkButton(frame, text="Ajouter utilisateur", width=250,
                      command=fenetre_ajout_user).pack(pady=5)
        ctk.CTkButton(frame, text="Ajouter ressource", width=250,
                      command=fenetre_ajout_ressource).pack(pady=5)
        ctk.CTkButton(frame, text="Supprimer utilisateur", width=250,
                      command=fenetre_suppr_user).pack(pady=5)
        ctk.CTkButton(frame, text="Supprimer ressource", width=250,
                      command=fenetre_suppr_ressource).pack(pady=5)
        ctk.CTkButton(frame, text="Voir utilisateurs", width=250,
                      command=fenetre_liste_users).pack(pady=5)
        ctk.CTkButton(frame, text="Voir ressources", width=250,
                      command=fenetre_afficher).pack(pady=5)


def fenetre_ajout_user():
    win = ctk.CTkToplevel(app)
    win.title("Ajouter utilisateur")
    win.geometry("350x200")

    ctk.CTkLabel(win, text="Nom utilisateur :").pack(pady=5)
    entry = ctk.CTkEntry(win)
    entry.pack()

    def valider():
        nom = entry.get()
        b.ajouter_utilisateur(nom)
        ctk.CTkLabel(win, text="Utilisateur ajouté !", text_color="green").pack(pady=10)

    ctk.CTkButton(win, text="Valider", command=valider).pack(pady=10)


def fenetre_ajout_ressource():
    win = ctk.CTkToplevel(app)
    win.title("Ajouter ressource")
    win.geometry("350x250")

    ctk.CTkLabel(win, text="ID ressource :").pack(pady=5)
    entry_id = ctk.CTkEntry(win)
    entry_id.pack()

    ctk.CTkLabel(win, text="Nom ressource :").pack(pady=5)
    entry_nom = ctk.CTkEntry(win)
    entry_nom.pack()

    def valider():
        identifiant = entry_id.get()
        nom = entry_nom.get()
        b.ajouter_ressource(identifiant, nom)
        ctk.CTkLabel(win, text="Ressource ajoutée !", text_color="green").pack(pady=10)

    ctk.CTkButton(win, text="Valider", command=valider).pack(pady=10)


def fenetre_suppr_user():
    win = ctk.CTkToplevel(app)
    win.title("Supprimer utilisateur")
    win.geometry("350x200")

    ctk.CTkLabel(win, text="Nom utilisateur :").pack(pady=5)
    entry = ctk.CTkEntry(win)
    entry.pack()

    def valider():
        nom = entry.get()
        if nom in b.utilisateurs:
            b.utilisateurs.remove(nom)
            b.sauvegarder()
            ctk.CTkLabel(win, text="Utilisateur supprimé !", text_color="green").pack(pady=10)
        else:
            ctk.CTkLabel(win, text="Utilisateur introuvable", text_color="red").pack(pady=10)

    ctk.CTkButton(win, text="Supprimer", command=valider).pack(pady=10)


def fenetre_suppr_ressource():
    win = ctk.CTkToplevel(app)
    win.title("Supprimer ressource")
    win.geometry("350x200")

    ctk.CTkLabel(win, text="ID ressource :").pack(pady=5)
    entry = ctk.CTkEntry(win)
    entry.pack()

    def valider():
        identifiant = entry.get()
        if identifiant in b.ressources:
            del b.ressources[identifiant]
            b.sauvegarder()
            ctk.CTkLabel(win, text="Ressource supprimée !", text_color="green").pack(pady=10)
        else:
            ctk.CTkLabel(win, text="Ressource introuvable", text_color="red").pack(pady=10)

    ctk.CTkButton(win, text="Supprimer", command=valider).pack(pady=10)


def fenetre_liste_users():
    win = ctk.CTkToplevel(app)
    win.title("Liste des utilisateurs")
    win.geometry("400x300")

    text = ctk.CTkTextbox(win, width=380, height=250)
    text.pack(pady=10)

    for u in b.utilisateurs:
        text.insert("end", f"- {u}\n")


# ============================
#   MENU PRINCIPAL (GUI)
# ============================

ctk.CTkLabel(app, text="Gestion de Bibliothèque", font=("Arial", 22)).pack(pady=20)

ctk.CTkButton(app, text="Mode utilisateur", width=250,
              command=lambda: fenetre_utilisateur()).pack(pady=10)

ctk.CTkButton(app, text="Mode administrateur", width=250,
              command=fenetre_admin).pack(pady=10)

ctk.CTkButton(app, text="Quitter", width=250,
              command=app.destroy).pack(pady=20)


def fenetre_utilisateur():
    win = ctk.CTkToplevel(app)
    win.title("Mode Utilisateur")
    win.geometry("400x350")

    ctk.CTkButton(win, text="Emprunter une ressource", width=250,
                  command=fenetre_emprunter).pack(pady=10)

    ctk.CTkButton(win, text="Rendre une ressource", width=250,
                  command=fenetre_rendre).pack(pady=10)

    ctk.CTkButton(win, text="Afficher les ressources", width=250,
                  command=fenetre_afficher).pack(pady=10)


# ============================
#   LANCEMENT
# ============================

app.mainloop()