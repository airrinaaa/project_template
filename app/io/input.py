
import pandas as pd

def read_from_console():
    """
        Reads a line of text from the console.

        Note:
            This function waits for user input and returns the entered text.

        Args:
            None

        Returns:
            str: The input text entered by the user.

        Examples:
            >>> user_input = read_from_console()
            >>> print(user_input)
            Hello, World!
        """
    return input("Enter text: ")


def read_from_file(filename):
    """
        Reads the content of a file using built-in Python functions.

        Note:
            This function opens a file in read mode and returns its content as a string.

        Args:
            filename (str): The path to the file to be read.

        Returns:
            str: The content of the file as a string.

        Examples:
            >>> content = read_from_file("example.txt")
            >>> print(content)
            This is the file content.
        """
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()


def read_with_pandas(filename):
    """
        Reads the content of a file using the pandas library.

        Note:
            This function is useful for reading structured data such as CSV or Excel files.

        Args:
            filename (str): The path to the file to be read.

        Returns:
            pandas.DataFrame: A DataFrame containing the file's content.

        Examples:
            >>> df = read_with_pandas("data.csv")
            >>> print(df.head())
        """
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
        return pd.DataFrame(lines, columns=["Content"])
    except FileNotFoundError:
        print(f"Error: The file '{filename}' was not found.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Error reading file '{filename}': {e}")
        return pd.DataFrame()
