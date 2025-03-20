import tkinter as tk
from tkinter import ttk

class Ruler(tk.Tk):
    def __init__(self):
        super().__init__()

        # Set window icon
        try:
            self.iconbitmap('e:\\programming\\PythonApplication1\\ruler.ico')
        except:
            pass  # If icon file is not found, use default icon
            
        self.title("Desktop Ruler")
        self.attributes('-alpha', 0.5) 
        self.attributes('-topmost', True)  
        
        # Create main frame
        self.ruler_frame = ttk.Frame(self)
        self.ruler_frame.pack(fill='both', expand=True)
        
        # Create canvas for ruler
        self.canvas = tk.Canvas(self.ruler_frame, height=50, width=400, 
                              bg='white', highlightthickness=1)
        self.canvas.pack(fill='both', expand=True)
        
        # Add buttons frame
        self.buttons_frame = ttk.Frame(self.ruler_frame)
        self.buttons_frame.pack(side='bottom', pady=2)
        
        # Add orientation buttons
        self.horizontal_btn = ttk.Button(self.buttons_frame, text="Horizontal", 
                                       command=lambda: self.change_orientation('horizontal'))
        self.horizontal_btn.pack(side='left', padx=2)
        
        self.vertical_btn = ttk.Button(self.buttons_frame, text="Vertical", 
                                     command=lambda: self.change_orientation('vertical'))
        self.vertical_btn.pack(side='left', padx=2)

        self.both_btn = ttk.Button(self.buttons_frame, text="Both", 
                                 command=lambda: self.change_orientation('both'))
        self.both_btn.pack(side='left', padx=2)
        
        self.canvas.bind('<Configure>', lambda e: self.draw_ruler())
        self.bind('<Button-1>', self.start_drag)
        self.bind('<B1-Motion>', self.on_drag)
        
        # Remove the right-click menu code
        self.orientation = 'horizontal'

    def draw_ruler(self):
        self.canvas.delete('all')
        width = self.canvas.winfo_width()
        height = self.canvas.winfo_height()
        
        if self.orientation == 'both':
            # Draw both horizontal and vertical markings
            # Horizontal markings
            for i in range(0, width, 10):
                if i % 50 == 0:
                    self.canvas.create_line(i, 0, i, height, fill='gray80', dash=(1,1))
                    self.canvas.create_line(i, 0, i, 15, fill='black')
                    self.canvas.create_text(i, 25, text=str(i), anchor='center')
                else:
                    self.canvas.create_line(i, 0, i, 10, fill='black')
            
            # Vertical markings
            for i in range(0, height, 10):
                if i % 50 == 0:
                    self.canvas.create_line(0, i, width, i, fill='gray80', dash=(1,1))
                    self.canvas.create_line(0, i, 15, i, fill='black')
                    self.canvas.create_text(25, i, text=str(i), anchor='center')
                else:
                    self.canvas.create_line(0, i, 10, i, fill='black')
        
        elif self.orientation == 'horizontal':
            # Draw horizontal ruler markings
            for i in range(0, width, 10):
                # Major ticks (every 50 pixels)
                if i % 50 == 0:
                    self.canvas.create_line(i, 0, i, 15, fill='black')
                    self.canvas.create_text(i, 25, text=str(i), anchor='center')
                # Minor ticks
                else:
                    self.canvas.create_line(i, 0, i, 10, fill='black')
        else:
            # Draw vertical ruler markings
            for i in range(0, height, 10):
                if i % 50 == 0:
                    self.canvas.create_line(0, i, 15, i, fill='black')
                    self.canvas.create_text(25, i, text=str(i), anchor='center')
                else:
                    self.canvas.create_line(0, i, 10, i, fill='black')

    def start_drag(self, event):
        self.x = event.x
        self.y = event.y

    def on_drag(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.winfo_x() + deltax
        y = self.winfo_y() + deltay
        self.geometry(f"+{x}+{y}")

    def show_menu(self, event):
        self.menu.post(event.x_root, event.y_root)

    def change_orientation(self, orientation):
        self.orientation = orientation
        if orientation == 'vertical':
            self.canvas.configure(width=50, height=400)
        elif orientation == 'horizontal':
            self.canvas.configure(width=400, height=50)
        else:  # both
            self.canvas.configure(width=400, height=400)
        self.draw_ruler()

if __name__ == "__main__":
    app = Ruler()
    app.mainloop()