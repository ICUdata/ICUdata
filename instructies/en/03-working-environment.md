# 3. Working environment

You work on the Linux desktop that opens after you log in ([2. Start the VM and log in](02-start-and-log-in.md)).

## VSCode

Open the "Terminal Emulator" from the start menu in the top left and type `code`. This starts the latest version of VSCode on the Linux VM.

We recommend turning on Auto-save in VSCode: click "File" and then "Autosave".

## The database

The read-only ICUdata database is at `/home/ICUdata`. DuckDB is a database format designed for research. It can be queried with SQL, but it is not hosted like other SQL databases: it is a single file that contains all the data, and you work with it through the DuckDB packages. The [Database Guide](database-guide.md) describes the tables and gives query examples.

## Python

Python is installed on the Linux VM. To install specific Python packages, create a virtual environment (`.venv`) in your project directory and use `pip` or another package manager.

## R

RStudio Server runs on the Linux VM, on port 8005. On the Linux desktop, open a web browser and go to `http://localhost:8005`. If that does not work, use the route in [6. Windows VM and SSH](06-windows-vm-and-ssh.md) and let us know at projectteam@icudata.nl.

## Applications

The Linux VM has `git`, `pip`, `pipx`, `uv`, `conda`, `poetry`, `pyenv`, the DuckDB command line interface, and Python installed. If a package you need cannot be downloaded through pip or pipx, contact us to see whether we can make it available.

**Note:** Not all of these tools have been widely tested. If you run into any issues, please e-mail projectteam@icudata.nl.

Next: [4. Network and GitHub](04-network-and-github.md)
