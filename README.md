# Activity 05 - Algorithm Performance Analysis: Doubling Experiments

CMPSC101 :: Fall 2025 :: Modern Python Project with uv

**Assigned**: TBD
**Due**: TBD (Cut off due date and time).

Welcome to your first exploration of algorithm performance analysis using a modern Python development setup.

In this activity, you will conduct doubling experiments to measure how different algorithms perform as input sizes grow. You will run pre-written algorithms, measure their running times, and analyze the patterns you observe. This hands-on experience will give you intuition about algorithm efficiency while learning modern Python project management.

## Quick Start

**Run the program**:
```bash
uv run python src/main.py
```

Or use the convenient script command:
```bash
uv run activity05
```

## Learning Objectives

By the end of this activity, you will be able to:

* Run timing experiments on different algorithms
* Observe how algorithm performance changes with input size
* Analyze experimental data to identify performance patterns
* Compare the efficiency of different algorithmic approaches
* Use doubling experiments to predict algorithm behavior

## What is a Doubling Experiment?

A **doubling experiment** is a method for analyzing algorithm performance by measuring running time as we systematically increase input size. We start with a base size N, then test with 2N, 4N, 8N, and so on.

### The Process

For each algorithm:

* Run experiments with doubling input sizes (N, 2N, 4N, 8N, ...)
* Measure the running time for each input size
* Calculate the ratio between consecutive measurements
* Identify patterns in these ratios

### Example Pattern Analysis

If an algorithm takes:

* 1 second for N=1000
* 2 seconds for N=2000  
* 4 seconds for N=4000
* 8 seconds for N=8000

The ratios are consistently 2:1, suggesting the algorithm has **linear growth** - doubling the input doubles the time.

## Algorithms We Will Analyze

### Search Algorithms

* **Linear Search**: Checks each element one by one until finding the target
* **Binary Search**: Divides the search space in half each step (requires sorted data)

### Sorting Algorithms  

* **Bubble Sort**: Repeatedly swaps adjacent elements that are in wrong order
* **Selection Sort**: Finds the minimum element and places it at the beginning

## Getting Started

### Step 1: Setup Your Environment

This project uses **uv** for modern Python package management. All dependencies are automatically managed through the `pyproject.toml` file.

```bash
# Dependencies are automatically installed when you run:
uv run python src/main.py
```

### Step 2: Run the Interactive Experiments

The program will guide you through setting up your own custom experiment:

```bash
uv run activity05
```

The program will ask you to:

1. **Choose experiment sizes**: Pick from suggested ranges or enter your own custom sizes
   - Quick test: 500, 1000, 2000, 4000 (recommended for first time)
   - Medium test: 1000, 2000, 4000, 8000, 16000 (good balance)
   - Comprehensive: 1000, 2000, 4000, 8000, 16000, 32000 (takes longer)
   - Custom: Enter your own sizes separated by commas

2. **Select algorithms to test**:
   - Search algorithms only (Linear Search, Binary Search)
   - Sorting algorithms only (Bubble Sort, Selection Sort)  
   - List operations only (Sum, Max, Min)
   - All algorithms (comprehensive)

### Step 3: Analyze Your Results

After running your experiments, the program will:

* Display timing results in formatted tables
* Show performance patterns and growth characteristics
* Create a visual plot of your results (if matplotlib is available)
* Generate a text-based visualization as backup
* Save results to `experiment_results.txt`

## Understanding the Results

### Linear Search Results

```
Size        Time (seconds)    Ratio
────────────────────────────────────
1000        0.000123         ─
2000        0.000245         1.99
4000        0.000489         2.00
8000        0.000978         2.00
16000       0.001956         2.00
32000       0.003912         2.00

Pattern: Linear - doubling input doubles time
Growth pattern: Doubles when input doubles
```

**What this means**: Linear search has to check potentially every element, so doubling the list size doubles the worst-case time.

### Binary Search Results

