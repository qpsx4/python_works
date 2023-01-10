import os
import exifread

my_dir = "photo"
my_list = os.listdir(my_dir)

for image in my_list:
    with open(f'{my_dir}/{image}', "rb") as f:
        tags = exifread.process_file(f)
        for tag in tags.keys():
            if tag == "Image DateTime" and str(tags[tag]).startswith("2019:09"):
                for all_tag in tags.keys():
                    if all_tag != "JPEGThumbnail":
                        print(f"{all_tag} {tags[all_tag]}")

