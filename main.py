
#region Imports
from pynput import keyboard
from PyQt5.QtWidgets import QApplication, QWidget, QListWidget, QVBoxLayout, QLabel, QPushButton
from PyQt5.QtCore import pyqtSignal, QObject, Qt
import pygetwindow as gw
import pyperclip
import pyautogui
import time
import sys
#endregion
#region SYMBOLS
SYMBOLS = {
    "Logic": ["∧", "∨", "¬", "→", "↔", "⊕", "↓"],
    "Quantifiers": ["∀", "∃", "∄", "∴", "∵"],
    "Set Theory": ["∈", "∉", "⊆", "⊂", "⊇", "⊃", "∪", "∩", "∅", "△", "×", "∁"],
    "Relations": ["=", "≠", "≡", "≢", "≤", "≥", "≺", "≻", "∼", "≅", "∣", "∤"],
    "Proof": ["⊢", "⊨", "⊥", "⊤", "□"],
    "Number Sets": ["ℕ", "ℤ", "ℚ", "ℝ", "ℂ", "ℙ"],
    "Functions": ["∘", "↦", "⌊", "⌋", "⌈", "⌉"],
    "Arithmetic": ["·", "÷", "Σ", "Π", "√", "∞"],
    "Combinatorics": ["!", "…"],
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
        
        layout = QVBoxLayout()
        self.setLayout(layout)
        
        controls = QLabel("W/S: navigate | Enter: select | Q: back/close")
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
        
        elif event.key() == Qt.Key_Return:
            selected = self.list_widget.currentItem().text()
            
            if self.level == "categories":
                self.show_symbols(selected)
            
            elif self.level == "symbols":
                self.hide()
                if previous_window:
                    previous_window.activate()
                time.sleep(0.1)
                pyperclip.copy(selected)
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
    window.show()
    window.raise_()
    window.activateWindow()

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