# Ultimate AutoClicker Engine

<p align="center">
  <a href="https://github.com/rorikuqu07421-pixel/Ultimate-AutoClicker-Engine/releases/latest">
    <img src="https://img.shields.io/github/v/release/rorikuqu07421-pixel/Ultimate-AutoClicker-Engine?color=4A90D9&label=Download&style=for-the-badge" alt="Download">
  </a>
  <img src="https://img.shields.io/badge/Platform-Windows%2010%2F11-blue?style=for-the-badge" alt="Windows">
  <img src="https://img.shields.io/badge/Anti--Detection-Enabled-green?style=for-the-badge" alt="Anti-Detection">
  <img src="https://img.shields.io/github/downloads/rorikuqu07421-pixel/Ultimate-AutoClicker-Engine/total?style=for-the-badge&color=orange" alt="Downloads">
</p>

> **Also available on SourceForge:** https://sourceforge.net/projects/ultimate-autoclicker-engine/

---

**Ultimate AutoClicker Engine** is a powerful, open-source autoclicker for Windows — built for gamers and automation enthusiasts. Supports Roblox, Minecraft, CS2, Fortnite, and general Windows tasks.

## ✨ Features

- ⚡ **Ultra-Fast Clicking** — intervals from 1ms, up to 10,000 CPS
- 🎮 **Game Profiles** — Roblox, Minecraft, CS2, Fortnite presets built-in
- 🖥️ **Modern GUI** — Clean Dark / Light mode interface
- 🛡️ **Human-like Randomization** — Smart jitter to avoid anti-cheat detection
- 🖱️ **Multi-Target Support** — Click at multiple screen coordinates
- ⌨️ **Hotkey Control** — Fully customizable (default: F6 toggle)
- 🔄 **Click Types** — Single, Double, Triple click support
- 📋 **Click Recorder** — Record and replay click sequences
- 🔧 **No Installation** — Portable, extract and run

## 📥 Download

**[⬇️ Download Latest Release (v1.1.0)](https://github.com/rorikuqu07421-pixel/Ultimate-AutoClicker-Engine/releases/latest)**

Or download from SourceForge: https://sourceforge.net/projects/ultimate-autoclicker-engine/files/latest/download

## 🚀 Quick Start

1. Download `Ultimate_AutoClicker_Engine_v1.1.0.zip`
2. Extract the archive
3. Run `AutoClicker.exe` as Administrator
4. Set your click interval and target
5. Press **F6** to start / stop

## 🛠️ Build From Source

```bash
git clone https://github.com/rorikuqu07421-pixel/Ultimate-AutoClicker-Engine.git
cd Ultimate-AutoClicker-Engine
pip install -r requirements.txt
python autoclicker.py
```

## ⚙️ Configuration

```bash
# Command-line usage
python autoclicker.py --click-rate 50 --location 960,540 --type single

# Arguments:
#   --click-rate    Interval in ms between clicks (default: 100)
#   --location      X,Y screen coordinates (default: cursor position)
#   --type          Click type: single / double / triple (default: single)
#   --hotkey        Toggle hotkey (default: F6)
#   --randomize     Enable human-like jitter (default: on)
```

## 🎮 Game Profiles

| Game | Preset | CPS | Notes |
|---|---|---|---|
| Roblox | roblox | 14 | Safe for most games |
| Minecraft | minecraft | 16 | Bridging / PvP optimized |
| CS2 | cs2 | 8 | Bhop / auto-buy |
| Fortnite | fortnite | 12 | Building assist |
| General | fast | 100 | No randomization |

## 🛡️ Anti-Detection

The engine uses a multi-layer randomization algorithm:
- **Jitter**: ±0.5–3ms random offset per click
- **Burst patterns**: Natural clustering like human clicking
- **Micro-pauses**: Random 50–200ms pauses every 2–8 seconds
- **Position drift**: Sub-pixel movement between clicks

> ⚠️ Use responsibly. Always check the terms of service of the game or software you are automating.

## 📋 Changelog

### v1.1.0 (2026-04-30)
- ⚡ 40% faster click execution engine
- 🎮 Added game profiles (Roblox, Minecraft, CS2, Fortnite)
- 🖥️ Redesigned GUI with Dark/Light mode
- 🛡️ Improved human-like randomization
- 🔧 Customizable hotkey editor
- 🐛 Fixed click drift on high-DPI displays

### v1.0.0 (2026-04-07)
- Initial release
- Ultra-fast clicking (1ms intervals)
- Human-like randomization
- Hotkey support (F6)
- Single / Double / Triple click types

## 📄 License

MIT License — see [LICENSE](LICENSE) for details.

---

<p align="center">
  ⭐ Star this repo if it helped you! · <a href="https://github.com/rorikuqu07421-pixel/Ultimate-AutoClicker-Engine/issues">Report Issues</a> · <a href="https://sourceforge.net/projects/ultimate-autoclicker-engine/">SourceForge Mirror</a>
</p>
