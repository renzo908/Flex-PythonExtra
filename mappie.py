Python 3.8.5 (tags/v3.8.5:580fbb0, Jul 20 2020, 15:43:08) [MSC v.1926 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> # Gebruiker om de naam van de map vragen
mapnaam = input("Welke naam wil je voor de map? ")

# Als de lengte van mapnaam > 0 is dan maken we de map
lengte_mapnaam = len(mapnaam)
if lengte_mapnaam > 0:
    os.mkdir(mapnaam)
    print("De map " + mapnaam + " is gemaakt.")
else:
    print("Je hebt geen naam ingevoerd")

 Zo open je een bestand om naar te schrijven 
bestand = open("test.txt", "w")

# Zet de variabele mapnaam eerst naar een lege tekst
mapnaam = ""

# Zolang de lengte_mapnaam gelijk is aan 0, blijft het script vragen om de mapnaam
while lengte_mapnaam == 0:
    # Vraag om mapnaam en sla deze op in de variabele mapnaam
    mapnaam = input("Welke naam wil je voor de map? "

# Sla de lengte van de mapnaam op in de variabele lengte_mapnaam
    lengte_mapnaam = len(mapnaam)

# Als lengte_mapnaam groter dan 0 is dan maken we de map aan
    if lengte_mapnaam > 0:
        os.mkdir(mapnaam)
    else:
        # En anders melden we dat er niets is ingevuld
        print("Je hebt geen naam ingevoerd")

# ... en anders gaat de code hier verder
print("De map " + mapnaam + " is gemaakt.")

# Zo open je een bestand om naar te schrijven 
bestand = open("test.txt", "w")

# Een tekst naar het bestand schrijven
bestand.write("Test 123!");  

# Vergeet bestand niet te sluiten!
bestand.close()

# Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")

# Een tekst naar het bestand schrijven
bestand2.write("Lekker alles overschrijven")

import io

# Bestand in read-only (r) mode openen
bestand2 = open("test.txt", "r")

# Alle tekst lezen met read() en opslaan in de variabele: inhoud
inhoud = bestand2.read()

# De inhoud op het scherm zetten:
print("De inhoud van het bestand is:")
print(inhoud)

