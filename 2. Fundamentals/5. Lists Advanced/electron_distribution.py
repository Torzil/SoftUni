def shell_stuffer(electrons):
    shells_list = []
    current_shell = 1
    while True:
        if electrons == 0:
            break
        current_electrons = 2 * current_shell ** 2
        if electrons < current_electrons:
            shells_list.append(electrons)
            break
        shells_list.append(current_electrons)
        electrons -= current_electrons
        current_shell += 1
    return shells_list


total_electrons = int(input())

print(shell_stuffer(total_electrons))
