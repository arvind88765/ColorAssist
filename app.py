import tkinter as tk
import numpy as np
import pandas as pd
import cv2
import pyautogui

# Load color data
colors_csv_path = r'C:\Users\mrpc\my_extension_backend\colors.csv'
index = ['color', 'color_name', 'hex', 'R', 'G', 'B']
df = pd.read_csv(colors_csv_path, names=index, header=None)

# Initialize global variables
r = g = b = xpos = ypos = 0

# Function to get color name from RGB values
def getColorName(R, G, B):
    minimum = 10000
    for i in range(len(df)):
        d = abs(R - int(df.loc[i, "R"])) + abs(G - int(df.loc[i, "G"])) + abs(B - int(df.loc[i, "B"]))
        if d <= minimum:
            minimum = d
            cname = df.loc[i, 'color_name'] + '   Hex=' + df.loc[i, 'hex']
    return cname

# Function to update color information based on cursor position
def update_color_info():
    global r, g, b
    
    # Get cursor position
    x, y = pyautogui.position()

    # Capture screen
    screen_capture = pyautogui.screenshot()
    screen_capture = cv2.cvtColor(np.array(screen_capture), cv2.COLOR_RGB2BGR)

    # Get color information at cursor position
    b, g, r = screen_capture[y, x]
    b = int(b)
    g = int(g)
    r = int(r)
    color_text = getColorName(r, g, b)

    # Update label text with color information
    color_label.config(text=f"Detected Color: {color_text}")

# Create Tkinter window
root = tk.Tk()
root.title("Real-Time Color Detector")
root.geometry("400x100")

# Create label for color information
color_label = tk.Label(root, text="Detected Color:", font=("Arial", 16))
color_label.pack(pady=20)

# Update color information continuously
def update_color_info_continuous():
    update_color_info()
    root.after(100, update_color_info_continuous)  # Update every 100 milliseconds

update_color_info_continuous()  # Start updating color info

# Function to keep the window on top
def keep_on_top():
    root.attributes("-topmost", True)
    root.after(100, keep_on_top)

keep_on_top()  # Start keeping window on top

root.mainloop()
