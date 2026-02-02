from biblioteque import Bibliotheque
b = Bibliotheque()

# Ajout simple
b.ajouter_ressource(1, "Livre Python")
b.ajouter_ressource(2, "PC Portable")

b.ajouter_utilisateur("Alice")
b.ajouter_utilisateur("Bob")

print("\n--- Ressources ---")
b.afficher()

# Emprunt
print("\n--- Emprunt ---")
b.emprunter("Alice", 1)
b.afficher()

# Retour
print("\n--- Retour ---")
b.rendre(1)
b.afficher()