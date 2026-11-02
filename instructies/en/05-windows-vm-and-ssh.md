# 5. Windows VM and SSH

Only for those who need the Windows VM. Everyone else works on the Linux VM directly ([2. Start the VM and log in](02-start-and-log-in.md)).

## The Windows VM

- At most 2 users can use the Windows VM at the same time (a Microsoft limit). To see who is using it, type `query user` in Command Prompt or PowerShell.
- The Windows VM is a visual interface with applications, such as Visual Studio Code, to connect to the Linux VM. No data is or should be stored on it.
- Start the Linux VM as well: the Windows VM only connects to it.
- The VMs shut down automatically. Shut down the Windows VM when it is not in use.

## Connecting to the Linux VM with VSCode (Remote-SSH)

1. **Launch Visual Studio Code** on the Windows VM. If it is not on the desktop, search for it by clicking the Windows button in the bottom left.
2. Install the **"Remote - SSH" extension** in VSCode by clicking on the **building blocks** in the left sidebar.
3. A new "PC-Display" icon appears in the left sidebar. Click it, hover over "SSH" in the left sidebar and click the **+** to add an SSH connection.
4. Enter the following line when prompted. Then click the upper option to save it in your personal config file:
   ```
   ssh <your_mydre_email>@<linux-vm-ip>
   ```
   **Example:** `ssh John.Doe@mydre.org@10.4.21.53`
5. Enter your **MyDRE password** when prompted.
6. Select **Linux** as the operating system and click "Continue".
7. Click on "File" in the top left, then "Open a folder" on the Linux server to start. To change the base folder of your working environment, follow this step again. You are asked for your password each time you do this.

## Avoiding repeated password prompts

Each new VSCode window over SSH normally asks for your MyDRE password again. You can set up an SSH key once, so that future connections do not ask for it. Do this from a PowerShell window on the Windows VM:

1. Create a key:
   ```
   ssh-keygen -t ed25519
   ```
   When asked for the file location, press Enter to accept the default. When asked for a passphrase, you **must** set one to protect the key; do **not** leave it empty. You enter this passphrase only once. If you leave it empty, VSCode keeps asking for your MyDRE password on every new connection.
2. Copy the key to the Linux VM. Replace `<your_mydre_email>` and `<linux-vm-ip>` with your own values (the same ones you use for the SSH connection above):
   ```
   type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh <your_mydre_email>@<linux-vm-ip> "cat >> ~/.ssh/authorized_keys"
   ```
   Example: `type $env:USERPROFILE\.ssh\id_ed25519.pub | ssh John.Doe@mydre.org@10.4.21.53 "cat >> ~/.ssh/authorized_keys"`
3. Enter your MyDRE password one last time when prompted. After this, new VSCode SSH windows connect without asking for your password.

## R: RStudio in the browser

1. Click the **Windows button** and type **"proxy"**.
2. In the Proxy settings, add a new IP address after the existing one, separated by a semicolon (`;`):
   ```
   <linux-vm-ip>:8005
   ```
   For example: `10.4.21.53:8005`
3. Open **Microsoft Edge** and go to the IP address you just added, including the port 8005.
4. This opens **RStudio in the browser**, connected to the Linux VM. Sign in with your MyDRE e-mail address and password.
