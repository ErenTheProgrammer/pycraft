menu = input('Welcome to Pycraft Alpha Demo 1.0! Do you want to start? Yes/No')
menu = menu.lower()
if menu == 'yes':
    print('Health - 10 and Hunger - 10')
    print('You spawned!')
    biome = input("There are 2 biomes close to you. One is the beach and the other the forest. Write 'forest' or 'beach'")
    biome = biome.lower()
    if biome == 'forest':
        print('Wow!,There are too many trees! You got 10 forest branchs')
        animal_kill = input('Do you want to kill a pig? It will give you 5 pork. Yes/No.')
        animal_kill = animal_kill.lower()
        if animal_kill == 'yes':
            print('You hunger is low. Hunger - 7. You ate one pork and you got Hunger - 10')
            print("A Spytho is attacking.He the final boss! Health - 8 for Spytho")
            attacking_beach = input('Should you use you Thinerx Sword? Yes/No')
            if attacking_beach == 'no':
                print('Player got killed. You got killed by a Sptho :(')
            else:
                print('You won the game!')
        else:
            print('Player got killed. You died out of hunger. :(')
            input('Press enter or any key then enter to leave.')
    else:
        print('There are cactuses, be careful!')
        print('Oops!, You touched a cactus!, Health - 9 and Hunger - 10')
        print('You got into the ocean')
        print("A Spytho is attacking.He the final boss! Health - 8 for Spytho")
        attacking_beach = input('Should you use you Thinerx Sword? Yes/No')
        if attacking_beach == 'no':
            print('Player got killed. You got killed by a Sptho :(')
        else:
            print('You won the game!')
else:
    print('Ok bye!')
