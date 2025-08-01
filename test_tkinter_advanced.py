import tkinter as tk
from tkinter import ttk
import random

class AdvancedBorderedTable:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("💼 Dashboard - Viền đen Excel")
        self.root.geometry("1000x600")
        self.root.configure(bg='#f5f5f5')
        
        self.setup_bordered_styles()
        self.create_widgets()
        self.load_data()
        
    def setup_bordered_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Style với viền đen rõ ràng
        self.style.configure("ExcelBorder.Treeview",
                           background="white",
                           foreground="black",
                           rowheight=35,
                           fieldbackground="white",
                           font=('Arial', 10),
                           borderwidth=1,
                           relief="solid")
        
        self.style.configure("ExcelBorder.Treeview.Heading",
                           background="#D9D9D9",
                           foreground="black",
                           font=('Arial', 11, 'bold'),
                           borderwidth=2,
                           relief="solid")
        
        # Map cho selection với viền
        self.style.map("ExcelBorder.Treeview",
                      background=[('selected', '#316AC5')],
                      foreground=[('selected', 'white')],
                      relief=[('selected', 'solid')],
                      borderwidth=[('selected', 2)])
        
    def create_widgets(self):
        # Header
        header_frame = tk.Frame(self.root, bg='#2c3e50', height=80)
        header_frame.pack(fill='x', padx=0, pady=0)
        header_frame.pack_propagate(False)
        
        title = tk.Label(header_frame, 
                        text="🏢 DANH SÁCH NHÂN VIÊN",
                        font=('Arial', 20, 'bold'),
                        bg='#2c3e50', fg='white')
        title.pack(expand=True)
        
        # Main content frame với viền
        content_frame = tk.Frame(self.root, bg='white', relief='solid', bd=2)
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Toolbar với viền
        toolbar = tk.Frame(content_frame, bg='#f0f0f0', height=50, relief='solid', bd=1)
        toolbar.pack(fill='x', pady=(10, 10))
        toolbar.pack_propagate(False)
        
        # Buttons
        btn_frame = tk.Frame(toolbar, bg='#f0f0f0')
        btn_frame.pack(side='left', padx=10, pady=10)
        
        buttons = [
            ("➕ Thêm", '#28a745', self.add_employee),
            ("✏️ Sửa", '#ffc107', self.edit_employee),
            ("🗑️ Xóa", '#dc3545', self.delete_employee)
        ]
        
        for text, color, cmd in buttons:
            btn = tk.Button(btn_frame, text=text, bg=color, fg='white',
                           font=('Arial', 9, 'bold'), relief='solid', bd=1,
                           padx=10, pady=5, command=cmd)
            btn.pack(side='left', padx=5)
        
        # Search với viền
        search_frame = tk.Frame(toolbar, bg='#f0f0f0')
        search_frame.pack(side='right', padx=10, pady=10)
        
        tk.Label(search_frame, text="🔍", bg='#f0f0f0',
                font=('Arial', 12)).pack(side='left')
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var,
                               font=('Arial', 10), width=20, relief='solid', bd=1)
        search_entry.pack(side='left', padx=5)
        
        # Table frame với viền đậm
        table_frame = tk.Frame(content_frame, bg='black', relief='solid', bd=3)
        table_frame.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Treeview với grid lines
        columns = ('ID', 'Họ tên', 'Phòng ban', 'Chức vụ', 'Lương', 'Trạng thái')
        self.tree = ttk.Treeview(table_frame, columns=columns, show='headings', 
                                style="ExcelBorder.Treeview")
        
        # Cấu hình columns với viền
        widths = [80, 200, 150, 120, 150, 100]
        for i, col in enumerate(columns):
            self.tree.heading(col, text=col, anchor='center')
            self.tree.column(col, width=widths[i], anchor='center',
                           minwidth=50)
        
        # Scrollbars với viền
        v_scrollbar = ttk.Scrollbar(table_frame, orient='vertical', command=self.tree.yview)
        h_scrollbar = ttk.Scrollbar(table_frame, orient='horizontal', command=self.tree.xview)
        self.tree.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack với padding để tạo viền
        v_scrollbar.pack(side='right', fill='y', padx=(1,0), pady=1)
        h_scrollbar.pack(side='bottom', fill='x', padx=1, pady=(1,0))
        self.tree.pack(side='left', fill='both', expand=True, padx=1, pady=1)
        
        # Status bar với viền
        status_frame = tk.Frame(self.root, bg='#343a40', height=30, relief='solid', bd=1)
        status_frame.pack(fill='x', side='bottom')
        status_frame.pack_propagate(False)
        
        self.status_label = tk.Label(status_frame, text="✅ Sẵn sàng",
                                    bg='#343a40', fg='white', font=('Arial', 9))
        self.status_label.pack(side='left', padx=10, pady=5)
        
        # Thêm grid lines sau khi render
        self.root.after(200, self.add_excel_grid)
        
    def add_excel_grid(self):
        """Thêm lưới grid giống Excel với viền đen"""
        # Tạo canvas overlay để vẽ grid
        tree_bbox = self.tree.bbox('')
        if tree_bbox:
            canvas = tk.Canvas(self.tree, highlightthickness=0, bg='')
            canvas.place(x=0, y=0, relwidth=1, relheight=1)
            
            # Vẽ đường kẻ dọc (cột)
            col_positions = [0]
            for i, col in enumerate(self.tree['columns']):
                col_width = self.tree.column(col, 'width')
                col_positions.append(col_positions[-1] + col_width)
                
                if i < len(self.tree['columns']) - 1:  # Không vẽ đường cuối
                    x = col_positions[-1]
                    canvas.create_line(x, 0, x, 2000, fill='black', width=1)
            
            # Vẽ đường kẻ ngang (hàng)
            row_height = 35
            for i in range(20):  # Vẽ nhiều đường để đảm bảo đủ
                y = i * row_height
                canvas.create_line(0, y, sum(col_positions), y, fill='black', width=1)
    
    def load_data(self):
        employees = [
            ('NV001', 'Nguyễn Văn An', 'IT', 'Trưởng nhóm', '25,000,000', 'Đang làm'),
            ('NV002', 'Trần Thị Bình', 'HR', 'Quản lý', '30,000,000', 'Đang làm'),
            ('NV003', 'Lê Văn Cường', 'Marketing', 'Nhân viên', '15,000,000', 'Thử việc'),
            ('NV004', 'Phạm Thị Dung', 'Sales', 'Trưởng nhóm', '22,000,000', 'Đang làm'),
            ('NV005', 'Hoàng Văn Em', 'Finance', 'Nhân viên', '18,000,000', 'Nghỉ phép'),
            ('NV006', 'Nguyễn Thị Lan', 'IT', 'Giám đốc', '50,000,000', 'Đang làm'),
            ('NV007', 'Trần Văn Nam', 'HR', 'Nhân viên', '12,000,000', 'Đang làm'),
            ('NV008', 'Lê Thị Hoa', 'Marketing', 'Quản lý', '28,000,000', 'Đang làm')
        ]
        
        for emp in employees:
            self.tree.insert('', 'end', values=emp)
        
        self.update_status(f"Đã tải {len(employees)} nhân viên")
    
    def add_employee(self):
        self.update_status("Chức năng thêm nhân viên")
    
    def edit_employee(self):
        selection = self.tree.selection()
        if selection:
            self.update_status("Chức năng sửa nhân viên")
        else:
            self.update_status("Vui lòng chọn nhân viên cần sửa")
    
    def delete_employee(self):
        selection = self.tree.selection()
        if selection:
            self.tree.delete(selection)
            self.update_status("Đã xóa nhân viên")
        else:
            self.update_status("Vui lòng chọn nhân viên cần xóa")
    
    def update_status(self, message):
        self.status_label.config(text=f"📊 {message}")
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = AdvancedBorderedTable()
    app.run()