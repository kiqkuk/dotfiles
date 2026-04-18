# Miru

A minimalist collection of system configurations and source code for daily workflow.
Focused on Arch Linux and Wayland (dwl).

*Miru is the name of my cat. I built this repository as a tribute to remember Miru, serving as the system I live in every day.*

## Structure
- `bin/`: Modular scripts and status bar utilities.
- `config/`: User application configurations (foot, qutebrowser, zsh, etc.).
- `etc/`: Core system configurations (nftables, sysctl, acpi).
- `pkg/`: Modified source code (dwl, somebar, someblocks).
- `data/`: Package lists (`pkglist.txt`) and shell environment.

## Installation
Ensure all dependencies listed in `data/pkglist.txt` are installed.

```bash
# Clone
git clone git@github.com:kiqkuk/miru.git ~/.local/share/miru

# Build & Deploy
cd ~/.local/share/miru
./bin/deploy

## Note on System Configs:
Files inside the `etc/` directory are currently not included in the `deploy` script. You must copy them manually. Most of these configurations are highly specific to my current hardware/device.
