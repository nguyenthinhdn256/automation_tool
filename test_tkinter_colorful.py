import tkinter as tk
from tkinter import ttk
import random

class ColorfulBorderedTable:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("🌈 Bảng Sản Phẩm - Viền đen + Màu sắc")
        self.root.geometry("900x600")
        self.root.configure(bg='#f0f8ff')
        
        self.setup_styles()
        self.create_widgets()
        self.load_data()
        
    def setup_styles(self):
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Colorful style với viền đen rõ ràng
        self.style.configure("ColorBorder.Treeview",
                           background="white",
                           foreground="black",
                           rowheight=40,
                           fieldbackground="white",
                           font=('Arial', 10, 'bold'),
                           borderwidth=2,
                           relief="solid")
        
        self.style.configure("ColorBorder.Treeview.Heading",
                           background="#4472C4",
                           foreground="white",
                           font=('Arial', 12, 'bold'),
                           relief="solid",
                           borderwidth=2)
        
        # Selection với viền đậm
        self.style.map("ColorBorder.Treeview",
                      background=[('selected', '#FFD700')],
                      foreground=[('selected', 'black')],
                      relief=[('selected', 'solid')],
                      borderwidth=[('selected', 3)])
    
    def create_widgets(self):
        # Main frame
        main_frame = tk.Frame(self.root, bg='#f0f8ff')
        main_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Title với viền
        title_frame = tk.Frame(main_frame, bg='white', relief='solid', bd=3)
        title_frame.pack(pady=(0, 20))
        
        title = tk.Label(title_frame, 
                        text="🛒 DANH SÁCH SẢN PHẨM 🛒",
                        font=('Arial', 18, 'bold'),
                        bg='white', fg='#e74c3c',
                        padx=20, pady=15)
        title.pack()
        
        # Table container với viền đậm
        table_container = tk.Frame(main_frame, bg='black', relief='solid', bd=4)
        table_container.pack(fill='both', expand=True)
        
        # Info labels với viền
        info_frame = tk.Frame(table_container, bg='#f39c12', height=40, relief='solid', bd=2)
        info_frame.pack(fill='x', padx=2, pady=(2, 0))
        info_frame.pack_propagate(False)
        
        tk.Label(info_frame, text="📊 Thống kê kho hàng - Viền Excel",
                font=('Arial', 12, 'bold'),
                bg='#f39c12', fg='white').pack(expand=True)
        
        # Treeview với viền
        columns = ('Mã SP', 'Tên sản phẩm', 'Giá bán', 'Tồn kho', 'Danh mục', 'Trạng thái')
        self.tree = ttk.Treeview(table_container, columns=columns, show='headings',
                                style="ColorBorder.Treeview", height=12)
        
        # Cấu hình columns
        widths = [80, 200, 120, 80, 120, 100]
        
        for i, col in enumerate(columns):
            self.tree.heading(col, text=f"{col}", anchor='center')
            self.tree.column(col, width=widths[i], anchor='center', minwidth=60)
        
        # Scrollbar với viền
        scrollbar_frame = tk.Frame(table_container, bg='black')
        scrollbar_frame.pack(side='right', fill='y', padx=(0, 2), pady=2)
        
        scrollbar = ttk.Scrollbar(scrollbar_frame, orient='vertical', command=self.tree.yview)
        self.tree.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(fill='y')
        
        self.tree.pack(side='left', padx=2, pady=2, fill='both', expand=True)
        
        # Footer với viền
        footer_frame = tk.Frame(main_frame, bg='#34495e', relief='solid', bd=2)
        footer_frame.pack(fill='x', pady=(10, 0))
        
        self.stats_label = tk.Label(footer_frame,
                                   text="📈 Thống kê sẽ hiển thị ở đây",
                                   font=('Arial', 10, 'bold'),
                                   bg='#34495e', fg='white', pady=15)
        self.stats_label.pack()
        
        # Thêm grid sau khi render
        self.root.after(300, self.create_excel_grid)
    
    def create_excel_grid(self):
        """Tạo lưới Excel với viền đen rõ ràng"""
        # Tạo canvas để vẽ grid
        canvas = tk.Canvas(self.tree, highlightthickness=0)
        canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Lấy thông tin cột
        total_width = 0
        col_positions = [0]
        
        for col in self.tree['columns']:
            width = self.tree.column(col, 'width')
            total_width += width
            col_positions.append(total_width)
        
        # Vẽ đường kẻ dọc (giữa các cột)
        for x in col_positions[1:-1]:  # Bỏ đường đầu và cuối
            canvas.create_line(x, 0, x, 3000, fill='black', width=2)
        
        # Vẽ đường kẻ ngang (giữa các hàng)
        row_height = 40
        for i in range(50):  # Đủ để cover tất cả hàng
            y = i * row_height
            canvas.create_line(0, y, total_width, y, fill='black', width=1)
        
        # Vẽ viền ngoài
        canvas.create_rectangle(0, 0, total_width, 20*row_height, 
                              outline='black', width=3, fill='')
    
    def load_data(self):
        # Dữ liệu sản phẩm với màu sắc
        products = [
            ('SP001', '📱 iPhone 15 Pro Max', '30,000,000', '25', 'Điện thoại', '🟢 Còn hàng'),
            ('SP002', '💻 MacBook Pro M3', '45,000,000', '12', 'Laptop', '🟢 Còn hàng'),
            ('SP003', '🎧 AirPods Pro', '6,000,000', '0', 'Phụ kiện', '🔴 Hết hàng'),
            ('SP004', '⌚ Apple Watch', '12,000,000', '8', 'Đồng hồ', '🟡 Sắp hết'),
            ('SP005', '📺 Smart TV 55"', '15,000,000', '15', 'TV', '🟢 Còn hàng'),
            ('SP006', '🖥️ iMac 24"', '35,000,000', '5', 'Desktop', '🟡 Sắp hết'),
            ('SP007', '📷 Canon EOS R5', '85,000,000', '3', 'Camera', '🟡 Sắp hết'),
            ('SP008', '🎮 PlayStation 5', '15,000,000', '20', 'Game', '🟢 Còn hàng'),
            ('SP009', '🖱️ Magic Mouse', '2,500,000', '50', 'Phụ kiện', '🟢 Còn hàng'),
            ('SP010', '⌨️ Magic Keyboard', '4,500,000', '30', 'Phụ kiện', '🟢 Còn hàng')
        ]
        
        # Thêm dữ liệu với màu nền xen kẽ
        total_value = 0
        in_stock = 0
        
        for i, product in enumerate(products):
            # Màu nền xen kẽ nhưng vẫn giữ viền
            tag = 'even_row' if i % 2 == 0 else 'odd_row'
            
            # Thêm tag cho trạng thái
            if '🔴' in product[5]:
                tag += '_out_stock'
            elif '🟡' in product[5]:
                tag += '_low_stock'
            else:
                tag += '_in_stock'
            
            self.tree.insert('', 'end', values=product, tags=(tag,))
            
            # Tính thống kê
            stock = int(product[3])
            if stock > 0:
                in_stock += 1
                price = int(product[2].replace(',', ''))
                total_value += price * stock
        
        # Cấu hình màu cho các tag với viền
        # Hàng chẵn
        self.tree.tag_configure('even_row_in_stock', background='#E8F5E8')
        self.tree.tag_configure('even_row_low_stock', background='#FFF3CD')
        self.tree.tag_configure('even_row_out_stock', background='#F8D7DA')
        
        # Hàng lẻ
        self.tree.tag_configure('odd_row_in_stock', background='#F0FFF0')
        self.tree.tag_configure('odd_row_low_stock', background='#FFFACD')
        self.tree.tag_configure('odd_row_out_stock', background='#FFE4E1')
        
        # Cập nhật thống kê
        self.stats_label.config(
            text=f"📊 Tổng: {len(products)} SP | 🟢 Còn hàng: {in_stock} | 💰 Giá trị: {total_value:,} VNĐ"
        )
        
        # Bind events
        self.tree.bind('<Double-1>', self.on_item_select)
    
    def on_item_select(self, event):
        selection = self.tree.selection()
        if selection:
            item = self.tree.item(selection[0])
            product_name = item['values'][1]
            # Hiển thị thông báo với viền
            popup = tk.Toplevel(self.root)
            popup.title("Thông tin sản phẩm")
            popup.geometry("300x150")
            popup.configure(bg='white', relief='solid', bd=3)
            
            tk.Label(popup, text=f"Đã chọn:\n{product_name}",
                    font=('Arial', 12, 'bold'),
                    bg='white', fg='#2c3e50',
                    justify='center').pack(expand=True)
            
            tk.Button(popup, text="Đóng", 
                     font=('Arial', 10, 'bold'),
                     bg='#e74c3c', fg='white',
                     relief='solid', bd=2,
                     command=popup.destroy).pack(pady=10)
    
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = ColorfulBorderedTable()
    app.run()