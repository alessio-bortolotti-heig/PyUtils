import csv

# Definizione della funzione per ottenere la massa atomica di un elemento
def get_atomic_mass(element_symbol):
    # Apre il file PeriodicTable.csv e lo assegna a una variabile
    with open('PeriodicTable.csv', mode='r') as file:
        # Legge il contenuto del file CSV
        csv_reader = csv.reader(file)
        
        # Itera attraverso le righe del file
        for row in csv_reader:
            # Controlla se il simbolo dell'elemento corrisponde a quello nella riga corrente
            if row[2] == element_symbol:
                # Restituisce la massa atomica corrispondente
                return float(row[3])
    
    # Se il simbolo dell'elemento non è presente nel file, restituisce None
    return None

# Definizione della funzione per separare elemento e moltiplicatore
def split_element_number(element_with_multiplier):
    # Inizializza le variabili per l'elemento e il suo moltiplicatore
    element = ''
    multiplier = ''

    # Itera attraverso i caratteri nella stringa fornita
    for char in element_with_multiplier:
        # Verifica se il carattere è una cifra
        if char.isdigit():
            # Aggiunge il carattere alla parte del moltiplicatore
            multiplier += char
        else:
            # Se il carattere non è una cifra, aggiunge il carattere alla parte dell'elemento
            element += char

    # Se la parte del moltiplicatore è vuota, assegna il valore 1
    if not multiplier:
        multiplier = '1'

    # Restituisce l'elemento e il moltiplicatore come tuple di stringhe
    return element, multiplier

# Definizione della funzione per calcolare la massa molecolare
def calculate_molecule_mass(molecular_formula):
    # Variabile iniziale
    molecular_mass = 0

    # Trova gli elementi basandosi sulla presenza di lettere maiuscole
    components = []
    current_component = ''

    for char in molecular_formula:
        # Inizia un nuovo componente quando trova una lettera maiuscola
        if char.isupper():
            if current_component:
                components.append(current_component)
            current_component = char
        # Aggiunge la lettera minuscola al componente corrente
        elif char.islower():
            current_component += char
        # Aggiunge il numero al componente corrente
        elif char.isdigit():
            current_component += char

    # Aggiunge l'ultimo componente alla lista
    if current_component:
        components.append(current_component)

    # Itera attraverso ogni componente
    for component in components:
        # Separa l'elemento e il moltiplicatore per ogni componente
        element, multiplier = split_element_number(component.strip())  # Aggiungi strip per gestire eventuali spazi

        # Cerca la massa atomica nel file .csv
        atomic_mass = get_atomic_mass(element)

        # Calcola la massa molecolare del componente e sommala alla massa totale
        molecular_mass += atomic_mass * float(multiplier)

    return molecular_mass

# Input dell'utente
user_input = input("Please enter a molecule: ")

# Calcola e stampa la massa molecolare
molecular_mass_calculated = calculate_molecule_mass(user_input)
print(f"The molar mass of {user_input} is: {molecular_mass_calculated}")
