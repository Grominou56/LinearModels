import tkinter as tk
from tkinter import filedialog
import pandas as pd
import matplotlib.pyplot as plt

# Fuction to load a excel file

def load_excel_file():
    # Create a Tkinter root window (it won't be shown)
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    root.call('wm', 'attributes', '.', '-topmost', True)  # Bring the file dialog to the front
    
    # Open the file dialog to select an Excel file
    file_path = filedialog.askopenfilename(
        title="Select an Excel file",
        filetypes=[
            ("Excel files", "*.xlsx *.xls"),
            ("All files", "*.*")
        ]
    )
    
    if file_path:
        # Load the selected Excel file into a pandas DataFrame
        
        print(f"Selected file: {file_path}")
        try:
            data = pd.read_excel(file_path)
            print("Excel file loaded successfully.")
            return data
        except Exception as e:
            print(f"Error loading the Excel file: {e}")
            return None


# Function to save figure as SVG

def save_figure_as_svg(fig):
    
    # Hide Tkinter main window
    root = tk.Tk()
    root.withdraw()

    # Ask user where to save the file
    file_path = filedialog.asksaveasfilename(defaultextension='.svg', filetypes=[('SVG files', '*.svg')])

    if file_path:
        # Save the figure as SVG
        fig.savefig(file_path, format='svg')
        print(f"Figure saved to {file_path}")
    
    # Close the figure
    plt.close(fig)
