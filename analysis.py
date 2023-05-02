import random
import time
from avltree import AVLTree
from redblacktree import RedBlackTree

# Create dataset


def create_datasets(size):
    random_integer_dataset = random.sample(range(1, size * 2), size)
    increasing_integer_dataset = list(range(1, size+1))
    decreasing_integer_dataset = list(range(size, 0, -1))
    return random_integer_dataset, increasing_integer_dataset, decreasing_integer_dataset

# Measure time and space complexities


def measure_avl_complexities(data_structure, dataset):
        root = None
        # Measure insertion performance
        start_time = time.time()
        for element in dataset:
            root = data_structure.insert(element, root)
        insertion_time = time.time() - start_time

        # Measure search performance
        start_time = time.time()
        for element in dataset:
            data_structure.search(element)
        search_time = time.time() - start_time

        # Measure deletion performance
        start_time = time.time()
        for element in dataset:
            root = data_structure.delete(element, root)
        deletion_time = time.time() - start_time

        return insertion_time, search_time, deletion_time

def measure_rb_complexities(data_structure, dataset):
        # Measure insertion performance
        start_time = time.time()
        for element in dataset:
            data_structure.insert(element)
        insertion_time = time.time() - start_time

        # Measure search performance
        start_time = time.time()
        for element in dataset:
            data_structure.search(element)
        search_time = time.time() - start_time

        # Measure deletion performance
        # start_time = time.time()
        # for element in dataset:
        #     if data_structure.search(element) is not None:
        #         data_structure.delete(element)
        # deletion_time = time.time() - start_time

        return insertion_time, search_time, 0 #, deletion_time

# Analyze data structures and generate results for plotting

def save_datasets_to_file(dataset_dict, filename='datasets.txt'):
    with open(filename, 'w') as f:
        for key, dataset in dataset_dict.items():
            f.write(f"{key}\n")
            f.write(" ".join(str(num) for num in dataset))
            f.write("\n\n")


def load_datasets_from_file(filename='datasets.txt'):
    datasets = {}
    with open(filename, 'r') as f:
        while True:
            name = f.readline().strip()
            if not name:
                break
            dataset_str = f.readline().strip()
            dataset = list(map(int, dataset_str.split()))
            datasets[name] = dataset
            f.readline()
    return datasets


def analyze_data_structures(dataset_size=1000):
    random_dataset, increasing_dataset, decreasing_dataset = create_datasets(dataset_size)
    datasets = {'Random': random_dataset, 'Increasing': increasing_dataset, 'Decreasing': decreasing_dataset}

    save_datasets_to_file(datasets)
    loaded_datasets = load_datasets_from_file()

    results = {}
    for name, dataset in loaded_datasets.items():
        avl_tree = AVLTree()
        rb_tree = RedBlackTree()
        avl_tree_results = measure_avl_complexities(avl_tree, dataset)
        rb_tree_results = measure_rb_complexities(rb_tree, dataset)

        results[name] = {
            'AVL Tree': avl_tree_results,
            'Red-Black Tree': rb_tree_results
        }

    return results

print(analyze_data_structures(10000))
