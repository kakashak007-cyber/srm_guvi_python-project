s = input("Enter a string: ")
normalized = ''.join(ch.lower() for ch in s if ch.isalnum())
if normalized == normalized[::-1]:
    print("Palindrome")
else:
    print("Not a palindrome")






















