class Ressource:
    def __init__(self, identifiant, nom, emprunte_par=None):
        self.id = identifiant
        self.nom = nom
        self.emprunte_par = emprunte_par

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

    def to_dict(self):
        return {
            "id": self.id,
            "nom": self.nom,
            "emprunte_par": self.emprunte_par
        }

    @staticmethod
    def from_dict(data):
        return Ressource(data["id"], data["nom"], data["emprunte_par"])

    def __str__(self):
        statut = "Disponible" if self.est_disponible() else f"Empruntée par {self.emprunte_par}"
        return f"[{self.id}] {self.nom} - {statut}"