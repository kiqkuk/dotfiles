# BASELINE SYSTEM DECISIONS
IdeaPad 3 14ITL6 - Arch Linux

---
## Filesystems & Storage {{{
**STATUS:** BASELINE
**DECISION:**
- `btrfs` for root filesystems
- EFI: `vfat`
- subvolume layout (implisit): `/`, `/home`, `/var/log`, `/.snapshots`

**MOUNT OPTIONS (global):**

    rw,noatime,compress=zstd:3,ssd,discard=async,space_cache=v2

**EXCEPTIONS:**
- `/var/log` -> `chattr +C` (nocow)
**RATIONALE:**
- rollback & snapshot capability to experiments
- zstd:3 = safe compromise
- CoW is disabled only on write-hot paths
**LEARNING:**
- SSD wear issues were caused by CoW misuse, not btrfs itself
- snapshots are not a substitute for backups and are not a solution to ABI mismatch }}}
---
## Initramfs & Boot {{{
**STATUS:** BASELINE
**DECISION:**
- initramfs: `booster`
- kernel: `linux` (mainline)
- bootloader: `systemd-boot`
**RATIONALE:**
- booster: small image size (~4MB), fast build
- systemd-boot: sufficient, deterministic, minimal state
**ASSUMPTION CHECK:**
- no need for exotic hooks
- single-disk, no LUKS/LVM complexity (for now) }}}
---
## Networking Stack {{{
**STATUS:** BASELINE
### Wi-Fi
- `iwd` for backend
- MAC randomization: enabled
### DNS
- `systemd-resolved`
- DNSOverTLS = `opportunistic`
- DNSSEC = `yes`
**RATIONALE:**
- strict DoT not realistic for mobile networks
- opportunistic = tradeoff stability vs security
**LEARNING:**
- network hardening **should be contextual**, not absolute }}}
---
## Firewall & Kernel Hardening {{{
**STATUS:** BASELINE
### Firewall
- `nftables`
- policy: drop (input, forward)
- explicit allow:
    - loopback
    - established/related
    - ICMP/ICMPv6
    - DHCP
    - DNS
**RATIONALE:**
- default-drop without DHCP/DNS = "safe but dead" system
- explicit > implicit
### sysctl
- IPv4 + IPv6
- `all` and `default`
**LEARNING:**
- `default` interfaces is often forgotten -> subtle bug }}}
---
## Memory Management {{{
**STATUS:** BASELINE
- `zram-generator`
- size = RAM / 2
- compression = `zstd`
- high priority
**RATIONALE:**
- laptop workload
- diskless swap is more predictable
- no extreme tuning }}}
---
## Privilege Escalation {{{
**STATUS:** BASELINE
- `sudo` (default Arch)
**REJECTED DECISION:**
- `doas`
**RATIONALE:**
- sudo is the ecosystem assumption in Arch
- replace = maintenance costs > benefits
**LEARNING:**
- minimalism != fewer packages
- minimalism = fewer *surprises* }}}
---
## Desktop / Userland {{{
**STATUS:** BASELINE
- compositor: `dwl`
- toolchain: self-built (`somebar`, `someblocks`)
- font: `ttf-hack-nerd`
**NOTE:**
- DE setup is considered **userland**, not core infra
- userland changes do not require baseline log entries }}}
---
## Tooling & Editor {{{
**STATUS:** BASELINE
- `neovim` (0.12.x)
- plugin manager: `vim.pack`
- philosophy: minimal, on-demand
**ASSUMPTION:**
- config editor **is not** a system dependency
- can be reset without any effect on the OS }}}
---
# META-DECISION
```
Baseline is defined by:
- survives reinstall
- minimal surprise
- low maintenance cost
```
experiments are **allowed**, but
- must be able to be thrown away without leaving any residue
- must leave *learning*, not config zombie
**EVALUATION CRITERIA**
- reinstall-safe
- predictable behavior
- ecosystem-compatible }}}

---

# SYSTEM LOG
IdeaPad 3 14ITL6 - Arch Linux

---

## [2026-04-06] - input fix (ghostkey) {{{

[RETIRED]

### CONTEXT
- scancode `0x56` (KEY_102ND) spamming
- causing log spam and input noise

### DECISION
- deploy udev rule to suppress scancode
- source: `~/dots/system/udev/` -> `/etc/udev/`

### RATIONALE
- fix at the lowest level (input layer)
- avoiding workarounds in userland

### OUTCOME
- udev hwdb does not completely suppress log spam

### LEARNING
- not all input issues can be resolved in udev

### STATUS
- superseded }}}

---

## [2026-04-07] - networking stack hardening {{{

[BASELINE]

### CONTEXT
- fresh system setup
- laptop wi-fi needs + DNS security

### DECISION
- Wi-Fi: `iwd`
- DNS: `systemd-resolved`
- enable DoT & DNSSEC

### RATIONALE
- native systemd stack
- systemd default first before trying alternatives

### OUTCOME
- stable network on static connection
- intermittent DNS failure on mobile network

### LEARNING
- absolute hardening is not suitable for mobile context

### STATUS
- partially revised }}}

---

## [2026-04-07] firewall & kernel hardening {{{

[BASELINE]

### CONTEXT
- add protection with firewall
- use existing tools, keep it minimal

