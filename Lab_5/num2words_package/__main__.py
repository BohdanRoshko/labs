"""This module is the entry point for the num2word_package package."""

from num2words_package import convert_num_to_word, get_user_input

def main():
    """The main function for the num2word_package package."""
    while True:
        try:
            # Read a number from the keyboard
            num = get_user_input()

            # If the user entered 'quit', stop the loop
            if num.lower() == 'quit':
                break

            # Convert the input to words and display it
            print(convert_num_to_word(num))

        except ValueError:
            # The input was not a valid number
            print("That's not a valid number. Try again.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
