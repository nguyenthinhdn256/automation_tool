import tkinter as tk
from tkinter import ttk
import subprocess
import sys

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_widgets()
    
    def setup_window(self):
        self.root.title("Automation Tool - NoCode Platform")
        self.root.geometry("1500x1500")
        self.root.configure(bg='#2b2b2b')
        self.root.resizable(True, True)
        
        # Thiết lập font mặc định
        self.font_title = ('Arial', 24, 'bold')
        self.font_label = ('Arial', 16)
        self.font_combo = ('Arial', 14)
        self.font_text = ('Arial', 14)
    
    def setup_widgets(self):
        # Tiêu đề chính
        title_label = tk.Label(self.root, text="AUTOMATION TOOL", font=self.font_title, fg='white', bg='#2b2b2b')
        title_label.pack(pady=50)
        
        # Profile Label với icon (sử dụng ký tự Unicode cho icon nhóm người)
        profile_label = tk.Label(self.root, text="Profile", font=self.font_label, fg='white', bg='#2b2b2b')
        profile_label.place(x=10, y=80)
        icon_profile_label = tk.Label(self.root, text="👥", font=self.font_label, fg='white', bg='#2b2b2b')
        icon_profile_label.place(x=76, y=78)
        
        # Combobox với các tùy chọn
        self.profile_var = tk.StringVar()
        profile_options = ["Chọn nền tảng", "Emulator", "Phone", "Trình duyệt"]
        
        # Thiết lập style cho combobox
        style = ttk.Style()
        style.theme_use('clam')
        style.configure('Custom.TCombobox', fieldbackground='#4a4a4a', background='#4a4a4a', foreground='white', borderwidth=1, relief='solid')
        style.map('Custom.TCombobox', fieldbackground=[('readonly', '#4a4a4a')], selectbackground=[('readonly', '#5a5a5a')])
        
        self.profile_combo = ttk.Combobox(self.root, textvariable=self.profile_var, values=profile_options, font=self.font_combo, width=15, state='readonly', style='Custom.TCombobox')
        self.profile_combo.place(x=115, y=83)
        self.profile_combo.set("Chọn nền tảng")
        self.profile_combo.bind('<<ComboboxSelected>>', self.on_profile_selected)

        
        # Thông tin phiên bản
        info_label = tk.Label(self.root, text="Version 1.0 - NoCode Automation Platform", font=('Arial', 10), fg='#888888', bg='#2b2b2b')
        info_label.pack(side=tk.BOTTOM, pady=20)
    
    def on_profile_selected(self, event):
        selected = self.profile_var.get()
        
        if selected == "Emulator":
            self.open_emulator_window()
        elif selected == "Phone":
            self.open_phone_window()
        elif selected == "Trình duyệt":
            self.open_browser_window()
        
        # Reset về trạng thái ban đầu sau khi chọn
        self.profile_combo.set("Chọn nền tảng...")
    
    def open_emulator_window(self):
        subprocess.Popen([sys.executable, 'gui/emulator_window.py'])
    
    def open_phone_window(self):
        subprocess.Popen([sys.executable, 'gui/phone_window.py'])
    
    def open_browser_window(self):
        subprocess.Popen([sys.executable, 'gui/browser_window.py'])
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.run()