# =======================================================
# Analyze Merge Sort and Quick Sort on Different Datasets 
# Author: Unique Karanjit
# Date: Jan 17, 2025
# =======================================================

# Importing necessary dependencies
import sys # to set up recursion limit
from merge_sort import merge_sort
from quick_sort import quick_sort
from performance_metrics import measure_performance
from generate_data import generate_data
from plot_graph import plot_performance

# Main Driver Code
def main():
    sys.setrecursionlimit(100000)  # Setting up high recursion limit exclusively.
    size = 50000  # Define the size of the dataset
    print(f"\n\nSorting array with {size} records.")
    
    # Generate different types of datasets
    sorted_data = generate_data('sorted', size)
    reverse_sorted_data = generate_data('reverse_sorted', size)
    random_data = generate_data('random', size)


    
    # List of datasets to test
    datasets = {
        'Sorted': sorted_data,
        'Reverse Sorted': reverse_sorted_data,
        'Random': random_data
    }
    
    # Dictionary to store performance metrics
    data_metrics = {dataset: {} for dataset in datasets}

    # Run and measure performance for each dataset and sorting algorithm
    for data_type, data in datasets.items():
        print(f"\n***Performance Metrics for {data_type} Data ***")
        
        # Measure performance for Merge Sort
        merge_sort_time, merge_sort_memory = measure_performance(merge_sort, data.copy())
        data_metrics[data_type]['Merge Sort'] = {'time': merge_sort_time, 'memory': merge_sort_memory}
        print(f"Merge Sort - Time: {merge_sort_time:.2f}s, Memory: {merge_sort_memory:.2f} MB")

        
        # Measure performance for Quick Sort
        quick_sort_time, quick_sort_memory = measure_performance(quick_sort, data.copy())
        data_metrics[data_type]['Quick Sort'] = {'time': quick_sort_time, 'memory': quick_sort_memory}
        print(f"Quick Sort - Time: {quick_sort_time:.2f}s, Memory: {quick_sort_memory:.2f} MB")
    
    plot_performance(data_metrics)

if __name__ == "__main__":
    main()
