# MathKey ⌨️

> A system-wide discrete math and logic symbol picker for Windows. Insert any symbol into any application in seconds — no LaTeX knowledge required.

---

## The Problem

Typing discrete math symbols is a pain. You either need to memorize verbose LaTeX commands like `\leftrightarrow`, hunt through character maps, or copy-paste from a browser tab. None of these options are fast, and none of them work everywhere.

MathKey fixes this. One chord opens a keyboard-navigable popup. Two keys navigate it. One key selects. The symbol appears wherever your cursor is — in Google Docs, Notepad, Word, a browser, anywhere.

---

## Features

- **System-wide** — works in any application on Windows
- **Keyboard-only navigation** — W/S to move, Enter to select, Escape to go back
- **Two-level symbol tree** — browse by category, then pick your symbol
- **Preset phrases** — common discrete math expressions ready to insert
- **Zero friction** — toggle the plugin on/off with a hotkey so it never gets in your way
- **No LaTeX required** — outputs real unicode characters that work everywhere

---

## Symbol Categories

| Category | Examples |
|---|---|
| Logic | ∧ ∨ ¬ → ↔ ⊕ |
| Quantifiers | ∀ ∃ ∄ ∴ ∵ |
| Set Theory | ∈ ∉ ⊆ ∪ ∩ ∅ |
| Relations | ≡ ≠ ≤ ≥ ∣ ∤ |
| Proof | ⊢ ⊨ ⊥ ⊤ □ |
| Number Sets | ℕ ℤ ℚ ℝ ℂ ℙ |
| Functions | ∘ ↦ ⌊ ⌋ ⌈ ⌉ |
| Arithmetic | Σ Π √ ∞ · ÷ |
| Combinatorics | ! … |
| Presets | ∀x(P(x) → Q(x)), f: A → B, n ≡ k (mod m) |

---

## Installation (I will implement an easier method as I revisit this)

**Requirements:** Python 3.8+, Windows

**1. Clone the repo**
```
git clone https://github.com/yourusername/mathkey.git
cd mathkey
```

**2. Install dependencies**
```
pip install pynput pyqt5 pygetwindow pyperclip pyautogui
```

**3. Run**
```
python main.py
```

---

## Usage

| Action | Key |
|---|---|
| Open popup | Ctrl + Space |
| Navigate down | S |
| Navigate up | W |
| Select / Enter category | E |
| Go back to categories | Escape/Q |
| Close popup | Escape (from category level) |

**Workflow:** Click into wherever you want to type → press Ctrl+Space → navigate to your symbol → press Enter → symbol appears.

---

## How It Works

MathKey runs as a lightweight background process. When you trigger the hotkey, it records which window you were focused on, opens the popup, and when you select a symbol it restores focus to your previous window and pastes the character automatically. No clicking required at any point.

The symbol tree is stored as a Python dictionary, making it easy to add, remove, or reorder symbols and categories.

---

## Planned Features

- Search bar for fuzzy symbol lookup
- Recently used symbols section
- Starred / favorites
- Adaptive ordering based on usage frequency
- LaTeX output mode (toggle between unicode and `\forall` style commands)
- Customizable keybinds
- Chrome extension version

---

## Built With

- [Python](https://python.org)
- [PyQt5](https://pypi.org/project/PyQt5/) — popup UI
- [pynput](https://pypi.org/project/pynput/) — global hotkey listening
- [pyautogui](https://pypi.org/project/pyautogui/) — simulated paste
- [pygetwindow](https://pypi.org/project/PyGetWindow/) — focus management
- [pyperclip](https://pypi.org/project/pyperclip/) — clipboard

---

## Author

Built at PearlHacks 2026 by Addam Dano — CS Student, UNC Chapel Hill
