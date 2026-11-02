# 5. Data and code

## Uploading data into MyDRE

1. Log in at mydre.org with your personal @mydre.org account.
2. Open your ICUdata workspace.
3. Go to "Files".
4. Click "Upload files". The folder you pick does not matter: every upload goes to an inbox.
5. Upload the files:
   - directly from your computer, for relatively small files; or
   - with Azure Storage Explorer, for large files. Install Azure Storage Explorer on your computer first.
6. After a few minutes you receive a confirmation e-mail.

On the Linux VM, the upload arrives in `/mnt/inbox` or `/mnt/data/inbox`, in a folder named `transfer-<date>-<time>-<username>`. When it has arrived, move that folder out of the inbox, for example to your own folder, so that only new uploads stay in the inbox:

```
mv /mnt/inbox/transfer-<date>-<time>-<username> ~/
```

`mv` moves a file or folder. The first part is the folder in the inbox; `~/` is your home folder. If your upload is in `/mnt/data/inbox`, use that path instead.

## Code

The best way to work with code:

1. Write your code on your own PC and push it to GitHub.
2. On the Linux VM, pull it from GitHub and run it there. [GitHub access](04-network-and-github.md#github-access) in guide 4 describes how to set up pull-only access.

We ask you not to push from the VM to GitHub.

This works the same for R: keep your R scripts in a Git repository, pull them on the VM with `git pull` (or with the Git pane in RStudio), and run them there. You can install packages on the VM; see [3. Working environment](03-working-environment.md).

## Getting results out of MyDRE

Because we ask you not to push from the VM, results leave MyDRE through the outbox:

1. Make a new folder for this export in `/mnt/data/outbox` and put the files in it. With many files, pack them into one file first, for example:
   ```
   mkdir /mnt/data/outbox/<export-name>
   tar -czf /mnt/data/outbox/<export-name>/<export-name>.tar.gz <your-folder>
   ```
   `mkdir` makes the folder. `tar` packs files into one file: `-c` creates a new file, `-z` compresses it, and `-f` gives the file name that follows. `<your-folder>` is the folder with your files.
2. In MyDRE, open your workspace and click "Files".
3. Find the files and click "Request download".

We approve the request as soon as possible.

Next, only if you need the Windows VM: [6. Windows VM and SSH](06-windows-vm-and-ssh.md)
