from typing import List, Callable


def repeat_function(func: Callable[[], None], times: int) -> None:
    """
    Repeats a given function a specified number of times.

    Args:
        func (Callable[[], None]): The function to repeat.
        times (int): Number of times to execute the function.
    """
    for _ in range(times):
        func()


def find_max(lst: List[int]) -> int:
    """
    Finds the maximum integer in a list.

    Args:
        lst (List[int]): A list of integers.

    Returns:
        int: The maximum integer. Raises ValueError if the list is empty.
    """
    if not lst:
        raise ValueError('The list must not be empty.')
    maximum = lst[0]
    for number in lst[1:]:
        if number > maximum:
            maximum = number
    return maximum


def average(lst: List[float]) -> float:
    """
    Calculates the average of a list of floats.

    Args:
        lst (List[float]): A list of floats.

    Returns:
        float: The average of the list. Raises ValueError if the list is empty.
    """
    if not lst:
        raise ValueError('The list must not be empty.')
    return sum(lst) / len(lst)