# kiqkuk's Dotfiles

Minimalist Wayland environment based on **dwl**, **somebar**, and **someblocks** on Arch Linux.

## Key Features
* **Custom Patches:** Tailored builds for dwl, somebar, and someblocks.
* **Signal Integration:** Real-time status bar updates via RTMIN signals.
* **Hardened Shell:** Modular Bash configuration.

## Setup
1. Clone the repository.
2. Symlink or copy `bash/config` to your `.bashrc`.
3. Apply patches found in `patches/` to the respective source directories.
4. Ensure `scripts/` is in your `$PATH`.

## Dependencies
- **Terminal:** foot
- **Status:** someblocks, somebar
- **Utils:** xorgproto (for multimedia keys), acpid
