import codecs
import urllib.parse
import base64


class Convertor:
    def __init__(self):
        self.user_input_and_run()

    def user_input_and_run(self):
        print("1 - encode\n2 - decode")
        if (user_action := input("Selected action: ")) == "1":
            self.encode()
        elif user_action == "2":
            self.decode()

    def encode(self):
        user_text = input("Enter text: ")
        user_text_byt = bytes(user_text, 'utf-8')
        formats = {"BASE64": base64.b64encode(user_text_byt).decode(),
                   "BASE32": base64.b32encode(user_text_byt).decode(),
                   "BASE16": base64.b16encode(user_text_byt).decode(),
                   "URLENCODE": urllib.parse.quote(user_text),
                   "HEX": '\\' + '\\'.join(hex(ord(c))[1:] for c in user_text),
                   "ROT13": codecs.encode(user_text, 'rot_13')}

        for key, value in formats.items():
            print(f"{key:<10} ==>  {value}")

    def decode(self):
        print("Select the desired format: BASE64, BASE32, BASE16,"
              " URLENCODE, HEX, ROT13")
        user_format = input("Enter format: ")
        user_text = input("Enter text: ")
        user_text_hex = user_text.replace('\\x', '')

        formats = {"BASE64": base64.b64decode,
                   "BASE32": base64.b32decode,
                   "BASE16": base64.b16decode,
                   "URLENCODE": urllib.parse.unquote,
                   "HEX": base64.b16decode,
                   "ROT13": codecs.encode
                   }

        try:
            for key, value in formats.items():
                if key == user_format:
                    if key.startswith("BASE"):
                        print(f"{key:<10} ==>  {value(user_text).decode()}")
                    elif key == "URLENCODE":
                        print(f"{key:<10} ==>  {value(user_text)}")
                    elif key == "HEX":
                        print(
                            f"{key:<10} ==> "
                            f" {value(user_text_hex.upper()).decode()}")
                    elif key == "ROT13":
                        print(f"{key:<10} ==>  {value(user_text, 'rot_13')}")
        except Exception as e:
            print(e)


Convertor()
