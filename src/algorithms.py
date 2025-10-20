"""
Algorithm Implementations for Performance Analysis - INSTRUCTOR SOLUTION
CS101 Fall 2025 - Activity 05

This module contains complete algorithm implementations for doubling experiments.
All TODOs have been completed with working implementations.
"""

import random
import time


def linear_search(data_list, target):
    """
    Search for a target value in an unsorted list using linear search.
    
    Args:
        data_list (list): List to search through
        target: Value to search for
        
    Returns:
        int: Index of target if found, -1 if not found
        
    Time needed: Checks each element one by one in worst case
    """
    # SOLUTION: Iterate through the list and compare each element to target
    for i in range(len(data_list)):
        if data_list[i] == target:
            return i
    return -1


def binary_search(data_list, target):
    """
    Search for a target value in a SORTED list using binary search.
    
    Args:
        data_list (list): SORTED list to search through  
        target: Value to search for
        
    Returns:
        int: Index of target if found, -1 if not found
        
    Time needed: Eliminates half the search space each step (requires sorted data)
    """
    # SOLUTION: Use left and right pointers, calculate middle, compare with target
    left = 0
    right = len(data_list) - 1
    
    while left <= right:
        middle = (left + right) // 2
        
        if data_list[middle] == target:
            return middle
        elif data_list[middle] < target:
            left = middle + 1
        else:
            right = middle - 1
    
    return -1


def bubble_sort(data_list):
    """
    Sort a list using the bubble sort algorithm.
    
    Args:
        data_list (list): List to sort (will be modified in place)
        
    Returns:
        list: The sorted list (same object as input)
        
    Time needed: Uses nested loops to compare adjacent elements repeatedly
    """
    # SOLUTION: Use nested loops. Outer loop runs n times, inner loop compares
    # adjacent elements and swaps if they're in wrong order
    n = len(data_list)
    
    for i in range(n):
        # Flag to track if any swaps were made in this pass
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if data_list[j] > data_list[j + 1]:
                # Swap if they are in wrong order
                data_list[j], data_list[j + 1] = data_list[j + 1], data_list[j]
                swapped = True
        
        # If no swapping occurred, the list is sorted
        if not swapped:
            break
    
    return data_list


def selection_sort(data_list):
    """
    Sort a list using the selection sort algorithm.
    
    Args:
        data_list (list): List to sort (will be modified in place)
        
    Returns:
        list: The sorted list (same object as input)
        
    Time needed: Finds minimum element and places it in correct position repeatedly
    """
    # SOLUTION: For each position, find the minimum element in the remaining unsorted
    # portion and swap it with the element at the current position
    n = len(data_list)
    
    for i in range(n):
        # Find the minimum element in the remaining unsorted array
        min_index = i
        for j in range(i + 1, n):
            if data_list[j] < data_list[min_index]:
                min_index = j
        
        # Swap the found minimum element with the first element
        data_list[i], data_list[min_index] = data_list[min_index], data_list[i]
    
    return data_list


def calculate_sum(data_list):
    """
    Calculate the sum of all elements in a list.
    
    Args:
        data_list (list): List of numbers
        
    Returns:
        number: Sum of all elements
        
    Time needed: Must visit each element once
    """
    total = 0
    for element in data_list:
        total += element
    return total


def find_maximum(data_list):
    """
    Find the maximum element in a list.
    
    Args:
        data_list (list): List of comparable elements
        
    Returns:
        element: Maximum element in the list
        
    Time needed: Must check each element to find maximum
    """
    if not data_list:
        return None
    
    maximum = data_list[0]
    for element in data_list:
        if element > maximum:
            maximum = element
    return maximum


def find_minimum(data_list):
    """
    Find the minimum element in a list.
    
    Args:
        data_list (list): List of comparable elements
        
    Returns:
        element: Minimum element in the list
        
    Time needed: Must check each element to find minimum
    """
    if not data_list:
        return None
    
    minimum = data_list[0]
    for element in data_list:
        if element < minimum:
            minimum = element
    return minimum


# Utility functions for generating test data

def generate_random_list(size, min_val=1, max_val=1000):
    """
    Generate a list of random integers for testing.
    
    Args:
        size (int): Number of elements to generate
        min_val (int): Minimum value for random numbers
        max_val (int): Maximum value for random numbers
        
    Returns:
        list: List of random integers
    """
    return [random.randint(min_val, max_val) for _ in range(size)]


def generate_sorted_list(size, min_val=1, max_val=1000):
    """
    Generate a sorted list of random integers for testing.
    
    Args:
        size (int): Number of elements to generate
        min_val (int): Minimum value for random numbers
        max_val (int): Maximum value for random numbers
        
    Returns:
        list: Sorted list of random integers
    """
    data = generate_random_list(size, min_val, max_val)
    return sorted(data)


def generate_reverse_sorted_list(size, min_val=1, max_val=1000):
    """
    Generate a reverse-sorted list (worst case for some algorithms).
    
    Args:
        size (int): Number of elements to generate
        min_val (int): Minimum value for random numbers
        max_val (int): Maximum value for random numbers
        
    Returns:
        list: Reverse-sorted list of random integers
    """
    data = generate_sorted_list(size, min_val, max_val)
    return list(reversed(data))


# Algorithm validation functions

def is_sorted(data_list):
    """
    Check if a list is sorted in ascending order.
    
    Args:
        data_list (list): List to check
        
    Returns:
        bool: True if sorted, False otherwise
    """
    for i in range(1, len(data_list)):
        if data_list[i] < data_list[i-1]:
            return False
    return True


def verify_search_result(data_list, target, result_index):
    """
    Verify that a search result is correct.
    
    Args:
        data_list (list): List that was searched
        target: Value that was searched for
        result_index (int): Index returned by search function
        
    Returns:
        bool: True if result is correct, False otherwise
    """
    if result_index == -1:
        return target not in data_list
    elif 0 <= result_index < len(data_list):
        return data_list[result_index] == target
    else:
        return False


# Performance testing helpers

def time_algorithm(algorithm_func, *args, trials=3):
    """
    Time an algorithm by running it multiple times and taking the average.
    
    Args:
        algorithm_func: Function to time
        *args: Arguments to pass to the function
        trials (int): Number of times to run the algorithm
        
    Returns:
        float: Average execution time in seconds
    """
    times = []
    
    for _ in range(trials):
        # Make a copy of mutable arguments to ensure fair testing
        args_copy = []
        for arg in args:
            if isinstance(arg, list):
                args_copy.append(arg.copy())
            else:
                args_copy.append(arg)
        
        start_time = time.time()
        algorithm_func(*args_copy)
        end_time = time.time()
        
        times.append(end_time - start_time)
    
    return sum(times) / len(times)


def warm_up_timing():
    """
    Perform some operations to warm up the timing system.
    This helps reduce variability in the first few measurements.
    """
    # Perform some quick operations to stabilize timing
    for _ in range(1000):
        test_list = [random.randint(1, 100) for _ in range(100)]
        sum(test_list)
        max(test_list)
        sorted(test_list)