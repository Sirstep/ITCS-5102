def countWords():
    file = input('Enter text file destination, name, and extension: ')
    text = open(file, 'r', encoding="utf-8-sig")
    open(input('Enter new text file destination, name, and extension: '), 'w').write(str(len(text.read().split())))
    return "Words counted and file created."

print(countWords())