# A script I wrote to scramble my email address for my website.
# 
# Author: Avneesh Mishra
# License: MIT License
# 

import random
import sys

real_email = sys.argv[1]
print(f"Encoding {real_email = }")
scr_pos = list(range(len(real_email)))
random.shuffle(scr_pos)
print(f"Scrambled positions: {scr_pos}")
print("Scrambled email: ", end="")
for i in scr_pos:
    print(real_email[i], end="")
print()
