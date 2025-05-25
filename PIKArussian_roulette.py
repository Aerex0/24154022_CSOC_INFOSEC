import numpy as np
import random
import time




def animation():
    print("Spinning the chamber", end="")
    for _ in range(3):
        time.sleep(0.5)
        print(".", end="", flush=True)
    print()


print(r"""



 \
 /                                 />
 \__+_____________________/\/\___/ /|
 ()______________________      / /|/\
             /0 0  ---- |----    /---\
            |0 o 0 ----|| - \ --|      \
             \0_0/____/ |    |  |\      \
                         \__/__/  |      \
Bang! Bang!                       |       \
                                  |         \
                                  |__________|

      
██████╗ ██╗   ██╗███████╗███████╗██╗ █████╗ ███╗   ██╗    ██████╗  ██████╗ ██╗   ██╗██╗     ███████╗████████╗████████╗███████╗
██╔══██╗██║   ██║██╔════╝██╔════╝██║██╔══██╗████╗  ██║    ██╔══██╗██╔═══██╗██║   ██║██║     ██╔════╝╚══██╔══╝╚══██╔══╝██╔════╝
██████╔╝██║   ██║███████╗███████╗██║███████║██╔██╗ ██║    ██████╔╝██║   ██║██║   ██║██║     █████╗     ██║      ██║   █████╗  
██╔══██╗██║   ██║╚════██║╚════██║██║██╔══██║██║╚██╗██║    ██╔══██╗██║   ██║██║   ██║██║     ██╔══╝     ██║      ██║   ██╔══╝  
██║  ██║╚██████╔╝███████║███████║██║██║  ██║██║ ╚████║    ██║  ██║╚██████╔╝╚██████╔╝███████╗███████╗   ██║      ██║   ███████╗
╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝    ╚═╝  ╚═╝ ╚═════╝  ╚═════╝ ╚══════╝╚══════╝   ╚═╝      ╚═╝   ╚══════╝
                                                                                                                              
""")






n = int(input("Enter the number of players playing: "))

old_position = np.empty(n, dtype=int)

for i in range(n):
    old_position[i] = int(input(f"Enter the bullet in chamber 1,2,3,4,5,6 for player {i+1} : "))

new_position = np.empty(n, dtype=int)

for i in range(n):
    new_position[i] = random.randint(1, 6)



alive = [True] * n
round_num = 1

while alive.count(True) > 1:
    print(f"\n=== Round {round_num} ===")
    animation()
    for i in range(n):
        if not alive[i]:
            continue
        if new_position[i] == old_position[i]:
            print(f"BANG!!.. player {i} got killed")
            alive[i] = False
        else:
            print(f"CLICK.. player {i} survives")
            if(new_position[i]==6):
                new_position[i] = 1
            else:
                new_position[i] += 1

    round_num += 1

