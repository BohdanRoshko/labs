"""This module contains logic to handle user input."""

def get_user_input():
    """Prompt the user for a number.

    Returns:
        str: The number entered by the user.

    Raises:
        KeyboardInterrupt: If the user interrupts the input.
    """
    try:
        return input("Enter a number (or 'quit' to stop): ")
    except KeyboardInterrupt:
        raise KeyboardInterrupt("Input interrupted.")
