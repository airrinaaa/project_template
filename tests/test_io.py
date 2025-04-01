import pytest
from unittest.mock import patch, mock_open
from app.io.input import read_from_file, read_with_pandas


def test_read_from_file_valid_content():
    """
    Test 1: Reading a correct file.
    """
    # Arrange
    mock_content = "This is a valid file content."
    expected = "This is a valid file content."

    # Act
    with patch("builtins.open", mock_open(read_data=mock_content)):
        actual = read_from_file("data/input.txt")

    # Assert
    assert expected == actual


def test_read_from_file_empty_content():
    """
    Test 2: Reading an empty file.
    """
    # Arrange
    mock_content = ""
    expected = ""

    # Act
    with patch("builtins.open", mock_open(read_data=mock_content)):
        actual = read_from_file("data/empty.txt")

    # Assert
    assert expected == actual


def test_read_from_file_nonexistent_file():
    """
    Test 3: Reading nonexisting file.
    """
    # Arrange
    filename = "data/nonexistent.txt"

    # Act & Assert
    with pytest.raises(FileNotFoundError):
        read_from_file(filename)


def test_read_with_pandas_valid_content():
    """
    Test 1: Reading a correct file with psndas.
    """
    # Arrange
    mock_content = "Line 1\nLine 2\nLine 3"
    expected_lines = ["Line 1", "Line 2", "Line 3"]

    # Act
    with patch("builtins.open", mock_open(read_data=mock_content)):
        df = read_with_pandas("data/input.txt")

    # Assert
    assert df["Content"].tolist() == expected_lines


def test_read_with_pandas_empty_content():
    """
    Test 2: Reading an empty file with pandas.
    """
    # Arrange
    mock_content = ""
    expected_lines = []

    # Act
    with patch("builtins.open", mock_open(read_data=mock_content)):
        df = read_with_pandas("data/empty.txt")

    # Assert
    assert df["Content"].tolist() == expected_lines


def test_read_with_pandas_nonexistent_file():
    """
    Test 3: Reading nonexisting file with pandas.
    """
    # Arrange
    filename = "data/nonexistent.txt"

    # Act & Assert
    with pytest.raises(FileNotFoundError):
        read_with_pandas(filename)