import random
import time
from avltree import AVLTree
from redblacktree import RedBlackTree

# Create dataset


def create_datasets(size):
    random_integer_dataset = [random.randint(1, size) for _ in range(size)]
    increasing_integer_dataset = list(range(1, size+1))
    decreasing_integer_dataset = list(range(size, 0, -1))
    return random_integer_dataset, increasing_integer_dataset, decreasing_integer_dataset

# Measure time and space complexities


def measure_complexities(data_structure, dataset):

    if type(data_structure) == AVLTree:
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
    start_time = time.time()
    for element in dataset:
        data_structure.delete(element)
    deletion_time = time.time() - start_time

    return insertion_time, search_time, deletion_time

# Analyze data structures and generate results for plotting


def analyze_data_structures(dataset_size=1000):
    random_dataset, increasing_dataset, decreasing_dataset = create_datasets(
        dataset_size)
    datasets = {'Random': random_dataset,
                'Increasing': increasing_dataset, 'Decreasing': decreasing_dataset}

    results = {}
    for name, dataset in datasets.items():
        avl_tree = AVLTree()
        rb_tree = RedBlackTree()
        avl_tree_results = measure_complexities(avl_tree, dataset)
        rb_tree_results = measure_complexities(rb_tree, dataset)

        results[name] = {
            'AVL Tree': avl_tree_results,
            'Red-Black Tree': rb_tree_results
        }

    return results
