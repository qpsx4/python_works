from tqdm import tqdm
import zipfile
import string as s
import itertools
import os


def generate_wordlist():
    pass_start = "o_main_got"
    with open("my_dict.txt", "w") as file:
        for i in list(itertools.product(s.digits, repeat=5)):
            file.write(pass_start + "".join(i) + "\n")


def bruteforce():
    print("Start bruteforce...")

    wordlist = 'my_dict.txt'
    words_count = len(list(open(os.getcwd() + "/my_dict.txt", "rb")))

    print(f"Total passwords to test: {words_count}")

    path_file = 'secure.zip'
    zip_file = zipfile.ZipFile(path_file)

    with open(wordlist, "rb") as file:
        for passwd in tqdm(file, total=words_count, unit=" word"):
            try:
                zip_file.extractall(pwd=passwd.strip())
            except:
                pass
            else:
                print("\nPassword found:" + "\033[32m", passwd.decode().strip())
                return 0
    print("Password not found", "\033[91m" + "try other wordlist.")


if __name__ == "__main__":
    generate_wordlist()
    bruteforce()
