version = [int(num) for num in input().split(".")]
version[2] += 1
if version[2] > 9:
    version[2] = 0
    version[1] += 1
if version[1] > 9:
    version[1] = 0
    version[0] += 1
new_version = [str(string) for string in version]
print(".".join(new_version))
