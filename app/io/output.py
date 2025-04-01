

def write_to_console(text):
    """
        Prints a given text to the console.

        Note:
            This function simply outputs the provided text to the standard output.

        Args:
            text (str): The text to be printed to the console.

        Returns:
            None

        Examples:
            >>>write_to_console("Hello, World!")
            Hello, World!
        """
    print(text)


def write_to_file(filename, text):
    """
        Writes a given text to a specified file using built-in Python functions.

        Note:
            This function opens a file in write mode and writes the given text into it.
            If the file already exists, its content will be overwritten.

        Args:
            filename (str): The path to the file where the text should be written.
            text (str): The text to be written to the file.

        Returns:
            None

        Examples:
            >>> write_to_file("output.txt", "This is a test.")
            # The text 'This is a test.' is written to 'output.txt'
        """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
