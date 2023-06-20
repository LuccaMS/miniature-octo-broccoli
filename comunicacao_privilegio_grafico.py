import tkinter as tk
import math

class TokenRingApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Mutual Exclusion - Token Ring Algorithm")
        self.window.bind('<space>', self.change_token_position)
        self.window.bind('a', self.send_messages)

        self.canvas = tk.Canvas(self.window, width=1100, height=500, bg='white')
        self.canvas.pack()

        # Main circles
        main_circle1_x = 300
        main_circle2_x = 800
        main_circle_y = 250
        main_circle_radius = 200
        self.canvas.create_oval(main_circle1_x - main_circle_radius, main_circle_y - main_circle_radius,
                                main_circle1_x + main_circle_radius, main_circle_y + main_circle_radius,
                                outline='black')

        self.canvas.create_oval(main_circle2_x - main_circle_radius, main_circle_y - main_circle_radius,
                                main_circle2_x + main_circle_radius, main_circle_y + main_circle_radius,
                                outline='black')

        # Inner circles representing senders
        num_senders = 5
        sender_radius = 30
        sender_positions = self.calculate_circle_positions(main_circle1_x, main_circle_y,
                                                           main_circle_radius - sender_radius,
                                                           num_senders)
        self.senders = []
        for pos in sender_positions:
            sender = self.canvas.create_oval(pos[0] - sender_radius, pos[1] - sender_radius,
                                             pos[0] + sender_radius, pos[1] + sender_radius, fill='blue')
            self.senders.append(sender)

        # Inner circles representing receivers
        num_receivers = 8
        receiver_positions = self.calculate_circle_positions(main_circle2_x, main_circle_y,
                                                             main_circle_radius - sender_radius,
                                                             num_receivers)
        self.receivers = []
        for pos in receiver_positions:
            receiver = self.canvas.create_oval(pos[0] - sender_radius, pos[1] - sender_radius,
                                               pos[0] + sender_radius, pos[1] + sender_radius, fill='red')
            self.receivers.append(receiver)

        self.token = self.senders[0]
        self.current_sender_index = 0
        self.current_receiver_index = 0
        self.token_label = self.canvas.create_text(450, 460, text="Token: None", font=("Arial", 14))

        self.arrow_ids = []  # To keep track of arrow IDs

        self.update_token_label()

    def change_token_position(self, event):
        if self.current_sender_index < len(self.senders) - 1:
            self.canvas.itemconfig(self.token, fill='blue')
            self.current_sender_index += 1
        else:
            self.canvas.itemconfig(self.token, fill='blue')
            self.current_sender_index = 0

        self.remove_arrows()  # Remove arrows when token changes
        self.token = self.senders[self.current_sender_index]
        self.canvas.itemconfig(self.token, fill='green')
        self.update_token_label()

    def send_messages(self, event):
        start_x, start_y = self.canvas.coords(self.token)[0] + 30, self.canvas.coords(self.token)[1] + 30
        receiver_radius = 30

        for receiver in self.receivers:
            receiver_x, receiver_y = self.canvas.coords(receiver)[0] + receiver_radius, self.canvas.coords(receiver)[1] + receiver_radius

            # Draw arrow from token to receiver
            arrow = self.canvas.create_line(start_x, start_y, receiver_x, receiver_y, arrow=tk.LAST, width=1)
            self.arrow_ids.append(arrow)  # Store arrow IDs

            # Draw arrow from receiver back to token
            return_arrow = self.canvas.create_line(receiver_x, receiver_y, start_x, start_y, arrow=tk.LAST, width=1)
            self.arrow_ids.append(return_arrow)  # Store arrow IDs

    def remove_arrows(self):
        for arrow_id in self.arrow_ids:
            self.canvas.delete(arrow_id)  # Delete arrows from canvas
        self.arrow_ids = []  # Reset arrow IDs

    def update_token_label(self):
        token_text = f"Token: {self.current_sender_index + 1}"
        self.canvas.itemconfig(self.token_label, text=token_text)

    def calculate_circle_positions(self, center_x, center_y, radius, num_positions):
        positions = []
        angle_increment = 360 / num_positions
        current_angle = 90

        for _ in range(num_positions):
            x = center_x + radius * math.cos(math.radians(current_angle))
            y = center_y - radius * math.sin(math.radians(current_angle))
            positions.append((x, y))
            current_angle += angle_increment

        return positions


if __name__ == "__main__":
    window = tk.Tk()
    app = TokenRingApp(window)
    window.geometry("1100x500")
    window.mainloop()
