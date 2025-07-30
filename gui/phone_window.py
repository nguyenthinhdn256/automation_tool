import tkinter as tk
from tkinter import ttk
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from configs.templates import PHONE_TEMPLATES

class PhoneWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_widgets()
    
    def setup_window(self):
        self.root.title("Tự động hóa Điện thoại")
        self.root.geometry("1000x700")
        self.root.configure(bg='#1e293b')
        self.root.resizable(True, True)
        
        self.font_title = ('Arial', 20, 'bold')
        self.font_category = ('Arial', 16, 'bold')
        self.font_template = ('Arial', 12)
        self.font_desc = ('Arial', 10)
    
    def setup_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#0f172a', height=80)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        title_label = tk.Label(header_frame, text="📱 TỰ ĐỘNG HÓA ĐIỆN THOẠI", 
                              font=self.font_title, fg='#3b82f6', bg='#0f172a')
        title_label.pack(pady=25)
        
        # Main content với scrollbar
        main_frame = tk.Frame(self.root, bg='#1e293b')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        canvas = tk.Canvas(main_frame, bg='#1e293b', highlightthickness=0)
        scrollbar = ttk.Scrollbar(main_frame, orient="vertical", command=canvas.yview)
        scrollable_frame = tk.Frame(canvas, bg='#1e293b')
        
        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        
        # Hiển thị các danh mục và mẫu
        for category, templates in PHONE_TEMPLATES.items():
            self.create_category_section(scrollable_frame, category, templates)
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")
        
        # Nút quay lại
        back_button = tk.Button(self.root, text="← Quay lại", font=self.font_template,
                               bg='#374151', fg='white', relief='flat', padx=20, pady=10,
                               command=self.root.destroy)
        back_button.pack(side='bottom', anchor='w', padx=20, pady=10)
    
    def create_category_section(self, parent, category_name, templates):
        # Tiêu đề danh mục
        category_label = tk.Label(parent, text=f"📂 {category_name}", 
                                 font=self.font_category, fg='#fbbf24', bg='#1e293b')
        category_label.pack(anchor='w', pady=(20, 10))
        
        # Danh sách mẫu trong danh mục
        for template in templates:
            self.create_template_card(parent, template)
    
    def create_template_card(self, parent, template):
        # Card frame
        card_frame = tk.Frame(parent, bg='#334155', relief='raised', bd=1)
        card_frame.pack(fill='x', pady=5, padx=10)
        
        # Template info frame
        info_frame = tk.Frame(card_frame, bg='#334155')
        info_frame.pack(side='left', fill='both', expand=True, padx=15, pady=10)
        
        # Tên template
        name_label = tk.Label(info_frame, text=template['name'], 
                             font=self.font_template, fg='white', bg='#334155')
        name_label.pack(anchor='w')
        
        # Mô tả
        desc_label = tk.Label(info_frame, text=template['description'], 
                             font=self.font_desc, fg='#cbd5e1', bg='#334155')
        desc_label.pack(anchor='w', pady=(2, 0))
        
        # Thông tin bổ sung
        detail_frame = tk.Frame(info_frame, bg='#334155')
        detail_frame.pack(anchor='w', pady=(5, 0), fill='x')
        
        difficulty_label = tk.Label(detail_frame, text=f"Độ khó: {template['difficulty']}", 
                                   font=('Arial', 9), fg='#94a3b8', bg='#334155')
        difficulty_label.pack(side='left')
        
        time_label = tk.Label(detail_frame, text=f"Thời gian: {template['time']}", 
                             font=('Arial', 9), fg='#94a3b8', bg='#334155')
        time_label.pack(side='left', padx=(20, 0))
        
        # Button frame
        button_frame = tk.Frame(card_frame, bg='#334155')
        button_frame.pack(side='right', padx=15, pady=10)
        
        # Nút sử dụng
        use_button = tk.Button(button_frame, text="Sử dụng", font=('Arial', 10, 'bold'),
                              bg='#3b82f6', fg='white', relief='flat', padx=20, pady=5,
                              command=lambda: self.use_template(template))
        use_button.pack()
    
    def use_template(self, template):
        # Tạo cửa sổ setup cho template
        setup_window = tk.Toplevel(self.root)
        setup_window.title(f"Thiết lập: {template['name']}")
        setup_window.geometry("600x400")
        setup_window.configure(bg='#1e293b')
        
        # Nội dung thiết lập
        setup_label = tk.Label(setup_window, text=f"Đang thiết lập: {template['name']}", 
                              font=self.font_title, fg='white', bg='#1e293b')
        setup_label.pack(pady=50)
        
        placeholder_label = tk.Label(setup_window, text="Giao diện thiết lập sẽ được phát triển...", 
                                    font=self.font_template, fg='#94a3b8', bg='#1e293b')
        placeholder_label.pack(pady=20)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PhoneWindow()
    app.run()