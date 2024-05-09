
import customtkinter
from customtkinter import filedialog
from PIL import Image
# Функция для декодирования строки
def txtdecode(encoded_str):
    decoded_str = ''
    i = 0
    while i < len(encoded_str):
        char = encoded_str[i]
        while (i + 1 < len(encoded_str) and encoded_str[i + 1] != "⁊" or i == len(encoded_str)):
            decoded_str += char
            i += 1
            char = encoded_str[i]
        i += 2
        count = ''
        while i < len(encoded_str) and encoded_str[i].isdigit():
            count += encoded_str[i]
            i += 1
        if count:
            decoded_str += char * int(count)
        if i < len(encoded_str) and encoded_str[i] == '⁊':
            i += 1
    decoded_str+=char
    return decoded_str

# Функция для кодирования строки
def txtencode(s):
    encoded = ""
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
        else:
            if count > 1:
                if s[i].isdigit():
                    encoded += s[i] + "⁊" + str(count) + "⁊"
                else:
                    encoded += s[i] + str(count)
            else:
                encoded += s[i]
            count = 1
    if count > 1:
        if s[-1].isdigit():
            encoded +=s[-1] + "⁊" + str(count) + "⁊"
        else:
            encoded += s[-1] + str(count)
    else:
        encoded += s[-1]
    return encoded

def get_resolution(data):
    height = ""
    width = ""
    i = len(data)-2
    data = data[:-1]
    while data[i]!='|':
        width = data[i] + width
        i+=-1
        data = data[:-1]
    i-=1
    while data[i]!='|':
        height = data[i] + height
        i+=-1
        data = data[:-1]
    data = data[:-2]
    return width,height,data
def bmp_to_bit(path):
    image = Image.open(path).convert("1")
    pixels = list(image.getdata())
    bit_string = ""
    for pixel in pixels:
        bit_string += "1" if pixel == 255 else "0"
    char = bit_string[-1]
    while bit_string[len(bit_string)-1] == char:
        bit_string=bit_string[:-1]
    return bit_string

def bit_to_bmp(bit_string, width, height):
    image = Image.new("1", (width, height))
    pixels = list(image.getdata())
    bits = [int(bit) for bit in bit_string]
    for i, bit in enumerate(bits):
        pixels[i] = 255 if bit == 1 else 0
    image.putdata(pixels)
    return image

def filewritting_encodedstr():
    file_path = filedialog.askopenfilename()
    extension = file_path.split(".")

    if extension[-1] == "txt":
        with open(file_path, 'r') as file:
            content = file.read()
        encoded_string = txtencode(content)
    elif extension[-1] == "bmp":
        bit_string = bmp_to_bit(file_path)
        encoded_string = txtencode(bit_string)
        image = Image.open(file_path)
        width, height = image.size
        encoded_string += "|"+ str(width) + "|"+ str(height) + "|"

    file_path = filedialog.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("RLE files", "*.rle"),
                   ("All files", "*.*")),
        defaultextension=".rle"
    )

    with open(file_path, 'w') as file:
        file.write(encoded_string)
    print("Строка успешно записана в файл.")

def filewritting_decodedstr():
    file_path = filedialog.askopenfilename()
    with open(file_path, 'r') as file:
        content = file.read()

    file_path = filedialog.asksaveasfilename(
        filetypes=(("TXT files", "*.txt"),
                   ("HTML files", "*.html;*.htm"),
                   ("BMP files", "*.bmp"),
                   ("All files", "*.*")),
        defaultextension=".txt"
    )
    extension = file_path.split(".")
    if extension[-1] == "bmp":
        width, height, content = get_resolution(content)
        width = int(width)
        height = int(height)
        decoded_string = txtdecode(content)
        image = bit_to_bmp(decoded_string,height,width)
        image.save(file_path)
    else:
        decoded_string = txtdecode(content)
        with open(file_path, 'w') as file:
            file.write(decoded_string)
    print("Строка успешно расшифрована в файл.")



root = customtkinter.CTk()
root.geometry("400x500+100+200")
root.title("Архиватор RLE 0.1")

labelencode = customtkinter.CTkLabel(master=root, text="ENCODE BMP OR TXT FILE")  # Указываем родителя
labelencode.pack()

compressbutton = customtkinter.CTkButton(master=root, text="Choose file", command=filewritting_encodedstr)
compressbutton.pack()

labeldecode = customtkinter.CTkLabel(master=root, text="DECODE RLE FILE")
labeldecode.pack()

decompressbutton = customtkinter.CTkButton(master=root, text="Choose file", command=filewritting_decodedstr)
decompressbutton.pack()
path_icon = "Main_icon.png"
root.iconbitmap(path_icon)
root.mainloop()
