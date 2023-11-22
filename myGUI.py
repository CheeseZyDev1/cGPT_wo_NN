import tkinter as tk
from tkinter import ttk
import numpy as np 
import matplotlib.pyplot as plt 
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Graph_Learner import doc_graph

mynums = [x for x in range(50)]

g = doc_graph(5)
g.add_doc(mynums)

def get_numbers():
    # Get the input values from the entry widgets
    input_values = entry.get()

    # Convert the input string to a list of numbers
    numbers = [int(num) for num in input_values.split()]
    output = g.gen_next(numbers, 5)
    result_label.config(text=f"Result: {output}")
    create_line_graph(numbers)

def create_line_graph(numbers):
    # Clear the previous graph (if any)
    if hasattr(create_line_graph, 'ax'):
        create_line_graph.ax.clear()
        
    else:
        # Create a line chart using Matplotlib for the first time
        fig, ax = plt.subplots()
        ax.set_xlabel('Index')
        ax.set_ylabel('Values')
        ax.set_title('Input Numbers')
        create_line_graph.ax = ax

    # Draw the new graph
    create_line_graph.ax.plot(range(len(numbers)), numbers, marker='o')

    # Embed the Matplotlib graph in the Tkinter window
    if hasattr(create_line_graph, 'canvas'):
        create_line_graph.canvas.get_tk_widget().destroy()

    create_line_graph.canvas = FigureCanvasTkAgg(create_line_graph.ax.figure, master=graph_page)
    canvas_widget = create_line_graph.canvas.get_tk_widget()
    canvas_widget.pack()

# Main program part
window = tk.Tk()
window.geometry('800x600')
window.title("Graph Creation Phase")

# Create a notebook for navigation
notebook = ttk.Notebook(window)

# Create a page for graph
graph_page = tk.Frame(notebook)
notebook.add(graph_page, text="Input Phase")

# Create a label and entry widget for input on the graph page
input_label = tk.Label(graph_page, text="Enter numbers (separated by space):")
input_label.pack()

entry = tk.Entry(graph_page)
entry.pack()

# Create a button to trigger the calculation on the graph page
calculate_button = tk.Button(graph_page, text="Show", command=get_numbers)
calculate_button.pack()

# Create a label to display the result on the graph page
result_label = tk.Label(graph_page, text="Result: ")
result_label.pack()

# Create a page for settings
Learning_page = tk.Frame(notebook)
notebook.add(Learning_page, text="Learning Phase")

# Add content to the settings page
settings_label = tk.Label(Learning_page, text="This is the Learning Page.")
settings_label.pack()


# Pack the notebook
notebook.pack(fill=tk.BOTH, expand=True)

# Start the tkinter event loop
window.mainloop()