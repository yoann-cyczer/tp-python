class Ressource:
    def __init__(self, identifiant, nom, emprunte_par=None):
        # Initialise une ressource avec un identifiant, un nom
        # et éventuellement l'utilisateur qui l'a empruntée.
        self.id = identifiant
        self.nom = nom
        self.emprunte_par = emprunte_par

    def est_disponible(self):
        # Indique si la ressource n'est pas empruntée.
        return self.emprunte_par is None

    def emprunter(self, utilisateur):
        # Associe la ressource à un utilisateur si elle est libre.
        if not self.est_disponible():
            raise Exception("Ressource déjà empruntée.")
        self.emprunte_par = utilisateur

    def rendre(self):
        # Libère la ressource si elle était empruntée.
        if self.est_disponible():
            raise Exception("Ressource non empruntée.")
        self.emprunte_par = None

    def to_dict(self):
        # Convertit l'objet en dictionnaire pour stockage JSON.
        return {
            "id": self.id,
            "nom": self.nom,
            "emprunte_par": self.emprunte_par
        }

    @staticmethod
    def from_dict(data):
        # Reconstruit une ressource à partir d'un dictionnaire.
        return Ressource(data["id"], data["nom"], data["emprunte_par"])