import requests
import sys
import os
from colorama import Fore as F
import argparse
import multiprocessing
import base64
import urllib.parse


DOMAIN = ""
DIRS = []


def greetings():
    """Функция отображает приветствие пользователя"""
    print(F.GREEN + '''
╔═══╗╔══╗╔═══╗     ╔═══╗╔╗─╔╗╔════╗╔════╗╔═══╗╔═══╗
╚╗╔╗║╚╣║╝║╔═╗║     ║╔══╝║║─║║╚══╗═║╚══╗═║║╔══╝║╔═╗║
─║║║║─║║─║╚═╝║     ║╚══╗║║─║║──╔╝╔╝──╔╝╔╝║╚══╗║╚═╝║
─║║║║─║║─║╔╗╔╝     ║╔══╝║║─║║─╔╝╔╝──╔╝╔╝─║╔══╝║╔╗╔╝
╔╝╚╝║╔╣║╗║║║╚╗     ║║───║╚═╝║╔╝═╚═╗╔╝═╚═╗║╚══╗║║║╚╗
╚═══╝╚══╝╚╝╚═╝     ╚╝───╚═══╝╚════╝╚════╝╚═══╝╚╝╚═╝
          ''' + F.RESET)


def check_wordlist_file(path_to_wordlist):
    """Функция проверяет наличие файла со словарём"""
    if not os.path.isfile(path_to_wordlist.replace("\'", "")):
        print(f"{path_to_wordlist}\nФайл со словарём не найден.")
        sys.exit(0)
    fill_dirs_from_file(path_to_wordlist)


def check_site_annotaion(hostname):
    set_url_format(hostname)
    """Функция проверяет есть ли коннект с хостом"""
    try:
        response = requests.get(DOMAIN, headers={"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.119 Safari/537.36"},
                                timeout=1)
        response.raise_for_status()
        if response.status_code == 200:
            print('OK!')
    except (requests.exceptions.HTTPError, requests.exceptions.Timeout, requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as e:
        print('ERROR: %s' % e)
        sys.exit(0)


def set_url_format(hostname):
    """Функция проверяет форматирование url сайта"""
    global DOMAIN

    if hostname.endswith("FUZZ"):
        DOMAIN = hostname.replace("FUZZ", "")
    else:
        print("Ошибка! Необходимо использовать FUZZ в домене!")
        sys.exit(0)


def check_app_keys():
    """Функция проверяет правильность аргументов"""

    check_wordlist_file(my_args.w)
    check_site_annotaion(my_args.u)
    print(f"\nРаботаем с сайтом {DOMAIN}. Путь к словарю {my_args.w}\n")


def fill_dirs_from_file(dirs_file):
    """Функция читает файл с адресами папок в список"""
    with open(dirs_file, "r") as reader:
        for line in reader.readlines():
            DIRS.append(line)
    print("\nЗагружено строк из словаря: " + str(len(DIRS)) + "\n")


def check_for_encode_keys(target_dir):
    if my_args.b64:
        target_dir = bytes(target_dir, 'utf-8')
        return base64.b64encode(target_dir).decode()
    elif my_args.uenc:
        return urllib.parse.quote(target_dir)
    else:
        return target_dir


def check_for_headers_key():
    list_keys, list_values = [], []
    if my_args.head:
        for elem in my_args.head.split(","):
            list_keys.append(elem.split(":")[0].strip())
            list_values.append(elem.split(":")[1].strip())

        my_dic = dict(zip(list_keys, list_values))
        return ", headers=" + str(my_dic)
    else:
        return ""


def get_site_dirs(target_dir, counter):
    """Функция проверки директорий"""
    lock.acquire()
    try:
        with open("fuzz.txt", "w") as file:
            if my_args.e:
                new_target_dir = target_dir.strip() + "." + my_args.e
                target_url = DOMAIN + check_for_encode_keys(new_target_dir)
                host_answer = requests.get(target_url + check_for_headers_key())
            else:
                target_url = DOMAIN + check_for_encode_keys(target_dir).strip() + '/'
                host_answer = requests.get(target_url + check_for_headers_key(), allow_redirects=False)

            if host_answer.status_code == 404:
                print(f"\r\033[K{counter:0>8} of {len(DIRS)}\t{host_answer.status_code}\t{target_url}", end="")
            elif host_answer.status_code == 200:
                print(f"\r{counter:0>8} of {len(DIRS)}\t{F.GREEN + str(host_answer.status_code) + F.RESET}\t{target_url}")
            elif str(host_answer.status_code)[0] == "4":
                print(f"\r{counter:0>8} of {len(DIRS)}\t{F.RED + str(host_answer.status_code) + F.RESET}\t{target_url}")
            elif str(host_answer.status_code)[0] == "3":
                print(f"\r{counter:0>8} of {len(DIRS)}\t{F.BLUE + str(host_answer.status_code) + F.RESET}\t{target_url}")
            else:
                print(f"\r{counter:0>8} of {len(DIRS)}\t{host_answer.status_code}\t{target_url}")

            file.write(f"\r{counter:0>8} of {len(DIRS)}\t{host_answer.status_code}\t{target_url}\n")

    except KeyboardInterrupt:
        print(F.RED + '  ERROR: manually stop Ctrl+C' + F.RESET)
        sys.exit(0)

    lock.release()


if __name__ == "__main__":
    my_parser = argparse.ArgumentParser(description="Dir Fuzzer",
                                        usage="Script options")
    my_parser.add_argument("-u",  type=str, help="Enter domain https://site.com")
    my_parser.add_argument("-w", type=str, help="Name amd path of the wordlist")
    my_parser.add_argument("-t", type=int, help="Count threads")
    my_parser.add_argument("-e", type=str, help="Extension")
    my_parser.add_argument("-b64", action='store_true', help="Converting payload to base64")
    my_parser.add_argument("-uenc", action='store_true', help="Converting payload to urlencode")
    my_parser.add_argument("-head", type=str, help="Add http headers")
    my_args = my_parser.parse_args()

    if not my_args.w or not my_args:
        my_parser.print_help()
        sys.exit(0)

    greetings()
    check_app_keys()

    lock = multiprocessing.Lock()
    if my_args.t:
        pool = multiprocessing.Pool(my_args.t)
        for target_dir in enumerate(DIRS, start=1):
            pool.apply(get_site_dirs, args=(target_dir[1], target_dir[0]))
    else:
        for target_dir in enumerate(DIRS, start=1):
            get_site_dirs(target_dir[1], target_dir[0])

