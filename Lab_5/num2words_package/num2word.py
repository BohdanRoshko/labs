"""This module contains logic to convert numbers to words."""

from num2words import num2words

def convert_num_to_word(num):
    """Convert a number to words using the num2words library.

    Args:
        num (float): The number to convert.

    Returns:
        str: The number in words.

    Raises:
        ValueError: If num is not a number.
    """
    try:
        return num2words(float(num))
    except ValueError:
        raise ValueError("Invalid number.")
