# 4. Network and GitHub

## Network restrictions

Outbound connections are only allowed to GitHub and package managers.

## GitHub access

To prevent accidental exposure of medical data, we advise using GitHub with a **Personal Access Token (PAT)** configured for pull-only access:

1. Go to your GitHub account on [github.com](https://github.com). You can do this in the MyDRE environment, so that pasting the token later is easier.
2. Go to **Settings** in **your account** in the top right, then to **Developer Settings**.
3. Click on Personal access tokens and create a **fine-grained Personal Access Token**.
4. Choose a name, an expiration date, and the repositories to access.
5. Add the **"Contents"** permission and set it to **read-only**.
6. Keep the PAT page open and copy the key.
7. Type `git config --global credential.helper store` in the terminal. This gives no output.
8. Clone your repository by typing `git clone https://....`. VSCode first asks whether you want to sign in with GitHub online; click No, because that does not allow you to set up pull-only access. Then enter your username, and when asked for your password, paste your PAT.
9. Your PAT is now saved in your credentials storage, so you do not have to enter it again when you clone your own repositories.

## Requesting applications or internet access

If you need access to a specific application or an outbound internet connection that is not available in the workspace, let projectteam@icudata.nl know. Some applications only work if specific domains are whitelisted. You can check [this overview](https://lookerstudio.google.com/embed/u/0/reporting/0cba74d6-0573-4675-8bb1-d754c7d88a6a/page/vhAYE) to see which applications have known domain requirements and whether they can be supported without changes.

For a VM with a GPU, more processor cores or memory, or no automatic shutdown, see [When to contact us](02-start-and-log-in.md#when-to-contact-us).

Next, only if you need the Windows VM: [5. Windows VM and SSH](05-windows-vm-and-ssh.md)
