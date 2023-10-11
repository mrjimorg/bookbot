filename = "books/frankenstein.txt"
with open(filename) as f:
    file_contents = f.read()
    words = file_contents.split()
    print(f"Length of book = {len(words)} words")
    lower_file_contents = file_contents.lower()
    chars = {}
    for a in lower_file_contents:
        if a not in chars:
            chars[a] = 0
        chars[a] += 1
    print("After " + str(chars))
    for a in chars.keys():
        if(a.isalpha()):
            print(f"The '{a}' character was found {chars[a]} times")