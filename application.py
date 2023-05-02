import tkinter as tk
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import seaborn as sns
import pandas as pd
import analysis

class Application(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Data Structure Analysis")

        # Set up the layout
        self.create_widgets()

    def create_widgets(self):
        self.dataset_length_label = tk.Label(self, text="Dataset Length:")
        self.dataset_length_label.grid(row=0, column=0)

        self.dataset_length_var = tk.IntVar()
        self.dataset_length_entry = tk.Entry(self, textvariable=self.dataset_length_var)
        self.dataset_length_entry.grid(row=0, column=1)

        self.generate_dataset_button = tk.Button(self, text="Generate Dataset", command=self.generate_dataset)
        self.generate_dataset_button.grid(row=1, column=0)

        self.choose_dataset_button = tk.Button(self, text="Choose Dataset", command=self.choose_dataset)
        self.choose_dataset_button.grid(row=1, column=1)

        self.run_analysis_button = tk.Button(self, text="Run Analysis", command=self.run_analysis)
        self.run_analysis_button.grid(row=2, column=0, columnspan=2)

    def generate_dataset(self):
        dataset_length = self.dataset_length_var.get()
        if dataset_length > 0:
            random_dataset, increasing_dataset, decreasing_dataset = analysis.create_datasets(dataset_length)
            datasets = {'Random': random_dataset, 'Increasing': increasing_dataset, 'Decreasing': decreasing_dataset}
            analysis.save_datasets_to_file(datasets)

    def choose_dataset(self):
        dataset_file = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
        if dataset_file:
            self.datasets = analysis.load_datasets_from_file(dataset_file)
    
    def run_analysis(self):
        dataset_length = self.dataset_length_var.get()
        if dataset_length > 0:
            results = analysis.analyze_data_structures(dataset_length)
            self.plot_results(results)

    def plot_results(self, results):
        data = pd.DataFrame(results)
        plot_data = data.melt(var_name='Operation', value_name='Time (s)')

        fig = Figure(figsize=(6, 4), dpi=100)
        ax = fig.add_subplot(111)
        sns.barplot(x='Dataset', y='Time (s)', hue='Data Structure', data=plot_data, ax=ax)

        if hasattr(self, 'canvas'):
            self.canvas.get_tk_widget().destroy()

        self.canvas = FigureCanvasTkAgg(fig, master=self)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=3, column=0, columnspan=2)

if __name__ == "__main__":
    app = Application()
    app.mainloop()
