# 2. Starten en inloggen

## De twee VMs

De ICUdata-werkruimte heeft twee virtuele machines (VMs):

- **Linux VM**: de VM waarop iedereen werkt. Deze VM bevat een eigen schijf met gebruikersspecifieke data, en de alleen-lezen DuckDB-database in `/home/ICUdata`, die ICUdata bevat.
- **Windows VM**: maximaal 2 gebruikers tegelijk (een beperking van Microsoft). De Linux VM heeft die beperking niet, dus iedereen gebruikt de Linux VM. Gebruik de Windows VM alleen als je die nodig hebt; zie [5. Windows VM en SSH](05-windows-vm-en-ssh.md).

## De Linux VM starten

- Start alleen de **Linux VM** in je MyDRE-werkruimte.
- De VMs worden **niet automatisch uitgeschakeld**. We vragen gebruikers om de VM uit te schakelen wanneer die niet in gebruik is.

## Inloggen

1. Klik in het Azure-scherm op het keuzemenu waar "Microsoft Entra ID" staat en kies "VM password".
2. Vul als gebruikersnaam je MyDRE-e-mailadres in en als wachtwoord je wachtwoord.
3. Klik op **RDP** (voor de Linux VM).

Daarna opent het Linux-bureaublad.

Volgende: [3. Werkomgeving](03-werkomgeving.md)
