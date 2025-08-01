import tkinter as tk
from tkinter import ttk
import sys
import os

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_widgets()
        self.current_view = "profiles"
        self.is_maximized = False
        self.current_view = "profiles"
    
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

    def setup_treeview_style(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure('Custom.Treeview', background='white', foreground='black', rowheight=25, fieldbackground='white', borderwidth=1, relief='solid')
        self.style.configure('Custom.Treeview.Heading', background='#4a4a4a', foreground='white', font=('Arial', 10, 'bold'), borderwidth=1, relief='solid')
        self.style.map('Custom.Treeview', background=[('selected', '#0078d4')])
        self.style.map('Custom.Treeview.Heading', background=[('active', '#5a5a5a')])
        self.style.layout('Custom.Treeview.Item', [('Treeitem.padding', {'children': [('Treeitem.indicator', {'side': 'left', 'sticky': ''}), ('Treeitem.image', {'side': 'left', 'sticky': ''}), ('Treeitem.text', {'side': 'left', 'sticky': ''}), ('Treeitem.border', {'side': 'right', 'sticky': 'ns', 'children': [('Treeitem.cell', {'sticky': 'nswe'})]})], 'sticky': 'nswe'})])
        self.style.configure('Custom.Treeview.Item', borderwidth=1, relief='solid')
    
    def setup_widgets(self):
        self.setup_treeview_style()
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
        minimize_btn.bind("<Enter>", lambda e: minimize_btn.configure(bg='#404040'))
        minimize_btn.bind("<Leave>", lambda e: minimize_btn.configure(bg='#2b2b2b'))
        self.maximize_btn.bind("<Enter>", lambda e: self.maximize_btn.configure(bg='#404040'))
        self.maximize_btn.bind("<Leave>", lambda e: self.maximize_btn.configure(bg='#2b2b2b'))
        close_btn.bind("<Enter>", lambda e: close_btn.configure(bg='#ff6666'))
        close_btn.bind("<Leave>", lambda e: close_btn.configure(bg='#ff4444'))
    
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
        self.menu_buttons = {}
        self.create_menu_item("👥 Profiles", "profiles")
        self.create_menu_item("🤖 Auto", "auto")
        self.create_menu_item("🔍 Explore", "explore")
        self.create_menu_item("💰 Selling", "selling")
    
    def create_menu_item(self, text, menu_id):
        menu_frame = tk.Frame(self.left_frame, bg='#404040')
        menu_frame.pack(fill='x', padx=5, pady=2)
        menu_label = tk.Label(menu_frame, text=text, font=('Arial', 12), fg='white', bg='#404040', anchor='w')
        menu_label.pack(fill='x', padx=15, pady=8)
        self.menu_buttons[menu_id] = {'frame': menu_frame, 'label': menu_label}
        menu_label.bind("<Button-1>", lambda e: self.on_menu_clicked(menu_id))
        menu_frame.bind("<Button-1>", lambda e: self.on_menu_clicked(menu_id))
        menu_label.bind("<Enter>", lambda e: self.set_menu_hover(menu_id, True))
        menu_label.bind("<Leave>", lambda e: self.set_menu_hover(menu_id, False))
        menu_frame.bind("<Enter>", lambda e: self.set_menu_hover(menu_id, True))
        menu_frame.bind("<Leave>", lambda e: self.set_menu_hover(menu_id, False))
    
    def set_menu_hover(self, menu_id, is_hover):
        if self.current_view == menu_id:
            return
        color = '#505050' if is_hover else '#404040'
        self.menu_buttons[menu_id]['label'].configure(bg=color)
        self.menu_buttons[menu_id]['frame'].configure(bg=color)
    
    def set_menu_active(self, menu_id):
        for mid, widgets in self.menu_buttons.items():
            if mid == menu_id:
                widgets['label'].configure(bg='#606060')
                widgets['frame'].configure(bg='#606060')
            else:
                widgets['label'].configure(bg='#404040')
                widgets['frame'].configure(bg='#404040')
    
    def create_right_panel(self):
        self.right_frame = tk.Frame(self.main_container, bg='#f0f0f0')
        self.right_frame.pack(side='right', fill='both', expand=True, padx=0, pady=0)
    
    def create_profiles_tab_header(self):
        self.tab_header_frame = tk.Frame(self.right_frame, bg='#e0e0e0', height=80)
        self.tab_header_frame.pack(fill='x')
        self.tab_header_frame.pack_propagate(False)
        
        self.ldplayer_tab = tk.Label(self.tab_header_frame, text="Emulator", font=('Arial', 14), fg='black', bg='white', relief='solid', bd=1, cursor="hand2", width=12)
        self.ldplayer_tab.pack(side='left', padx=2, pady=20, ipady=10)
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
        
        self.directbot_tab = tk.Label(self.tab_header_frame, text="DIRECTBOT", font=('Arial', 14), fg='black', bg='#e0e0e0', relief='solid', bd=1, width=12)
        self.directbot_tab.pack(side='left', padx=2, pady=20, ipady=10)
    
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
        self.ldplayer_tab.configure(text=option)
        if option == "Phone":
            self.show_phone_content()
        elif option == "Emulator":
            self.show_emulator_content()
        elif option == "Trình duyệt":
            self.show_browser_content()
    
    def clear_right_panel(self):
        for widget in self.right_frame.winfo_children():
            widget.destroy()
    
    def on_menu_clicked(self, menu_id):
        self.current_view = menu_id
        self.set_menu_active(menu_id)
        if menu_id == "profiles":
            self.show_profiles_view()
        elif menu_id == "auto":
            self.show_auto_view()
        elif menu_id == "explore":
            self.show_explore_view()
        elif menu_id == "selling":
            self.show_selling_view()
    
    def show_profiles_view(self):
        self.clear_right_panel()
        self.create_profiles_tab_header()
        self.content_area = tk.Frame(self.right_frame, bg='white')
        self.content_area.pack(fill='both', expand=True, padx=5, pady=5)
        self.create_profile_table()
        self.create_bottom_controls()
        self.ldplayer_tab.configure(text="Emulator")
     
    def create_profile_table(self):
        self.table_frame = tk.Frame(self.content_area, bg='white')
        self.table_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        canvas = tk.Canvas(self.table_frame, bg='white')
        scrollbar = ttk.Scrollbar(self.table_frame, orient='vertical', command=canvas.yview)
        self.table_scrollable_frame = tk.Frame(canvas, bg='white')
        
        self.table_scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=self.table_scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        self.table_headers = [("Num", 100), ("ProfileName", 200), ("Title", 200), ("IndexProfile", 150)]
        self.table_rows = []
        
        # Tạo header
        for col, (header_text, width) in enumerate(self.table_headers):
            header_label = tk.Label(self.table_scrollable_frame, text=header_text, font=('Arial', 10, 'bold'), fg='white', bg='#4a4a4a', width=width//8, relief='solid', bd=1, anchor='center')
            header_label.grid(row=0, column=col, sticky='ew')
        
        # Tạo sample data rows
        sample_data = [('1', 'MAX', 'MAX', '0'), ('2', 'MAX-1', 'MAX-1', '1'), ('3', 'MAX-2', 'MAX-2', '2'), ('4', 'MAX-3', 'MAX-3', '3'), ('5', 'MAX-4', 'MAX-4', '4'), ('6', 'MAX-5', 'MAX-5', '5')]
        self.create_profile_rows(len(sample_data), sample_data)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

    def create_profile_rows(self, row_count, data=None):
        # Xóa các rows cũ trước
        for widget in self.table_scrollable_frame.winfo_children():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()
        
        # Reset table_rows để lưu trữ references
        self.table_rows = []
        
        # Tạo rows mới dựa trên row_count
        for row in range(1, row_count + 1):
            if data:
                cells = list(data[row-1])
            else:
                cells = ["", str(row), "", ""]
            row_widgets = []
            
            for col, (cell_data, (_, width)) in enumerate(zip(cells, self.table_headers)):
                bg_color = '#f9f9f9' if row % 2 == 0 else 'white'
                cell_label = tk.Label(self.table_scrollable_frame, text=cell_data, font=('Arial', 9), bg=bg_color, fg="black", width=width//8, relief="solid", bd=1, anchor="center")
                cell_label.grid(row=row, column=col, sticky="ew")
                row_widgets.append(cell_label)
            
            # Lưu reference
            self.table_rows.append(row_widgets)

    
    def create_bottom_controls(self):
        self.bottom_frame = tk.Frame(self.content_area, bg='white', height=50)
        self.bottom_frame.pack(fill='x', side='bottom', padx=5, pady=5)
        self.bottom_frame.pack_propagate(False)
        page_label = tk.Label(self.bottom_frame, text="1/1", font=('Arial', 10), fg='black', bg='white')
        page_label.pack(side='left', padx=10, pady=10)
        profiles_label = tk.Label(self.bottom_frame, text="Devices / Trang:", font=('Arial', 10), fg='black', bg='white')
        profiles_label.pack(side='left', padx=(20, 5), pady=10)
        page_combo = ttk.Combobox(self.bottom_frame, values=['20', '50', '100'], width=5, state='readonly')
        page_combo.pack(side='left', padx=5, pady=10)
        page_combo.set('20')
        sl_label = tk.Label(self.bottom_frame, text="SL: 6", font=('Arial', 10), fg='black', bg='white')
        sl_label.pack(side='left', padx=10, pady=10)
        add_profile_btn = tk.Button(self.bottom_frame, text="Thêm Devices", font=('Arial', 10), bg='#4CAF50', fg='white', relief='flat', padx=15, pady=5)
        add_profile_btn.pack(side='right', padx=10, pady=10)

    def create_phone_table(self):
        self.table_frame = tk.Frame(self.content_area, bg='white')
        self.table_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        canvas = tk.Canvas(self.table_frame, bg='white')
        scrollbar = ttk.Scrollbar(self.table_frame, orient='vertical', command=canvas.yview)
        self.table_scrollable_frame = tk.Frame(canvas, bg='white')
        
        self.table_scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=self.table_scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        self.table_headers = [("Num", 100), ("DeviceName", 200), ("PhoneModel", 200), ("Status", 150)]
        self.table_rows = []
        
        # Tạo header
        for col, (header_text, width) in enumerate(self.table_headers):
            header_label = tk.Label(self.table_scrollable_frame, text=header_text, font=('Arial', 10, 'bold'), fg='white', bg='#4a4a4a', width=width//8, relief='solid', bd=1, anchor='center')
            header_label.grid(row=0, column=col, sticky='ew')
        
        # Tạo sample data rows
        sample_data = [('1', 'iPhone-01', 'iPhone 14', 'Connected'), ('2', 'Samsung-01', 'Galaxy S23', 'Offline'), ('3', 'Xiaomi-01', 'Mi 13', 'Connected')]
        self.create_phone_rows(len(sample_data), sample_data)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

    def create_phone_rows(self, row_count, data=None):
        # Xóa các rows cũ trước
        for widget in self.table_scrollable_frame.winfo_children():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()
        
        # Reset table_rows để lưu trữ references
        self.table_rows = []
        
        # Tạo rows mới dựa trên row_count
        for row in range(1, row_count + 1):
            if data:
                cells = list(data[row-1])
            else:
                cells = ["", str(row), "", ""]
            row_widgets = []
            
            for col, (cell_data, (_, width)) in enumerate(zip(cells, self.table_headers)):
                bg_color = '#f9f9f9' if row % 2 == 0 else 'white'
                cell_label = tk.Label(self.table_scrollable_frame, text=cell_data, font=('Arial', 9), bg=bg_color, fg="black", width=width//8, relief="solid", bd=1, anchor="center")
                cell_label.grid(row=row, column=col, sticky="ew")
                row_widgets.append(cell_label)
            
            # Lưu reference
            self.table_rows.append(row_widgets)

    def create_phone_controls(self):
        self.bottom_frame = tk.Frame(self.content_area, bg='white', height=50)
        self.bottom_frame.pack(fill='x', side='bottom', padx=5, pady=5)
        self.bottom_frame.pack_propagate(False)
        page_label = tk.Label(self.bottom_frame, text="1/1", font=('Arial', 10), fg='black', bg='white')
        page_label.pack(side='left', padx=10, pady=10)
        devices_label = tk.Label(self.bottom_frame, text="Devices / Trang:", font=('Arial', 10), fg='black', bg='white')
        devices_label.pack(side='left', padx=(20, 5), pady=10)
        page_combo = ttk.Combobox(self.bottom_frame, values=['20', '50', '100'], width=5, state='readonly')
        page_combo.pack(side='left', padx=5, pady=10)
        page_combo.set('20')
        sl_label = tk.Label(self.bottom_frame, text="SL: 3", font=('Arial', 10), fg='black', bg='white')
        sl_label.pack(side='left', padx=10, pady=10)
        add_device_btn = tk.Button(self.bottom_frame, text="Thêm Device", font=('Arial', 10), bg='#4CAF50', fg='white', relief='flat', padx=15, pady=5)
        add_device_btn.pack(side='right', padx=10, pady=10)
    
    def create_browser_table(self):
        self.table_frame = tk.Frame(self.content_area, bg='white')
        self.table_frame.pack(fill='both', expand=True, padx=5, pady=5)
        
        canvas = tk.Canvas(self.table_frame, bg='white')
        scrollbar = ttk.Scrollbar(self.table_frame, orient='vertical', command=canvas.yview)
        self.table_scrollable_frame = tk.Frame(canvas, bg='white')
        
        self.table_scrollable_frame.bind('<Configure>', lambda e: canvas.configure(scrollregion=canvas.bbox('all')))
        canvas.create_window((0, 0), window=self.table_scrollable_frame, anchor='nw')
        canvas.configure(yscrollcommand=scrollbar.set)
        
        self.table_headers = [("Num", 100), ("BrowserName", 200), ("Version", 150), ("UserAgent", 200)]
        self.table_rows = []
        
        # Tạo header
        for col, (header_text, width) in enumerate(self.table_headers):
            header_label = tk.Label(self.table_scrollable_frame, text=header_text, font=('Arial', 10, 'bold'), fg='white', bg='#4a4a4a', width=width//8, relief='solid', bd=1, anchor='center')
            header_label.grid(row=0, column=col, sticky='ew')
        
        # Tạo sample data rows
        sample_data = [('1', 'Chrome-01', 'v118.0', 'Windows 10'), ('2', 'Firefox-01', 'v119.0', 'macOS'), ('3', 'Edge-01', 'v118.0', 'Linux')]
        self.create_browser_rows(len(sample_data), sample_data)
        
        canvas.pack(side='left', fill='both', expand=True)
        scrollbar.pack(side='right', fill='y')

    def create_browser_rows(self, row_count, data=None):
        # Xóa các rows cũ trước
        for widget in self.table_scrollable_frame.winfo_children():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()
        
        # Reset table_rows để lưu trữ references
        self.table_rows = []
        
        # Tạo rows mới dựa trên row_count
        for row in range(1, row_count + 1):
            if data:
                cells = list(data[row-1])
            else:
                cells = ["", str(row), "", ""]
            row_widgets = []
            
            for col, (cell_data, (_, width)) in enumerate(zip(cells, self.table_headers)):
                bg_color = '#f9f9f9' if row % 2 == 0 else 'white'
                cell_label = tk.Label(self.table_scrollable_frame, text=cell_data, font=('Arial', 9), bg=bg_color, fg="black", width=width//8, relief="solid", bd=1, anchor="center")
                cell_label.grid(row=row, column=col, sticky="ew")
                row_widgets.append(cell_label)
            
            # Lưu reference
            self.table_rows.append(row_widgets)

    def create_browser_controls(self):
        self.bottom_frame = tk.Frame(self.content_area, bg='white', height=50)
        self.bottom_frame.pack(fill='x', side='bottom', padx=5, pady=5)
        self.bottom_frame.pack_propagate(False)
        page_label = tk.Label(self.bottom_frame, text="1/1", font=('Arial', 10), fg='black', bg='white')
        page_label.pack(side='left', padx=10, pady=10)
        browsers_label = tk.Label(self.bottom_frame, text="Browsers / Trang:", font=('Arial', 10), fg='black', bg='white')
        browsers_label.pack(side='left', padx=(20, 5), pady=10)
        page_combo = ttk.Combobox(self.bottom_frame, values=['20', '50', '100'], width=5, state='readonly')
        page_combo.pack(side='left', padx=5, pady=10)
        page_combo.set('20')
        sl_label = tk.Label(self.bottom_frame, text="SL: 3", font=('Arial', 10), fg='black', bg='white')
        sl_label.pack(side='left', padx=10, pady=10)
        add_browser_btn = tk.Button(self.bottom_frame, text="Thêm Browser", font=('Arial', 10), bg='#4CAF50', fg='white', relief='flat', padx=15, pady=5)
        add_browser_btn.pack(side='right', padx=10, pady=10)

    def show_phone_content(self):
        if hasattr(self, 'content_area'):
            for widget in self.content_area.winfo_children():
                widget.destroy()
            self.create_phone_table()
            self.create_phone_controls()
    
    def show_emulator_content(self):
        if hasattr(self, 'content_area'):
            for widget in self.content_area.winfo_children():
                widget.destroy()
            self.create_profile_table()
            self.create_bottom_controls()
    
    def show_browser_content(self):
        if hasattr(self, 'content_area'):
            for widget in self.content_area.winfo_children():
                widget.destroy()
            self.create_browser_table()
            self.create_browser_controls()
    
    def show_auto_view(self):
        self.clear_right_panel()
        content_area = tk.Frame(self.right_frame, bg='white')
        content_area.pack(fill='both', expand=True)
        auto_label = tk.Label(content_area, text="AUTO AUTOMATION", font=('Arial', 20, 'bold'), fg='black', bg='white')
        auto_label.pack(expand=True)
    
    def show_explore_view(self):
        self.clear_right_panel()
        content_area = tk.Frame(self.right_frame, bg='white')
        content_area.pack(fill='both', expand=True)
        explore_label = tk.Label(content_area, text="EXPLORE SECTION", font=('Arial', 20, 'bold'), fg='black', bg='white')
        explore_label.pack(expand=True)
    
    def show_selling_view(self):
        self.clear_right_panel()
        content_area = tk.Frame(self.right_frame, bg='white')
        content_area.pack(fill='both', expand=True)
        selling_label = tk.Label(content_area, text="SELLING PANEL", font=('Arial', 20, 'bold'), fg='black', bg='white')
        selling_label.pack(expand=True)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = MainWindow()
    app.run()