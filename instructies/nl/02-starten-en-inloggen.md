# 2. Starten en inloggen

## De twee VMs

De ICUdata-werkruimte heeft twee virtuele machines (VMs):

- **Linux VM**: de VM waarop iedereen werkt. Deze VM bevat een eigen schijf met gebruikersspecifieke data, en de alleen-lezen DuckDB-database in `/home/ICUdata`, die ICUdata bevat.
- **Windows VM**: maximaal 2 gebruikers tegelijk (een beperking van Microsoft). De Linux VM heeft die beperking niet, dus iedereen gebruikt de Linux VM. Gebruik de Windows VM alleen als je die nodig hebt; zie [6. Windows VM en SSH](06-windows-vm-en-ssh.md).

## De Linux VM starten

Start alleen de **Linux VM** in je MyDRE-werkruimte.

## Inloggen

1. Klik in het Azure-scherm op het keuzemenu waar "Microsoft Entra ID" staat en kies "VM password".
2. Vul als gebruikersnaam je MyDRE-e-mailadres in en als wachtwoord je wachtwoord.
3. Klik op **RDP** (voor de Linux VM).

Daarna opent het Linux-bureaublad.

## De Linux VM uitschakelen

De VMs schakelen automatisch uit; het tijdstip staat in het VM-scherm van je MyDRE-werkruimte. We vragen gebruikers om de VM uit te schakelen wanneer die niet in gebruik is.

Voer voordat je de Linux VM uitschakelt `/home/ICUdata/can-i-shut-down` uit in de Terminal Emulator. Het script bekijkt 10 seconden lang de programma's van andere gebruikers. Schakel alleen uit als de eerste regel JA zegt.

- **NEE**: een programma van iemand anders is aan het werk, bijvoorbeeld een lopende pipeline.
- **JA**: niemand anders is aan het werk. Anderen kunnen nog ingelogd zijn of een programma open hebben dat niets doet, zoals een inactieve Python-sessie; het script noemt ze dan, en uitschakelen sluit hun sessies.

Om het zelf te controleren, voer je `top` uit en kijk je naar de kolommen USER en %CPU. Als een programma van een andere gebruiker CPU gebruikt, laat de VM dan aan.

## Wanneer contact opnemen

Neem contact op met projectteam@icudata.nl als:

- je een lang proces draait en de automatische uitschakeling uitgezet moet worden;
- je een VM met een GPU nodig hebt;
- je een VM met meer processorkernen of geheugen nodig hebt;
- Spot-evictions je programma blijven stoppen, ook na meerdere pogingen. De VMs zijn Azure Spot VMs, die Azure kan stoppen wanneer Azure de capaciteit ergens anders nodig heeft (een "eviction").

Volgende: [3. Werkomgeving](03-werkomgeving.md)
