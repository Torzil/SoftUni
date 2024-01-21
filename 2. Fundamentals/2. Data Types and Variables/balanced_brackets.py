number_of_lines = int(input())
opening_brackets = 0
closing_brackets = 0
expression_is_invalid = False
expression_is_balanced = True
last_line = ""

for line in range(number_of_lines):
    current_line = input()
    if current_line == ")" and opening_brackets == 0:
        expression_is_invalid = True
    if (last_line == "(" and current_line == "(") or (last_line == ")" and current_line == ")"):
        expression_is_invalid = True
    if current_line == "(":
        opening_brackets += 1
    if current_line == ")":
        closing_brackets += 1
    last_line = current_line

if expression_is_invalid:
    expression_is_balanced = False
elif opening_brackets == closing_brackets:
    expression_is_balanced = True

if expression_is_balanced:
    print("BALANCED")
else:
    print("UNBALANCED")
