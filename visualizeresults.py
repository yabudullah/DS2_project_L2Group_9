import matplotlib.pyplot as plt
import numpy as np
from analysis import analyze_data_structures

def plot_data_structure_analysis(results):
    operations = ['Insertion', 'Search'] # 'Deletion' can be added if needed
    datasets = list(results.keys())
    data_structures = list(results[datasets[0]].keys())

    # Set the width of the bars
    bar_width = 0.35
    index = np.arange(len(datasets))

    # Plot the bars
    for op_idx, operation in enumerate(operations):
        fig, ax = plt.subplots()
        for ds_idx, data_structure in enumerate(data_structures):
            performance = [results[dataset][data_structure][op_idx] for dataset in datasets]
            ax.bar(index + ds_idx * bar_width, performance, bar_width, label=data_structure)

        ax.set_xlabel('Datasets')
        ax.set_ylabel('Time (s)')
        ax.set_title(f'{operation} Time Comparison')
        ax.set_xticks(index + bar_width / 2)
        ax.set_xticklabels(datasets)
        ax.legend()

    plt.show()

results = analyze_data_structures(100000)
print(results)
plot_data_structure_analysis(results)
