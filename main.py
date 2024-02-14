import tkinter as tk
from tkinter import filedialog

# Функция для декодирования строки
def txtdecode(s):
    output = ""
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i + 1].isdigit():
            count = int(s[i + 1])
            output += count * s[i]
            i += 2
        else:
            output += s[i]
            i += 1
    return output

# Функция для кодирования строки
def txtencode(s):
    encoded = ""
    count = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            count += 1
        else:
            if count > 1:
                encoded += s[i] + str(count)
            else:
                encoded += s[i]
            count = 1
    if count > 1:
        encoded += s[-1] + str(count)
    else:
        encoded += s[-1]
    return encoded


def write_to_file(file_path, content):
    with open(file_path, 'w') as file:
        file.write(content) 
    print("Строка успешно записана в файл.")


def filework():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
            content = file.read()
    encoded_string = txtencode(content)
    write_to_file(file_path, encoded_string)

# main 

root = tk.Tk()
root.geometry(f"400x500+100+200")
root.title("Архиватор RLE 0.1")
label = tk.Label(text="encode txt or bmp file")
label.pack()
file_take_button = tk.Button(root, text="Choose file", command=filework)
file_take_button.pack()
root.mainloop()