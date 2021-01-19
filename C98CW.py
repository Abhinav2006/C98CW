def countWords():
    filename = input("Enter File name")
    file = open(filename, 'r')
    wordCount = 0
    characterCount = 0
    for i in file:
        words = i.split()
    print(len(words))
countWords()