
#region Imports
from pynput import keyboard
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject, Qt
import pygetwindow as gw
import pyperclip
import pyautogui
import time
import sys
import ctypes
#endregion
#region SYMBOLS
SYMBOLS = {
    "Logic": ["∧ - and (conjunction)", "∨ - or (disjunction)", "¬ - not (negation)", "→ - implies (implication)", "↔ - if and only if (biconditional)", "⊕ - exclusive or (xor)", "↓ - nor (negation of or)", "↑ - nand (negation of and)"],
    "Quantifiers": ["∀ - for all", "∃ - there exists", "∄ - there does not exist", "∴ - therefore", "∵ - because"],
    "Set Theory": ["∈ - element of", "∉ - not element of", "⊆ - subset of", "⊂ - proper subset of", "⊇ - superset of", "⊃ - proper superset of", "∪ - union", "∩ - intersection", "∅ - empty set", "△ - symmetric difference", "× - Cartesian product", "∁ - complement"],
    "Relations": ["= - equal to", "≠ - not equal to", "≡ - equivalent to", "≢ - not equivalent to", "≤ - less than or equal to", "≥ - greater than or equal to", "≺ - precedes", "≻ - succeeds", "∼ - similar to", "≅ - congruent to", "∣ - divides", "∤ - does not divide"],
    "Proof": ["⊢ - proves", "⊨ - models", "⊥ - contradiction", "⊤ - tautology", "□ - necessarily"],
    "Number Sets": ["ℕ - natural numbers", "ℤ - integers", "ℚ - rational numbers", "ℝ - real numbers", "ℂ - complex numbers", "ℙ - prime numbers"],
    "Functions": ["∘ - composition", "↦ - maps to", "⌊ - floor", "⌋ - floor", "⌈ - ceiling", "⌉ - ceiling"],
    "Arithmetic": ["· - multiplication", "÷ - division", "Σ - summation", "Π - product", "√ - square root", "∞ - infinity"],
    "Combinatorics": ["! - factorial", "… - ellipsis"],
    "Presets": ["P(x)", "Q(x)", "R(x)", "∀x ∈ ℕ", "∃x ∈ ℕ", "∀x(P(x) → Q(x))", "∃x(P(x) ∧ Q(x))", "P(x) ∧ Q(x)", "P(x) ∨ Q(x)", "¬P(x)", "A ⊆ B", "A ∪ B", "A ∩ B", "f: A → B", "n ≡ k (mod m)", "∑ᵢ₌₁ⁿ", "n!"]
}
#endregion
#region FUNCTION
class Communicator(QObject):
    trigger = pyqtSignal()

class PopupWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Math Keyboard")
        self.setFixedSize(300, 400)
        self.setWindowFlags(Qt.Tool | Qt.WindowStaysOnTopHint)
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        controls = QLabel("W/S: navigate | E: select | Q: back/close")
        controls.setAlignment(Qt.AlignCenter)
        layout.addWidget(controls)
        
        self.list_widget = QListWidget()    
        layout.addWidget(self.list_widget)  
        
        quit_button = QPushButton("Quit")
        quit_button.clicked.connect(sys.exit)
        layout.addWidget(quit_button)

        self.list_widget.setFocusPolicy(Qt.NoFocus)
        self.setFocus()
        
        self.level = "categories"
        
        self.show_categories()
    
    def show_categories(self):
        self.level = "categories"
        self.list_widget.clear()
        for category in SYMBOLS.keys():
            self.list_widget.addItem(category)
        self.list_widget.setCurrentRow(0)
    
    def show_symbols(self, category):
        self.level = "symbols"
        self.current_category = category
        self.list_widget.clear()
        for symbol in SYMBOLS[category]:
            self.list_widget.addItem(symbol)
        self.list_widget.setCurrentRow(0)
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            if self.level == "symbols":
                self.show_categories()
            else:
                self.hide()
        
        elif event.key() == Qt.Key_E:
            selected = self.list_widget.currentItem().text()
            if self.level == "categories":
                self.show_symbols(selected)
            
            elif self.level == "symbols":
                selected = self.list_widget.currentItem().text()
                symbol_only = selected.split(" ")[0]
                if previous_window:
                    previous_window.activate()
                time.sleep(0.1)
                pyperclip.copy(symbol_only)
                pyautogui.hotkey('ctrl', 'v')
        
        elif event.key() == Qt.Key_S:
            current = self.list_widget.currentRow()
            next_row = (current + 1) % self.list_widget.count()
            self.list_widget.setCurrentRow(next_row)
        elif event.key() == Qt.Key_W:  
            current = self.list_widget.currentRow()
            prev_row = (current - 1) % self.list_widget.count()
            self.list_widget.setCurrentRow(prev_row)
    
    def closeEvent(self, event):
        event.ignore()
        self.hide()

current_keys = set()
previous_window = None

def open_popup():
    global previous_window
    previous_window = gw.getActiveWindow()
    window.show_categories()
    screen = QApplication.primaryScreen().geometry()
    window.move(screen.width() - window.width() - 20, 20)
    window.show()
    window.raise_()
    window.activateWindow()
    window.setFocus()
    hwnd = int(window.winId())
    foreground_thread = ctypes.windll.user32.GetWindowThreadProcessId(
        ctypes.windll.user32.GetForegroundWindow(), None
    )
    current_thread = ctypes.windll.kernel32.GetCurrentThreadId()
    ctypes.windll.user32.AttachThreadInput(foreground_thread, current_thread, True)
    ctypes.windll.user32.SetForegroundWindow(hwnd)
    ctypes.windll.user32.AttachThreadInput(foreground_thread, current_thread, False)
    window.setFocus()

app = QApplication(sys.argv)
window = PopupWindow()

comm = Communicator()
comm.trigger.connect(open_popup)

def on_press(key):
    current_keys.add(key)
    if keyboard.Key.ctrl_l in current_keys and key == keyboard.Key.space:
        comm.trigger.emit()

def on_release(key):
    try:
        current_keys.discard(key)
    except KeyError:
        pass

listener = keyboard.Listener(on_press=on_press, on_release=on_release)
listener.start()

sys.exit(app.exec_())
#endregion