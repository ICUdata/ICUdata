# 5. Data en code

## Data uploaden naar MyDRE

1. Log in op mydre.org met je persoonlijke @mydre.org-account.
2. Open je ICUdata-werkruimte.
3. Ga naar "Files".
4. Klik op "Upload files". Welke map je kiest, maakt niet uit: elke upload komt in een inbox terecht.
5. Upload de bestanden:
   - rechtstreeks vanaf je computer, voor relatief kleine bestanden; of
   - met Azure Storage Explorer, voor grote bestanden. Installeer Azure Storage Explorer eerst op je computer.
6. Na een paar minuten krijg je een bevestigingsmail.

Op de Linux VM komt de upload aan in `/mnt/inbox` of `/mnt/data/inbox`, in een map met de naam `transfer-<datum>-<tijd>-<gebruikersnaam>`. Verplaats die map uit de inbox zodra hij is aangekomen, bijvoorbeeld naar je eigen map, zodat alleen nieuwe uploads in de inbox blijven staan:

```
mv /mnt/inbox/transfer-<datum>-<tijd>-<gebruikersnaam> ~/
```

`mv` verplaatst een bestand of map. Het eerste deel is de map in de inbox; `~/` is je eigen map (je home-map). Staat je upload in `/mnt/data/inbox`, gebruik dan dat pad.

## Code

De beste manier om met code te werken:

1. Schrijf je code op je eigen pc en push die naar GitHub.
2. Pull de code op de Linux VM van GitHub en voer hem daar uit. Hoe je alleen-lezen toegang instelt, staat in [GitHub-toegang](04-netwerk-en-github.md#github-toegang) in handleiding 4.

We vragen je om niet vanaf de VM naar GitHub te pushen.

Voor R werkt het net zo: zet je R-scripts in een Git-repository, pull ze op de VM met `git pull` (of met het Git-paneel in RStudio) en voer ze daar uit. Packages kun je op de VM installeren; zie [3. Werkomgeving](03-werkomgeving.md).

## Resultaten uit MyDRE halen

Omdat we je vragen niet vanaf de VM te pushen, gaan resultaten via de outbox uit MyDRE:

1. Maak in `/mnt/data/outbox` een nieuwe map voor deze export en zet de bestanden daarin. Bij veel bestanden pak je ze eerst in tot één bestand, bijvoorbeeld:
   ```
   mkdir /mnt/data/outbox/<exportnaam>
   tar -czf /mnt/data/outbox/<exportnaam>/<exportnaam>.tar.gz <jouw-map>
   ```
   `mkdir` maakt de map aan. `tar` pakt bestanden in tot één bestand: `-c` maakt een nieuw bestand, `-z` comprimeert het, en `-f` geeft de bestandsnaam die erop volgt. `<jouw-map>` is de map met je bestanden.
2. Open in MyDRE je werkruimte en klik op "Files".
3. Zoek de bestanden op en klik op "Request download".

We keuren de aanvraag zo snel mogelijk goed.

Volgende, alleen als je de Windows VM nodig hebt: [6. Windows VM en SSH](06-windows-vm-en-ssh.md)
