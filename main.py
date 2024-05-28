



def print_longest_name(filename):
    print(max(open(filename).read().splitlines(), key=len))
    #מדפיסה את השם האורך ביותר בקובץ

def print_total_length(filename):
    print("Total length of all names in the file:")
    total_length = sum(len(name) for name in open(filename).read().splitlines())
    print(total_length)
    #מדפיסה את אורך כל המילים  בקובץ


def print_shortest_names(filename):
    print("\nShortest names in the file:")
    names = open(filename).read().splitlines()
    min_length = min(len(name) for name in names)
    shortest_names = "\n".join(name for name in names if len(name) == min_length)
    print(shortest_names)

    #מדפיס  את המילים הקצרות ביותר בקובץ





def create_name_length_file(input_filename, output_filename):
    with open(output_filename, 'w') as f:
        name_lengths = "\n".join(str(len(name)) for name in open(input_filename).read().splitlines())
        f.write(name_lengths)
    print(f"\nName lengths written to {output_filename}")

    #מכניסה לקובץ הנתום את אורך המילים בקובת הקלט


def print_names_of_length(filename, length):
    print(f"\nNames of length {length} in the file:")
    names_of_length = "\n".join(name for name in open(filename).read().splitlines() if len(name) == length)
    print(names_of_length)

    #מדפיסה את המילים בוקבץ עם אורך המילה שנקלט


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

