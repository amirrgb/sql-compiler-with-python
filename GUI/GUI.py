from tkinter import *
import tkinter as tk
from tkinter import ttk
import sys
sys.path.append('../')
sys.path.append('./')
sys.path.append('/')
sys.path.append('.')
sys.path.append('/.')
sys.path.append('/..')
sys.path.append('./Python-compiler')
from .WorkBench import WorkBenchClass
from .LexicalAnalyzerGUI import LexicalAnalyzerGUIClass
from .MenuBar import *
from .showTable import ShowTableClass



class SqlIdleGUI:
    def __init__(self, root):
        self.root = root
        width = int(self.root.winfo_screenwidth() * 1) 
        height = int(self.root.winfo_screenheight() * 0.95)
        self.root.geometry(f"{width}x{height}+0+0")
        label = tk.Label(self.root, text="SQL COMPILER")
        label.pack()
        self.root.title("SQL COMPILER")
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill='both', expand=True, side='left') 
        self.workBenchTab = WorkBenchClass(self.notebook, self)
        self.lexicalAnalyzerTab = LexicalAnalyzerGUIClass(self.root,self.notebook,self.workBenchTab)
        self.menuBar = MenuBarClass(self.root,self.workBenchTab,self.lexicalAnalyzerTab)