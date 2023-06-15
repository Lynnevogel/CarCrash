# CarCrash - Jade, Isabelle en Lynne

### Rush Hour

Rush Hour is een schuifpuzzel bestaande uit een veld, gevuld met auto's. Doorgaans wordt het spel gespeeld op een bord van 6 bij 6, maar er bestaan ook borden van 9 bij 9 en 12 bij 12. Op het bord staat een rode auto die naar de uitgang moet. De weg van de auto is versperd door andere auto's en vrachtwagens. Het doel van het spel is om de auto's zo te verplaatsen dat de rode auto naar de uitgang kan.

### Statespace van de case
De statespace van de case kan berekend worden door alle mogelijke plaatsen voor alle auto's bij elkaar op te tellen. Wanneer het bord n lang is, kan de auto op n - lengte_auto aantal plekken staan. Hierbij wordt geen rekening gehouden met dat auto's niet over elkaar heen mogen bewegen. Dit geldt hetzelfde voor de vrachtwagens. Dit levert de volgende formule op:

```
(n - lengte) ^ aantal_auto's + (n - lengte_vrachtwagen) ^ aantal_vrachtwagens
```

## Aan de slag

### Vereisten

De code voor het oplossen van de case is geschreven in 3.10.10 en 3.11.3. Voor de visualisatie van de case is gebruik gemaakt van matplotlib. Meer informatie hierover is te vinden in requirements.txt. Matplotlib is te downloaden via het volgende commando:

```
pip install -r requirements.txt
``` 

### Gebruik

De code kan met een voorbeeld bord gerund worden door het volgende commando: 

```
python3 main.py 6x6_1
```

### Structuur

Hieronder is een lijst te vinden van de mappen en bestanden in de repository van dit project.
- **/code**: deze map bevat alle code.
    - **/code/algorithms**: bevat de code voor de verschillende algoritmes.
    - **/code/classes**: bevat de code voor de verschillende classes.
- **/gameboards**: bevat de verschillende datafiles met spelborden voor het runnen van het programma.
- **/images**: bevat een afbeelding van de berekende statespace.