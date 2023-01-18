# Het maken van een kopie van Alien Invasion
Dit is een project waar ik mijn eigen versie maak van Alien invasion

# Taal
Python (Pygame)

# Wat heb ik geleerd

  * het oefenen en gebruiken van pygame
  * meer bezig geweest met Classes, zodat dat makkelijker wordt in de toekomst
  * Ervaring opdoen met grotere projecten
  * het maken van een interactive button binnen in python
  
 # Gebruikte files
 
  * alien_invasion.py : main file
  * settings.py : alle variabelen, zoals hoogte en breedte van het scherm, etc
  * game_functions.py : alle functies die het spel gebruikt
  * game_stats.py : houdt alle stats in de gaten die gedurende het spel kunnen veranderen
  * scoreboard.py : een Class voor het laten zien van informatie, bijv de huidige score
  * ship.py : Class, puur voor het ship dat je speelt
  * bullet.py : kogels die het ship afvuurt
  * alien.py : Class, voor de aliens die op het scherm staan
  * alien_bullet.py : kogels die de aliens afvuren
  * button.py : het maken van eeen playbutton
  
 # Bedoeling van het programma
 Wanneer je het spel opstart, moet het nog niet activeren. Wanneer je op 'P' klikt of met de linker muisknop op de playbutton, moet het spel beginnen. De aliens schuiven langzaam naar rechts, totdat ze een muur raken. Wanneer de muur geraakt word, gaan ze naar links bewegen, totdat ze de linker muur raken. Dit blijft door gaan totdat ze de bodem van het scherm bereiken of het ship raken. 
Terwijl dit bezig is, kun je als schip naar links en rechts bewegen. Ook kun je kogels afvuren met de spatiebalk. Deze kogels moeten als ze een alien raken, deze alien en de kogel verwijderen van het scherm.
Elke keer als je een alien 'dood', krijg je een bepaalde hoeveelheid punten. Terwijl jij probeert de aliens te raken, moeten er kogels van de aliens komen die als ze jou raken, je een leven kosten. De game moet de hoeveelheid levens die je over hebt boven in de linker hoek aangeven en elke keer als je een leven verliest, moet ook een van de levens links boven verdwijnen.
Wanneer alle aliens van het scherm zijn, moet een nieuwe vloot komen en moet het level dat onder de punten staat 1 omhoog gaan. Ook moet het spel versneld worden. Hieronder valt de snelheid van de aliens en het schip, maar ook de snelheid van de kogels. En als laats, moet de hoevelheid punten die je krijgt per alien omhoog gaan.\
Om het spel te beeindigen, kun je op het kruisje klikken, maar je kunt ook op q te klikken. Wanneer je dit doet, wordt je huidige highscore overgescreven naar een document genaamd 'high_scores.txt'. Wanneer je de volgende keer het spel weer opstart, moet het spel deze file lezen en de highscore aangeven boven in het scherm.
