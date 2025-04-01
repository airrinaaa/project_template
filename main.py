from app.io.input import read_from_console, read_from_file, read_with_pandas
from app.io.output import write_to_console, write_to_file


def main():
    console_text = read_from_console()
    write_to_console(console_text)
    write_to_file("data/output.txt", console_text)

    file_text = read_from_file("data/input.txt")
    write_to_console(file_text)
    write_to_file("data/output.txt", file_text)

    df = read_with_pandas("data/input.txt")
    write_to_console(df.to_string())
    write_to_file("data/output.txt", df.to_string())


if __name__ == "__main__":
    main()

