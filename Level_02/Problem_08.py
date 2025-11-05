ch = input("Enter a single alphabet character: ")

if len(ch) != 1 or not ch.isalpha():
    print("Invalid input. Enter a single letter.")
else:
    c = ch.lower()
    if 'a' <= c <= 'm':
        print(f"{ch} lies between 'a' and 'm'")
    else:
        print(f"{ch} lies between 'n' and 'z'")
