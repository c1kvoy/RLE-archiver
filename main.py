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

s = input("Введите строку для кодирования: ")
encoded_string = txtencode(s)
print("Закодированная строка:", encoded_string)
decoded_string = txtdecode(encoded_string)
print("Декодированная строка:", decoded_string)
