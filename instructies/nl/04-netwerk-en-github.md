# 4. Netwerk en GitHub

## Netwerkbeperkingen

Uitgaande verbindingen zijn alleen toegestaan naar GitHub en packagemanagers.

## GitHub-toegang

Om onbedoelde blootstelling van medische data te voorkomen, adviseren we GitHub te gebruiken met een **Personal Access Token (PAT)** dat is ingesteld voor alleen-lezen toegang:

1. Ga naar je GitHub-account op [github.com](https://github.com). Dit kan binnen de MyDRE-omgeving, zodat je het token daarna makkelijker kunt plakken.
2. Ga naar **Settings** in **je account** rechtsboven en daarna naar **Developer Settings**.
3. Klik op Personal access tokens en maak een **fine-grained Personal Access Token** aan.
4. Kies een naam, een vervaldatum en de repositories waartoe je toegang wilt.
5. Voeg de **"Contents"**-permissie toe en zet deze op **read-only**.
6. Houd de PAT-pagina open en kopieer de key.
7. Typ `git config --global credential.helper store` in de terminal. Dit geeft geen output.
8. Kloon je repository door `git clone https://....` te typen. VSCode vraagt eerst of je online wilt inloggen bij GitHub; klik op No, omdat je dan geen alleen-lezen toegang kunt instellen. Voer daarna je gebruikersnaam in en plak bij de vraag om je wachtwoord je PAT.
9. Je PAT is nu opgeslagen in je credentials-opslag, zodat je het niet opnieuw hoeft in te voeren bij het klonen van je eigen repositories.

## Applicaties of internettoegang aanvragen

Als je toegang nodig hebt tot een specifieke applicatie of een uitgaande internetverbinding die niet beschikbaar is in de werkruimte, laat het projectteam@icudata.nl weten. Sommige applicaties werken alleen als specifieke domeinen op een whitelist staan. Je kunt [dit overzicht](https://lookerstudio.google.com/embed/u/0/reporting/0cba74d6-0573-4675-8bb1-d754c7d88a6a/page/vhAYE) raadplegen om te zien welke applicaties bekende domeinvereisten hebben en of ze zonder aanpassingen ondersteund kunnen worden.

Volgende, alleen als je de Windows VM nodig hebt: [5. Windows VM en SSH](05-windows-vm-en-ssh.md)
