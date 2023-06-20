import tkinter as tk
import time
import math

class TokenRingApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Mutual Exclusion - Token Ring Algorithm")
        self.window.bind('<space>', self.change_token_position)
        self.window.bind('a', self.toggle_critical_region)
        
        self.canvas = tk.Canvas(self.window, width=900, height=500, bg='white')
        self.canvas.pack()
        
        # Main circle
        main_circle_x = 450
        main_circle_y = 250
        main_circle_radius = 200
        self.canvas.create_oval(main_circle_x - main_circle_radius, main_circle_y - main_circle_radius,
                                main_circle_x + main_circle_radius, main_circle_y + main_circle_radius,
                                outline='black')
        
        # Inner circles representing members
        num_nodes = 5
        node_radius = 30
        node_positions = self.calculate_circle_positions(main_circle_x, main_circle_y,
                                                         main_circle_radius - node_radius,
                                                         num_nodes)
        self.nodes = []
        for pos in node_positions:
            node = self.canvas.create_oval(pos[0]-node_radius, pos[1]-node_radius,
                                           pos[0]+node_radius, pos[1]+node_radius, fill='blue')
            self.nodes.append(node)
        
        # Critical region
        crit_region_x1 = main_circle_x + main_circle_radius + 50
        crit_region_y1 = main_circle_y - 100
        crit_region_x2 = crit_region_x1 + 200
        crit_region_y2 = crit_region_y1 + 200
        self.critical_region = self.canvas.create_rectangle(crit_region_x1, crit_region_y1, crit_region_x2, crit_region_y2,
                                     fill='white', outline='black')
        
        self.token = self.nodes[0]
        self.current_node_index = 0
        self.in_critical_region = False
        self.token_label = self.canvas.create_text(450, 460, text="Token: None", font=("Arial", 14))
        
        self.update_token_label()
        
    def change_token_position(self, event):
        if not self.in_critical_region:
            self.canvas.itemconfig(self.token, fill='blue')
            self.current_node_index = (self.current_node_index + 1) % len(self.nodes)
            self.token = self.nodes[self.current_node_index]
            self.canvas.itemconfig(self.token, fill='green')
            self.update_token_label()
        
    def toggle_critical_region(self, event):
        self.in_critical_region = not self.in_critical_region
        if self.in_critical_region:
            self.canvas.itemconfig(self.critical_region, fill='lightgreen')
        else:
            self.canvas.itemconfig(self.critical_region, fill='white')
        
    def update_token_label(self):
        token_text = f"Token: {self.current_node_index + 1}"
        self.canvas.itemconfig(self.token_label, text=token_text)
        
    def calculate_circle_positions(self, center_x, center_y, radius, num_positions):
        positions = []
        angle_increment = 360 / num_positions
        current_angle = 90  # Start at 90 degrees to place the first position at the top
        
        for _ in range(num_positions):
            x = center_x + radius * math.cos(math.radians(current_angle))
            y = center_y - radius * math.sin(math.radians(current_angle))
            positions.append((x, y))
            current_angle += angle_increment
        
        return positions

if __name__ == "__main__":
    window = tk.Tk()
    app = TokenRingApp(window)
    window.geometry("1100x500")  # Adjust the window size as needed
    window.mainloop()
