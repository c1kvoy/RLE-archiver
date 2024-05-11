import customtkinter
from customtkinter import filedialog
from PIL import Image
# Функция для декодирования строки
def bmp_encode(pixels):
    result = ""
    for row in pixels:
        for i in range(3):
            result += f"{row[i]:02X}"
        result += " "
    results = result[:-1]
    results = results.split(' ')
    count = 1
    flag = 1
    encoded_string = ""
    for i in range(len(results)-1):
        if results[i] == results[i+1]:
            count+=1
        else:
            encoded_string+=str(count)+'x'+results[i]+' '
            flag = 0
            count = 1
    encoded_string += str(count) + 'x' + results[-1]
    return encoded_string

def bmp_decode(encoded_string):
    colors = []
    encoded_string = encoded_string.split(' ')
    for i in range(len(encoded_string)):
        count = ""
        for j in range(len(encoded_string[i])):
            if encoded_string[i][j]!='x':
                count += encoded_string[i][j]
            else:
                break
        encoded_string[i] = encoded_string[i][len(count)+1:]
        t = 1
        for t in range(int(count)):
            decimal_value = int(encoded_string[i], 16)
            r = decimal_value >> 16
            g = (decimal_value >> 8) & 0xFF
            b = decimal_value & 0xFF
            colors.append((r, g, b))
    return colors
def txtdecode(s):
    decoded_str = ""
    i = 0
    while i < len(s):
        char = s[i]
        j = i + 2
        count = ''
        while s[j] != ' ':
            count += s[j]
            j += 1
        decoded_str += char * int(count)
        i = j + 1
    return decoded_str

# Функция для кодирования строки
def txtencode(s):
    i, count = 1, 1
    encoded_str = ""

    while i < len(s):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_str += s[i - 1] + " " + str(count) + " "
            count = 1
        i += 1

    encoded_str += s[i - 1] + " " + str(count) + " "

    return encoded_str

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

def filewritting_encodedstr():
    file_path = filedialog.askopenfilename()
    extension = file_path.split(".")

    if extension[-1] == "txt":
        with open(file_path, 'r') as file:
            content = file.read()
        encoded_string = txtencode(content)
    elif extension[-1] == "bmp":
        image = Image.open(file_path)
        image = image.convert("RGB")
        pixels = list(image.getdata())
        encoded_string = bmp_encode(pixels)
        width, height = image.size
        encoded_string += "|"+ str(width) + "|"+ str(height) + "|"

    file_path = filedialog.asksaveasfilename(
        filetypes=(("RLE files", "*.rle"),
                   ("HTML files", "*.html;*.htm"),
                   ("TXT files", "*.txt"),
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
        pixels = bmp_decode(content)
        image = Image.new("RGB", (width, height))
        image.putdata(pixels)
        image.save(file_path)
    else:
        decoded_string = txtdecode(content)
        with open(file_path, 'w') as file:
            file.write(decoded_string)
    print("Строка успешно расшифрована в файл.")



root = customtkinter.CTk()
root.geometry("400x500+100+200")
root.title("Архиватор RLE 0.1")

labelencode = customtkinter.CTkLabel(master=root, text="ENCODE BMP OR TXT FILE")
labelencode.pack()

compressbutton = customtkinter.CTkButton(master=root, text="Choose file", command=filewritting_encodedstr)
compressbutton.pack()

labeldecode = customtkinter.CTkLabel(master=root, text="DECODE RLE FILE")
labeldecode.pack()

decompressbutton = customtkinter.CTkButton(master=root, text="Choose file", command=filewritting_decodedstr)
decompressbutton.pack()

root.mainloop()
