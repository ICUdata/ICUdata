# 2. Start the VM and log in

## The two VMs

The ICUdata workspace has two virtual machines (VMs):

- **Linux VM**: the VM everyone works on. It contains a dedicated drive with user-specific data, and the read-only DuckDB database at `/home/ICUdata`, which contains ICUdata.
- **Windows VM**: at most 2 users can use it at the same time (a Microsoft limit). The Linux VM has no such limit, so everyone uses the Linux VM. Use the Windows VM only if you need it; see [5. Windows VM and SSH](05-windows-vm-and-ssh.md).

## Start the Linux VM

Start only the **Linux VM** in your MyDRE workspace.

## Log in

1. When you open the Azure screen, click the dropdown where it says "Microsoft Entra ID" and select "VM password".
2. Enter your MyDRE e-mail address as the username and your password as the password.
3. Click **RDP** (for the Linux VM).

Then the Linux desktop opens.

## Shut down the Linux VM

The VMs shut down automatically. We ask users to shut down the VM when it is not in use.

Before you shut down the Linux VM, check whether others are logged in: run `loginctl list-users` in the Terminal Emulator. If it lists anyone besides you, leave the VM running.

## When to contact us

Contact projectteam@icudata.nl if:

- you run a long process and need the automatic shutdown turned off;
- you need a VM with a GPU;
- you need a VM with more processor cores or memory;
- Spot evictions keep stopping your program after several tries. The VMs are Azure Spot VMs, which Azure can stop when it needs the capacity elsewhere (an "eviction").

Next: [3. Working environment](03-working-environment.md)
