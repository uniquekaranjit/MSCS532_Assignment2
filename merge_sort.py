# ----------------------------------------------------------------------------------------------------------------------
# Merge Sort Algorithm
# Description: This Python code implements the merge sort algorithm. 
# The function sorts an array in ascending order by recursively splitting it into halves and merging the sorted halves.
# Author: Unique Karanjit
# Date: 2025-01-17
# ----------------------------------------------------------------------------------------------------------------------

def merge_sort(arr):
    """
    Sorts an array using the merge sort algorithm.
    
    Parameters:
    arr (list): The list of elements to be sorted.

    Returns:
    list: The sorted list.
    """
    if len(arr) <= 1:
        return arr    # Base case: A list of one element is already sorted.
    # Step 1: Divide the list into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]  # Elements from the start to mid
    right_half = arr[mid:]  # Elements from mid to the end

    # Step 2: Recursively sort both halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Step 3: Merge the sorted halves and return the merged list
    return merge(left_half, right_half)


def merge(left, right):
    """
    Merges two sorted lists into one sorted list.

    Parameters:
    left (list): A sorted list.
    right (list): Another sorted list.

    Returns:
    list: A merged and sorted list.
    """
    merged = []  # Resultant list to store the merged values
    i = 0  # Pointer for the left list
    j = 0  # Pointer for the right list
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])  # Add smaller element from the left list
            i += 1
        else:
            merged.append(right[j])  # Add smaller element from the right list
            j += 1

    # Step 2: If any elements remain in the left list, add them to the merged list
    while i < len(left):
        merged.append(left[i])
        i += 1

    # Step 3: If any elements remain in the right list, add them to the merged list
    while j < len(right):
        merged.append(right[j])
        j += 1
    return merged
