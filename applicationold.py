import sys
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
from analysis import analyze_data_structures
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)

        # Set up the layout
        widget = QWidget(self)
        self.setCentralWidget(widget)
        layout = QVBoxLayout()
        widget.setLayout(layout)

        # Create the seaborn plot
        data = analyze_data_structures(1000)
        df = pd.DataFrame(data)
        plot_data = df.melt(var_name='Operation', value_name='Time (s)')

        fig, ax = plt.subplots()
        sns.barplot(x='Dataset', y='Time (s)', hue='Data Structure', data=plot_data, ax=ax)

        # Add the plot to the layout
        canvas = FigureCanvas(fig)
        layout.addWidget(canvas)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWin = MainWindow()
    mainWin.show()
    sys.exit(app.exec_())
