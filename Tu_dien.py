#!/usr/bin/env python
# coding: utf-8

# In[ ]:


tu_dien = {
    "happy": "vui vẻ",

}

def print_main_menu():
    print("1. Xem thông tin từ")
    print("0. Thoát chương trình")

def input_selection():
    return input("Nhập lựa chọn của bạn: ")

BORDER_PADDING = 3 # padding 3 space characters
def print_word(dictionary, word):
    print("Thông tin của từ")
    # create border formatting
    print("=" * (len(word) + 2 + len(dictionary[word]) + BORDER_PADDING * 2 + 2))
    print("|" + ' ' * BORDER_PADDING + word + ": " + dictionary[word] + ' ' * BORDER_PADDING + '|')
    print("=" * (len(word) + 2 + len(dictionary[word]) + BORDER_PADDING * 2 + 2))

while True:
    print_main_menu()
    lua_chon = input_selection()
    if lua_chon == "0":
        print("Thoát chương trình")
        break
    elif lua_chon == "1":
        print("Bạn chọn chức năng 1")
        # Kiểm tra xem từ có chưa -> function để kiểm
        # menu con -> lặp đi lặp lại
        word = input("Nhập từ muốn xem: ")
        print_word(tu_dien, word)
    else:
        print("Không có lựa chọn này trong menu")
        print("Hãy chọn lại")		

