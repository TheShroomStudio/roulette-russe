import random
import time

print("\033[2J\033[H", end="")

print("""


	 /\_/\\
	( I I )      hey!
	 (   )       bienvenue dans mon jeu!
	  | |        appuie sur entrée pour valider



""")

input()

print("\033[2J\033[H", end="")

print("""


	 /\_/\\
	( I I )      tu va jouer à un jeu très sympa!
	 (   )       ça s'appelle la roulette russe
	  | |        


""")

input()

print("\033[2J\033[H", end="")

print("""


pour commencer voicie à quoi va ressembler ton visage
	 ______
	/\/\/\/\\
	| O  O |
	|@ __ @|
	\______/

""")

input()

print("\033[2J\033[H", end="")

print("""


et voilà celui de ton adversaire
         ______
        /______\\
        | I  I |
        || -- ||
        \______/


sale geule hein?


""")


input()

print("\033[2J\033[H", end="")

print("""


         /\_/\\
        ( I I )      maintenant passons aux choses sêrieuses
         (   )       
          | |        



""")

input()

print("\033[2J\033[H", end="")

print("""

	
	
	__   ________________
	  \_/(___)     _____/
	  ( \|___|_______/
	 ( // \_(/
	 |____\     ceci est un revolver
	 ///  /     il peut contenir jusqu'à 6 munitions
	/_____\     mais ici il n'en n'aura qu'une seule


""")

input()

print("\033[2J\033[H", end="")

print("""


         /\_/\\
        ( I I )      évidemment tu ne sais pas dans quel chambre
         (   )       le but de jeu va donc être se tirer dessus à tour de rôle
          | |        jusqu'à qu'un de vous deux clamse



""")

input()

print("\033[2J\033[H", end="")

print("""


         /\_/\\
        ( I I )      j'aimerai te demander si t'as bien tout compris
         (   )       mais j'ai un peu la flemme de coder un truc pur tout redire
          | |        donc bonne chance! (ta vie en dépendra)



""")

input()

ammo = 6

true_ammo = random.randint(1,6)

print("\033[2J\033[H", end="")

while True:
	print("\033[2J\033[H", end="")
	print("ton tour:")
	print("""


		                      ______
        __   ________________        /\/\/\/\\
          \_/(___)     _____/        | O  O |
          ( \|___|_______/	     |@ __ @|
         ( // \_(/		     \______/
         |____\     		
         ///  /     		
        /_____\     		

		tirer une fois:1
		tirer deux fois:2
		fais ton choix...


""")
	print("		coups restants: " + str(ammo) + "/6")

	player_input = input()

	time.sleep(2)
	
	print("\033[2J\033[H", end="")

	print("""



                                      ______
        __   ________________        /\/\/\/\\
          \_/(___)     _____/        |O  O  |
          ( \|___|_______/           |@ __ @|
         ( // \_(/                   \______/
         |____\	
         ///  /
        /_____\	



""")

	time.sleep(2)
	
	print("\033[2J\033[H", end="")

	print("""



                                      ______
        __   ________________        /\/\/\/\\
          \_/(___)     _____/        | O  O |
          ( \|___|_______/           |@ __ @|
         ( // \_(/                   \______/
         |____\	
         ///  /
        /_____\	



""")

	time.sleep(2)

	print("\033[2J\033[H", end="")

	if player_input == "1":
		ammo -= 1
	if player_input == "2":
		ammo -= 2
	if ammo == true_ammo -1:
		print("""



                                      ______
        __   ________________        /\/\/\/\\
          \_/(___)     _____/        / X  X |
          ( \|___|_______/           |@ __ @|
         ( // \_(/                   \______/
         |____\ 
         ///  /     BANG!
        /_____\ 



""")
		time.sleep(2)

		print("\033[2J\033[H", end="")

		print("""

	 ____  ___   _    _   __    ___          __  ___
	|   | |___| | \  / | |     |   | \    / |   |___|
	| ___ |   | |  \/  | |--   |   |  \  /  |-- | \	
	|___| |   | |      | |__   |___|   \/   |__ |  \	



""")
		break
	if ammo == true_ammo -2:
		print("""


                                      ______
        __   ________________        /\/\/\/\\
          \_/(___)     _____/        / X  X |
          ( \|___|_______/           |@ __ @|
         ( // \_(/                   \______/
         |____\ 
         ///  /     BANG!
        /_____\ 



""")

		time.sleep(2)

		print("\033[2J\033[H", end="")

		print("""

         ____  ___   _    _   __    ___          __  ___
        |   | |___| | \  / | |     |   | \    / |   |___|
        | ___ |   | |  \/  | |--   |   |  \  /  |-- | \ 
        |___| |   | |      | |__   |___|   \/   |__ |  \        



""")
		break

	print("""



                                      ______
        __   ________________        /\/\/\/\\
          \_/(___)     _____/        | 0  0 |
          ( \|___|_______/           |@ __ @|
         ( // \_(/                   \______/
         |____\ 
         ///  /     click!
        /_____\	 



""")

	time.sleep(2)

	print("\033[2J\033[H", end="")


	if player_input == "quit":
		break

	print("tour de l'adversaire")

	time.sleep(2)

	print("""


                                      ______
        __   ________________        /______\\
          \_/(___)     _____/        | I  I |
          ( \|___|_______/           || -- ||
         ( // \_(/                   \______/
         |____\ 
         ///  /
        /_____\ 



""")

	time.sleep(2)

	print("\033[2J\033[H", end="")

	print("""



                                      ______
        __   ________________        /______\\
          \_/(___)     _____/        |I  I  |
          ( \|___|_______/           || -- ||
         ( // \_(/                   \______/
         |____\ 
         ///  /
        /_____\ 



""")
	
	time.sleep(2)

	print("\033[2J\033[H", end="")

	print("""



                                      ______
        __   ________________        /______\\
          \_/(___)     _____/        | I  I |
          ( \|___|_______/           || -- ||
         ( // \_(/                   \______/
         |____\ 
         ///  /
        /_____\ 



""")

	time.sleep(2)

	print("\033[2J\033[H", end="")

	ammo -= 1
	if ammo ==true_ammo -1:
		print("""



                                      ______
        __   ________________        /______\\
          \_/(___)     _____/        / X  X |
          ( \|___|_______/           || -- ||
         ( // \_(/                   \______/
         |____\ 
         ///  /     BANG!
        /_____\ 



""")

		time.sleep(2)

		print("\033[2J\033[H", end="")

		print("""

           ____  ____
       !  |   | |   |  !
       !  | ___ | ___  !
       !  |___| |___|  !

	merci d'avoir joué!

""")

		break
	print("""



                                      ______
        __   ________________        /______\\
          \_/(___)     _____/        | =  = |
          ( \|___|_______/           || -- ||
         ( // \_(/                   \______/
         |____\ 
         ///  /     click!
        /_____\ 



""")

	time.sleep(2)

