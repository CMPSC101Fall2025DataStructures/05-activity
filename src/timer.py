"""
Timing and Experiment Management Module - INSTRUCTOR SOLUTION
CS101 Fall 2025 - Activity 05

This module provides utilities for conducting doubling experiments and timing algorithms.
All TODOs have been completed with working implementations.
"""

import time
import random
try:
    import matplotlib.pyplot as plt
    import numpy as np
    PLOTTING_AVAILABLE = True
except ImportError:
    PLOTTING_AVAILABLE = False
    
from algorithms import (
    linear_search, binary_search, bubble_sort, selection_sort,
    calculate_sum, find_maximum, find_minimum,
    generate_random_list, generate_sorted_list, time_algorithm, warm_up_timing
)


class ExperimentResults:
    """Class to store and manage experimental results."""
    
    def __init__(self, algorithm_name):
        self.algorithm_name = algorithm_name
        self.sizes = []
        self.times = []
        self.ratios = []
    
    def add_result(self, size, time_taken):
        """Add a result to the experiment."""
        self.sizes.append(size)
        self.times.append(time_taken)
        
        # Calculate ratio compared to previous measurement
        if len(self.times) > 1:
            ratio = time_taken / self.times[-2]
            self.ratios.append(ratio)
        else:
            self.ratios.append(None)  # No ratio for first measurement
    
    def print_results(self):
        """Print the results in a formatted table."""
        print(f"\n=== {self.algorithm_name} Experiment ===")
        print("Size        Time (seconds)    Ratio")
        print("────────────────────────────────────")
        
        for i, (size, time_val, ratio) in enumerate(zip(self.sizes, self.times, self.ratios)):
            if ratio is None:
                ratio_str = "─"
            else:
                ratio_str = f"{ratio:.2f}"
            
            print(f"{size:<10} {time_val:<15.6f} {ratio_str}")
    
    def analyze_pattern(self):
        """Analyze the pattern in timing ratios."""
        if len(self.ratios) < 2:
            return "Insufficient data for analysis"
        
        # Calculate average ratio (excluding None)
        valid_ratios = [r for r in self.ratios if r is not None]
        if not valid_ratios:
            return "No valid ratios to analyze"
        
        avg_ratio = sum(valid_ratios) / len(valid_ratios)
        
        # Classify the pattern based on average ratio
        if avg_ratio < 1.2:
            return "Logarithmic - small increase as input doubles"
        elif 1.8 <= avg_ratio <= 2.2:
            return "Linear - doubling input roughly doubles time"
        elif 3.5 <= avg_ratio <= 4.5:
            return "Quadratic - doubling input roughly quadruples time"
        elif 7.0 <= avg_ratio <= 9.0:
            return "Cubic - doubling input increases time ~8-fold"
        else:
            return f"Unknown pattern - average ratio: {avg_ratio:.2f}"


def run_search_experiment(search_func, algorithm_name, max_size=32000):
    """
    Run a doubling experiment for a search algorithm.
    
    Args:
        search_func: The search function to test
        algorithm_name (str): Name of the algorithm for reporting
        max_size (int): Maximum input size to test
        
    Returns:
        ExperimentResults: Results of the experiment
    """
    print(f"\nTesting {algorithm_name.lower()}...")
    results = ExperimentResults(algorithm_name)
    
    size = 1000
    while size <= max_size:
        # Generate appropriate test data
        if "binary" in algorithm_name.lower():
            data = generate_sorted_list(size)
        else:
            data = generate_random_list(size)
        
        # Choose a target (sometimes in list, sometimes not)
        if random.random() < 0.7:  # 70% chance target is in list
            target = random.choice(data)
        else:  # 30% chance target is not in list
            target = max(data) + 1
        
        # Time the algorithm
        avg_time = time_algorithm(search_func, data, target, trials=3)
        results.add_result(size, avg_time)
        
        print(f"  Size {size}: {avg_time:.6f} seconds")
        size *= 2
    
    return results


