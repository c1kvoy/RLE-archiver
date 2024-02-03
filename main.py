#today we are write RLE encoder
def txtdecode(s):
    output = ""
    i = 0
    while i < len(s)-1:
        if s[i+1].isdigit():
            count = int(s[i+1])
            output += count * s[i]
            i += 2
        else:
            output += s[i]
            i += 1
    return output
def txtencode(s):
    encoded =""
    count=1
    for i in range(0,len(s)-1):
        if s[i]==s[i-1]:
            count+=1
        else:
            encoded += s[i-1]+str(count)
            count=1
    encoded += s[-1]+str(count)
    return encoded
s = "aaaaaakkkkk"
s = txtencode(s)
print(s)
decodestring = txtdecode(s)
print(decodestring)