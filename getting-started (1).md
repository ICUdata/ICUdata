# Aan de slag met ICUdata

Welkom op de ICUdata GitHub! Deze handleiding beschrijft hoe je toegang krijgt, de virtuele machines instelt en je werkomgeving configureert.

Voor informatie over de database zelf, zie de [Database handleiding](database-guide.md).

---

## Toegang verkrijgen

De ICUdata-database wordt gehost op het MyDre-platform van AnDREa, een beschermde onderzoeksomgeving met minimale internetverbinding. Een aanvraag voor leestoegang tot de data kan worden gedaan via de primaire ICUdata-contactpersoon van je instelling, die een MyDre-account kan aanvragen voor onderzoekers. Na goedkeuring wordt een MyDre-account voor je aangemaakt, waarna je wordt toegevoegd aan de ICUdata-onderzoekswerkruimte. Als je de data wilt gebruiken voor onderzoek, moet een onderzoeksaanvraag worden ingediend bij de Wetenschappelijke Commissie van ICUdata.

> **Let op:** Bij het aanmaken van een nieuw wachtwoord raden we aan om geen wachtwoord uit een wachtwoordmanager te gebruiken, aangezien je het vaak moet invoeren in de VM die geen internetverbinding of cross-PC kopieer-plakfunctionaliteit heeft.

---

## Toegang tot de VMs

### Werkruimte-opzet

De werkruimte bestaat uit twee VMs:

- **Windows VM**: Dit is voornamelijk een visuele interface met applicaties om verbinding te maken met de Linux VM. Er worden/mogen geen data op opgeslagen worden.
- **Linux VM**: Deze VM bevat een eigen schijf vergelijkbaar met een C:-schijf in Windows. Het bevat gebruikersspecifieke data en de alleen-lezen DuckDB-database in `/home/ICUData`, die ICUdata bevat.

**Opmerkingen over de VMs**
- Om ICUdata te gebruiken moet je **beide VMs starten**.
- We vragen gebruikers om **de VMs uit te schakelen wanneer ze niet in gebruik zijn**.
- De VMs worden **niet automatisch uitgeschakeld**, dus vergeet niet ze te stoppen na gebruik.
- Om te controleren of andere gebruikers de Windows VM gebruiken, typ `query user` in Command Prompt of PowerShell.

**Opmerking over DuckDB**
- DuckDB is een databaseformaat dat specifiek ontworpen is voor onderzoek. Het is bevraagbaar met SQL, maar wordt niet op dezelfde manier gehost als andere SQL-databases; het is een enkel bestand dat alle data bevat en waarmee je kunt werken via de DuckDB-packages.

### Toegang tot de Linux VM

#### Via Python

1. **Start Visual Studio Code** op de Windows VM. Als het niet als snelkoppeling op het bureaublad staat, zoek dan op de VM door op de Windows-knop linksonder te klikken.
2. Installeer de **"Remote - SSH"-extensie** in VSCode door op de **bouwblokken** in de linkerzijbalk te klikken.
3. Er verschijnt een nieuw "PC-Display"-pictogram in de linkerzijbalk. Klik erop, beweeg de muis boven "SSH" in de veranderde linkerzijbalk en klik op **+** om een SSH-verbinding toe te voegen.
4. Voer de volgende regel in wanneer daarom gevraagd wordt. Klik na correcte invoer op de bovenste optie om op te slaan in je persoonlijke configuratiebestand:
   ```
   ssh <je_mydre_email>@<linux-vm-ip>
   ```
   **Voorbeeld:** ssh [Jan.Jansen@mydre.org](mailto:Jan.Jansen@mydre.org)@10.4.21.53
5. Voer je **MyDre-wachtwoord** in wanneer daarom gevraagd wordt.
6. Selecteer **Linux** als besturingssysteem en klik op "Continue".
7. Klik op "File" linksboven en vervolgens op "Open a folder" op de Linux-server om te beginnen. Om de basismap van je werkomgeving te wijzigen kun je deze stap opnieuw volgen. Je wordt elke keer opnieuw om je wachtwoord gevraagd.

Opmerking: we raden aan om Auto-save in te schakelen in VSCode door op "File" te klikken en vervolgens op "Autosave".

#### Via R

1. Klik op de **Windows-knop** en typ **"proxy"**.
2. Voeg in de Proxy-instellingen een nieuw IP-adres toe na het bestaande, gescheiden door een puntkomma (`;`):
   ```
   <linux-vm-ip>:8005
   ```
   Bijvoorbeeld: `10.4.21.53:8005`
3. Open **Microsoft Edge** en navigeer naar het IP-adres dat je zojuist hebt toegevoegd, inclusief poort 8005.
4. Dit opent **RStudio in de browser**, verbonden met de Linux VM. Log in met je MyDre-email en wachtwoord.

### Applicaties

- **Windows VM**: Wordt geleverd met Visual Studio Code (VSCode).
- **Linux VM**: Vooraf geïnstalleerd met `git`, `pip`, `pipx`, `uv`, `conda`, `poetry`, `pyenv`, de DuckDB command line interface en Python. Als bepaalde packages niet te downloaden zijn via pip of pipx, neem dan contact met ons op om te kijken of we ze beschikbaar kunnen maken.

**Let op:** Niet al deze tools zijn uitgebreid getest. Als je problemen ondervindt, mail dan naar projectteam@icudata.nl.

### Python-packages installeren

Om specifieke Python-packages te installeren, maak je een virtuele omgeving (`.venv`) aan in je projectmap en gebruik `pip` of een andere packagemanager.

### Netwerkbeperkingen

- **Uitgaande verbindingen**: Alleen verbindingen met GitHub en packagemanagers zijn toegestaan.

### GitHub-toegang

Om onbedoelde blootstelling van medische data te voorkomen, adviseren we GitHub te gebruiken met een **Personal Access Token (PAT)** geconfigureerd voor alleen-lezen toegang. Volg deze stappen:

1. Ga naar je GitHub-account op [github.com](https://github.com) (dit kan binnen de MyDre-omgeving voor makkelijker plakken).
2. Navigeer naar **Settings** in **je account** rechtsboven en ga naar **Developer Settings**.
3. Klik op Personal access tokens en maak een **fine-grained Personal Access Token** aan.
4. Kies een naam, een vervaldatum en de repositories waartoe je toegang wilt.
5. Voeg de **"Contents"**-permissie toe en zet deze op **read-only**.
6. Houd de PAT-pagina open en kopieer de key.
7. Typ "git config --global credential.helper store" in de terminal. Dit geeft geen output.
8. Kloon je gewenste repo door "git clone https://...." te typen. VSCode vraagt eerst of je online wilt inloggen bij GitHub; klik op No (aangezien dit je niet in staat stelt pull-only toegang in te stellen). Voer vervolgens je gebruikersnaam in en plak bij de wachtwoordprompt je PAT.
9. Je PAT wordt nu opgeslagen in je credentials-opslag, zodat je het niet opnieuw hoeft in te voeren bij het klonen van persoonlijke repos.

---

## Applicaties of internettoegang aanvragen

Als je toegang nodig hebt tot een specifieke applicatie of een uitgaande internetverbinding die momenteel niet beschikbaar is in de werkruimte, laat het projectteam@icudata.nl weten. Sommige applicaties vereisen dat specifieke domeinen worden gewhitelist om te functioneren. Je kunt [dit overzicht](https://lookerstudio.google.com/embed/u/0/reporting/0cba74d6-0573-4675-8bb1-d754c7d88a6a/page/vhAYE) raadplegen om te zien welke applicaties bekende domeinvereisten hebben en of ze direct ondersteund kunnen worden.