```
Size        Time (seconds)    Ratio
────────────────────────────────────
1000        0.000008         ─
2000        0.000009         1.13
4000        0.000010         1.11
8000        0.000011         1.10
16000       0.000012         1.09
32000       0.000013         1.08

Pattern: Logarithmic - small increase as input doubles
Growth pattern: Very slow increase as input doubles
```

**What this means**: Binary search eliminates half the possibilities each step, so it only needs a few more steps even when the input doubles.

### Sorting Algorithm Results

For bubble sort and selection sort, you should see ratios around 4:1, indicating that doubling the input quadruples the time (quadratic growth).

## Technical Details

### Key Features

* **Interactive Experiment Design**: Choose your own input sizes and algorithms
* **Visual Performance Plots**: Automatic generation of performance graphs
* **Multiple Algorithm Support**: Search, sorting, and list operation algorithms
* **Comprehensive Analysis**: Detailed timing reports with growth pattern analysis

## Reflection Questions

After running your experiments, answer these questions in `writing/reflection.md`:

1. **Linear vs Binary Search**: How do the timing ratios compare between linear and binary search? Why do you think binary search performs better?

2. **Sorting Comparison**: Compare the performance of bubble sort and selection sort. Are they similar? What do the ratios tell you about their efficiency?

3. **Prediction**: Based on your bubble sort results, predict how long it would take to sort 64000 elements if 32000 elements took 2 seconds.

4. **Real-World Applications**: Think of three real-world scenarios where you would prefer binary search over linear search, and explain why.

5. **Limitations**: What are some limitations of these timing experiments? What factors might affect the accuracy of your measurements?

## Sample Reflection Response

```
## Algorithm Performance Analysis Reflection

### Experimental Results Summary
After running all experiments, I observed the following patterns:

Linear Search: Consistent 2:1 ratios, indicating linear growth
Binary Search: Ratios around 1.1:1, indicating logarithmic growth
Bubble Sort: Ratios around 4:1, indicating quadratic growth
Selection Sort: Similar to bubble sort with 4:1 ratios

### Analysis
[Your detailed analysis here...]

### Conclusions
[Your conclusions about algorithm efficiency...]
```

## Submission

Submit the following files:

* `writing/reflection.md` - Your completed reflection with experimental analysis
* Any screenshots of your experimental results (optional)

The algorithms and timing code are provided complete - your job is to run experiments and analyze the results.

## Additional Resources

