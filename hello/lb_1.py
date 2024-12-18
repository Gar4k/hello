import tkinter as tk
from tkinter import colorchooser, messagebox

class SimpleGraphicEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Графічний редактор")

        # Змінні
        self.current_color = "black"
        self.brush_size = 5
        self.tool = "pen"  # pen, eraser, rectangle, oval
        self.start_x = None
        self.start_y = None
        self.history = []
        self.redo_stack = []

        # Полотно для малювання
        self.canvas = tk.Canvas(root, bg="white", width=800, height=600)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        self.canvas.bind("<B1-Motion>", self.paint)
        self.canvas.bind("<Button-1>", self.set_start_point)
        self.canvas.bind("<ButtonRelease-1>", self.draw_shape)

        # Панель інструментів
        self.tools_frame = tk.Frame(root)
        self.tools_frame.pack(side=tk.RIGHT, fill=tk.Y)

        # Палітра кольорів
        colors = ["black", "red", "green", "blue", "yellow", "purple", "orange", "gray"]
        for color in colors:
            btn = tk.Button(self.tools_frame, bg=color, width=3, height=1, command=lambda c=color: self.set_color(c))
            btn.pack(pady=2)

        color_picker_btn = tk.Button(self.tools_frame, text="Обрати колір", command=self.choose_color)
        color_picker_btn.pack(pady=5)

        # Регулятор ширини пензля
        tk.Label(self.tools_frame, text="Товщина пензля:").pack(pady=5)
        self.brush_size_slider = tk.Scale(self.tools_frame, from_=1, to=20, orient=tk.HORIZONTAL)
        self.brush_size_slider.set(self.brush_size)
        self.brush_size_slider.pack(pady=5)

        # Кнопки інструментів
        tk.Button(self.tools_frame, text="Ластик", command=lambda: self.set_tool("eraser")).pack(pady=5)
        tk.Button(self.tools_frame, text="Прямокутник", command=lambda: self.set_tool("rectangle")).pack(pady=5)
        tk.Button(self.tools_frame, text="Овал", command=lambda: self.set_tool("oval")).pack(pady=5)
        tk.Button(self.tools_frame, text="Очистити", command=self.clear_canvas).pack(pady=5)
        tk.Button(self.tools_frame, text="Відміна", command=self.undo).pack(pady=5)
        tk.Button(self.tools_frame, text="Повернути", command=self.redo).pack(pady=5)
        tk.Button(self.tools_frame, text="Про програму", command=self.show_about).pack(pady=5)

    def set_color(self, color):
        self.current_color = color
        self.tool = "pen"

    def choose_color(self):
        color_code = colorchooser.askcolor(title="Обрати колір")[1]
        if color_code:
            self.set_color(color_code)

    def set_tool(self, tool):
        self.tool = tool

    def set_start_point(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def paint(self, event):
        if self.tool == "pen":
            line = self.canvas.create_line(event.x, event.y, event.x + 1, event.y + 1,
                                           fill=self.current_color, width=self.brush_size_slider.get(),
                                           capstyle=tk.ROUND, smooth=tk.TRUE)
            self.history.append(line)
        elif self.tool == "eraser":
            line = self.canvas.create_line(event.x, event.y, event.x + 1, event.y + 1,
                                           fill="white", width=self.brush_size_slider.get(),
                                           capstyle=tk.ROUND, smooth=tk.TRUE)
            self.history.append(line)

    def draw_shape(self, event):
        if self.start_x and self.start_y:
            shape = None
            if self.tool == "rectangle":
                shape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y,
                                                     outline=self.current_color, width=self.brush_size_slider.get())
            elif self.tool == "oval":
                shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y,
                                                 outline=self.current_color, width=self.brush_size_slider.get())
            if shape:
                self.history.append(shape)
        self.start_x = None
        self.start_y = None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.history.clear()
        self.redo_stack.clear()

   print("----------------------------------------")
    
    def undo(self):
        if self.history:
            last_action = self.history.pop()
            self.redo_stack.append(last_action)
            self.canvas.delete(last_action)

    def redo(self):
        if self.redo_stack:
            action = self.redo_stack.pop()
            self.history.append(action)
            # Redraw action (requires more complex tracking in full implementation)

    def show_about(self):
        messagebox.showinfo("Про програму", "Графічний редактор\nСтудент: Гармідер Богдан\nГрупа: ІПЗ-21")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimpleGraphicEditor(root)
    root.mainloop()

    print("----------------------------------------")
