import time
import resource
import tracemalloc  # For memory measurement


# ----------------------------------------------------------------------------------------------------------------------
# Performance Metrics 
# Author: Unique Karanjit
# Jan 17, 2025
# ----------------------------------------------------------------------------------------------------------------------

def measure_performance(sort_function, data):
    """
    Measure the execution time and memory usage of a sorting function.
    
    Parameters:
    sort_function (function): The sorting function (merge_sort or quick_sort)
    data (list): The data to be sorted
    
    Returns:
    tuple: (execution time in seconds, memory usage in MB)
    """
    # Memory before in bytes and start time. 
    memory_before = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss # in bytes
    start_time = time.time() # in seconds. 
    tracemalloc.start()

    
    # Call the sorting method
    sort_function(data)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    
    return time.time() - start_time, peak/ 10**6  # Convert from bytes to megabytes
