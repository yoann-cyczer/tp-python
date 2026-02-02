import json
import os
from ressource import Ressource

class Bibliotheque:
    def __init__(self, fichier="data.json"):
        self.fichier = fichier
        self.ressources = {}
        self.utilisateurs = set()
        self.charger()

    # ---------- JSON ----------
    def sauvegarder(self):
        data = {
            "utilisateurs": list(self.utilisateurs),
            "ressources": [r.to_dict() for r in self.ressources.values()]
        }
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def charger(self):
        if not os.path.exists(self.fichier):
            return
        with open(self.fichier, "r", encoding="utf-8") as f:
            data = json.load(f)

        self.utilisateurs = set(data.get("utilisateurs", []))
        self.ressources = {
            r["id"]: Ressource.from_dict(r)
            for r in data.get("ressources", [])
        }

    # ---------- LOGIQUE ----------
    def ajouter_ressource(self, identifiant, nom):
        self.ressources[identifiant] = Ressource(identifiant, nom)
        self.sauvegarder()

    def ajouter_utilisateur(self, nom):
        self.utilisateurs.add(nom)
        self.sauvegarder()

    def emprunter(self, nom, id_ressource):
        if nom not in self.utilisateurs:
            raise Exception("Utilisateur inconnu.")
        self.ressources[id_ressource].emprunter(nom)
        self.sauvegarder()

    def rendre(self, id_ressource):
        self.ressources[id_ressource].rendre()
        self.sauvegarder()

    def afficher(self):
        for r in self.ressources.values():
            print(r)