def run_sort_experiment(sort_func, algorithm_name, max_size=16000):
    """
    Run a doubling experiment for a sorting algorithm.
    
    Args:
        sort_func: The sorting function to test
        algorithm_name (str): Name of the algorithm for reporting
        max_size (int): Maximum input size to test (smaller for slow sorts)
        
    Returns:
        ExperimentResults: Results of the experiment
    """
    print(f"\nTesting {algorithm_name.lower()}...")
    results = ExperimentResults(algorithm_name)
    
    size = 1000
    while size <= max_size:
        # Generate random test data for sorting
        data = generate_random_list(size)
        
        # Time the algorithm
        avg_time = time_algorithm(sort_func, data, trials=3)
        results.add_result(size, avg_time)
        
        print(f"  Size {size}: {avg_time:.6f} seconds")
        size *= 2
    
    return results


def run_operation_experiment(operation_func, algorithm_name, max_size=64000):
    """
    Run a doubling experiment for a list operation (sum, max, min).
    
    Args:
        operation_func: The operation function to test
        algorithm_name (str): Name of the algorithm for reporting
        max_size (int): Maximum input size to test
        
    Returns:
        ExperimentResults: Results of the experiment
    """
    print(f"\nTesting {algorithm_name.lower()}...")
    results = ExperimentResults(algorithm_name)
    
    size = 1000
    while size <= max_size:
        # Generate random test data
        data = generate_random_list(size)
        
        # Time the algorithm
        avg_time = time_algorithm(operation_func, data, trials=5)
        results.add_result(size, avg_time)
        
        print(f"  Size {size}: {avg_time:.6f} seconds")
        size *= 2
    
    return results


def run_all_experiments():
    """
    Run all doubling experiments and collect results.
    
    Returns:
        list: List of ExperimentResults objects
    """
    print("=== Algorithm Performance Analysis ===")
    print("Conducting doubling experiments to analyze algorithm efficiency...")
    print("\nWarming up timing system...")
    warm_up_timing()
    
    all_results = []
    
    # SOLUTION: Run experiments for basic list operations
    print("\n" + "="*50)
    print("LIST OPERATION EXPERIMENTS")
    print("="*50)
    
    all_results.append(run_operation_experiment(calculate_sum, "List Sum"))
    all_results.append(run_operation_experiment(find_maximum, "Find Maximum"))
    all_results.append(run_operation_experiment(find_minimum, "Find Minimum"))
    
    # Search algorithm experiments
    print("\n" + "="*50)
    print("SEARCH ALGORITHM EXPERIMENTS")
    print("="*50)
    
    # SOLUTION: Run search experiments
    all_results.append(run_search_experiment(linear_search, "Linear Search"))
    all_results.append(run_search_experiment(binary_search, "Binary Search"))
    
    # Sorting algorithm experiments  
    print("\n" + "="*50)
    print("SORTING ALGORITHM EXPERIMENTS")
    print("="*50)
    print("Warning: Sorting experiments may take longer for large inputs...")
    
    # SOLUTION: Run sorting experiments with appropriate max sizes
    all_results.append(run_sort_experiment(bubble_sort, "Bubble Sort", max_size=8000))
    all_results.append(run_sort_experiment(selection_sort, "Selection Sort", max_size=16000))
    
    return all_results


