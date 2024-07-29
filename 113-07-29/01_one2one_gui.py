import tkinter as tk
from tkinter import simpledialog, messagebox
import requests

# Function to send the message using LINE Notify API
def send_message():
    global token
    URL = 'https://notify-api.line.me/api/notify'
    headers = {
        'Authorization': f'Bearer {token}'
    }
    message = message_entry.get()
    data = {
        'message': message
    }

    response = requests.post(URL, headers=headers, data=data)
    if response.status_code == 200:
        messagebox.showinfo("Success", "Message sent successfully!")
    else:
        messagebox.showerror("Error", f"Failed to send message. Status code: {response.status_code}")

# Create the main window
root = tk.Tk()
root.title("LINE Notify Messenger")

# Prompt user for the LINE Notify token
token = simpledialog.askstring("Input", "Please enter your LINE Notify token:", parent=root)

if token:
    # Create and place the label
    label = tk.Label(root, text="Enter your message:")
    label.pack(pady=10)

    # Create and place the entry field
    message_entry = tk.Entry(root, width=50)
    message_entry.pack(pady=10)

    # Create and place the send button
    send_button = tk.Button(root, text="Send", command=send_message)
    send_button.pack(pady=10)

    # Run the application
    root.mainloop()
else:
    messagebox.showerror("Error", "You must enter a token to use this application.")
    root.destroy()
