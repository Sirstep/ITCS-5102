# implement a GUI: text box (1: highlight current character, or 2: space between and "hold" current char)
# use for loop to wait or find better function

d = {
    ')': '(',
    '}': '{',
    ']': '['
}
s = list(input("Please enter string of parentheses: "))
if (len(s) % 2 == 0):
    i = 0
    while len(s) != 0:
        p = s[i]
        print('\np: \'' + str(p) + '\'\ni: ' + str(i))
        print(''.join(s))
        if p in d.keys():
            if s[i-1] == d.get(p):
                del s[i-1:i+1]
                i -= 2
            else:
                print('\nResult: NO')
                break
        i += 1
    if len(s) == 0:
        print('\nResult: YES')
else:
    print('NO')
