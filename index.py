def encrypt(string):
    i = 0
    result = ''
    while i < len(string):
        result = result + string[i:i+2][::-1]
        i = i + 2
    return result

# Проверка

string = 'abcdef'
print(encrypt(string))