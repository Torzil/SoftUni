all_strings = input().split()
set_palindrome = input()


def palindrome_finder():
    palindromes = [string for string in all_strings if string == string[::-1]]
    given_palindromes_found = palindromes.count(set_palindrome)
    print(palindromes)
    print(f"Found palindrome {given_palindromes_found} times")


palindrome_finder()
