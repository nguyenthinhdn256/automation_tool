import tkinter as tk
from tkinter import ttk

def create_basic_excel_table():
    root = tk.Tk()
    root.title("📊 Bảng Excel - Viền đen rõ ràng")
    root.geometry("800x500")
    root.configure(bg='#f0f0f0')
    
    # Title
    title_label = tk.Label(root, text="BẢNG ĐIỂM SINH VIÊN", 
                          font=('Arial', 16, 'bold'), 
                          bg='#f0f0f0', fg='#2c3e50')
    title_label.pack(pady=20)
    
    # Frame cho bảng
    frame = tk.Frame(root, bg='white', relief='solid', bd=2)
    frame.pack(padx=20, pady=10, fill='both', expand=True)
    
    # Treeview với viền đen rõ ràng
    style = ttk.Style()
    style.theme_use('clam')
    
    # Cấu hình style với viền đen
    style.configure("Bordered.Treeview", 
                   background="white",
                   foreground="black",
                   rowheight=30,
                   fieldbackground="white",
                   font=('Arial', 10),
                   borderwidth=1,
                   relief="solid")
    
    style.configure("Bordered.Treeview.Heading", 
                   background="#E7E6E6",
                   foreground="black",
                   font=('Arial', 11, 'bold'),
                   borderwidth=1,
                   relief="solid")
    
    # Map để thêm viền khi selected
    style.map("Bordered.Treeview",
             background=[('selected', '#B3D9FF')],
             relief=[('selected', 'solid')],
             borderwidth=[('selected', 1)])
    
    # Tạo Treeview
    columns = ('Mã SV', 'Họ tên', 'Ngành học', 'Điểm', 'Xếp loại')
    tree = ttk.Treeview(frame, columns=columns, show='headings', style="Bordered.Treeview")
    
    # Định nghĩa headers với viền
    for col in columns:
        tree.heading(col, text=col, anchor='center')
        tree.column(col, width=150, anchor='center', 
                   minwidth=100)  # Đảm bảo có độ rộng tối thiểu
    
    # Dữ liệu
    data = [
        ('SV001', 'Nguyễn Văn An', 'Tin học', '85', 'Giỏi'),
        ('SV002', 'Trần Thị Bình', 'Toán học', '92', 'Xuất sắc'),
        ('SV003', 'Lê Văn Cường', 'Vật lý', '78', 'Khá'),
        ('SV004', 'Phạm Thị Dung', 'Hóa học', '88', 'Giỏi'),
        ('SV005', 'Hoàng Văn Em', 'Sinh học', '95', 'Xuất sắc'),
        ('SV006', 'Nguyễn Thị Lan', 'Anh văn', '83', 'Giỏi'),
        ('SV007', 'Trần Văn Nam', 'Lịch sử', '76', 'Khá'),
        ('SV008', 'Lê Thị Hoa', 'Địa lý', '90', 'Xuất sắc')
    ]
    
    # Thêm dữ liệu vào bảng với viền
    for i, row in enumerate(data):
        tree.insert('', 'end', values=row)
    
    # CSS-like configuration cho viền rõ ràng
    tree.configure(selectmode='browse')
    
    # Scrollbar
    scrollbar = ttk.Scrollbar(frame, orient='vertical', command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    scrollbar.pack(side='right', fill='y')
    tree.pack(side='left', fill='both', expand=True)
    
    # Thêm viền bằng cách sử dụng Frame wrapper
    border_frame = tk.Frame(tree, bg='black')
    border_frame.place(x=0, y=0, relwidth=1, relheight=1)
    
    # Footer
    footer_label = tk.Label(root, text="✅ Tổng cộng: 8 sinh viên", 
                           font=('Arial', 10), bg='#f0f0f0', fg='#666')
    footer_label.pack(pady=10)
    
    # Thêm CSS để tạo viền grid
    def add_grid_lines():
        # Tạo hiệu ứng viền grid bằng cách vẽ lines
        canvas = tk.Canvas(tree, highlightthickness=0)
        canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Vẽ các đường kẻ dọc
        col_widths = [150, 150, 150, 150, 150]  # Độ rộng các cột
        x_pos = 0
        for width in col_widths[:-1]:  # Không vẽ đường cuối
            x_pos += width
            canvas.create_line(x_pos, 0, x_pos, 1000, fill='black', width=1)
        
        # Vẽ các đường kẻ ngang
        for i in range(len(data) + 2):  # +2 cho header và buffer
            y_pos = i * 30
            canvas.create_line(0, y_pos, 1000, y_pos, fill='black', width=1)
    
    # Gọi sau khi widget được render
    root.after(100, add_grid_lines)
    
    root.mainloop()

if __name__ == "__main__":
    create_basic_excel_table()