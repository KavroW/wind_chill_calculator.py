t = float(input('Enter the temperature in Fahreneit be tween -58 and 41: '))
v = float(input('Enter the wind speed miles per hour (must be >= 2): '))
wc = 35.74 + (0.6215*t) - (35.75*(v**0.16)) + (0.4275*(t)*(v**0.16))
print(f'The wind chill index is {wc:.2f}')
