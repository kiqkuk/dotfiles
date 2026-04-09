# SYSTEM LOG - IdeaPad 3 14ITL6 (82H7)

## [2026-04-06] - initial recovery & hardening
### input fix (ghostkey)
- **issue:**  scancode `0x56` (KEY_102ND) spamming.
- **src:**      `~/dots/system/udev/`
- **target:**   `/etc/udev/`
- **verify:**   `sudo udevadm info /dev/input/eventX` | `libinput debug-events` 

---

## [2026-04-07] - networking & security
### network core (iwd & resolved)
- **configs:**
    - `iwd`:    `~/dots/system/iwd/main.conf` -> `/etc/iwd/main.conf` (MAC randomization)
    - `resolved`:   `~/dots/system/systemd/resolved.conf` -> `/etc/systemd/resolved.conf` (DoT)
- **verify:**   `resolvectl status` (Check +DOT) | `iwctl device list`

### kernel & firewall hardening
- **sysctl:**   `~/dots/system/sysctl.d/99-hardening.conf` -> `/etc/sysctl.d/`
- **nftables:** native config (Policy DROP, No SSH)
- **verify:**   `sudo nft list ruleset` | `sudo sysctl --system`

### Desktop Environment (DWL)
- **Repo:** `~/projects/dwl` & `someblocks` & `somebar`
- **Note:** compiled with custom `config.h` and patches.

---

## [2026-04-08] - system stability & optimization
### ghost key fix mitigation
- **issue:**  `udev` hwdb rules failed to suppress log spam.
- **action:**   migrated fix to a dedicated systemd service
- **src:**      `~/dots/system/systemd/system/fix-ghostkey.service` -> `/etc/systemd/system/fix-ghostkey.service`

### initramfs migration (booster)
- **issue:**  `mkinitcpio` build process was inefficient and output size was too bulky (~20MB)
- **action:**   migrated to `booster`. configured `/etc/booster.yaml` with `strip: true` and `compression: zstd`
- **result:**   initramfs image size reduzed to **4MB**

### migrate to doas
- **action:**   replaced `sudo` with `doas` for a smaller footprint
- **config:**   `/etc/doas.conf` with `permit persist :wheel`
- **tweak:**    created wrapper at `/usr/local/bin/sudo` to `exec doas "$@"`

### pam & d-bus cleanup
- **issue:**    persistent log spam `activation request for `org.freedesktop.home1` failed` during login
- **fix:**      hard-disabled `pam_systemd_home.so` in `/etc/pam.d/system-auth`

### zram
- **action:**   deployed `zram-generator` using `zstd` compression algorithm

---


