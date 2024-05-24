is_palindrome
def is_palindrome(p):
    return p == p[::-1]
a = input("Input a text:")
if is_palindrome(a):
    print("This is a palindrome.")
else :
    print("This is not a palindrome.")