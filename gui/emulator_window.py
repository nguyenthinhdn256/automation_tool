import tkinter as tk
from tkinter import ttk

class EmulatorWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_widgets()
    
    def setup_window(self):
        self.root.title("Emulator Automation Setup")
        self.root.geometry("1200x800")
        self.root.configure(bg='#2b2b2b')
        self.root.resizable(True, True)
        
        self.font_title = ('Arial', 20, 'bold')
        self.font_text = ('Arial', 12)
    
    def setup_widgets(self):
        title_label = tk.Label(self.root, text="EMULATOR AUTOMATION", font=self.font_title, fg='white', bg='#2b2b2b')
        title_label.pack(pady=30)
        
        info_label = tk.Label(self.root, text="Cửa sổ thiết lập automation cho Emulator", font=self.font_text, fg='white', bg='#2b2b2b')
        info_label.pack(pady=20)
        
        placeholder_label = tk.Label(self.root, text="Nội dung sẽ được thêm sau...", font=self.font_text, fg='#888888', bg='#2b2b2b')
        placeholder_label.pack(pady=50)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = EmulatorWindow()
    app.run()