import tkinter as tk
from tkinter import messagebox, filedialog
import csv

class RGBGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("RGB 数值生成器")
        
        # 设置窗口大小和位置
        window_width = 400
        window_height = 300
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width/2)
        center_y = int(screen_height/2 - window_height/2)
        self.root.geometry(f"{window_width}x{window_height}+{center_x}+{center_y}")
        
        # 创建界面元素
        self.create_widgets()
    
    def create_widgets(self):
        # 标题
        title_label = tk.Label(self.root, text="RGB 数值生成器", font=("Microsoft YaHei", 16))
        title_label.pack(pady=10)
        
        # R 通道设置
        r_frame = tk.Frame(self.root)
        r_frame.pack(pady=5)
        tk.Label(r_frame, text="R 范围:", font=("Microsoft YaHei", 10)).pack(side=tk.LEFT)
        self.r_min = tk.Entry(r_frame, width=5)
        self.r_min.pack(side=tk.LEFT, padx=5)
        tk.Label(r_frame, text="到", font=("Microsoft YaHei", 10)).pack(side=tk.LEFT)
        self.r_max = tk.Entry(r_frame, width=5)
        self.r_max.pack(side=tk.LEFT, padx=5)
        self.r_min.insert(0, "0")
        self.r_max.insert(0, "0")
        
        # G 通道设置
        g_frame = tk.Frame(self.root)
        g_frame.pack(pady=5)
        tk.Label(g_frame, text="G 范围:", font=("Microsoft YaHei", 10)).pack(side=tk.LEFT)
        self.g_min = tk.Entry(g_frame, width=5)
        self.g_min.pack(side=tk.LEFT, padx=5)
        tk.Label(g_frame, text="到", font=("Microsoft YaHei", 10)).pack(side=tk.LEFT)
        self.g_max = tk.Entry(g_frame, width=5)
        self.g_max.pack(side=tk.LEFT, padx=5)
        self.g_min.insert(0, "0")
        self.g_max.insert(0, "0")
        
        # B 通道设置
        b_frame = tk.Frame(self.root)
        b_frame.pack(pady=5)
        tk.Label(b_frame, text="B 范围:", font=("Microsoft YaHei", 10)).pack(side=tk.LEFT)
        self.b_min = tk.Entry(b_frame, width=5)
        self.b_min.pack(side=tk.LEFT, padx=5)
        tk.Label(b_frame, text="到", font=("Microsoft YaHei", 10)).pack(side=tk.LEFT)
        self.b_max = tk.Entry(b_frame, width=5)
        self.b_max.pack(side=tk.LEFT, padx=5)
        self.b_min.insert(0, "1")
        self.b_max.insert(0, "255")
        
        # 步长设置
        step_frame = tk.Frame(self.root)
        step_frame.pack(pady=5)
        tk.Label(step_frame, text="步长:", font=("Microsoft YaHei", 10)).pack(side=tk.LEFT)
        self.step = tk.Entry(step_frame, width=5)
        self.step.pack(side=tk.LEFT, padx=5)
        self.step.insert(0, "1")
        
        # 生成按钮
        generate_btn = tk.Button(
            self.root, 
            text="生成 CSV 文件", 
            font=("Microsoft YaHei", 12), 
            command=self.generate_csv
        )
        generate_btn.pack(pady=20)
    
    def validate_inputs(self):
        try:
            r_min = int(self.r_min.get())
            r_max = int(self.r_max.get())
            g_min = int(self.g_min.get())
            g_max = int(self.g_max.get())
            b_min = int(self.b_min.get())
            b_max = int(self.b_max.get())
            step = int(self.step.get())
            
            if (r_min < 0 or r_max < 0 or g_min < 0 or g_max < 0 or b_min < 0 or b_max < 0 or
                r_min > 255 or r_max > 255 or g_min > 255 or g_max > 255 or b_min > 255 or b_max > 255):
                raise ValueError("RGB 值必须在 0-255 之间")
                
            if step <= 0:
                raise ValueError("步长必须大于 0")
                
            return True, (r_min, r_max, g_min, g_max, b_min, b_max, step)
        except ValueError as e:
            messagebox.showerror("输入错误", str(e))
            return False, None
    
    def generate_csv(self):
        valid, values = self.validate_inputs()
        if not valid:
            return
        
        r_min, r_max, g_min, g_max, b_min, b_max, step = values
        
        # 询问保存位置
        file_path = filedialog.asksaveasfilename(
            defaultextension=".csv",
            filetypes=[("CSV 文件", "*.csv"), ("所有文件", "*.*")],
            title="保存 CSV 文件"
        )
        
        if not file_path:
            return  # 用户取消了保存
        
        try:
            with open(file_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                
                # 生成 RGB 组合
                for r in range(r_min, r_max + 1, step):
                    for g in range(g_min, g_max + 1, step):
                        for b in range(b_min, b_max + 1, step):
                            writer.writerow([r, g, b])
            
            messagebox.showinfo("成功", f"CSV 文件已成功生成并保存到:\n{file_path}")
        except Exception as e:
            messagebox.showerror("错误", f"生成 CSV 文件时出错:\n{str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = RGBGeneratorApp(root)
    root.mainloop()