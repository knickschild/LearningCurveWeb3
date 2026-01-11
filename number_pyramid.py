#!/usr/bin/env python3
"""
Number Pyramid Generator

This program creates a pyramid pattern using numbers.
"""

def print_number_pyramid(rows):
    """
    Prints a number pyramid with the specified number of rows.

    Args:
        rows (int): Number of rows in the pyramid

    Example output for rows=5:
        1
       1 2
      1 2 3
     1 2 3 4
    1 2 3 4 5
    """
    for i in range(1, rows + 1):
        # Print leading spaces for alignment
        print(' ' * (rows - i), end='')

        # Print numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end=' ')

        # Move to next line
        print()


def print_repeated_number_pyramid(rows):
    """
    Prints a pyramid where each row contains the row number repeated.

    Args:
        rows (int): Number of rows in the pyramid

    Example output for rows=5:
        1
       2 2
      3 3 3
     4 4 4 4
    5 5 5 5 5
    """
    for i in range(1, rows + 1):
        # Print leading spaces for alignment
        print(' ' * (rows - i), end='')

        # Print the current row number i times
        for j in range(i):
            print(i, end=' ')

        # Move to next line
        print()


def print_inverted_pyramid(rows):
    """
    Prints an inverted number pyramid.

    Args:
        rows (int): Number of rows in the pyramid

    Example output for rows=5:
    1 2 3 4 5
     1 2 3 4
      1 2 3
       1 2
        1
    """
    for i in range(rows, 0, -1):
        # Print leading spaces
        print(' ' * (rows - i), end='')

        # Print numbers from 1 to i
        for j in range(1, i + 1):
            print(j, end=' ')

        # Move to next line
        print()


def main():
    """Main function to demonstrate different pyramid patterns."""
    print("=" * 40)
    print("Number Pyramid Patterns")
    print("=" * 40)

    rows = 5

    print(f"\n1. Standard Number Pyramid ({rows} rows):")
    print_number_pyramid(rows)

    print(f"\n2. Repeated Number Pyramid ({rows} rows):")
    print_repeated_number_pyramid(rows)

    print(f"\n3. Inverted Number Pyramid ({rows} rows):")
    print_inverted_pyramid(rows)

    # Interactive mode
    print("\n" + "=" * 40)
    try:
        user_rows = int(input("\nEnter number of rows for custom pyramid: "))
        if user_rows > 0:
            print("\nYour custom pyramid:")
            print_number_pyramid(user_rows)
        else:
            print("Please enter a positive number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except KeyboardInterrupt:
        print("\n\nProgram terminated.")


if __name__ == "__main__":
    main()