def print_summary_report(all_results):
    """
    Print a summary report comparing all algorithms.
    
    Args:
        all_results (list): List of ExperimentResults objects
    """
    print("\n" + "="*60)
    print("EXPERIMENT SUMMARY REPORT")
    print("="*60)
    
    # Print individual results
    for result in all_results:
        result.print_results()
        pattern = result.analyze_pattern()
        print(f"Pattern: {pattern}")
        
        # Add pattern interpretation
        if "linear" in pattern.lower():
            print("Growth pattern: Doubles when input doubles")
        elif "logarithmic" in pattern.lower():
            print("Growth pattern: Very slow increase as input doubles")
        elif "quadratic" in pattern.lower():
            print("Growth pattern: Quadruples when input doubles")
        elif "cubic" in pattern.lower():
            print("Growth pattern: Time increases rapidly")
        else:
            print("Growth pattern: Pattern unclear from this data")
        
        print()
    
    # Performance ranking
    print("="*60)
    print("PERFORMANCE RANKING")
    print("="*60)
    
    # Group by algorithm type and provide insights
    search_algorithms = [r for r in all_results if "search" in r.algorithm_name.lower()]
    sort_algorithms = [r for r in all_results if "sort" in r.algorithm_name.lower()]
    operation_algorithms = [r for r in all_results if r not in search_algorithms and r not in sort_algorithms]
    
    if search_algorithms:
        print("\nSearch Algorithms (fastest to slowest):")
        print("1. Binary Search: Fastest - logarithmic growth")
        print("2. Linear Search: Slower - linear growth")
    
    if sort_algorithms:
        print("\nSorting Algorithms (fastest to slowest):")
        print("1. Selection Sort: Faster - quadratic but more efficient implementation")
        print("2. Bubble Sort: Slowest - quadratic with many swaps")
    
    if operation_algorithms:
        print("\nList Operations:")
        for result in operation_algorithms:
            print(f"• {result.algorithm_name}: Time grows proportionally with input size")
    
    print("\n" + "="*60)
    print("KEY INSIGHTS")
    print("="*60)
    print("• Logarithmic algorithms (Binary Search) scale excellently")
    print("• Linear algorithms (Linear Search, List Operations) scale reasonably") 
    print("• Quadratic algorithms (Sorting) become slow with large inputs")
    print("• Algorithm choice matters significantly for performance!")
    print("\nExperiment completed! Check writing/reflection.md for analysis questions.")


def save_results_to_file(all_results, filename="experiment_results.txt"):
    """
    Save experimental results to a text file.
    
    Args:
        all_results (list): List of ExperimentResults objects
        filename (str): Name of file to save results to
    """
    try:
        with open(filename, 'w') as f:
            f.write("Algorithm Performance Analysis Results\n")
            f.write("="*50 + "\n\n")
            
            for result in all_results:
                f.write(f"{result.algorithm_name} Results:\n")
                f.write("Size\tTime (s)\tRatio\n")
                
                for size, time_val, ratio in zip(result.sizes, result.times, result.ratios):
                    ratio_str = "─" if ratio is None else f"{ratio:.2f}"
                    f.write(f"{size}\t{time_val:.6f}\t{ratio_str}\n")
                
                f.write(f"Pattern: {result.analyze_pattern()}\n\n")
        
        print(f"\nResults saved to {filename}")
    except Exception as e:
        print(f"Error saving results: {e}")


# Additional analysis functions

def compare_algorithms(results_list, size_to_compare=8000):
    """
    Compare algorithm performance at a specific input size.
    
    Args:
        results_list (list): List of ExperimentResults objects
        size_to_compare (int): Input size to compare at
    """
    print(f"\nPerformance Comparison at Size {size_to_compare}:")
    print("-" * 50)
    
    comparisons = []
    for result in results_list:
        # Find the time for the closest size
        for i, size in enumerate(result.sizes):
            if size >= size_to_compare:
                time_at_size = result.times[i]
                comparisons.append((result.algorithm_name, time_at_size))
                break
    
    # Sort by time (fastest first)
    comparisons.sort(key=lambda x: x[1])
    
    for i, (name, time_val) in enumerate(comparisons, 1):
        print(f"{i}. {name}: {time_val:.6f} seconds")


def predict_future_performance(result, target_size):
    """
    Predict performance at a larger input size based on observed pattern.
    
    Args:
        result (ExperimentResults): Results object to analyze
        target_size (int): Size to predict performance for
        
    Returns:
        float: Predicted time in seconds
    """
    if len(result.times) < 2:
        return None
    
    # Use the last measurement as a baseline
    last_size = result.sizes[-1]
    last_time = result.times[-1]
    
    # Calculate size ratio
    size_ratio = target_size / last_size
    
    # Estimate time ratio based on pattern
    pattern = result.analyze_pattern()
    if "linear" in pattern.lower():
        time_ratio = size_ratio  # Linear relationship
    elif "logarithmic" in pattern.lower():
        import math
        time_ratio = math.log2(size_ratio) if size_ratio > 1 else 1
    elif "quadratic" in pattern.lower():
        time_ratio = size_ratio ** 2  # Quadratic relationship
    else:
        time_ratio = size_ratio  # Default to linear
    
    return last_time * time_ratio


