#today we are write RLE encoder
def txtencode(s):
    encoded =""
    count=1
    for i in range(1,len(s)):
        if s[i]==s[i-1]:
            count+=1
        else:
            encoded += s[i-1]+str(count)
            count=1
    encoded += s[-1]+str(count)
    return encoded
s = "aaabbbgggGGG"
s = txtencode(s)
print(s)