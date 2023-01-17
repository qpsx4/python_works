![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

<h1 align="center">Всем привет, вы находитесь на страничке моего проекта <img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>

[![Typing SVG](https://readme-typing-svg.herokuapp.com?color=%23F7F6F7&lines=Приятного+просмотра+:%29)](https://git.io/typing-svg)


<h3>В данном проекте я собрал некоторые примеры своих работ, написанных во время учебы в Codeby:</h3>

---

<h3> 1. bruteforce_zip_example.py </h3>

У нас есть архив secure.zip и по имеющимся сведениям, пароль архива
o_main_got***** в котором последние 5 знаков это цифры.
Скрипт, используя прогрессбар, подбирает пароль и 
вытаскивает содержимое архива.

---

<h3>2. chiper.py</h3>

Шифр замены на китайские иероглифы. 
Заменяются латинские буквы обоих регистров и пробел. Остальные символы игнорируются.

---

<h3>3. convertor_payloads.py</h3>

Конвертор, который делает преобразование сразу в несколько 
форматов при кодировании, а при декодировании на выбор.

---

<h3>4. exif.py</h3>

Есть группа снимков, которые находятся в папке photo.
Скрипт найдёт фото, сделанное в сентябре 2019 года, и выведет метаданные в консоль.

---

<h3>5. fuzzer.py</h3>

Фаззер, использующий многопоточность.
Есть возможность указывать расширения файлов, путь до словаря, кодировать полезную нагрузку.

---

<h3>6. gen_bruteforce_list.py</h3>

Скрипт, в котором можно выбрать генерацию словаря, используя следующие опции:

B - большие буквы
L - маленькие буквы
S – спецсимволы
N – числа

Пользователь может выбрать любое сочетание этих опций, или одну из них для 
генерации словаря. Сгенерированный словарь запишется в файл gen_dict.txt.
Пользователь может вводить имя опции в любом регистре.

---

<h3>7. osint_box_ser-1.0.zip</h3>

Фреймворк для осинта:
  1. Определение IP сайта
  2. Поиск по IP таких данных как страна, координаты, часовой пояс, название 
  континета, города, кода страны и т.п.
  3. Данные whois домена
  4. Данные nslookup домена
  5. DNS MX-Record
  6. Reverse DNS
  7. Содержимое файла robots.txt при его наличии
  8. Содержимое файла sitemap.xml при его наличии
  9. Reverse ip lookup
  10. Все пункты одновременно

---

<h3>8. parser_example.py</h3> 

Пример парсера, который спарсит с http://foxtools.ru/Proxy адреса прокси со всех страниц и выведет их в консоль.

---

<h3>9. scaner.py</h3> 

Многопоточный сканер портов. 
Сканер принимает на вход любой диапазон IP-адресов и сканирует их 
на наличие открытых портов следующего ряда:
43, 80, 109, 110, 115, 118, 119, 143, 194, 220, 443, 540, 585, 591, 1112, 1433, 1443, 
3128, 3197, 3306, 3899, 4224, 4444, 5000, 5432, 6379, 8000, 8080, 10000

---

<h3>10. cryptographer-1.5.zip</h3>

Дипломная работа. Фреймворк по шифрам. 

Программа cryptographer.py, которая шифрует/хэширует введённый пользователем текст согласно следующим пунктам на выбор:

1. BASE64
2. BASE32
3. BASE16
4. HEX
5. URLENCODE
6. ROT13 
7. MD5 
8. SHA-1 
9. SHA-256
10. SHA-512
11. All items

Работа программы выполняется в бесконечном цикле, пока не будет введён ноль.
При выборе пункта All items шифрование делается во всех 10 вариантах,
но результат записывается в файл res_ciphers.txt, а в консоль выводится "Done!".

Собран установочный переносимый пакет в формате zip.
Пакет предназначен для установки в систему, а также для дальнейшего импорта пользователем в свои программы.
В пакет входят: файл readme.md с примером подключения импорта модулей, файл requirements.txt и др.

---
