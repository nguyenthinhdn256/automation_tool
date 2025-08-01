import tkinter as tk
from tkinter import ttk
import datetime
import random

class DashboardBorderedTable:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("📈 Dashboard Analytics - Viền Excel rõ ràng")
        self.root.geometry("1200x700")
        self.root.configure(bg='#f5f5f5')
        
        self.setup_styles()
        self.create_header()
        self.create_sidebar()
        self.create_main_content()
        self.load_data()
        self.start_live_updates()
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Dashboard style với viền đen
        self.style.configure("DashBorder.Treeview",
                           background="white",
                           foreground="black",
                           rowheight=35,
                           fieldbackground="white",
                           font=('Arial', 9),
                           borderwidth=2,
                           relief="solid")
        
        self.style.configure("DashBorder.Treeview.Heading",
                           background="#D0D0D0",
                           foreground="black",
                           font=('Arial', 10, 'bold'),
                           relief="solid",
                           borderwidth=2)
        
        # Selection với viền đậm
        self.style.map("DashBorder.Treeview",
                    background=[('selected', '#0078D4')],
                    foreground=[('selected', 'white')],
                    relief=[('selected', 'solid')],
                    borderwidth=[('selected', 3)])
        
    def create_header(self):
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80, relief='solid', bd=2)
        header_frame.pack(fill='x')
        header_frame.pack_propagate(False)
        
        # Logo và title
        left_frame = tk.Frame(header_frame, bg='#2c3e50')
        left_frame.pack(side='left', padx=20, pady=15)
        
        tk.Label(left_frame, text="📊", font=('Arial', 24),
                bg='#2c3e50', fg='#00d4aa').pack(side='left')
        
        tk.Label(left_frame, text="ANALYTICS DASHBOARD",
                font=('Arial', 16, 'bold'),
                bg='#2c3e50', fg='white').pack(side='left', padx=(10, 0))
        
        # Real-time info với viền
        right_frame = tk.Frame(header_frame, bg='#34495e', relief='solid', bd=1)
        right_frame.pack(side='right', padx=20, pady=15)
        
        self.time_label = tk.Label(right_frame, text="",
                                  font=('Arial', 10),
                                  bg='#34495e', fg='#00d4aa', padx=10, pady=5)
        self.time_label.pack()
        
        self.status_label = tk.Label(right_frame, text="🟢 ONLINE",
                                    font=('Arial', 8, 'bold'),
                                    bg='#34495e', fg='#00ff88', padx=10)
        self.status_label.pack()
    
    def create_sidebar(self):
        sidebar_frame = tk.Frame(self.root, bg='#34495e', width=200, relief='solid', bd=2)
        sidebar_frame.pack(side='left', fill='y')
        sidebar_frame.pack_propagate(False)
        
        # Menu title với viền
        title_frame = tk.Frame(sidebar_frame, bg='#2c3e50', relief='solid', bd=1)
        title_frame.pack(fill='x', padx=5, pady=5)
        
        tk.Label(title_frame, text="📋 MENU",
                font=('Arial', 12, 'bold'),
                bg='#2c3e50', fg='white', pady=15).pack()
        
        # Menu buttons với viền
        menu_items = [
            ("📊 Tổng quan", "#17a2b8"),
            ("💰 Doanh thu", "#fd7e14"),
            ("👥 Khách hàng", "#dc3545"),
            ("📦 Sản phẩm", "#20c997"),
            ("📈 Báo cáo", "#0d6efd"),
            ("⚙️ Cài đặt", "#ffc107")
        ]
        
        for item, color in menu_items:
            btn = tk.Button(sidebar_frame, text=item,
                           font=('Arial', 10, 'bold'),
                           bg=color, fg='white',
                           relief='solid', bd=2, pady=8, anchor='w',
                           activebackground='#495057',
                           activeforeground='white',
                           command=lambda x=item: self.menu_click(x))
            btn.pack(fill='x', padx=10, pady=3)
    
    def create_main_content(self):
        main_frame = tk.Frame(self.root, bg='#f8f9fa', relief='solid', bd=1)
        main_frame.pack(side='right', fill='both', expand=True)
        
        # Stats cards với viền rõ ràng
        stats_frame = tk.Frame(main_frame, bg='#f8f9fa', height=120)
        stats_frame.pack(fill='x', padx=20, pady=20)
        stats_frame.pack_propagate(False)
        
        # Tạo 4 thẻ thống kê với viền
        stats_data = [
            ("💰 Doanh thu", "1,250,000,000", "+15.3%", "#28a745"),
            ("👥 Khách hàng", "3,456", "+8.7%", "#dc3545"),
            ("📦 Đơn hàng", "1,234", "+12.1%", "#17a2b8"),
            ("⭐ Đánh giá", "4.8/5", "+2.1%", "#fd7e14")
        ]
        
        for i, (title, value, change, color) in enumerate(stats_data):
            card = tk.Frame(stats_frame, bg='white', relief='solid', bd=3)
            card.place(x=i*230, y=0, width=200, height=100)
            
            tk.Label(card, text=title, font=('Arial', 10),
                    bg='white', fg='#666').pack(pady=(15, 5))
            
            tk.Label(card, text=value, font=('Arial', 16, 'bold'),
                    bg='white', fg=color).pack()
            
            tk.Label(card, text=change, font=('Arial', 9, 'bold'),
                    bg='white', fg='#28a745').pack(pady=(0, 10))
        
        # Table section với viền đậm
        table_section = tk.Frame(main_frame, bg='black', relief='solid', bd=4)
        table_section.pack(fill='both', expand=True, padx=20, pady=(0, 20))
        
        # Table header với viền
        table_header = tk.Frame(table_section, bg='#e9ecef', height=50, relief='solid', bd=2)
        table_header.pack(fill='x', padx=2, pady=(2, 0))
        table_header.pack_propagate(False)
        
        tk.Label(table_header, text="📊 BÁO CÁO DOANH SỐ THEO THÁNG",
                font=('Arial', 14, 'bold'),
                bg='#e9ecef', fg='#212529').pack(expand=True, pady=15)
        
        # Filter frame với viền
        filter_frame = tk.Frame(table_section, bg='white', height=50, relief='solid', bd=1)
        filter_frame.pack(fill='x', padx=2)
        filter_frame.pack_propagate(False)
        
        # Filter controls với viền
        left_filter = tk.Frame(filter_frame, bg='white')
        left_filter.pack(side='left', padx=20, pady=10)
        
        tk.Label(left_filter, text="🔍 Lọc:", font=('Arial', 9),
                bg='white', fg='#666').pack(side='left')
        
        self.filter_var = tk.StringVar(value="Tất cả")
        filter_combo = ttk.Combobox(left_filter, textvariable=self.filter_var,
                                   values=["Tất cả", "Q1", "Q2", "Q3", "Q4"],
                                   width=10, font=('Arial', 9))
        filter_combo.pack(side='left', padx=10)
        filter_combo.bind('<<ComboboxSelected>>', self.filter_data)
        
        # Export button với viền
        export_btn = tk.Button(filter_frame, text="📤 Xuất Excel",
                              font=('Arial', 9, 'bold'),
                              bg='#28a745', fg='white', relief='solid', bd=2,
                              padx=15, pady=5,
                              command=self.export_data)
        export_btn.pack(side='right', padx=20, pady=10)
        
        # Treeview với viền rõ ràng
        tree_frame = tk.Frame(table_section, bg='black')
        tree_frame.pack(fill='both', expand=True, padx=2, pady=(0, 2))
        
        columns = ('Tháng', 'Doanh thu', 'Chi phí', 'Lợi nhuận', 'Đơn hàng', 'Khách hàng', 'Tăng trưởng')
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings',
                                style="DashBorder.Treeview")
        
        # Configure columns với viền
        widths = [100, 120, 120, 120, 100, 100, 100]
        for i, col in enumerate(columns):
            self.tree.heading(col, text=col, anchor='center')
            self.tree.column(col, width=widths[i], anchor='center', minwidth=80)
        
        # Scrollbars với viền
        v_scroll = ttk.Scrollbar(tree_frame, orient='vertical', command=self.tree.yview)
        h_scroll = ttk.Scrollbar(tree_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scroll.set, xscrollcommand=h_scroll.set)
        
        v_scroll.pack(side='right', fill='y', padx=(1, 0), pady=1)
        h_scroll.pack(side='bottom', fill='x', padx=1, pady=(1, 0))
        self.tree.pack(side='left', fill='both', expand=True, padx=1, pady=1)
        
        # Bottom status với viền
        status_frame = tk.Frame(main_frame, bg='#495057', height=35, relief='solid', bd=2)
        status_frame.pack(fill='x', side='bottom')
        status_frame.pack_propagate(False)
        
        self.bottom_status = tk.Label(status_frame, text="📊 Dashboard sẵn sàng",
                                     font=('Arial', 9), bg='#495057', fg='white')
        self.bottom_status.pack(side='left', padx=20, pady=8)
        
        # Thêm Excel grid
        self.root.after(400, self.add_excel_borders)
    
    def add_excel_borders(self):
        """Thêm viền Excel grid rõ ràng"""
        # Tạo canvas overlay
        canvas = tk.Canvas(self.tree, highlightthickness=0)
        canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Tính toán vị trí cột
        col_positions = [0]
        total_width = 0
        
        for col in self.tree['columns']:
            width = self.tree.column(col, 'width')
            total_width += width
            col_positions.append(total_width)
        
        # Vẽ đường kẻ dọc (cột) với độ dày 2px
        for i, x in enumerate(col_positions[1:-1], 1):
            canvas.create_line(x, 0, x, 2000, fill='black', width=2)
        
        # Vẽ đường kẻ ngang (hàng) với độ dày 1px
        row_height = 35
        for i in range(30):
            y = i * row_height
            canvas.create_line(0, y, total_width, y, fill='black', width=1)
        
        # Viền ngoài đậm
        canvas.create_rectangle(0, 0, total_width, 15*row_height, 
                              outline='black', width=3, fill='')
        
        # Đường phân cách header đậm hơn
        canvas.create_line(0, row_height, total_width, row_height, 
                          fill='black', width=3)
    
    def load_data(self):
        # Dữ liệu báo cáo 12 tháng
        months_data = []
        for i in range(1, 13):
            revenue = random.randint(80, 250) * 1000000
            cost = int(revenue * random.uniform(0.5, 0.7))
            profit = revenue - cost
            orders = random.randint(150, 400)
            customers = random.randint(80, 200)
            growth = random.uniform(-5, 25)
            
            months_data.append((
                f"Tháng {i:02d}",
                f"{revenue:,} VNĐ",
                f"{cost:,} VNĐ",
                f"{profit:,} VNĐ",
                f"{orders:,}",
                f"{customers:,}",
                f"{growth:+.1f}%"
            ))
        
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Insert data với color coding và viền
        for i, data in enumerate(months_data):
            growth_val = float(data[6][:-1])
            
            if growth_val >= 15:
                tag = 'high_growth'
            elif growth_val >= 0:
                tag = 'positive'
            else:
                tag = 'negative'
            
            # Thêm tag cho hàng chẵn/lẻ
            if i % 2 == 0:
                tag += '_even'
            
            self.tree.insert('', 'end', values=data, tags=(tag,))
        
        # Configure tags với màu nền nhưng giữ viền
        self.tree.tag_configure('high_growth', foreground='#0d6efd', font=('Arial', 9, 'bold'))
        self.tree.tag_configure('high_growth_even', background='#e7f3ff', foreground='#0d6efd', font=('Arial', 9, 'bold'))
        self.tree.tag_configure('positive', foreground='#198754')
        self.tree.tag_configure('positive_even', background='#f0fff0', foreground='#198754')
        self.tree.tag_configure('negative', foreground='#dc3545')
        self.tree.tag_configure('negative_even', background='#fff5f5', foreground='#dc3545')
        
        self.bottom_status.config(text=f"📊 Đã tải {len(months_data)} bản ghi - Viền Excel rõ ràng")
    
    def filter_data(self, event=None):
        filter_value = self.filter_var.get()
        self.bottom_status.config(text=f"🔍 Áp dụng bộ lọc: {filter_value}")
    
    def export_data(self):
        self.bottom_status.config(text="📤 Đang xuất dữ liệu ra Excel...")
        self.root.after(2000, lambda: self.bottom_status.config(text="✅ Xuất Excel thành công"))
    
    def menu_click(self, item):
        self.bottom_status.config(text=f"📋 Đã chọn: {item}")
    
    def start_live_updates(self):
        self.update_time()
        self.root.after(1000, self.start_live_updates)
    
    def update_time(self):
        now = datetime.datetime.now()
        time_str = now.strftime("%H:%M:%S - %d/%m/%Y")
        self.time_label.config(text=time_str)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = DashboardBorderedTable()
    app.run()