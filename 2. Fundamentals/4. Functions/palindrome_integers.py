def palindrome_checker(num):
    if num == num[::-1]:
        print("True")
    else:
        print("False")


numbers = input().split(", ")
for number in numbers:
    palindrome_checker(number)
