height = int(input('Enter the height of the rhombus (must be odd number): '))
side = int((3 ** 0.5) * height)
for i in range(height):
    for j in range(side):
        if i <= height // 2 and j == side // 2 - i:
            print('* ' * (2 * i + 1), end='')
        elif (height // 2) < i and height - i - 1 == abs(j - (side // 2)):
            print('* ', end='')
        else:
            print('  ', end='')
    print()
print()