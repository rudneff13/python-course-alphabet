"""
This is a list of functions that should be completed.
"""

from typing import Any
from typing import List


class OurAwesomeException(Exception):
    pass


def is_two_object_has_same_value(first: Any, second: Any) -> bool:
    """
    If @first and @second has same value should return True
    In another case should return False
    """
    if first == second:
        return True
    else:
        return False


def is_two_objects_has_same_type(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if type(first) == type(second):
        return True
    else:
        return False


def is_two_objects_is_the_same_objects(first: Any, second: Any) -> bool:
    """
    If @first and @second has same type should return True
    In another case should return False
    """
    if first is second:
        return True
    else:
        return False


def multiple_ints(first_value: int, second_value: int) -> int:
    """
    Should calculate product of all args.
    if first_value or second_value is not int should raise ValueError

    Raises:
        ValueError

    Params:
        first_value: value for multiply
        second_value
    Returns:
        Product of elements
    """
    if isinstance(first_value, int) and isinstance(second_value, int):
        return first_value * second_value
    else:
        raise ValueError


def multiple_ints_with_conversion(first_value: Any, second_value: Any) -> int:
    """
    If possible to convert arguments to int value - convert and multiply them.
    If it is impossible raise OurAwesomeException

    Args:
        first_value: number for multiply
        second_value: number for multiply

    Raises:
        OurAwesomeException

    Returns: multiple of two numbers.

    Examples:
        multiple_ints_with_conversion(6, 6)
        >>> 36
        multiple_ints_with_conversion(2, 2.0)
        >>> 4
        multiple_ints_with_conversion("12", 1)
        >>> 12
        try:
            multiple_ints_with_conversion("Hello", 2)
        except ValueError:
            print("Not valid input data")
        >>> "Not valid input data"
    """
    # if type(int(first_value)) == type(int(second_value)) == int:
    #         return int(first_value) * int(second_value)
    # else:
    #     raise OurAwesomeException
    if isinstance(int(first_value), int) and isinstance(int(second_value), int):
        return int(first_value) * int(second_value)
    else:
        raise OurAwesomeException


def is_word_in_text(word: str, text: str) -> bool:
    """
    If text contain word return True
    In another case return False.

    Args:
        word: Searchable substring
        text: Text for searching

    Examples:
        is_word_in_text("Hello", "Hello word")
        >>> True
        is_word_in_text("Glad", "Nice to meet you ")
        >>> False

    """
    if word in text:
        return True
    else:
        return False


def some_loop_exercise() -> list:
    """
    Use loop to create list that contain int values from 0 to 12 except 6 and 7
    """
    new_list = []
    i = 0
    while i < 13:
        if i == 6 or i == 7:
            pass
        else:
            new_list.append(i)
        i += 1
    return new_list


def remove_from_list_all_negative_numbers(data: List[int]) -> list:
    """
    Use loops to solve this task.
    You could use data.remove(negative_number) to solve this issue.
    Also you could create new list with only positive numbers.
    Examples:
        remove_from_list_all_negative_numbers([1, 5, -7, 8, -1])
        >>> [1, 5, 8]
    """
    # new_list = []
    # for value in data:
    #     if value >=0:
    #         new_list.append(value)
    #     else:
    #         pass
    # return new_list

    i = 0
    while i < len(data):
        if data[i] >= 0:
            i += 1
        else:
            data.remove(data[i])
    return data

    # j = 0
    # for i in range(0, len(List)):
    #     if List[j] >= 0:
    #         j += 1
    #         continue
    #     else:
    #         List.remove(List[j])
    # return List


def alphabet() -> dict:
    """
    Create dict which keys is alphabetic characters. And values their number in alphabet
    Notes You could see an implementaion of this one in test, but create another one
    Examples:
        alphabet()
        >>> {"a": 1, "b": 2 ...}
    """

    import string

    values = list(string.ascii_lowercase)
    keys = list(range(1, len(values)+1))
    new_dict = dict(zip(keys, values))
    return new_dict


def simple_sort(data: List[int]) -> List[list]:
    """
    Sort list of ints without using built-in methods.
    Examples:
        simple_sort([2, 9, 6, 7, 3, 2, 1])
        >>> [1, 2, 2, 3, 6, 7, 9]
    Returns:

    """

    # new_data = []
    # for i in range(0, len(data)):
    #     new_data.append(min(data))
    #     data.remove(min(data))
    # return new_data

    # last_item = len(data)-1
    # for i in range(0, last_item):
    #     for j in range(0, last_item - i):
    #         if data[j] > data[j + 1]:
    #             data[j], data[j + 1] = data[j + 1], data[j]
    # return data

    for j in range(len(data) - 1, 0, -1):
        for i in range(j):
            if data[i] > data[i + 1]:
                data[i], data[i + 1] = data[i + 1], data[i]
    return data
