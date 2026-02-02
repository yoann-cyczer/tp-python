class Ressource:
    def __init__(self, identifiant, nom):
        self.id = identifiant
        self.nom = nom
        self.emprunte_par = None

    def est_disponible(self):
        return self.emprunte_par is None

    def emprunter(self, utilisateur):
        if not self.est_disponible():
            raise Exception("Ressource déjà empruntée.")
        self.emprunte_par = utilisateur

    def rendre(self):
        if self.est_disponible():
            raise Exception("Ressource non empruntée.")
        self.emprunte_par = None

    def __str__(self):
        statut = "Disponible" if self.est_disponible() else f"Empruntée par {self.emprunte_par}"
        return f"[{self.id}] {self.nom} - {statut}"