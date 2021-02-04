# matt
# type 'python reverse.py STRING' and this will reverse that string
import sys

args = sys.argv[1:]
new_args = []
if len(args) == 0:
    print("Please enter a string!")
else:
    args.reverse()
    for a in args:
        new_args.append(a[::-1])

print("----Reversed String----\n"+ (" ".join(new_args)))
