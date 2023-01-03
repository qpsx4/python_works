import string as s
import itertools


def greetings():
    print("Keyword generator")

    my_str = '''
    B - большие буквы
    L - маленькие буквы
    S - спецсимволы
    N - числа
    '''
    print(my_str)


def input_and_make_str_symbols():
    user_options = input("Выберите аргументы:\n").lower()
    global symbol_str

    for elem in user_options:
        if elem == "b":
            symbol_str += s.ascii_uppercase
        elif elem == "l":
            symbol_str += s.ascii_lowercase
        elif elem == "s":
            symbol_str += s.punctuation
        elif elem == "N":
            symbol_str += s.digits
    symbol_str = "".join(set(symbol_str))


def counting():
    count = int(input("Количество символов в слове?\n"))

    print(f"Количество комбинаций: {len(symbol_str)**count}")
    print("Done!")
    return count


def write_to_file():
    with open("gen_dict.txt", "w") as file:
        for i in list(itertools.product(symbol_str,
                                        repeat=int(counting()))):
            file.write("".join(i) + "\n")


if __name__ == "__main__":
    symbol_str = ""
    greetings()
    input_and_make_str_symbols()
    write_to_file()
