"""
Main Experiment Runner - INSTRUCTOR SOLUTION
CS101 Fall 2025 - Activity 05

This program runs doubling experiments to analyze algorithm performance.
This is the complete working version with all functionality implemented.
"""

from timer import run_custom_experiments, print_summary_report, save_results_to_file, create_performance_plot


def get_experiment_sizes():
    """
    Get experiment sizes from user input with suggestions.
    """
    print("Now let's set up your experiment sizes!")
    print("You'll test algorithms with different input sizes to see how performance changes.")
    print("\nSuggested ranges:")
    print("• Quick test: 500, 1000, 2000, 4000")
    print("• Medium test: 1000, 2000, 4000, 8000, 16000") 
    print("• Comprehensive: 1000, 2000, 4000, 8000, 16000, 32000")
    print("• Custom: Enter your own sizes")
    
    while True:
        print("\nChoose an option:")
        print("1. Quick test (recommended for first time)")
        print("2. Medium test (good balance)")
        print("3. Comprehensive test (takes longer)")
        print("4. Custom sizes")
        
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == "1":
            return [500, 1000, 2000, 4000]
        elif choice == "2":
            return [1000, 2000, 4000, 8000, 16000]
        elif choice == "3":
            return [1000, 2000, 4000, 8000, 16000, 32000]
        elif choice == "4":
            return get_custom_sizes()
        else:
            print("Please enter 1, 2, 3, or 4")


def get_custom_sizes():
    """
    Get custom experiment sizes from user.
    """
    print("\nEnter your custom sizes:")
    print("• Use at least 3 sizes for meaningful patterns")
    print("• Keep sizes reasonable (100-100000)")
    print("• Separate with commas (e.g., 1000,2000,4000)")
    
    while True:
        try:
            sizes_input = input("\nEnter sizes: ").strip()
            sizes = [int(s.strip()) for s in sizes_input.split(',')]
            
            # Validate sizes
            if len(sizes) < 3:
                print("Please enter at least 3 sizes")
                continue
            if any(s < 100 or s > 100000 for s in sizes):
                print("Please keep sizes between 100 and 100000")
                continue
            
            # Sort sizes
            sizes.sort()
            print(f"Using sizes: {sizes}")
            return sizes
            
        except ValueError:
            print("Please enter valid numbers separated by commas")


def get_algorithms_to_test():
    """
    Let user choose which algorithms to test.
    """
    print("\nWhich algorithms would you like to test?")
    print("1. Search algorithms only (Linear Search, Binary Search)")
    print("2. Sorting algorithms only (Bubble Sort, Selection Sort)")
    print("3. List operations only (Sum, Max, Min)")
    print("4. All algorithms (comprehensive)")
    
    while True:
        choice = input("\nEnter choice (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("Please enter 1, 2, 3, or 4")


def main():
    """
    Main function to run all performance experiments.
    """
    print("Welcome to Algorithm Performance Analysis!")
    print("This program will test various algorithms with increasing input sizes.")
    print("You will see how different approaches perform as data grows larger.\n")
    
    # Get experiment configuration from user
    sizes = get_experiment_sizes()
    algorithm_choice = get_algorithms_to_test()
    
    print(f"\nYour experiment will test sizes: {sizes}")
    print("This may take a few moments, especially for larger sizes...")
    
    # Give user a chance to cancel
    input("\nPress Enter to start experiments (or Ctrl+C to cancel)...")
    
    try:
        # Run experiments with user's choices
        results = run_custom_experiments(sizes, algorithm_choice)
        
        # Print comprehensive summary
        print_summary_report(results)
        
        # Save results to file
        save_results_to_file(results)
        
        # Create and show plot
        create_performance_plot(results)
        
        print("\n" + "="*60)
        print("EXPERIMENT COMPLETE!")
        print("="*60)
        print("Next steps:")
        print("1. Review the timing patterns above")
        print("2. Check the performance plot that was generated")
        print("3. Complete the reflection questions in writing/reflection.md")
        print("4. Think about what these patterns mean for real-world programming")
        print("\nGreat work exploring algorithm performance!")
        
    except KeyboardInterrupt:
        print("\n\nExperiment cancelled by user.")
    except Exception as e:
        print(f"\n\nError during experiment: {e}")
        print("Make sure all algorithms are implemented correctly in algorithms.py")


if __name__ == "__main__":
    main()