import os
import glob


def delete_given_file(image_name):

    file_name = image_name.split(".")[0]
    IMG_PATH = "./annotated_dataset/img"
    TXT_PATH = "./annotated_dataset/txt_label"
    XML_PATH = "./annotated_dataset/xml_label"

    img_file = f"{IMG_PATH}/{file_name}.jpg"
    txt_file = f"{TXT_PATH}/{file_name}.txt"
    xml_file = f"{XML_PATH}/{file_name}.xml"

    files_list = [img_file, txt_file, xml_file]
    int_files = len(files_list)
    try:
        for item in files_list:
            os.remove(item)
        if int_files == 3:
            print(f"removed {int_files} file of {file_name}")
    except:
        print(f"FAIL: removing {file_name} failed")


# delete_given_file("naver_0074.jpg")
removable_file_list = [
    "naver_0074.jpg",
    "naver_0341.jpg",
    "naver_0339.jpg",
    "naver_0325.jpg",
    "naver_0040.jpg",
    "naver_0000_duplicate.jpg",
    "naver_0318.jpg",
    "naver_0271.jpg",
    "naver_0234.jpg",
]

for file_item in removable_file_list:
    delete_given_file(file_item)
