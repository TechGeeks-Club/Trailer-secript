from tqdm import tqdm
from time import sleep
import os
import readchar


if os.name == "nt":
    command = "cls"
else:
    command = "clear"

def question():
    yes_colore = 37
    no_colore  = 44
    
    while (1):
        os.system(f'{command}')

        print("\n"*14)
        print("                          \033[34m      __   ___         __      \033[0m           ___  ___  __   ___  __  ___  ___  __             \033[31m        \033[0m       __   /")
        print("                          \033[34m /\  |__) |__     \ / /  \ |  |\033[0m    | |\ |  |  |__  |__) |__  /__`  |  |__  |  \    | |\ |  \033[31m   /\  |\033[0m        _| / ")
        print("                          \033[34m/~~\ |  \ |___     |  \__/ \__/\033[0m    | | \|  |  |___ |  \ |___ .__/  |  |___ |__/    | | \|  \033[31m  /~~\ |\033[0m ...    . .  ")
                                                                                                                
        print("\n\n")
        print(f"                                                                         \033[{yes_colore}m╦ ╦┌─┐┌─┐\033[0m")
        print(f"                                                                         \033[{yes_colore}m╚╦╝├┤ └─┐\033[0m")
        print(f"                                                                         \033[{yes_colore}m ╩ └─┘└─┘\033[0m")
        # print("\n")
        print(f"                                                                         \033[{no_colore}m ╔╗╔┌─┐ \033[0m")
        print(f"                                                                         \033[{no_colore}m ║║║│ │ \033[0m")
        print(f"                                                                         \033[{no_colore}m ╝╚╝└─┘ \033[0m")   

        key = readchar.readkey()
        if key == readchar.key.ENTER:
            break
        elif key == readchar.key.UP or key == readchar.key.DOWN :
            temp       = yes_colore
            yes_colore = no_colore
            no_colore  =temp


os.system(f'{command}')
print("\n"*11)

print("\033[31m                                          .:dkO0KK0l       \033[34m.xNKkl,.                             .:dOXx.      \033[31m.cOOOOOkd:.           ")
print("\033[31m                                       .:x0NWMMMMMMx.      \033[34m.xMMMWXOo,.                       .cx0NWMMk.      \033[31m.xMMMMMMWN0d;.        ")
print("\033[31m                                      ;OWMMMMMMMMMMx.      \033[34m.dWMMMMMMN0l.                  .;xXWMMMMMMk.      \033[31m.xMMMMMMMMMMNk;       ")
print("\033[31m                                     lNMMMMWXOxoooo;       \033[34m .;cd0NMMMMWKo'              .:ONMMMMWXko:'       \033[31m ;oddddkXWMMMMXc      ")
print("\033[31m                                    ,KMMMMNd'                   \033[34m.,oKWMMMWXd'          .:OWMMMMNk:.                 \033[31m  .xNMMMMK,     ")
print("\033[31m                                    lNMMMMk.  \033[0m      .;:::;'.    \033[34m   .oKWMMMMXx,      .cOWMMMMNk,   \033[0m     .',,'.      \033[31m   .kMMMMNc     ")
print("\033[31m                                   'OMMMMWo   \033[0m   .lOXWMMMWN0o'  \033[34m     .l0WMMMMXx,  .cOWMMMMNk;     \033[0m  .lOXNWWNXOo'   \033[31m    oWMMMMk.    ")
print("\033[31m                               ..'l0WMMMM0,   \033[0m  ;0WMXklclxKWMKc \033[34m       .c0WMMMMXOk0WMMMMNk;       \033[0m cKWWXkooxKWMXl. \033[31m    ,0MMMMW0l'..")
print("\033[31m                               KXNWMMMMW0,    \033[0m '0MWO,     .xWMK;\033[34m         .c0WMMMMMMMMMNx,         \033[0m;XMWx'    .dNMNc \033[31m     ,OWMMMMMNXK")
print("\033[31m                               MMMMMMMMK;     \033[0m :XMNc       ;XMWl\033[34m           ;0WMMMMMMMNd.          \033[0mlWMX;      '0MWd \033[31m      ;KMMMMMMMM")
print("\033[31m                               XXWMMMMMWO'    \033[0m '0MWO'     .xWMK;\033[34m         .c0WMMMMMMMMMXd'         \033[0m;XMWx'    .oNMNc \033[31m     ,OWMMMMMWNX")
print("\033[31m                               ..,o0WMMMM0'   \033[0m  ;0WWXxlccdKWMXc \033[34m       .c0WMMMMNOk0WMMMMXx,       \033[0m cKMWXxooxKWMXl. \033[31m    '0MMMMWKl,..")
print("\033[31m                                   .OMMMMWo   \033[0m   .lONWMMMWNKd'  \033[34m     .c0WMMMMXx,  .c0WMMMMXx,     \033[0m  'oOXWWWWN0o'   \033[31m    oWMMMM0,    ")
print("\033[31m                                    lWMMMMk.  \033[0m     .';ccc:'.    \033[34m   .l0WMMMMXd'      .c0WMMMMXd'   \033[0m     .,;;,..     \033[31m   .kMMMMWl     ")
print("\033[31m                                    ,KMMMMNd.                   \033[34m 'l0WMMMMXd'          .c0WMMMMXx;.                 \033[31m  .dNMMMMK;     ")
print("\033[31m                                     lXMMMMWKxooooo;       \033[34m .,:oONMMMMMXo'              .cOWMMMMW0xc;.       \033[31m ,lllodkKWMMMMNl.     ")
print("\033[31m                                      ;OWMMMMMMMMMMx.      \033[34m.dWMMMMMMW0l.                  .:kXMMMMMMWx.      \033[31m.xMMMMMMMMMMW0:       ")
print("\033[31m                                       .:xKNMMMMMMMx.      \033[34m.xMMMWXOo;.                       'ckKNMMMk.      \033[31m.xMMMMMMMWXk:.        ")
print("\033[31m                                          'cx0KKKKKl.      \033[34m.xWXOo,.                             'cxKNk.      \033[31m.lKKKKK0xl'           ")