* [Python time module documentation](https://docs.python.org/3/library/time.html)
* [Algorithm Analysis fundamentals](https://www.geeksforgeeks.org/analysis-of-algorithms-set-1-asymptotic-analysis/)

Ready to discover how algorithms really perform? Start with choosing your experiment parameters and explore the performance patterns.

Size        Time (seconds)    Ratio
────────────────────────────────────
1000        0.045123         ─
2000        0.180489         4.00
4000        0.721956         4.00
8000        2.887824         4.00
16000       11.551296        4.00

Pattern: Quadratic - doubling input quadruples time
Growth pattern: Quadruples when input doubles

=== Summary Report ===
Algorithm Performance Rankings (1000 to 32000 elements):
1. Binary Search:    Fastest - logarithmic growth
2. Linear Search:    Moderate - linear growth  
3. Selection Sort:   Slow - quadratic growth
4. Bubble Sort:      Slowest - quadratic growth

Experiment completed! Check writing/reflection.md for analysis questions.
```

## 🛠 Getting Started

### Setting Up Your Environment

1. **Open the project in VS Code:**

```bash
   # Navigate to the project directory
   that you cloned from GitHub
   
   # Open in VS Code
   code .
```

2. **Verify Python is working:**

   * Open the VS Code terminal (`Terminal` → `New Terminal` or `` Ctrl+` ``)
   * Check your Python version:
  
    ```bash
     python --version
     # or
     python3 --version
    ```

3. **Running Your Code:**

**From the project root directory:**

```bash
uv run python src/main.py
```

## Assessment

This is a check mark activity. Please run the experiments and complete your reflection analysis by the end of class.

## Deliverables

### What to Submit

1. **Completed reflection file:**

   * `writing/reflection.md` (analysis of your experimental results including experiment configuration, data tables, and answers to analysis questions)

2. **Optional:**

   * Screenshots of your experimental results
   * Performance plots (if generated)

Note: please be sure to change the names of the files so that they can be identified for their contents.

## Optimistic Notes

This activity introduces you to the fascinating world of algorithm analysis! You'll discover how different approaches to solving problems can have dramatically different performance characteristics. This hands-on experience with measuring and comparing algorithms will give you intuition that will serve you well throughout your programming journey.

Remember: every programmer needs to understand how their code performs. Learning to measure and analyze algorithm efficiency is a crucial skill that will help you write better, faster programs.

## The Writing Component

After completing your experiments, you'll analyze your results in `writing/reflection.md`:

### Analysis Categories

1. **Experimental Methodology** - How you conducted the experiments
2. **Results Interpretation** - What patterns you observed
3. **Algorithm Comparison** - Which algorithms performed best/worst
4. **Hypothesis Formation** - Predictions about algorithm behavior
5. **Real-world Applications** - Where these insights matter

### Sample Questions You'll Answer

* Which algorithm showed the fastest growth in running time?
* How did the binary search times compare to linear search?
* What patterns did you notice in the sorting algorithms?
* Which algorithm would you choose for large datasets and why?
* How might these insights apply to real-world programming?

---

## GatorGrade

You can check the baseline writing and commit requirements for this lab assignment by running department's assignment checking `gatorgrade` tool. To use `gatorgrade`, you first need to make sure you have Python3 installed (type `python --version` or `python3 --version` to check). If you do not have Python installed, please see:

* [Setting Up Python on Windows](https://realpython.com/lessons/python-windows-setup/)
* [Python 3 Installation and Setup Guide](https://realpython.com/installing-python/)
* [How to Install Python 3 and Set Up a Local Programming Environment on Windows 10](https://www.digitalocean.com/community/tutorials/how-to-install-python-3-and-set-up-a-local-programming-environment-on-windows-10)

Then, if you have not done so already, you need to install `gatorgrade`:

* First, [install `pipx`](https://pypa.github.io/pipx/installation/)
* Then, install `gatorgrade` with `pipx install gatorgrade`

Finally, you can run `gatorgrade`:

`gatorgrade --config config/gatorgrade.yml`

## Seeking Assistance

## 🆘 Getting Help

**Stuck on an algorithm?**

* Review the algorithm descriptions and examples
* Check the hints in the TODO comments
* Test with small inputs first before scaling up
* Ask for help with specific algorithm steps

**Unexpected timing results?**

* Make sure you're running multiple trials
* Check that your algorithms are implemented correctly
* Verify input sizes are actually doubling
* Consider computer performance variations

**Common Issues:**

* **Import errors**: Check file names and function names
* **Timing inconsistencies**: Run experiments multiple times
* **Memory issues**: Start with smaller maximum input sizes
* **Slow execution**: Some algorithms are intentionally slow for large inputs

**Markdown:**

* Extra resources for using markdown include:
  * [Markdown Tidbits](https://www.youtube.com/watch?v=cdJEUAy5IyA)
  * [Markdown Cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet)

## Modern Python Development

This activity introduces you to modern Python development practices:

* **Package Management**: Using `uv` for fast, reliable dependency management
* **Project Configuration**: All settings managed through `pyproject.toml`
* **Dependency Locking**: `uv.lock` ensures reproducible environments
* **Script Entry Points**: Convenient commands defined in project configuration
* **Structured Code**: Well-organized source code in dedicated directories

These practices prepare you for real-world Python development and open-source contribution.

## Development Resources

* [uv Documentation](https://github.com/astral-sh/uv) - Modern Python package manager
* [Python Packaging Guide](https://packaging.python.org/) - Official packaging documentation
* [Algorithm Analysis](https://en.wikipedia.org/wiki/Analysis_of_algorithms) - Wikipedia overview

If you have questions, please ask the Technical Leaders or the instructor.

**Good luck, and happy experimenting!**

---

*Ready to discover how algorithms really perform? Let's start measuring!*
