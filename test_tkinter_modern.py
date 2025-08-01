import tkinter as tk
from tkinter import ttk, messagebox
import random
import math

class ModernBorderedTable:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("✨ Modern Excel Table - Viền đen rõ ràng")
        self.root.geometry("1100x650")
        self.root.configure(bg='#ffffff')
        
        self.setup_modern_theme()
        self.create_header()
        self.create_control_panel()
        self.create_modern_table()
        self.load_sample_data()
        
    def setup_modern_theme(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Modern style với viền đen rõ ràng
        self.style.configure("ModernBorder.Treeview",
                           background="white",
                           foreground="black",
                           rowheight=45,
                           fieldbackground="white",
                           font=('Arial', 11),
                           borderwidth=2,
                           relief="solid")
        
        self.style.configure("ModernBorder.Treeview.Heading",
                           background="#4472C4",
                           foreground="white",
                           font=('Arial', 12, 'bold'),
                           relief="solid",
                           borderwidth=2)
        
        # Hover effects với viền
        self.style.map("ModernBorder.Treeview",
                      background=[('selected', '#FFD700')],
                      foreground=[('selected', 'black')],
                      relief=[('selected', 'solid')],
                      borderwidth=[('selected', 3)])
    
    def create_header(self):
        # Header với viền
        header_frame = tk.Frame(self.root, bg='#f8f9fa', height=100, relief='solid', bd=3)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        # Main title với viền
        title_container = tk.Frame(header_frame, bg='white', relief='solid', bd=2)
        title_container.pack(expand=True, padx=20, pady=20)
        
        self.main_title = tk.Label(title_container,
                                  text="💼 QUẢN LÝ DỰ ÁN CÔNG TY",
                                  font=('Arial', 24, 'bold'),
                                  bg='white', fg='#2c3e50',
                                  padx=30, pady=15)
        self.main_title.pack()
        
        # Subtitle
        self.subtitle = tk.Label(title_container,
                               text="Dashboard hiện đại với viền Excel rõ ràng",
                               font=('Arial', 12),
                               bg='white', fg='#6c757d',
                               pady=(0, 10))
        self.subtitle.pack()
    
    def create_control_panel(self):
        # Control panel với viền rõ ràng
        control_frame = tk.Frame(self.root, bg='#e9ecef', relief='solid', bd=3)
        control_frame.pack(fill='x', padx=0, pady=0)
        
        # Left controls với viền
        left_controls = tk.Frame(control_frame, bg='#e9ecef')
        left_controls.pack(side='left', padx=20, pady=15)
        
        # Modern buttons với viền đậm
        buttons_data = [
            ("➕ Thêm mới", "#198754", self.add_project),
            ("✏️ Chỉnh sửa", "#fd7e14", self.edit_project),
            ("📊 Thống kê", "#0d6efd", self.show_stats),
            ("🗑️ Xóa", "#dc3545", self.delete_project)
        ]
        
        for text, color, command in buttons_data:
            btn = tk.Button(left_controls, text=text,
                           font=('Arial', 10, 'bold'),
                           bg=color, fg='white', relief='solid', bd=3,
                           padx=15, pady=8, cursor='hand2',
                           command=command)
            btn.pack(side='left', padx=5)
        
        # Right controls với viền
        right_controls = tk.Frame(control_frame, bg='#f8f9fa', relief='solid', bd=2)
        right_controls.pack(side='right', padx=20, pady=15)
        
        # Search với viền
        search_frame = tk.Frame(right_controls, bg='#f8f9fa')
        search_frame.pack(side='right', padx=10, pady=5)
        
        tk.Label(search_frame, text="🔍", font=('Arial', 14),
                bg='#f8f9fa').pack(side='left')
        
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var,
                               font=('Arial', 10),
                               width=20, relief='solid', bd=2)
        search_entry.pack(side='left', padx=5)
        search_entry.bind('<KeyRelease>', self.search_projects)
        
        # Status filter với viền
        filter_frame = tk.Frame(right_controls, bg='#f8f9fa')
        filter_frame.pack(side='right', padx=10, pady=5)
        
        tk.Label(filter_frame, text="Trạng thái:",
                font=('Arial', 10, 'bold'),
                bg='#f8f9fa').pack(side='left')
        
        self.status_var = tk.StringVar(value="Tất cả")
        status_combo = ttk.Combobox(filter_frame, textvariable=self.status_var,
                                   values=["Tất cả", "Đang thực hiện", "Hoàn thành", "Tạm dừng"],
                                   width=12, font=('Arial', 9))
        status_combo.pack(side='left', padx=5)
        status_combo.bind('<<ComboboxSelected>>', self.filter_by_status)
    
    def create_modern_table(self):
        # Table container với viền đậm
        table_container = tk.Frame(self.root, bg='black', relief='solid', bd=4)
        table_container.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Table header info với viền
        info_frame = tk.Frame(table_container, bg='#f8f9fa', height=50, relief='solid', bd=2)
        info_frame.pack(fill='x', padx=2, pady=(2, 0))
        info_frame.pack_propagate(False)
        
        self.info_label = tk.Label(info_frame,
                                  text="📋 Danh sách dự án - Excel Style",
                                  font=('Arial', 14, 'bold'),
                                  bg='#f8f9fa', fg='#212529')
        self.info_label.pack(side='left', padx=20, pady=15)
        
        # Live status với viền
        status_container = tk.Frame(info_frame, bg='#198754', relief='solid', bd=2)
        status_container.pack(side='right', padx=20, pady=10)
        
        self.live_status = tk.Label(status_container,
                                   text="🟢 LIVE",
                                   font=('Arial', 10, 'bold'),
                                   bg='#198754', fg='white',
                                   padx=10, pady=5)
        self.live_status.pack()
        
        # Treeview với viền rõ ràng
        tree_frame = tk.Frame(table_container, bg='black')
        tree_frame.pack(fill='both', expand=True, padx=2, pady=(0, 2))
        
        columns = ('ID', 'Tên dự án', 'Khách hàng', 'Ngày bắt đầu', 'Deadline', 'Tiến độ', 'Ngân sách', 'Trạng thái')
        self.tree = ttk.Treeview(tree_frame, columns=columns, show='headings',
                                style="ModernBorder.Treeview")
        
        # Configure columns với viền
        widths = [60, 200, 150, 100, 100, 80, 120, 120]
        for i, col in enumerate(columns):
            self.tree.heading(col, text=col, anchor='center')
            self.tree.column(col, width=widths[i], anchor='center', minwidth=50)
        
        # Custom scrollbars với viền
        v_scrollbar = ttk.Scrollbar(tree_frame, orient='vertical', command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(tree_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        v_scrollbar.pack(side='right', fill='y', padx=(1, 0), pady=1)
        h_scrollbar.pack(side='bottom', fill='x', padx=1, pady=(1, 0))
        self.tree.pack(side='left', fill='both', expand=True, padx=1, pady=1)
        
        # Double click binding
        self.tree.bind('<Double-1>', self.on_item_double_click)
        
        # Thêm Excel grid lines
        self.root.after(500, self.create_excel_grid_lines)
    
    def create_excel_grid_lines(self):
        """Tạo lưới Excel với viền đen rõ ràng như Excel thật"""
        # Canvas để vẽ grid
        canvas = tk.Canvas(self.tree, highlightthickness=0, bg='white')
        canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Tính toán vị trí các cột
        col_positions = [0]
        total_width = 0
        
        for col in self.tree['columns']:
            width = self.tree.column(col, 'width')
            total_width += width
            col_positions.append(total_width)
        
        # Vẽ viền ngoài đậm (như Excel)
        canvas.create_rectangle(1, 1, total_width-1, 600, 
                              outline='black', width=3, fill='')
        
        # Vẽ đường kẻ dọc (cột) với độ dày 2px
        for x in col_positions[1:-1]:  # Bỏ đường đầu và cuối
            canvas.create_line(x, 0, x, 600, fill='black', width=2)
        
        # Vẽ đường kẻ ngang (hàng)
        row_height = 45
        
        # Đường header đậm hơn
        canvas.create_line(0, row_height, total_width, row_height, 
                          fill='black', width=3)
        
        # Các đường hàng thường
        for i in range(1, 20):  # Đủ cho nhiều hàng
            y = i * row_height
            canvas.create_line(0, y, total_width, y, fill='black', width=1)
        
        # Tạo hiệu ứng shadow cho header
        canvas.create_rectangle(0, 0, total_width, row_height, 
                              outline='#4472C4', width=2, fill='')
    
    def load_sample_data(self):
        # Dữ liệu dự án với viền rõ ràng
        projects = [
            ('DX001', 'Website E-commerce', 'FPT Software', '01/01/2024', '31/03/2024', '85%', '500,000,000', '🟡 Đang thực hiện'),
            ('DX002', 'Mobile App Banking', 'Vietcombank', '15/02/2024', '15/05/2024', '100%', '800,000,000', '✅ Hoàn thành'),
            ('DX003', 'ERP System', 'Vingroup', '01/03/2024', '30/06/2024', '60%', '1,200,000,000', '🟡 Đang thực hiện'),
            ('DX004', 'AI Chatbot', 'VNPT', '10/01/2024', '28/02/2024', '100%', '300,000,000', '✅ Hoàn thành'),
            ('DX005', 'IoT Platform', 'Viettel', '01/04/2024', '31/07/2024', '30%', '900,000,000', '🟡 Đang thực hiện'),
            ('DX006', 'Blockchain Wallet', 'Techcombank', '15/03/2024', '15/06/2024', '0%', '600,000,000', '⏸️ Tạm dừng'),
            ('DX007', 'Cloud Migration', 'VNG Corporation', '01/02/2024', '30/04/2024', '95%', '700,000,000', '🟡 Đang thực hiện'),
            ('DX008', 'Data Analytics', 'FLC Group', '20/01/2024', '20/03/2024', '100%', '450,000,000', '✅ Hoàn thành'),
            ('DX009', 'Mobile Game', 'Gameloft', '05/03/2024', '05/08/2024', '45%', '350,000,000', '🟡 Đang thực hiện'),
            ('DX010', 'Smart Home App', 'Vinfast', '10/04/2024', '10/09/2024', '25%', '420,000,000', '🟡 Đang thực hiện')
        ]
        
        # Clear existing data
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Insert data với màu và viền
        for i, project in enumerate(projects):
            status = project[7]
            progress = int(project[5][:-1])  # Remove % and convert to int
            
            # Xác định tag dựa trên trạng thái và tiến độ
            if '✅' in status:
                tag = 'completed'
            elif '🟡' in status:
                if progress >= 80:
                    tag = 'near_completion'
                elif progress >= 50:
                    tag = 'in_progress'
                else:
                    tag = 'early_stage'
            elif '⏸️' in status:
                tag = 'paused'
            else:
                tag = 'default'
            
            # Add row alternation
            if i % 2 == 0:
                tag += '_even'
            
            self.tree.insert('', 'end', values=project, tags=(tag,))

        # Configure tags với màu nền và viền rõ ràng
        self.tree.tag_configure('completed', background='#d4edda', foreground='#155724')
        self.tree.tag_configure('completed_even', background='#e8f5e9', foreground='#155724')
        
        self.tree.tag_configure('near_completion', background='#d1ecf1', foreground='#0c5460')
        self.tree.tag_configure('near_completion_even', background='#e7f4f8', foreground='#0c5460')
        
        self.tree.tag_configure('in_progress', background='#fff3cd', foreground='#856404')
        self.tree.tag_configure('in_progress_even', background='#fffaed', foreground='#856404')
        
        self.tree.tag_configure('early_stage', background='#f8d7da', foreground='#721c24')
        self.tree.tag_configure('early_stage_even', background='#fdeced', foreground='#721c24')
        
        self.tree.tag_configure('paused', background='#e2e3e5', foreground='#383d41')
        self.tree.tag_configure('paused_even', background='#f1f3f4', foreground='#383d41')
        
        # Update info
        self.update_project_stats(len(projects))
    
    def update_project_stats(self, total):
        completed = len([item for item in self.tree.get_children() 
                        if '✅' in self.tree.item(item)['values'][7]])
        in_progress = len([item for item in self.tree.get_children() 
                          if '🟡' in self.tree.item(item)['values'][7]])
        paused = len([item for item in self.tree.get_children() 
                     if '⏸️' in self.tree.item(item)['values'][7]])
        
        self.info_label.config(
            text=f"📋 {total} dự án | ✅ {completed} hoàn thành | 🟡 {in_progress} đang thực hiện | ⏸️ {paused} tạm dừng"
        )
    
    # Event handlers
    def add_project(self):
        # Tạo popup thêm dự án với viền
        popup = tk.Toplevel(self.root)
        popup.title("Thêm dự án mới")
        popup.geometry("400x300")
        popup.configure(bg='white', relief='solid', bd=3)
        popup.resizable(False, False)
        
        # Center popup
        popup.transient(self.root)
        popup.grab_set()
        
        # Header với viền
        header = tk.Frame(popup, bg='#198754', height=60, relief='solid', bd=2)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        tk.Label(header, text="➕ THÊM DỰ ÁN MỚI",
                font=('Arial', 14, 'bold'),
                bg='#198754', fg='white').pack(expand=True)
        
        # Form với viền
        form_frame = tk.Frame(popup, bg='white', relief='solid', bd=1)
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Form fields
        fields = [
            ("Tên dự án:", ""),
            ("Khách hàng:", ""),
            ("Ngày bắt đầu:", "dd/mm/yyyy"),
            ("Deadline:", "dd/mm/yyyy"),
            ("Ngân sách:", "VNĐ")
        ]
        
        entries = {}
        for i, (label, placeholder) in enumerate(fields):
            tk.Label(form_frame, text=label, font=('Arial', 10, 'bold'),
                    bg='white', fg='#333').grid(row=i, column=0, sticky='w', pady=8)
            
            entry = tk.Entry(form_frame, font=('Arial', 10), width=25,
                           relief='solid', bd=2)
            entry.grid(row=i, column=1, padx=(10, 0), pady=8)
            entry.insert(0, placeholder)
            entries[label] = entry
        
        # Buttons với viền
        btn_frame = tk.Frame(form_frame, bg='white')
        btn_frame.grid(row=len(fields), column=0, columnspan=2, pady=20)
        
        tk.Button(btn_frame, text="✅ Lưu",
                 font=('Arial', 10, 'bold'),
                 bg='#198754', fg='white', relief='solid', bd=2,
                 padx=20, pady=8,
                 command=popup.destroy).pack(side='left', padx=10)
        
        tk.Button(btn_frame, text="❌ Hủy",
                 font=('Arial', 10, 'bold'),
                 bg='#dc3545', fg='white', relief='solid', bd=2,
                 padx=20, pady=8,
                 command=popup.destroy).pack(side='left')
    
    def edit_project(self):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            project_data = item['values']
            
            # Popup chỉnh sửa với viền
            popup = tk.Toplevel(self.root)
            popup.title(f"Chỉnh sửa - {project_data[1]}")
            popup.geometry("450x350")
            popup.configure(bg='white', relief='solid', bd=3)
            
            # Header
            header = tk.Frame(popup, bg='#fd7e14', height=60, relief='solid', bd=2)
            header.pack(fill='x')
            header.pack_propagate(False)
            
            tk.Label(header, text="✏️ CHỈNH SỬA DỰ ÁN",
                    font=('Arial', 14, 'bold'),
                    bg='#fd7e14', fg='white').pack(expand=True)
            
            # Content với thông tin hiện tại
            content = tk.Frame(popup, bg='white', relief='solid', bd=1)
            content.pack(fill='both', expand=True, padx=20, pady=20)
            
            info_text = f"""
📋 Thông tin hiện tại:
- ID: {project_data[0]}
- Tên: {project_data[1]}
- Khách hàng: {project_data[2]}
- Bắt đầu: {project_data[3]}
- Deadline: {project_data[4]}
- Tiến độ: {project_data[5]}
- Ngân sách: {project_data[6]} VNĐ
- Trạng thái: {project_data[7]}
            """
            
            tk.Label(content, text=info_text,
                    font=('Arial', 11),
                    bg='white', fg='#333',
                    justify='left').pack(pady=20)
            
            tk.Button(content, text="Đóng",
                     font=('Arial', 10, 'bold'),
                     bg='#6c757d', fg='white', relief='solid', bd=2,
                     padx=30, pady=10,
                     command=popup.destroy).pack()
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn dự án cần chỉnh sửa")
    
    def show_stats(self):
        # Tạo popup thống kê với viền
        popup = tk.Toplevel(self.root)
        popup.title("📊 Thống kê dự án")
        popup.geometry("500x400")
        popup.configure(bg='white', relief='solid', bd=3)
        
        # Header
        header = tk.Frame(popup, bg='#0d6efd', height=60, relief='solid', bd=2)
        header.pack(fill='x')
        header.pack_propagate(False)
        
        tk.Label(header, text="📊 THỐNG KÊ DỰ ÁN",
                font=('Arial', 14, 'bold'),
                bg='#0d6efd', fg='white').pack(expand=True)
        
        # Stats content với viền
        stats_frame = tk.Frame(popup, bg='white', relief='solid', bd=1)
        stats_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Tính toán thống kê
        total_projects = len(self.tree.get_children())
        total_budget = 0
        completed = 0
        in_progress = 0
        paused = 0
        
        for item in self.tree.get_children():
            values = self.tree.item(item)['values']
            budget = int(values[6].replace(',', ''))
            total_budget += budget
            
            status = values[7]
            if '✅' in status:
                completed += 1
            elif '🟡' in status:
                in_progress += 1
            elif '⏸️' in status:
                paused += 1
        
        # Hiển thị thống kê với viền
        stats_data = [
            ("📊 Tổng số dự án:", f"{total_projects} dự án"),
            ("💰 Tổng ngân sách:", f"{total_budget:,} VNĐ"),
            ("✅ Hoàn thành:", f"{completed} dự án ({completed/total_projects*100:.1f}%)"),
            ("🟡 Đang thực hiện:", f"{in_progress} dự án ({in_progress/total_projects*100:.1f}%)"),
            ("⏸️ Tạm dừng:", f"{paused} dự án ({paused/total_projects*100:.1f}%)"),
            ("💵 Ngân sách trung bình:", f"{total_budget//total_projects:,} VNĐ/dự án")
        ]
        
        for i, (label, value) in enumerate(stats_data):
            # Frame cho mỗi stat với viền
            stat_frame = tk.Frame(stats_frame, bg='#f8f9fa', relief='solid', bd=1)
            stat_frame.pack(fill='x', pady=5)
            
            tk.Label(stat_frame, text=label,
                    font=('Arial', 11, 'bold'),
                    bg='#f8f9fa', fg='#495057').pack(side='left', padx=15, pady=10)
            
            tk.Label(stat_frame, text=value,
                    font=('Arial', 11),
                    bg='#f8f9fa', fg='#0d6efd').pack(side='right', padx=15, pady=10)
        
        # Close button
        tk.Button(stats_frame, text="Đóng",
                 font=('Arial', 10, 'bold'),
                 bg='#6c757d', fg='white', relief='solid', bd=2,
                 padx=30, pady=10,
                 command=popup.destroy).pack(pady=20)
    
    def delete_project(self):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            project_name = item['values'][1]
            
            # Confirmation dialog với viền
            if messagebox.askyesno("Xác nhận xóa", 
                                 f"Bạn có chắc muốn xóa dự án:\n'{project_name}'?",
                                 icon='warning'):
                self.tree.delete(selection[0])
                self.update_project_stats(len(self.tree.get_children()))
                messagebox.showinfo("Thành công", f"Đã xóa dự án '{project_name}'")
        else:
            messagebox.showwarning("Cảnh báo", "Vui lòng chọn dự án cần xóa")
    
    def search_projects(self, event):
        search_term = self.search_var.get().lower()
        # Simple search implementation - có thể mở rộng
        if search_term:
            self.info_label.config(text=f"🔍 Tìm kiếm: '{search_term}'")
        else:
            self.update_project_stats(len(self.tree.get_children()))
    
    def filter_by_status(self, event):
        status = self.status_var.get()
        self.info_label.config(text=f"📋 Lọc theo: {status}")
    
    def on_item_double_click(self, event):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            project_data = item['values']
            
            # Popup chi tiết với viền đẹp
            detail_window = tk.Toplevel(self.root)
            detail_window.title(f"Chi tiết - {project_data[1]}")
            detail_window.geometry("600x500")
            detail_window.configure(bg='white', relief='solid', bd=4)
            detail_window.resizable(False, False)
            
            # Center the window
            detail_window.transient(self.root)
            detail_window.grab_set()
            
            # Header với gradient effect
            header = tk.Frame(detail_window, bg='#4472C4', height=80, relief='solid', bd=3)
            header.pack(fill='x')
            header.pack_propagate(False)
            
            tk.Label(header, text=f"📋 {project_data[1]}",
                    font=('Arial', 18, 'bold'),
                    bg='#4472C4', fg='white').pack(expand=True)
            
            # Content với viền
            content = tk.Frame(detail_window, bg='white', relief='solid', bd=2)
            content.pack(fill='both', expand=True, padx=20, pady=20)
            
            # Details với viền cho mỗi thông tin
            details = [
                ("🆔 Mã dự án", project_data[0]),
                ("👤 Khách hàng", project_data[2]),
                ("📅 Ngày bắt đầu", project_data[3]),
                ("⏰ Deadline", project_data[4]),
                ("📊 Tiến độ", project_data[5]),
                ("💰 Ngân sách", f"{project_data[6]} VNĐ"),
                ("📈 Trạng thái", project_data[7])
            ]
            
            for label, value in details:
                detail_frame = tk.Frame(content, bg='#f8f9fa', relief='solid', bd=1)
                detail_frame.pack(fill='x', pady=8)
                
                tk.Label(detail_frame, text=label,
                        font=('Arial', 12, 'bold'),
                        bg='#f8f9fa', fg='#495057').pack(side='left', padx=20, pady=15)
                
                tk.Label(detail_frame, text=value,
                        font=('Arial', 12),
                        bg='#f8f9fa', fg='#0d6efd').pack(side='right', padx=20, pady=15)
            
            # Progress bar
            progress_val = int(project_data[5][:-1])
            progress_frame = tk.Frame(content, bg='white')
            progress_frame.pack(fill='x', pady=20)
            
            tk.Label(progress_frame, text="Tiến độ thực hiện:",
                    font=('Arial', 11, 'bold'),
                    bg='white').pack()
            
            # Custom progress bar với viền
            progress_bg = tk.Frame(progress_frame, bg='#e9ecef', height=20, relief='solid', bd=2)
            progress_bg.pack(fill='x', padx=50, pady=10)
            
            progress_fill = tk.Frame(progress_bg, bg='#198754', height=16)
            progress_fill.place(x=2, y=2, width=(progress_val/100)*(progress_bg.winfo_reqwidth()-4))
            
            # Close button với viền
            btn_frame = tk.Frame(content, bg='white')
            btn_frame.pack(pady=20)
            
            tk.Button(btn_frame, text="Đóng",
                     font=('Arial', 12, 'bold'),
                     bg='#6c757d', fg='white', relief='solid', bd=3,
                     padx=40, pady=12,
                     command=detail_window.destroy).pack()
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ModernBorderedTable()
    app.run()