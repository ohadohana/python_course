<<<<<<< HEAD
# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
=======

def print_longest_name(filename):
    print(max(open(filename).read().splitlines(), key=len))
def print_total_length(filename):
    print("Total length of all names in the file:")
    total_length = sum(len(name) for name in open(filename).read().splitlines())
    print(total_length)


def print_shortest_names(filename):
    print("\nShortest names in the file:")
    names = open(filename).read().splitlines()
    min_length = min(len(name) for name in names)
    shortest_names = "\n".join(name for name in names if len(name) == min_length)
    print(shortest_names)


def create_name_length_file(input_filename, output_filename):
    with open(output_filename, 'w') as f:
        name_lengths = "\n".join(str(len(name)) for name in open(input_filename).read().splitlines())
        f.write(name_lengths)
    print(f"\nName lengths written to {output_filename}")


def print_names_of_length(filename, length):
    print(f"\nNames of length {length} in the file:")
    names_of_length = "\n".join(name for name in open(filename).read().splitlines() if len(name) == length)
    print(names_of_length)


def main():
    filename = "C:\\Users\\User\\python.txt"
    output_filename = "C:\\Users\\User\\python2.txt"
    length_to_find = 4

    print_longest_name(filename)
    print_total_length(filename)
    print_shortest_names(filename)
    create_name_length_file(filename, output_filename)
    print_names_of_length(filename, length_to_find)


main()

