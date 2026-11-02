# 3. Werkomgeving

Je werkt op het Linux-bureaublad dat opent nadat je bent ingelogd ([2. Starten en inloggen](02-starten-en-inloggen.md)).

## VSCode

Open de "Terminal Emulator" vanuit het startmenu linksboven en typ `code`. Hiermee start de nieuwste versie van VSCode op de Linux VM.

We raden aan om Auto-save in te schakelen in VSCode: klik op "File" en vervolgens op "Autosave".

## De database

De alleen-lezen ICUdata-database staat in `/home/ICUdata`. DuckDB is een databaseformaat dat speciaal is ontworpen voor onderzoek. Het is bevraagbaar met SQL, maar wordt niet gehost zoals andere SQL-databases: het is één bestand dat alle data bevat, en je werkt ermee via de DuckDB-packages. De [Database handleiding](database-uitleg.md) beschrijft de tabellen en geeft voorbeeldqueries.

## Python

Python is geïnstalleerd op de Linux VM. Om specifieke Python-packages te installeren, maak je een virtuele omgeving (`.venv`) aan in je projectmap en gebruik je `pip` of een andere packagemanager.

## R

RStudio Server draait op de Linux VM, op poort 8005. Open op het Linux-bureaublad een webbrowser en ga naar `http://localhost:8005`. Als dat niet werkt, gebruik dan de route in [5. Windows VM en SSH](05-windows-vm-en-ssh.md) en laat het ons weten via projectteam@icudata.nl.

## Applicaties

Op de Linux VM zijn `git`, `pip`, `pipx`, `uv`, `conda`, `poetry`, `pyenv`, de DuckDB command line interface en Python geïnstalleerd. Als een package dat je nodig hebt niet te downloaden is via pip of pipx, neem dan contact met ons op om te kijken of we het beschikbaar kunnen maken.

**Let op:** Niet al deze tools zijn uitgebreid getest. Als je problemen ondervindt, mail dan naar projectteam@icudata.nl.

Volgende: [4. Netwerk en GitHub](04-netwerk-en-github.md)
