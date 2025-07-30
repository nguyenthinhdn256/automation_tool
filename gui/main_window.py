import tkinter as tk
from tkinter import ttk
import sys
import os

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_widgets()
        self.current_view = "main"
        self.is_maximized = False
    
    def setup_window(self):
        self.root.title("")
        self.root.geometry("1500x1500")
        self.root.configure(bg='#2b2b2b')
        self.root.resizable(True, True)
        self.root.overrideredirect(True)
        self.font_title = ('Arial', 24, 'bold')
        self.font_label = ('Arial', 16)
        self.font_combo = ('Arial', 14)
        self.font_text = ('Arial', 14)
    
    def setup_widgets(self):
        self.create_custom_title_bar()
        self.create_main_container()
        self.create_left_panel()
        self.create_right_panel()
        self.root.bind("<Button-1>", self.on_click_outside)
    
    def create_custom_title_bar(self):
        self.title_bar_frame = tk.Frame(self.root, bg='#404040', height=40)
        self.title_bar_frame.pack(fill='x', side='top')
        self.title_bar_frame.pack_propagate(False)
        title_label = tk.Label(self.title_bar_frame, text="", font=('Arial', 10), fg='white', bg='#404040', anchor='w')
        title_label.pack(side='left', padx=10, fill='both', expand=True)
        control_frame = tk.Frame(self.title_bar_frame, bg='#404040')
        control_frame.pack(side='right')
        minimize_btn = tk.Button(control_frame, text='−', font=('Arial', 14, 'bold'), fg='white', bg='#2b2b2b', relief='flat', width=3, command=self.minimize_window)
        minimize_btn.pack(side='left')
        self.maximize_btn = tk.Button(control_frame, text='□', font=('Arial', 12, 'bold'), fg='white', bg='#2b2b2b', relief='flat', width=3, command=self.toggle_maximize)
        self.maximize_btn.pack(side='left')
        close_btn = tk.Button(control_frame, text='×', font=('Arial', 14, 'bold'), fg='white', bg='#ff4444', relief='flat', width=3, command=self.close_window)
        close_btn.pack(side='left')
        self.bind_title_bar_events(title_label)
        def on_minimize_hover(event):
            minimize_btn.configure(bg='#404040')
        def on_minimize_leave(event):
            minimize_btn.configure(bg='#2b2b2b')
        def on_maximize_hover(event):
            self.maximize_btn.configure(bg='#404040')
        def on_maximize_leave(event):
            self.maximize_btn.configure(bg='#2b2b2b')
        def on_close_hover(event):
            close_btn.configure(bg='#ff6666')
        def on_close_leave(event):
            close_btn.configure(bg='#ff4444')
        minimize_btn.bind("<Enter>", on_minimize_hover)
        minimize_btn.bind("<Leave>", on_minimize_leave)
        self.maximize_btn.bind("<Enter>", on_maximize_hover)
        self.maximize_btn.bind("<Leave>", on_maximize_leave)
        close_btn.bind("<Enter>", on_close_hover)
        close_btn.bind("<Leave>", on_close_leave)
    
    def bind_title_bar_events(self, title_widget):
        title_widget.bind('<Button-1>', self.start_move)
        title_widget.bind('<B1-Motion>', self.move_window)
        title_widget.bind('<Double-Button-1>', self.toggle_maximize)
    
    def start_move(self, event):
        self.x = event.x
        self.y = event.y
    
    def move_window(self, event):
        if not self.is_maximized:
            deltax = event.x - self.x
            deltay = event.y - self.y
            x = self.root.winfo_x() + deltax
            y = self.root.winfo_y() + deltay
            self.root.geometry(f"+{x}+{y}")
    
    def minimize_window(self):
        self.root.iconify()
    
    def toggle_maximize(self, event=None):
        if self.is_maximized:
            self.root.geometry("1500x1500")
            self.maximize_btn.configure(text='□')
            self.is_maximized = False
        else:
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            self.root.geometry(f"{screen_width}x{screen_height}+0+0")
            self.maximize_btn.configure(text='❐')
            self.is_maximized = True
    
    def close_window(self):
        self.root.destroy()
    
    def create_main_container(self):
        self.main_container = tk.Frame(self.root, bg='#2b2b2b')
        self.main_container.pack(fill='both', expand=True)
    
    def create_left_panel(self):
        self.left_frame = tk.Frame(self.main_container, bg='#404040', width=200)
        self.left_frame.pack(side='left', fill='y', padx=0, pady=0)
        self.left_frame.pack_propagate(False)
        title_label = tk.Label(self.left_frame, text="Automation Tool", font=('Arial', 16, 'bold'), fg='white', bg='#404040')
        title_label.pack(pady=(20, 30), padx=10)
        self.create_menu_item("👥 Profiles", "profiles")
        self.create_menu_item("🤖 Auto", "auto")
        self.create_menu_item("🔍 Explore", "explore")
        self.create_menu_item("⚙️ Setting", "setting")
    
    def create_menu_item(self, text, menu_id):
        menu_frame = tk.Frame(self.left_frame, bg='#404040')
        menu_frame.pack(fill='x', padx=5, pady=2)
        menu_label = tk.Label(menu_frame, text=text, font=('Arial', 12), fg='white', bg='#404040', anchor='w')
        menu_label.pack(fill='x', padx=15, pady=8)
        def on_click(event):
            self.on_menu_clicked(menu_id)
        menu_label.bind("<Button-1>", on_click)
        menu_frame.bind("<Button-1>", on_click)
        def on_enter(event):
            menu_label.configure(bg='#505050')
            menu_frame.configure(bg='#505050')
        def on_leave(event):
            menu_label.configure(bg='#404040')
            menu_frame.configure(bg='#404040')
        menu_label.bind("<Enter>", on_enter)
        menu_label.bind("<Leave>", on_leave)
        menu_frame.bind("<Enter>", on_enter)
        menu_frame.bind("<Leave>", on_leave)
    
    def create_right_panel(self):
        self.right_frame = tk.Frame(self.main_container, bg='#f0f0f0')
        self.right_frame.pack(side='right', fill='both', expand=True, padx=0, pady=0)
        self.create_tab_header()
        self.create_content_area()
    
    def create_tab_header(self):
        self.tab_header_frame = tk.Frame(self.right_frame, bg='#e0e0e0', height=80)
        self.tab_header_frame.pack(fill='x')
        self.tab_header_frame.pack_propagate(False)
        
        self.ldplayer_tab = tk.Label(self.tab_header_frame, text="Emulator", font=('Arial', 14), fg='black', bg='white', relief='solid', bd=1, cursor="hand2")
        self.ldplayer_tab.pack(side='left', padx=2, pady=20, ipadx=25, ipady=10)
        self.ldplayer_tab.bind("<Button-1>", self.toggle_dropdown)
        
        self.dropdown_menu = tk.Frame(self.root, bg='white', relief='solid', bd=1)
        self.dropdown_visible = False
        
        dropdown_options = ["Emulator", "Phone", "Trình duyệt"]
        for option in dropdown_options:
            option_btn = tk.Button(self.dropdown_menu, text=option, font=('Arial', 14), fg='black', bg='white', relief='flat', anchor='w', padx=20, pady=5, cursor="hand2", command=lambda opt=option: self.select_dropdown_option(opt))
            option_btn.pack(fill='x')
            def on_option_enter(event, btn=option_btn):
                btn.configure(bg='#e0e0e0')
            def on_option_leave(event, btn=option_btn):
                btn.configure(bg='white')
            option_btn.bind("<Enter>", on_option_enter)
            option_btn.bind("<Leave>", on_option_leave)
        
        self.directbot_tab = tk.Label(self.tab_header_frame, text="DIRECTBOT", font=('Arial', 14), fg='black', bg='#e0e0e0', relief='solid', bd=1)
        self.directbot_tab.pack(side='left', padx=2, pady=20, ipadx=25, ipady=10)
    
    def toggle_dropdown(self, event=None):
        if self.dropdown_visible:
            self.hide_dropdown()
        else:
            self.show_dropdown()
    
    def show_dropdown(self):
        ldplayer_x = self.ldplayer_tab.winfo_rootx()
        ldplayer_y = self.ldplayer_tab.winfo_rooty() + self.ldplayer_tab.winfo_height()
        self.dropdown_menu.place(x=ldplayer_x - self.root.winfo_rootx(), y=ldplayer_y - self.root.winfo_rooty())
        self.dropdown_visible = True
    
    def hide_dropdown(self):
        self.dropdown_menu.place_forget()
        self.dropdown_visible = False
    
    def on_click_outside(self, event):
        if self.dropdown_visible:
            widget = event.widget
            if widget != self.ldplayer_tab and not self.is_child_of_dropdown(widget):
                self.hide_dropdown()
    
    def is_child_of_dropdown(self, widget):
        parent = widget
        while parent:
            if parent == self.dropdown_menu:
                return True
            parent = parent.master
        return False
    
    def select_dropdown_option(self, option):
        self.hide_dropdown()
        if option == "Phone":
            self.current_view = "phone"
            self.show_phone_view()
        elif option == "Emulator":
            self.current_view = "emulator"
            self.show_emulator_view()
        elif option == "Trình duyệt":
            self.current_view = "browser"
            self.show_browser_view()
    
    def create_content_area(self):
        self.content_area = tk.Frame(self.right_frame, bg='white')
        self.content_area.pack(fill='both', expand=True, padx=5, pady=5)
        self.create_profile_table()
        self.create_bottom_controls()
    
    def create_profile_table(self):
        self.table_frame = tk.Frame(self.content_area, bg='white')
        self.table_frame.pack(fill='both', expand=True, padx=5, pady=5)
        columns = ['Num', 'ProfileName', 'Title', 'IndexProfile']
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show='headings', height=15)
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=150, anchor='center')
        sample_data = [('1', 'MAX', 'MAX', '0'), ('2', 'MAX-1', 'MAX-1', '1'), ('3', 'MAX-2', 'MAX-2', '2'), ('4', 'MAX-3', 'MAX-3', '3'), ('5', 'MAX-4', 'MAX-4', '4'), ('6', 'MAX-5', 'MAX-5', '5')]
        for data in sample_data:
            self.tree.insert('', 'end', values=data)
        scrollbar = ttk.Scrollbar(self.table_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        self.tree.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')
    
    def create_bottom_controls(self):
        self.bottom_frame = tk.Frame(self.content_area, bg='white', height=50)
        self.bottom_frame.pack(fill='x', side='bottom', padx=5, pady=5)
        self.bottom_frame.pack_propagate(False)
        page_label = tk.Label(self.bottom_frame, text="1/1", font=('Arial', 10), fg='black', bg='white')
        page_label.pack(side='left', padx=10, pady=10)
        profiles_label = tk.Label(self.bottom_frame, text="Profiles / Trang:", font=('Arial', 10), fg='black', bg='white')
        profiles_label.pack(side='left', padx=(20, 5), pady=10)
        page_combo = ttk.Combobox(self.bottom_frame, values=['20', '50', '100'], width=5, state='readonly')
        page_combo.pack(side='left', padx=5, pady=10)
        page_combo.set('20')
        sl_label = tk.Label(self.bottom_frame, text="SL: 6", font=('Arial', 10), fg='black', bg='white')
        sl_label.pack(side='left', padx=10, pady=10)
        add_profile_btn = tk.Button(self.bottom_frame, text="Thêm Profile", font=('Arial', 10), bg='#4CAF50', fg='white', relief='flat', padx=15, pady=5)
        add_profile_btn.pack(side='right', padx=10, pady=10)
    
    def on_menu_clicked(self, menu_id):
        if menu_id == "profiles":
            self.show_profiles_view()
        elif menu_id == "auto":
            self.show_auto_view()
        elif menu_id == "explore":
            self.show_explore_view()
        elif menu_id == "setting":
            self.show_setting_view()
    
    def show_profiles_view(self):
        pass
    
    def show_auto_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        auto_label = tk.Label(self.content_area, text="AUTO AUTOMATION", font=('Arial', 20, 'bold'), fg='black', bg='white')
        auto_label.pack(pady=50)
    
    def show_explore_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        explore_label = tk.Label(self.content_area, text="EXPLORE SECTION", font=('Arial', 20, 'bold'), fg='black', bg='white')
        explore_label.pack(pady=50)
    
    def show_setting_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        setting_label = tk.Label(self.content_area, text="SETTING PANEL", font=('Arial', 20, 'bold'), fg='black', bg='white')
        setting_label.pack(pady=50)
    
    def show_phone_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        phone_label = tk.Label(self.content_area, text="PHONE AUTOMATION", font=('Arial', 20, 'bold'), fg='black', bg='white')
        phone_label.pack(pady=50)
    
    def show_emulator_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        emulator_label = tk.Label(self.content_area, text="EMULATOR AUTOMATION", font=('Arial', 20, 'bold'), fg='black', bg='white')
        emulator_label.pack(pady=50)
    
    def show_browser_view(self):
        for widget in self.content_area.winfo_children():
            widget.destroy()
        browser_label = tk.Label(self.content_area, text="BROWSER AUTOMATION", font=('Arial', 20, 'bold'), fg='black', bg='white')
        browser_label.pack(pady=50)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.run()