def run_custom_experiments(sizes, algorithm_choice):
    """
    Run experiments with user-selected sizes and algorithms.
    
    Args:
        sizes (list): List of input sizes to test
        algorithm_choice (str): Which algorithms to test ('1', '2', '3', or '4')
        
    Returns:
        list: List of ExperimentResults objects
    """
    print("=== Custom Algorithm Performance Analysis ===")
    print("Conducting experiments with your chosen parameters...")
    print("\nWarming up timing system...")
    warm_up_timing()
    
    all_results = []
    
    # Algorithm choice mapping
    run_searches = algorithm_choice in ['1', '4']
    run_sorts = algorithm_choice in ['2', '4'] 
    run_operations = algorithm_choice in ['3', '4']
    
    if run_operations:
        print("\n" + "="*50)
        print("LIST OPERATION EXPERIMENTS")
        print("="*50)
        
        max_op_size = max([s for s in sizes if s <= 50000])  # Limit for operations
        op_sizes = [s for s in sizes if s <= max_op_size]
        
        all_results.append(run_custom_operation_experiment(calculate_sum, "List Sum", op_sizes))
        all_results.append(run_custom_operation_experiment(find_maximum, "Find Maximum", op_sizes))
        all_results.append(run_custom_operation_experiment(find_minimum, "Find Minimum", op_sizes))
    
    if run_searches:
        print("\n" + "="*50)
        print("SEARCH ALGORITHM EXPERIMENTS")
        print("="*50)
        
        max_search_size = max([s for s in sizes if s <= 50000])
        search_sizes = [s for s in sizes if s <= max_search_size]
        
        all_results.append(run_custom_search_experiment(linear_search, "Linear Search", search_sizes))
        all_results.append(run_custom_search_experiment(binary_search, "Binary Search", search_sizes))
    
    if run_sorts:
        print("\n" + "="*50)
        print("SORTING ALGORITHM EXPERIMENTS")
        print("="*50)
        print("Warning: Sorting experiments may take longer for large inputs...")
        
        # Limit sorting to reasonable sizes
        max_sort_size = max([s for s in sizes if s <= 20000])
        sort_sizes = [s for s in sizes if s <= max_sort_size]
        
        all_results.append(run_custom_sort_experiment(bubble_sort, "Bubble Sort", sort_sizes))
        all_results.append(run_custom_sort_experiment(selection_sort, "Selection Sort", sort_sizes))
    
    return all_results


def run_custom_search_experiment(search_func, algorithm_name, sizes):
    """Run search experiment with custom sizes."""
    print(f"\nTesting {algorithm_name.lower()}...")
    results = ExperimentResults(algorithm_name)
    
    for size in sizes:
        if algorithm_name == "Binary Search":
            data = generate_sorted_list(size)
        else:
            data = generate_random_list(size)
        
        # Choose a target (sometimes in list, sometimes not)
        if random.random() < 0.7:  # 70% chance target is in list
            target = random.choice(data)
        else:  # 30% chance target is not in list
            target = max(data) + 1
        
        # Time the algorithm
        avg_time = time_algorithm(search_func, data, target, trials=3)
        results.add_result(size, avg_time)
        
        print(f"  Size {size}: {avg_time:.6f} seconds")
    
    return results


def run_custom_sort_experiment(sort_func, algorithm_name, sizes):
    """Run sorting experiment with custom sizes."""
    print(f"\nTesting {algorithm_name.lower()}...")
    results = ExperimentResults(algorithm_name)
    
    for size in sizes:
        # Generate random test data for sorting
        data = generate_random_list(size)
        
        # Time the algorithm
        avg_time = time_algorithm(sort_func, data, trials=3)
        results.add_result(size, avg_time)
        
        print(f"  Size {size}: {avg_time:.6f} seconds")
    
    return results


