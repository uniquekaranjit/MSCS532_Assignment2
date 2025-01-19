# ----------------------------------------------------------------------------------------------------------------------
# Quick Sort Algorithm
# Description: This Python code implements the quick sort algorithm
# The function sorts an array in ascending order by choosing a pivot element and partitioning the array around it.
# Author: Unique Karanjit
# Date: 2025-01-17
# ----------------------------------------------------------------------------------------------------------------------

def quick_sort(arr):
    """
    Sorts an array using the quick sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        # Base case: A list of one element is already sorted.
        return arr

    # Step 1: Choose the pivot element (for simplicity, choosing the last element)
    pivot = arr[-1]

    # Step 2: Partition the array into two sublists (elements less than pivot and elements greater than pivot)
    left = [x for x in arr[:-1] if x <= pivot]  # Elements less than or equal to pivot
    right = [x for x in arr[:-1] if x > pivot]  # Elements greater than pivot

    # Step 3: Recursively sort the left and right sublists, then combine them with the pivot
    return quick_sort(left) + [pivot] + quick_sort(right)