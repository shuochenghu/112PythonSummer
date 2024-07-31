import tkinter as tk
from tkinter import filedialog, simpledialog
import requests

def send_line_notify(token, message, sticker_package_id=None, sticker_id=None, image_path=None, image_url=None):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    payload = {'message': message}
    files = {}

    if sticker_package_id and sticker_id:
        payload['stickerPackageId'] = sticker_package_id
        payload['stickerId'] = sticker_id

    if image_path:
        files = {'imageFile': open(image_path, 'rb')}

    if image_url:
        files = {'imageFile': ('image.jpg', requests.get(image_url).content)}

    response = requests.post(url, headers=headers, params=payload, files=files)
    return response

def on_submit():
    token = 'BLJxO0Y8dDcWMukYMFBD36b54wNB4GR2bEPCCSLPiKc'  # Replace with your LINE Notify Token
    choice = menu_var.get()

    if choice == 'Line Sticker':
        send_line_notify(token, "Sending LINE Sticker", sticker_package_id=sticker_package_id_var.get(), sticker_id=sticker_id_var.get())
    elif choice == 'Local Image File':
        send_line_notify(token, "Sending Local Image File", image_path=image_path_var.get())
    elif choice == 'Web Image File':
        send_line_notify(token, "Sending Web Image File", image_url=image_url_var.get())

def update_input_fields(*args):
    for widget in frame.winfo_children():
        widget.destroy()

    choice = menu_var.get()
    if choice == 'Line Sticker':
        tk.Label(frame, text="Sticker Package ID:").pack()
        tk.Entry(frame, textvariable=sticker_package_id_var).pack()
        tk.Label(frame, text="Sticker ID:").pack()
        tk.Entry(frame, textvariable=sticker_id_var).pack()
    elif choice == 'Local Image File':
        tk.Label(frame, text="Image File Path:").pack()
        tk.Entry(frame, textvariable=image_path_var).pack()
        tk.Button(frame, text="Browse", command=lambda: image_path_var.set(filedialog.askopenfilename())).pack()
    elif choice == 'Web Image File':
        tk.Label(frame, text="Image URL:").pack()
        tk.Entry(frame, textvariable=image_url_var).pack()

# GUI Setup
root = tk.Tk()
root.title("LINE Notify Sender")

menu_var = tk.StringVar(root)
sticker_package_id_var = tk.StringVar(root)
sticker_id_var = tk.StringVar(root)
image_path_var = tk.StringVar(root)
image_url_var = tk.StringVar(root)

choices = ['Line Sticker', 'Local Image File', 'Web Image File']
menu_var.set(choices[0])  # set the default option
menu_var.trace('w', update_input_fields)

popup_menu = tk.OptionMenu(root, menu_var, *choices)
popup_menu.pack()

frame = tk.Frame(root)
frame.pack()

submit_button = tk.Button(root, text="Submit", command=on_submit)
submit_button.pack()

root.mainloop()
