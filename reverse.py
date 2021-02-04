# matt

import sys

args = sys.argv[1:]
new_args = []
if len(args) == 0:
    print("Please enter a string!")
else:
    args.reverse()
    for a in args:
        new_args.append(a[::-1])

print("----REVERSED STRING----\n"+ (" ".join(new_args)))