sleep(5)

os.system(f'{command}')
print("\n\n\n\n\n\n\n")

print("\033[31m                           ███████████                   █████                   █████████                    █████             \033[0m")
print("\033[31m                          ░█░░░███░░░█                  ░░███                   ███░░░░░███                  ░░███              \033[0m")
print("\033[31m                          ░   ░███  ░   ██████   ██████  ░███████              ███     ░░░   ██████   ██████  ░███ █████  █████ \033[0m")
print("\033[31m                              ░███     ███░░███ ███░░███ ░███░░███  ██████████░███          ███░░███ ███░░███ ░███░░███  ███░░  \033[0m")
print("\033[31m                              ░███    ░███████ ░███ ░░░  ░███ ░███ ░░░░░░░░░░ ░███    █████░███████ ░███████  ░██████░  ░░█████ \033[0m")
print("\033[31m                              ░███    ░███░░░  ░███  ███ ░███ ░███            ░░███  ░░███ ░███░░░  ░███░░░   ░███░░███  ░░░░███\033[0m")
print("\033[31m                              █████   ░░██████ ░░██████  ████ █████            ░░█████████ ░░██████ ░░██████  ████ █████ ██████ \033[0m")
print("\033[31m                             ░░░░░     ░░░░░░   ░░░░░░  ░░░░ ░░░░░              ░░░░░░░░░   ░░░░░░   ░░░░░░  ░░░░ ░░░░░ ░░░░░░  \033[0m")

print("\033[34m                                                ______           __   \033[0m")
print("\033[34m                                               / ____/_  _____  / /___ ___  ____ _      __  ______  (_)   __                    \033[0m")
print("\033[34m                                              / / __/ / / / _ \/ / __ `__ \/ __ `/_____/ / / / __ \/ / | / /                    \033[0m")
print("\033[34m                                             / /_/ / /_/ /  __/ / / / / / / /_/ /_____/ /_/ / / / / /| |/ /                     \033[0m")
print("\033[34m                                             \____/\__,_/\___/_/_/ /_/ /_/\__,_/      \__,_/_/ /_/_/ |___/                      \033[0m")
sleep(1 )

print("\n"*5)
for i in tqdm(range(100), bar_format="                                                  {l_bar}{bar}", desc="\033[91mLoading...\033[0m", position=0, leave=True, ncols=100):
    sleep(0.05)  
    
sleep(0.1)     
os.system(f'{command}')

question()

os.system(f'{command}')
print("\n"*11)

sleep(0.5)
print("\033[31m                                                     █████████   █████            ██████████                       ")
print("\033[31m                                                    ███░░░░░███ ░░███            ░░███░░░░███                      ")
print("\033[31m                                                   ░███    ░███  ░███             ░███   ░░███  ██████   █████ ████")
print("\033[31m                                                   ░███████████  ░███  ██████████ ░███    ░███ ░░░░░███ ░░███ ░███ ")
print("\033[31m                                                   ░███░░░░░███  ░███ ░░░░░░░░░░  ░███    ░███  ███████  ░███ ░███ ")
print("\033[31m                                                   ░███    ░███  ░███             ░███    ███  ███░░███  ░███ ░███ ")
print("\033[31m                                                   █████   █████ █████            ██████████  ░░████████ ░░███████ ")
print("\033[31m                                                  ░░░░░   ░░░░░ ░░░░░            ░░░░░░░░░░    ░░░░░░░░   ░░░░░███ ")
print("\033[31m                                                                                                          ███ ░███ ")
print("\033[31m                                                                                                         ░░██████  ")
print("\033[31m                                                                                                          ░░░░░░   ")
sleep(1)  

print("\033[34m                                                                   _                    _   _  _      \033[0m") 
print("\033[34m                                                               /| |_     /\  ._  ._ |    ) / \  ) |_|_\033[0m") 
print("\033[34m                                                                |  _) o /--\ |_) |  | o /_ \_/ /_   | \033[0m") 
print("\033[34m                                                                             |\033[0m") 

sleep(1.5)                                 


print("\n\n ")
print("                                                             \033[33mAI DAY:\033[0m WHERE INTELLIGENCE MEETS INNOVATION.")
print("                      Explore cutting-edge advancements, engage with experts, and discover how Al can empower individuals and communities to thrive")
print("                                                           We are looking forward to see you on \033[32mApril 15,2024\033[0m...")
print("\n"*4)
print("                                                                       © 2011/2024 Tech-Geeks")
input()

os.system(f'{command}')
print("\n"*17)

print("\033[34m                                              ______         ____          ______                 _                      __     \033[0m")    
print("\033[34m                                             /_  __/___     / __ )___     / ____/___  ____  _____(_)___  __  _____  ____/ /     \033[0m")    
print("\033[34m                                              / / / __ \   / __  / _ \   / /   / __ \/ __ \/ ___/ / __ \/ / / / _ \/ __  /      \033[0m")    
print("\033[34m                                             / / / /_/ /  / /_/ /  __/  / /___/ /_/ / / / / /  / / / / / /_/ /  __/ /_/ / _ _   \033[0m")    
print("\033[34m                                            /_/  \____/  /_____/\___/   \____/\____/_/ /_/_/  /_/_/ /_/\__,_/\___/\__,_(_|_|_)  \033[0m") 
sleep(2)
os.system(f'{command}')
os.system("cmatrix -C green")
