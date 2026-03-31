# phone-keypad-combination

A Python solution to generate all possible letter combinations that a given string of digits could represent on a standard phone keypad. 

## Project Structure

The project is modularized into two files to separate business logic from testing:

* `letter_combinations.py`: Contains the core algorithm and the custom sorting implementation.
* `test_letter_combinations.py`: Contains the unit testing suite.

## Algorithmic Approach

### 1. Combination Generation (Backtracking)
The primary logic uses a recursive Backtracking algorithm to explore all possible character mappings. It iterates through the input digits, looks up the corresponding characters in a dictionary, and recursively builds the resulting strings.

### 2. Custom Sorting (Quick Sort)
To fulfill the requirement of returning a sorted output, a custom Quick Sort algorithm is implemented. 
* While the backtracking naturally generates combinations in lexicographical order, the `quick_sort` function ensures the final list is explicitly sorted by returning a new sorted list.
* The test suite includes a dedicated test case with an unsorted array to verify the isolated functionality of the sorting algorithm.

## How to Run the Tests

The testing suite uses Python's built-in `unittest` framework. No external dependencies are required.

To run the tests, open your terminal in the project directory and execute:

```bash
python test_letter_combinations.py
```