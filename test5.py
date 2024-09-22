def demander_coefficient(note_num):
    """Demande à l'utilisateur si une note est coefficientée, et retourne le coefficient."""
    while True:
        try:
            coefficient = int(input(f"Quel est le coefficient de la note {note_num} (1, 2 ou 3) ?: "))
            if coefficient in [1, 2, 3]:
                return coefficient
            else:
                print("Veuillez entrer un coefficient valide (1, 2 ou 3).")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

def demander_note(note_num):
    """Demande la note pour un numéro spécifique."""
    while True:
        try:
            note = float(input(f"Entrez la note {note_num} : "))
            return note
        except ValueError:
            print("Veuillez entrer une valeur numérique pour la note.")

def main():
    # Demander les coefficients pour chaque note
    coeff1 = demander_coefficient(1)
    coeff2 = demander_coefficient(2)
    coeff3 = demander_coefficient(3)
    coeff4 = demander_coefficient(4)

    # Demander les notes
    note1 = demander_note(1)
    note2 = demander_note(2)
    note3 = demander_note(3)
    note4 = demander_note(4)

    # Calcul de la somme des notes pondérées
    somme_ponderee = (note1 * coeff1) + (note2 * coeff2) + (note3 * coeff3) + (note4 * coeff4)
    
    # Calcul de la somme des coefficients
    somme_coefficients = coeff1 + coeff2 + coeff3 + coeff4  # Assurez-vous que cela soit bien là

    # Vérification pour éviter la division par zéro
    if somme_coefficients > 0:
        # Calcul de la moyenne pondérée
        result = somme_ponderee / somme_coefficients
        print("Le résultat est : " + str(result))
    else:
        print("Erreur : la somme des coefficients ne peut pas être zéro.")

if __name__ == '__main__':
    main()
#result = (note1 + note2 + note3 + note4) /4