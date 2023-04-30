from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QLineEdit, QCheckBox, QPushButton, QGroupBox, QGridLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(800, 600)

        # Create main layout
        main_layout = QVBoxLayout()

        self.setStyleSheet("""
            QWidget {
                background-color: #f0f0f0;
                font-size: 14px;
                color: #333333;
            }

            QLabel {
                color: #666666;
            }

            QPushButton {
                background-color: #0072c6;
                color: #ffffff;
                border: none;
                border-radius: 3px;
                padding: 6px 12px;
            }

            QPushButton:hover {
                background-color: #005bac;
                cursor: pointer;
            }
            
            QGroupBox {
                font-weight: bold;
            }
        """)

        # Move "select dataset size" and "input data type" side by side
        top_layout = QHBoxLayout()

        data_structure_layout = QVBoxLayout()
        data_structure_label = QLabel("Select Dataset Size:")
        data_structure_layout.addWidget(data_structure_label)
        self.data_structure_dropdown = QComboBox()
        self.data_structure_dropdown.addItems(["100", "1000", "10000"])
        data_structure_layout.addWidget(self.data_structure_dropdown)
        top_layout.addLayout(data_structure_layout)

        input_data_layout = QVBoxLayout()
        input_data_label = QLabel("Input Dataset Type:")
        input_data_layout.addWidget(input_data_label)
        self.input_data_dropdown = QComboBox()
        self.input_data_dropdown.addItems(["Random Integers", "Increasing Integers", "Decreasing Integers"])
        input_data_layout.addWidget(self.input_data_dropdown)
        top_layout.addLayout(input_data_layout)
        
        main_layout.addLayout(top_layout)

        run_button = QPushButton("Run Operation")
        run_button.clicked.connect(self.run_comparison)
        main_layout.addWidget(run_button)

        # Add 3 plot windows below for "Insert operation", "Search operation", and "Delete operation"
        plots_layout = QGridLayout()

        self.insert_plot = FigureCanvas(Figure(figsize=(5, 3)))
        self.search_plot = FigureCanvas(Figure(figsize=(5, 3)))
        self.delete_plot = FigureCanvas(Figure(figsize=(5, 3)))

        insert_group = QGroupBox("Insert Operation")
        search_group = QGroupBox("Search Operation")
        delete_group = QGroupBox("Delete Operation")

        insert_group_layout = QVBoxLayout()
        search_group_layout = QVBoxLayout()
        delete_group_layout = QVBoxLayout()

        insert_group_layout.addWidget(self.insert_plot)
        search_group_layout.addWidget(self.search_plot)
        delete_group_layout.addWidget(self.delete_plot)

        insert_group.setLayout(insert_group_layout)
        search_group.setLayout(search_group_layout)
        delete_group.setLayout(delete_group_layout)

        plots_layout.addWidget(insert_group, 0, 0)
        plots_layout.addWidget(search_group, 0, 1)
        plots_layout.addWidget(delete_group, 1, 0)

        main_layout.addLayout(plots_layout)

        self.setLayout(main_layout)

    def run_comparison(self):
        # You'll need to implement this method to generate plots based on your specific data structures and benchmarks
        pass


if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