def run_custom_operation_experiment(operation_func, algorithm_name, sizes):
    """Run list operation experiment with custom sizes."""
    print(f"\nTesting {algorithm_name.lower()}...")
    results = ExperimentResults(algorithm_name)
    
    for size in sizes:
        # Generate random test data
        data = generate_random_list(size)
        
        # Time the algorithm
        avg_time = time_algorithm(operation_func, data, trials=5)
        results.add_result(size, avg_time)
        
        print(f"  Size {size}: {avg_time:.6f} seconds")
    
    return results


def create_performance_plot(results_list):
    """
    Create a performance plot showing algorithm timing results.
    
    Args:
        results_list: List of ExperimentResults objects
    """
    if not PLOTTING_AVAILABLE:
        print("\nNote: matplotlib not available - skipping plot generation.")
        print("To see performance plots, install matplotlib with: pip install matplotlib")
        create_text_based_plot(results_list)
        return
        
    try:
        # Set up the plot
        plt.figure(figsize=(12, 8))
        
        # Colors for different algorithm types
        colors = ['blue', 'green', 'red', 'purple', 'orange', 'brown', 'pink', 'gray']
        
        for i, result in enumerate(results_list):
            if len(result.sizes) > 0:  # Only plot if we have data
                color = colors[i % len(colors)]
                plt.plot(result.sizes, result.times, 'o-', 
                        label=result.algorithm_name, color=color, linewidth=2, markersize=6)
        
        plt.xlabel('Input Size', fontsize=12)
        plt.ylabel('Time (seconds)', fontsize=12)
        plt.title('Algorithm Performance Analysis\nTime vs Input Size', fontsize=14, fontweight='bold')
        
        # Use log scale if times vary significantly
        max_time = max([max(r.times) for r in results_list if r.times])
        min_time = min([min(r.times) for r in results_list if r.times])
        if max_time / min_time > 100:
            plt.yscale('log')
            plt.ylabel('Time (seconds) - Log Scale', fontsize=12)
        
        plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.grid(True, alpha=0.3)
        plt.tight_layout()
        
        # Save the plot
        plot_filename = 'algorithm_performance_plot.png'
        plt.savefig(plot_filename, dpi=300, bbox_inches='tight')
        print(f"\nPerformance plot saved as: {plot_filename}")
        
        # Try to show the plot
        try:
            plt.show()
            print("Plot displayed on screen.")
        except:
            print("Could not display plot on screen, but it has been saved to file.")
            
    except Exception as e:
        print(f"\nError creating plot: {e}")
        print("Falling back to text-based visualization...")
        create_text_based_plot(results_list)


def create_text_based_plot(results_list):
    """
    Create a simple text-based visualization when matplotlib isn't available.
    
    Args:
        results_list: List of ExperimentResults objects
    """
    print("\n" + "="*80)
    print("TEXT-BASED PERFORMANCE VISUALIZATION")
    print("="*80)
    
    # Find the range of sizes and times
    all_sizes = []
    all_times = []
    for result in results_list:
        all_sizes.extend(result.sizes)
        all_times.extend(result.times)
    
    if not all_sizes:
        print("No data to visualize.")
        return
    
    min_size = min(all_sizes)
    max_size = max(all_sizes)
    min_time = min(all_times)
    max_time = max(all_times)
    
    print(f"Size range: {min_size:,} to {max_size:,}")
    print(f"Time range: {min_time:.6f} to {max_time:.6f} seconds")
    print()
    
    # Create a simple bar chart representation
    for result in results_list:
        if len(result.sizes) == 0:
            continue
            
        print(f"{result.algorithm_name}:")
        for size, time_val in zip(result.sizes, result.times):
            # Create a simple bar representation
            if max_time > 0:
                bar_length = int((time_val / max_time) * 50)
                bar = "█" * bar_length + "░" * (50 - bar_length)
            else:
                bar = "░" * 50
            print(f"  Size {size:>6,}: {time_val:>8.6f}s |{bar}|")
        print()
    
    print("Legend: █ = relative time (longer bars = more time)")
    print("="*80)