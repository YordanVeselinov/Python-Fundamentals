electrons = int(input())
shell = []

for current_shell in range(1, electrons+1):
    maximum_shell_power = 2 * current_shell ** 2
    if electrons > maximum_shell_power:
        shell.append(maximum_shell_power)
        electrons -= maximum_shell_power
    else:
        shell.append(electrons)
        break
print(shell)
