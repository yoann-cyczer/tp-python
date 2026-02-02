from ressource import Ressource

class Bibliotheque:
    def __init__(self):
        self.ressources = {}
        self.utilisateurs = set()

    def ajouter_ressource(self, identifiant, nom):
        self.ressources[identifiant] = Ressource(identifiant, nom)

    def ajouter_utilisateur(self, nom):
        self.utilisateurs.add(nom)

    def emprunter(self, nom, id_ressource):
        if nom not in self.utilisateurs:
            raise Exception("Utilisateur inconnu.")
        self.ressources[id_ressource].emprunter(nom)

    def rendre(self, id_ressource):
        self.ressources[id_ressource].rendre()

    def afficher(self):
        for r in self.ressources.values():
            print(r)