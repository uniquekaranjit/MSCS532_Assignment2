# ----------------------------------------------------------------------------------------------------------------------
# Generate Data
# Description: This Python code to generate sorted, reverse sorted or random data based on user provided size. 
# Author: Unique Karanjit
# Date: 2025-01-17
# ----------------------------------------------------------------------------------------------------------------------

# import necessary dependencies
import random

# function declarations
def generate_data(data_type, size):
    """
    Generate different types of data for sorting: sorted, reverse sorted, and random.
    
    Parameters:
    data_type (str): Type of data to generate ('sorted', 'reverse_sorted', 'random')
    size (int): The size of the dataset to generate
    
    Returns:
    list: A list of integers representing the dataset
    """
    if data_type == 'sorted':
        return list(range(size))  # Sorted list from 0 to size-1
    elif data_type == 'reverse_sorted':
        return list(range(size, 0, -1))  # Reverse sorted list from size-1 to 0
    elif data_type == 'random':
        return [random.randint(0, size) for _ in range(size)]  # Random list of integers between 0 and size
    else:
        raise ValueError("Unknown data type. Use 'sorted', 'reverse_sorted', or 'random'.")