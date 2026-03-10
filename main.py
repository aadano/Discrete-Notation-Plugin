
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
SYMBOLSFORAPPENDIX = {
    "Limits": ["lim - limit", "→ - approaches", "∞ - infinity", "lim⁺ - right-hand limit", "lim⁻ - left-hand limit", "∞⁺ - positive infinity", "∞⁻ - negative infinity", "≈ - approximately equal to", "∼ - asymptotically equal to", "o - little-o (grows slower than)", "O - big-O (grows no faster than)"],
    "Derivatives": ["′ - prime (first derivative)", "″ - double prime (second derivative)", "‴ - triple prime (third derivative)", "∂ - partial derivative", "d - differential", "δ - variation / small change", "Δ - finite difference", "∇ - nabla / gradient", "D - differential operator", "df/dx - derivative of f w.r.t. x", "∂f/∂x - partial derivative of f w.r.t. x"],
    "Integrals": ["∫ - integral", "∬ - double integral", "∭ - triple integral", "∮ - line integral (closed curve)", "∯ - surface integral (closed surface)", "∰ - volume integral", "⨌ - quadruple integral", "dx - differential element"],
    "Series & Sequences": ["Σ - summation", "Π - product", "aₙ - sequence term", "Sₙ - partial sum", "R - radius of convergence"],
    "Multivariable": ["∇ - gradient", "∇· - divergence", "∇× - curl", "∇² - Laplacian", "∂²f/∂x² - second partial derivative", "∂²f/∂x∂y - mixed partial derivative", "J - Jacobian", "H - Hessian"],
    "Vector Calculus": ["· - dot product", "× - cross product", "‖ - norm / magnitude", "û - unit vector", "r⃗ - position vector", "F⃗ - vector field", "ds - arc length element", "dA - area element", "dV - volume element", "n̂ - outward unit normal"],
    "Differential Equations": ["y′ - first derivative of y", "y″ - second derivative of y", "ẏ - time derivative (dot notation)", "ÿ - second time derivative", "λ - eigenvalue", "e - Euler's number", "W - Wronskian", "ℒ - Laplace transform", "ℱ - Fourier transform"],
    "Special Functions": ["Γ - Gamma function", "Β - Beta function", "ζ - Zeta function", "erf - error function", "ln - natural logarithm", "log - logarithm", "sin - sine", "cos - cosine", "tan - tangent", "arcsin - inverse sine", "arccos - inverse cosine", "arctan - inverse tangent", "sinh - hyperbolic sine", "cosh - hyperbolic cosine", "tanh - hyperbolic tangent"],
    "Number Sets": ["ℝ - real numbers", "ℂ - complex numbers", "ℝⁿ - n-dimensional real space", "ℝ² - 2D real plane", "ℝ³ - 3D real space", "i - imaginary unit", "π - pi", "e - Euler's number", "φ - golden ratio"],
    "Presets": ["lim_{x→a} f(x)", "lim_{x→∞} f(x)", "lim_{x→0} (sin x)/x = 1", "f′(x) = lim_{h→0} (f(x+h)-f(x))/h", "∫ f(x) dx", "∫ₐᵇ f(x) dx", "∂f/∂x", "∂²f/∂x∂y", "∇f(x,y)", "∇·F⃗", "∇×F⃗", "∑ₙ₌₁^∞ aₙ", "∑ₙ₌₀^∞ xⁿ/n!", "f(x) = f(a) + f′(a)(x-a) + f″(a)(x-a)²/2! + …", "∫∫_D f(x,y) dA", "∮_C F⃗·dr⃗", "dy/dx + P(x)y = Q(x)"]
}
# SYMBOLSFORAPPENDIX = 
# SYMBOLSFOROTHERAPPENDIX = 
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
        
        controls = QLabel("WASD: navigate | E: select | Q: back/close")
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
    
    def show_appendix(self,category):
        self.level = "appendix"
        self.list_widget.clear()
        for category in SYMBOLSFORAPPENDIX.keys():
            self.list_widget.addItem(category)
        self.list_widget.setCurrentRow(0)
    
    def show_appendix_symbols(self, category):
        self.level = "appendix_symbols"
        self.current_category = category
        self.list_widget.clear()
        for symbol in SYMBOLSFORAPPENDIX[category]:
            self.list_widget.addItem(symbol)
        self.list_widget.setCurrentRow(0)
        
    def show_otherappendix(self,category):
        self.level = "otherappendix"
        self.list_widget.clear()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Q:
            selected = self.list_widget.currentItem().text()
            if self.level == "symbols" or self.level == "appendix" or self.level == "otherappendix":
                self.show_categories()
            elif self.level == "appendix_symbols":
                self.show_appendix(selected)
            else:
                self.hide()

        elif event.key() == Qt.Key_A:
            if self.level == "categories":
                selected = self.list_widget.currentItem().text()
                self.show_otherappendix(selected)
            elif self.level == "appendix":
                self.show_categories()

        elif event.key() == Qt.Key_D or event.key() == Qt.Key_Q:
            if self.level == "categories":
                selected = self.list_widget.currentItem().text()
                self.show_appendix(selected)
            elif self.level == "otherappendix":
                self.show_categories()
        
        elif event.key() == Qt.Key_E or event.key() == Qt.Key_Enter:
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
            elif self.level == "appendix":
                self.show_appendix_symbols(selected)
            elif self.level == "appendix_symbols": 
                selected = self.list_widget.currentItem().text()
                symbol_only = selected.split(" ")[0]
                if previous_window:
                    previous_window.activate()
                time.sleep(0.1)
                pyperclip.copy(symbol_only)
                pyautogui.hotkey('ctrl', 'v')
            elif self.level == "otherappendix":      
                pass   
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