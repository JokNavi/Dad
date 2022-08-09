LineColourHex = input('Enter hex: ').lstrip('#')
print('RGB =', tuple(int(LineColourHex[i:i+2], 16) for i in (0, 2, 4)))
