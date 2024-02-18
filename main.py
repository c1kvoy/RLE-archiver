from tkinter import *
from tkinter import filedialog

# Функция для декодирования строки
def txtdecode(s):
    output = ""
    i = 0
    while i < len(s):
        if i < len(s) - 1 and s[i + 1].isdigit():
            count = ""
            j = i + 1
            while j < len(s) and s[j].isdigit(): 
                count += s[j]
                j += 1
            output += int(count) * s[i]
            i = j
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

def filewritting_encodedstr():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        content = file.read()
    encoded_string = txtencode(content)
    file_path = filedialog.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")),
        defaultextension=".txt"
        )
    
    with open(file_path, 'w') as file:
        file.write(encoded_string) 
    print("Строка успешно записана в файл.")

def filewritting_decodedstr():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        content = file.read()
    dencoded_string = txtdecode(content)
    file_path = filedialog.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("All files", "*.*")),
        defaultextension=".txt"
        )
    print(file_path)

    with open(file_path, 'w') as file:
        file.write(dencoded_string) 
    print("Строка успешно расшифрована в файл.")

# main

root = Tk()
root.geometry("400x500+100+200")
root.title("Архиватор RLE 0.1")

labelencode = Label(text="encode txt or bmp file", background="#FFCDD2",font='Times 30',bg='grey')  # Указываем родителя
labelencode.pack()

compressbutton = Button(text="Choose file", command=filewritting_encodedstr)
compressbutton.pack()

labeldecode = Label(text="decode txt or bmp file", background="#FFCDD2",font='Times 30',bg='grey')  # Указываем родителя
labeldecode.pack()

decompressbutton = Button(text="Choose file", command=filewritting_decodedstr)
decompressbutton.pack()

root.mainloop()
