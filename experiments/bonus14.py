from experiments.bonus14functions import parse, convert

feet_inches = input("Enter feet and inches: ")

f,i = parse(feet_inches)
result = convert(f, i)
print(f"{result} m")

if result < 1 :
    print('Kid is too small.')
else:
    print('Kid can use the slide.')
