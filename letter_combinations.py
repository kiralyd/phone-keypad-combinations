
def quick_sort(arr):
    """
    Sorts a list of comparable elements using the quick sort algorithm.

    Args:
        arr (list): The list of elements to be sorted (e.g., ints, floats, strings).

    Returns:
        list: A new list containing the sorted elements.
    """

    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def letter_combinations(digits: str) -> list[str]:
    """
    Maps digits to their corresponding letters on a phone keypad and generates all possible letter combinations for the given input digits.
   
    Args:
        digits (str): A string containing digits from 2-9.
    
    Returns:
        list[str]: A lexicographically sorted list of the letter combinations.
    """

    if digits == "":
        return []

    letter_map = {
        '2': 'abc', 
        '3': 'def', 
        '4': 'ghi', 
        '5': 'jkl', 
        '6': 'mno', 
        '7': 'pqrs', 
        '8': 'tuv', 
        '9': 'wxyz'
    }
    
    result = []

    def backtrack(index, path):
        """
        Helper function to perform backtracking and generate letter combinations.

        Args:
            index (int): The current index in the input digits string.
            path (str): The current combination of letters being formed.

        Returns:
            None.
        """
        if index == len(digits):
            result.append(path)
            return
            
        digit = digits[index]
        if digit in letter_map:
            for char in letter_map[digit]:
                backtrack(index + 1, path + char)

    backtrack(0, '')

    return quick_sort(result)  