import tkinter as tk
from tkinter import messagebox
from collections import deque
import os

class KnightPathGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Задача про шахового коня (Найкоротший шлях)")
        
        self.N = 8
        self.cell_size = 50
        self.start_pos = None
        self.end_pos = None
        self.path = []

        self.setup_ui()
        self.draw_board()

    def setup_ui(self):
        control_frame = tk.Frame(self.root, padx=10, pady=10)
        control_frame.pack(side=tk.LEFT, fill=tk.Y)

        instructions = (
            "Інструкція:\n"
            "1. Клікніть на дошку, щоб \nвстановити СТАРТ (зелений).\n"
            "2. Клікніть вдруге, щоб \nвстановити ФІНІШ (червоний).\n"
            "3. Шлях побудується автоматично.\n\n"
            "Щоб почати заново -- \nклікніть ще раз."
        )
        tk.Label(control_frame, text=instructions, justify=tk.LEFT).pack(pady=10)

        self.info_label = tk.Label(control_frame, text="Кроків: 0", font=("Helvetica", 12, "bold"), fg="blue")
        self.info_label.pack(pady=20)

        tk.Button(control_frame, text="Зчитати з input.txt", command=self.process_files, bg="lightgray").pack(fill=tk.X, pady=5)
        tk.Button(control_frame, text="Очистити дошку", command=self.reset_board).pack(fill=tk.X, pady=5)

        self.canvas = tk.Canvas(self.root, width=self.N*self.cell_size, height=self.N*self.cell_size, bg="white")
        self.canvas.pack(side=tk.RIGHT, padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.on_canvas_click)

    def draw_board(self):
        self.canvas.delete("all")
        self.canvas.config(width=self.N*self.cell_size, height=self.N*self.cell_size)

        for r in range(self.N):
            for c in range(self.N):
                color = "white" if (r + c) % 2 == 0 else "black"
                x1 = c * self.cell_size
                y1 = r * self.cell_size
                x2 = x1 + self.cell_size
                y2 = y1 + self.cell_size
                self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="gray")

        if self.path:
            for i, (r, c) in enumerate(self.path):
                x = c * self.cell_size + self.cell_size // 2
                y = r * self.cell_size + self.cell_size // 2
                
                if i > 0:
                    prev_r, prev_c = self.path[i-1]
                    px = prev_c * self.cell_size + self.cell_size // 2
                    py = prev_r * self.cell_size + self.cell_size // 2
                    self.canvas.create_line(px, py, x, y, fill="blue", width=3)
                
                if (r, c) != self.start_pos and (r, c) != self.end_pos:
                    self.canvas.create_text(x, y, text="X", fill="red", font=("Arial", 16, "bold"))

        if self.start_pos:
            r, c = self.start_pos
            x = c * self.cell_size + self.cell_size // 2
            y = r * self.cell_size + self.cell_size // 2
            self.canvas.create_oval(x-15, y-15, x+15, y+15, fill="green")
            self.canvas.create_text(x, y, text="S", fill="white", font=("Arial", 12, "bold"))

        if self.end_pos:
            r, c = self.end_pos
            x = c * self.cell_size + self.cell_size // 2
            y = r * self.cell_size + self.cell_size // 2
            self.canvas.create_oval(x-15, y-15, x+15, y+15, fill="red")
            self.canvas.create_text(x, y, text="F", fill="white", font=("Arial", 12, "bold"))

    def on_canvas_click(self, event):
        col = event.x // self.cell_size
        row = event.y // self.cell_size

        if 0 <= row < self.N and 0 <= col < self.N:
            if self.start_pos is None:
                self.start_pos = (row, col)
                self.draw_board()
            elif self.end_pos is None:
                self.end_pos = (row, col)
                self.solve()
            else:
                self.start_pos = (row, col)
                self.end_pos = None
                self.path = []
                self.info_label.config(text="Кроків: 0")
                self.draw_board()

    def solve(self):
        if not self.start_pos or not self.end_pos:
            return

        moves = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
        
        queue = deque([(self.start_pos[0], self.start_pos[1], [self.start_pos])])
        visited = set([self.start_pos])
        self.path = []

        while queue:
            r, c, current_path = queue.popleft()

            if (r, c) == self.end_pos:
                self.path = current_path
                break

            for dr, dc in moves:
                nr, nc = r + dr, c + dc
                if 0 <= nr < self.N and 0 <= nc < self.N and (nr, nc) not in visited:
                    visited.add((nr, nc))
                    queue.append((nr, nc, current_path + [(nr, nc)]))

        self.draw_board()
        if self.path:
            steps = len(self.path) - 1
            self.info_label.config(text=f"Мінімальна кількість кроків: {steps}")
        else:
            self.info_label.config(text="Шлях не знайдено!")

    def process_files(self):
        if not os.path.exists("input.txt"):
            messagebox.showwarning("Файл не знайдено", "Створіть файл 'input.txt' у папці з програмою!")
            return

        try:
            with open("input.txt", "r", encoding="utf-8") as f:
                lines = f.readlines()
                
                self.N = int(lines[0].split('#')[0].strip())
                
                start_str = lines[1].split('#')[0].strip().split(',')
                self.start_pos = (int(start_str[0].strip()), int(start_str[1].strip()))
                
                end_str = lines[2].split('#')[0].strip().split(',')
                self.end_pos = (int(end_str[0].strip()), int(end_str[1].strip()))

            self.solve()

            with open("output.txt", "w", encoding="utf-8") as f:
                if self.path:
                    steps = len(self.path) - 1
                    f.write(f"{steps}\n")
                else:
                    f.write("-1\n") 

            messagebox.showinfo("Успіх", f"Дані завантажено з input.txt.\nРозмір дошки: {self.N}x{self.N}\nРезультат записано у output.txt")
            
        except Exception as e:
            messagebox.showerror("Помилка читання", f"Перевірте формат файлу input.txt.\nДеталі: {e}")

    def reset_board(self):
        self.start_pos = None
        self.end_pos = None
        self.path = []
        self.info_label.config(text="Кроків: 0")
        self.draw_board()


if __name__ == "__main__":
    root = tk.Tk()
    root.resizable(False, False)
    app = KnightPathGUI(root)
    root.mainloop()