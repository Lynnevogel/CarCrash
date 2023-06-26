# CarCrash - Isabelle Koops, Lynne Vogel en Jade van de Wal

## Rush Hour

Rush Hour is een schuifpuzzel bestaande uit een veld, gevuld met auto's. Doorgaans wordt het spel gespeeld op een bord van 6 bij 6, maar er bestaan ook borden van 9 bij 9 en 12 bij 12. Op het bord staat een rode auto die naar de uitgang moet. De weg van de auto is versperd door andere auto's en vrachtwagens. Het doel van het spel is om de auto's zo te verplaatsen dat de rode auto naar de uitgang kan. In deze opdracht is het de bedoeling om verschillende algoritmes toe te passen, op zoek naar de snelste manier om de puzzel op te lossen.

## Statespace van de case
De statespace van de case kan berekend worden door alle mogelijke plaatsen voor alle auto's bij elkaar op te tellen. Wanneer het bord n lang is, kan de auto op n - lengte_auto aantal plekken staan. Hierbij wordt geen rekening gehouden met dat auto's niet over elkaar heen mogen bewegen. Dit geldt hetzelfde voor de vrachtwagens. Dit levert de volgende formule op:

```
(n - lengte_auto) ^ aantal_auto's + (n - lengte_vrachtwagen) ^ aantal_vrachtwagens
```

## Aan de slag

### Algoritmes

Voor deze case is gebruik gemaakt van vier verschillende algoritmes. 

Random algoritme

In het random algoritme wordt telkens een willekeurige auto op het bord geselecteerd. Afhankelijk van het aantal bewegingen dat de auto kan maken, wordt een richting gekozen. Wanneer er 0 mogelijke bewegingen zijn, blijft de auto staan. Bij 1 mogelijke beweging moet de auto die kant op. Wanneer er 2 mogelijkheden zijn, wordt de richting willekeurig gekozen. 

Depth-first search

Bij het depth-first search algoritme worden alle mogelijke oplossingen afgegaan. Het algoritme begint bij de begin-state. Vervolgens wordt gekeken welke auto's op het bord kunnen verschuiven en waarheen. Vervolgens wordt een bord gekozen en wordt dit herhaald. Wanneer het algoritme een oplossing tegenkomt, gaat hij terug naar een ondieper niveau in de "boom". Vanuit daar wordt verder gekeken naar mogelijke bewegingen. Op deze manier gaat het algoritme de hele boom af. Dit wordt geïmplementeerd door gebruik te maken van een stack.

Breadth-first search

Een breadt-first search algoritme verschilt in implementatie weinig van de depth-first search. Een belangrijk verschil is dat breadth-first search gebruik maakt van een queue in plaats van een stack. De breadth-first search gaat in een boom eerst alle mogelijkheden af op hetzelfde niveau, en gaat pas een niveau lager wanneer het huidige niveau geen mogelijkheden meer heeft. 

Hillclimber

Tot slot is gebruik gemaakt van een hillclimber algoritme. Bij dit algoritme is het van belang dat er een bestaande oplossing is die mogelijk verbeterd kan worden. De hillclimber is in deze case zo geïmplementeerd dat eerst tien random oplossingen worden gegenereerd. Vervolgens is dit de state space die wordt afgezocht door een breadth-first search.


### Vereisten

De code voor het oplossen van de case is geschreven in 3.10.10 en 3.11.3. Voor de visualisatie van de case is gebruik gemaakt van matplotlib, scipy en numpy. De versies die zijn gebruikt tijdens dit project, zijn terug te vinden in requirements.txt. De requirements zijn te downloaden via het volgende commando:

```
pip install -r requirements.txt
``` 

### Gebruik

De algoritmes kunnen gerund worden door het volgende commando: 

```
"python main.py [game] [algorithm] [amount of runs]"

```
Dus dit zou het commando zijn om spelbord 6x6_1 10 keer op te lossen met het random algoritme: 
```
python3 main.py 6x6_1 random 10
```

### Structuur

Hieronder is een lijst te vinden van de mappen en bestanden in de repository van dit project.
- **/main.py**: in dit bestand wordt het bord in geladen en het gewenste algoritme aangehaald.
- **/experiment.py**: in dit bestand wordt de data per run gegenereert.
- **/code**: deze map bevat code, die aangehaald wordt in main.py en experiment.py.
    - **/code/algorithms**: bevat de code voor de verschillende algoritmes.
    - **/code/classes**: bevat de code voor de verschillende classes.
- **/gameboards**: bevat de verschillende datafiles met spelborden voor het runnen van het programma.
- **/images**: bevat een afbeelding van de berekende statespace.

### Taakverdeling

De taakverdeling moet nog verder uitgewerkt worden maar dit is de voorlopige taakverdeling. 

- Lynne: visualisatie, depth first, experiment
- Isabelle: A* algoritme, depth first limit, experiment
- Jade: depth first en breadth first search, experiment