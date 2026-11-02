# 6. Windows VM en SSH

Alleen voor wie de Windows VM nodig heeft. Alle anderen werken direct op de Linux VM ([2. Starten en inloggen](02-starten-en-inloggen.md)).

## De Windows VM

- Maximaal 2 gebruikers kunnen de Windows VM tegelijk gebruiken (een beperking van Microsoft). Om te zien wie de VM gebruikt, typ je `query user` in Command Prompt of PowerShell.
- De Windows VM is een visuele interface met applicaties, zoals Visual Studio Code, om verbinding te maken met de Linux VM. Er worden en mogen geen data op opgeslagen worden.
- Start ook de Linux VM: de Windows VM maakt alleen verbinding met de Linux VM.
- De VMs schakelen automatisch uit; het tijdstip staat in het VM-scherm van je MyDRE-werkruimte. Schakel de Windows VM uit wanneer die niet in gebruik is.

## Verbinden met de Linux VM via VSCode (Remote-SSH)

1. **Start Visual Studio Code** op de Windows VM. Als het niet op het bureaublad staat, zoek het dan door op de Windows-knop linksonder te klikken.
2. Installeer de **"Remote - SSH"-extensie** in VSCode door op de **bouwblokken** in de linkerzijbalk te klikken.
3. Er verschijnt een nieuw "PC-Display"-pictogram in de linkerzijbalk. Klik erop, beweeg de muis boven "SSH" in de linkerzijbalk en klik op **+** om een SSH-verbinding toe te voegen.
4. Voer de volgende regel in wanneer daarom gevraagd wordt. Klik daarna op de bovenste optie om op te slaan in je persoonlijke configuratiebestand:
   ```
   ssh <je_mydre_email>@<linux-vm-ip>
   ```
   **Voorbeeld:** `ssh Jan.Jansen@mydre.org@10.4.21.53`
5. Voer je **MyDRE-wachtwoord** in wanneer daarom gevraagd wordt.
6. Selecteer **Linux** als besturingssysteem en klik op "Continue".
7. Klik op "File" linksboven en vervolgens op "Open a folder" op de Linux-server om te beginnen. Om de basismap van je werkomgeving te wijzigen, volg je deze stap opnieuw. Je wordt elke keer opnieuw om je wachtwoord gevraagd.

## Herhaalde wachtwoordvragen voorkomen

Elk nieuw VSCode-venster via SSH vraagt normaal opnieuw om je MyDRE-wachtwoord. Je kunt eenmalig een SSH-sleutel instellen, zodat volgende verbindingen er niet meer om vragen. Doe dit vanuit een PowerShell-venster op de Windows VM:

1. Maak een sleutel aan:
   ```
   ssh-keygen -t ed25519
   ```
   Wanneer om de bestandslocatie wordt gevraagd, druk je op Enter om de standaardwaarde te accepteren. Wanneer om een passphrase wordt gevraagd, **moet** je er een instellen om de sleutel te beveiligen; laat deze **niet** leeg. Deze passphrase voer je maar één keer in. Als je deze leeg laat, blijft VSCode bij elke nieuwe verbinding om je MyDRE-wachtwoord vragen.
2. Kopieer de sleutel naar de Linux VM. Vervang `<je_mydre_email>` en `<linux-vm-ip>` door je eigen waarden (dezelfde die je hierboven gebruikt voor de SSH-verbinding):
   ```
   type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh <je_mydre_email>@<linux-vm-ip> "cat >> ~/.ssh/authorized_keys"
   ```
   Voorbeeld: `type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh Jan.Jansen@mydre.org@10.4.21.53 "cat >> ~/.ssh/authorized_keys"`
3. Voer je MyDRE-wachtwoord nog één keer in wanneer daarom gevraagd wordt. Hierna maken nieuwe VSCode SSH-vensters verbinding zonder om je wachtwoord te vragen.

## R: RStudio in de browser

1. Klik op de **Windows-knop** en typ **"proxy"**.
2. Voeg in de Proxy-instellingen een nieuw IP-adres toe na het bestaande, gescheiden door een puntkomma (`;`):
   ```
   <linux-vm-ip>:8005
   ```
   Bijvoorbeeld: `10.4.21.53:8005`
3. Open **Microsoft Edge** en ga naar het IP-adres dat je zojuist hebt toegevoegd, inclusief poort 8005.
4. Dit opent **RStudio in de browser**, verbonden met de Linux VM. Log in met je MyDRE-e-mailadres en wachtwoord.
