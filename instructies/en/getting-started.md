# Getting Started with ICUdata

Welcome to the ICUdata GitHub! This guide covers how to gain access, set up the virtual machines, and configure your working environment.

For information about the database itself, see the [Database Guide](database-guide.md).

---

## Gaining Access

The ICUdata database is hosted on the MyDre platform by AnDREa, a protected research environment with minimal connection to the internet. A request for reading the data can be done through your institutions' primary ICUdata contact person, that can request a MyDre account for researchers of their institution. After approval, a MyDre account will be created for you, after which you will be added to the ICUdata research workspace. If you want to use the data for research, a research request will have to be sent to the Scientific Committee of ICUdata.

> **Note:** When you create a new password, it is recommended to not use one created by a password manager, as you will have to enter it in the VM many times which has no internet connection or cross-PC copy-paste functionality.

---

## Accessing the VMs

### Workspace Setup

The workspace consists of two main VMs:

- **Windows VM**: This is primarily a visual interface with applications to connect to the Linux VM. No data is/should be stored here.
- **Linux VM**: This VM contains a dedicated drive similar to a C: drive in Windows. It includes user-specific data and the read-only DuckDB database located at `/home/ICUData`, which contains ICUdata.

**Note on the VMs**
- To use ICUdata, you need to **start both VMs**.
- We ask users to **shut down the VMs when they are not in use**.
- The VMs are **not automatically shut down**, so please remember to stop them after use.
- To check if other users are using the Windows VM, type `query user` in Command Prompt or PowerShell.

**Note on DuckDB**
- DuckDB is a database format specifically designed for research. It is queryable with SQL, but is not hosted in a similar way to other SQL-databases; instead, it is a single file that contains all the data, and can be interacted with through the DuckDB packages.

### Accessing the Linux VM

#### Using Python

1. **Launch Visual Studio Code** on the Windows VM. If not present as a desktop shortcut, search the VM by clicking the Windows button in the bottom left.
2. Install the **"Remote - SSH" extension** in VSCode by clicking on the **building blocks** in the left sidebar
3. A new "PC-Display" icon will appear on the left sidebar. Click it, hover above "SSH" in the changed left sidebar and click the **+** in the Remote window to add an SSH connection.
4. Enter the following line when prompted. After correct entry, click the upper option to save in your personal config file:
   ```
   ssh <your_mydre_email>@<linux-vm-ip>
   ```
   **Example:** ssh [John.Doe@mydre.org](mailto:John.Doe@mydre.org)@10.4.21.53
5. Enter your **MyDre password** when prompted.
6. Select **Linux** as the operating system and click "Continue"
7. Click on "File" in the top left, then "Open a folder" on the Linux server to start. To change the base folder of your working environment, you can follow this step again. You will be prompted again for your password each time you do this.

Note: we recommend turning on Auto-save in VScode by clicking on "File" and then "Autosave"

#### Using R

1. Click the **Windows button** and type **"proxy"**.
2. In the Proxy settings, add a new IP address after the existing one, separated by a semicolon (`;`):
   ```
   <linux-vm-ip>:8005
   ```
   For example: `10.4.21.53:8005`
3. Open **Microsoft Edge** and navigate to the IP address you just added, including the port 8005
4. This will open **RStudio in the browser**, connected to the Linux VM. Sign in with your MyDre email and password.

### Applications

- **Windows VM**: Comes with Visual Studio Code (VSCode).
- **Linux VM**: Pre-installed with `git`, `pip`, `pipx`, `uv`, `conda`, `poetry`, `pyenv`, the DuckDB command line interface, and Python. If any packages you need are not downloadable through pip or pipx, reach out to us to see if we can make them available.

**Note:** Not all of the above tools have been widely tested. If you run into any issues, please email projectteam@icudata.nl.

### Installing Python Packages

To install specific Python packages, create a virtual environment (`.venv`) in your project directory and use `pip` or another package manager.

### Network Restrictions

- **Outbound Connections**: Only connections to GitHub and package managers are allowed.

### GitHub Access

To prevent accidental exposure of medical data, we advise using GitHub with a **Personal Access Token (PAT)** configured for pull-only access. Follow these steps:

1. Go to your GitHub account on [github.com](https://github.com) (this can be done in the MyDre environment for easier pasting)
2. Navigate to **Settings** in **your account** on the top right, then go to **Developer Settings**.
3. Click on Personal access tokens and create a **fine-grained Personal Access Token**.
4. Choose a name, an expiration date, and the repositories to access.
5. Add the **"Contents"** permission and set it to **read-only**.
6. Keep the PAT page open and copy the key.
7. Type "git config --global credential.helper store" in the terminal. This won't result in output.
8. Clone your desired repo by typing "git clone https://....". VSCode will first ask you whether you want to sign in with GitHub online; click No (since this does not allow you to set up pull-only access). Then enter your username, and on the prompt for your password, paste your PAT.
9. Your PAT will now be saved in your credentials storage, meaning you will not have to enter it again on cloning personal repos.

---

## Requesting Applications or Internet Access

If you need access to a specific application or an outbound internet connection that is not currently available in the workspace, let projectteam@icudata.nl know. Some applications require specific domains to be whitelisted in order to function. You can check [this overview](https://lookerstudio.google.com/embed/u/0/reporting/0cba74d6-0573-4675-8bb1-d754c7d88a6a/page/vhAYE) to see which applications have known domain requirements and whether they can be supported out of the box.
