import json
import os
from ressource import Ressource

class Bibliotheque:
    def __init__(self, fichier="db.json"):
        self.fichier = fichier
        self.ressources = {}
        self.utilisateurs = set()
        self.charger()

    #   JSON 
    def sauvegarder(self):
        data = {
            "utilisateurs": list(self.utilisateurs),
            "ressources": [r.to_dict() for r in self.ressources.values()]
        }
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def charger(self):
        # Si le fichier n'existe pas  on crée un fichier JSON propre
        if not os.path.exists(self.fichier):
            self.sauvegarder()
            return

        # Si le fichier existe mais est vide ou cassé  on réinitialise
        try:
            with open(self.fichier, "r", encoding="utf-8") as f:
                data = json.load(f)
        except (json.JSONDecodeError, ValueError):
            data = {"utilisateurs": [], "ressources": []}
            self.sauvegarder()

        self.utilisateurs = set(data.get("utilisateurs", []))
        self.ressources = {
            r["id"]: Ressource.from_dict(r)
            for r in data.get("ressources", [])
        }

    #  LOGIQUE 
    def ajouter_ressource(self, identifiant, nom):
        if identifiant in self.ressources:
            raise Exception("Une ressource avec cet ID existe déjà.")
        self.ressources[identifiant] = Ressource(identifiant, nom)
        self.sauvegarder()

    def ajouter_utilisateur(self, nom):
        self.utilisateurs.add(nom)
        self.sauvegarder()

    def emprunter(self, nom, id_ressource):
        if nom not in self.utilisateurs:
            raise Exception("Utilisateur inconnu.")
        if id_ressource not in self.ressources:
            raise Exception("Ressource introuvable.")
        self.ressources[id_ressource].emprunter(nom)
        self.sauvegarder()

    def rendre(self, id_ressource):
        if id_ressource not in self.ressources:
            raise Exception("Ressource introuvable.")
        self.ressources[id_ressource].rendre()
        self.sauvegarder()

    def afficher(self):
        if not self.ressources:
            print("Aucune ressource enregistrée.")
            return

        for r in self.ressources.values():
            statut = "Disponible" if r.est_disponible() else f"Empruntée par {r.emprunte_par}"
            print(f"[{r.id}] {r.nom} - {statut}")