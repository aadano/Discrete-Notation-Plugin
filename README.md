# MathKey ⌨️

> A system-wide discrete math and logic symbol picker for Windows. Insert any symbol into any application in seconds — no LaTeX knowledge required.

---

**Important: Upon running the program, nothing will show up at first. Press Ctrl + Space to open the popup!**

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

## Installation

**Requirements:** Python 3.8+, Windows

1. Go to the [Releases](link to your releases page) page
2. Download `MathKey.exe`
3. Run it — no installation required

> Windows may show a SmartScreen warning. Click "More info" then "Run anyway." 
> The full source code is available above if you'd like to verify it yourself.

### Option 2: Run from source
1. Clone the repo
2. Install Python 3.8+
3. Run `python -m pip install pynput pyqt5 pygetwindow pyperclip pyautogui`
4. Run `python main.py`

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