### DECISION
- create custom sysctl config `99-hardening.conf`
- enable nftables

### RATIONALE
- config template is good enough

### OUTCOME
- can connect to internet but ping no response

### LEARNING
- config template is too strict

### STATUS
- partially revised }}}

---

## [2026-04-07] desktop environment {{{

[BASELINE]

### CONTEXT
- previously used `dwm` but wanted to move to `wayland`

### DECISION
- use `dwl` - dwm for wayland

### RATIONALE
- manual build and can install patches, feels the same as dwm

### OUTCOME
- no status bar, so added somebar and someblocks

### LEARNING
- somebar build uses ninja

### STATUS
- active }}}

---

## [2026-04-08] - ghost key mitigation via systemd {{{

[BASELINE]

### CONTEXT
- udev approach failed to stop log spam

### DECISION
- migrate mitigation to dedicated systemd service
- service: `fix-ghostkey.service`

### RATIONALE
- systemd service provides lifecycle control
- more predictable than hwdb hack

### OUTCOME
- spam log stop
- spam input stop

### LEARNING
- systemd is better suited for mitigating runtime hardware quirks

### STATUS
- active }}}

---

## [2026-04-08] - migrate to doas {{{

[EXPERIMENT]

### CONTEXT
- interest in reducing privilege escalation footprint

### DECISION
- replace sudo with doas
- add sudo wrapper for compatibility

### RATIONALE
- doas is small and simple

### OUTCOME
- increasing maintenance burden
- conflict with Arch tooling

### LEARNING
- sudo is the ecosystem assumption in Arch

### STATUS
- reverted }}}

---

## [2026-04-08] initramfs migration {{{

[EXPERIMENT]

### CONTEXT
- interest in reducing initramfs size

### DECISION
- replace `mkinitcpio` with `booster`

### RATIONALE
- automatic host configuration discovery

### OUTCOME
- build is fast and the image size is smaller
- can boot into the system

### LEARNING
- need busybox to fallback to emergency mode

### STATUS
- promoted-to-baseline }}}

---

## [2026-04-08] pam & d-bus cleanup {{{

[EXPERIMENT]

### CONTEXT
- persistent log spam `activation request for `org.freedesktop.home1` failed` during login

### DECISION
- hard-disabled `pam_systemd_home.so` in `/etc/pam.d/system-auth`

### RATIONALE
- turn off request to stop request

### OUTCOME
- spam activation request no longer appears

### LEARNING
- reinstalling using the old `@home` subvol can cause a situation like this

### STATUS
- reverted }}}

---

## [2026-04-08] zram {{{

[BASELINE]

### CONTEXT
- ram management without swap partition

### DECISION
- `zram-generator`

### RATIONALE
- integrated with systemd
- compression = zstd

### OUTCOME
- swap active
- no performance measurements yet

### LEARNING
- swap memory not only from partitions and files

### STATUS
- active }}}

---

## [2026-04-10] - DNS hardening refactor {{{

[BASELINE]

### CONTEXT
- DoT strict causes DNS failures on certain networks

### DECISION
- `DNSOverTLS=yes` -> `opportunistic`

### RATIONALE
- prefer availability over strictness
- still get security benefits if available

### OUTCOME
- stable connection
- git clone HTTPS success

### LEARNING
- security policy must degrade gracefully

### STATUS
- active }}}

---

## [2026-04-10] - refactor sysctl {{{

[BASELINE]

### CONTEXT
- add `default` interface sysctl to cover newly created interfaces

### DECISION
- `net.ipv4.conf.default.accept_redirects = 0`, `net.ipv6.conf.default.accept_redirects = 0`

### RATIONALE
- potential subtle bug

### OUTCOME
- config is more predictable

### LEARNING
- `default` interface is often forgotten

### STATUS
- active }}}

---

## [2026-04-10] - refactor nftables {{{

[BASELINE]

### CONTEXT
- default-drop policy blocked DHCP/DNS under certain conditions

### DECISION
- explicit allow: DHCP (udp 67/68) and DNS

### RATIONALE
- explicit > implicit

### OUTCOME
- reliable DHCP and DNS connections

### LEARNING
- server setup is not suitable on laptop

### STATUS
- active }}}

---

## [2026-04-10] - suspend instant wake fix (serio0) {{{

[BASELINE]

### CONTEXT
- system resume immediately after suspend (s2idle)
- wake_sources shows high event_count on serio0
- known ghostkey on scancode 0x56

### DECISION
- disable wakeup on i8042 serio0
- path: `/sys/devices/platform/i8042/serio0/power/wakeup`

### RATIONALE
- input remap does not stop hardware interrupt
- wakeup must be blocked at controller level

### OUTCOME
- suspend is stable stable and predictable

### STATUS
- active }}}

---

## [2026-04-10] - baseline snapshot created {{{

[BASELINE]

### CONTEXT
- system state considered stable and predictable
- suspend, network, and storage validated

### DECISION
- create read-only btrfs snapshot
- snapshot name: 2026-04-10-baseline

### RATIONALE
- provide rollback anchor for future experiments
- snapshot is reference, not daily recovery tool

### STATUS
- active (read-only) }}}

---

<!-- vim: set foldmethod=marker foldmarker={{{,}}} foldlevel=0 : -->
