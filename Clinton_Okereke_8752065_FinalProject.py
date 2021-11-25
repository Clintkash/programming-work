import random
score = 0

#Hero classes for the game.
class warrior (object):
    health = 10
    defence = 40
    strength = 25
    magic = 10

class elf (object):
    health = 75
    defence = 30
    strength = 15
    magic = 70

class wizard (object):
    health = 70
    defence = 20
    strength = 10
    magic = 75



#enemy classes

class goblin(object):
    name = 'Goblin'
    health = 50
    defence = 20
    strength = 10
    loot = random.randint(0,3)

class wolf(object):
    name = 'Wolf'
    health = 60
    defence = 20
    strength = 25
    loot = random.randint(0,3)

class orc(object):
    name = 'Orc'
    health = 70
    defence = 30
    strength = 40
    loot = random.randint(0,3)

class bat (object):
    name = 'Bat'
    health = 15
    defence = 5
    strength = 10
    loot = random.randint(0,3)

class beast (object):
    name = 'Beast'
    health = 75
    defence = 35
    strength = 50
    loot = random.randint(0,3)

#GAME OVER FUNCTION PHEW :)
def gameover(character,score):
    if character.health <1:
        print('Thanks for playing')
        print ('GAME OVER!!!')
        print ('YOU HAVE SCORED........', score)
        exit ()

#HERO SELECTION
def selecthero():
    print('SELECT YOUR HERO!!')
    selection= input('1. Warrior. \n2. Elf. \n3. Wizard.\n')
    if selection == '1':
        character=warrior
        print('YOU HAVE SELECTED A WARRIOR BELOW ARE THEIR ATTRIBUTES, AND GOODLUCK :) ')
        print('Health - ', character.health)
        print('Defence - ', character.defence)
        print('Strength - ', character.strength)
        print('Magic - ', character.magic)
        return character
    elif selection == '2':
        character=elf
        print('YOU HAVE SELECTED AN ELF BELOW ARE THEIR ATTRIBUTES, AND GOODLUCK :) ')
        print('Health - ', character.health)
        print('Defence - ', character.defence)
        print('Strength - ', character.strength)
        print('Magic - ', character.magic)
        return character

    elif selection == '3':
        character=wizard
        print('YOU HAVE SELECTED A WIZARD BELOW ARE THEIR ATTRIBUTES, AND GOODLUCK :) ')
        print('Health - ', character.health)
        print('Defence - ', character.defence)
        print('Strength - ', character.strength)
        print('Magic - ', character.magic)
        return character
    else:
        print('ERROR!!!! PLEASE ENTER ONLY 1,2 OR 3 :) ')
        selecthero()
#ENEMY SELECTION IS BY RANDOM
def selectenemy(goblin, wolf, orc, bat, beast):
    listofenemies=[goblin, wolf, orc, bat, beast]
    chance= random.randint(0,4)
    enemy=listofenemies[chance]
    return enemy

def loot():
    loot=['Healthpotion', 'Strengthpotion', 'Shield',]
    lootchance= random.randint(0,2)
    lootdrop=loot[lootchance]
    return lootdrop

def lootEffect(lootdrop,character):
    if lootdrop == 'Healthpotion':
        character.health = character.health + 10
        print('YOU PICKED UP THE HEALTH POTION, INCREASING YOUR HEALTH BY 1O!! :)')
        print("YOUR HEALTH IS NOW ", character.health)
        return character

    elif lootdrop == 'Strengthpotion':
        character.strength = character.strength + 8
        print('YOU PICKED UP THE STRENGTH POTION, INCREASING YOUR STRENGTH BY 8!! :)')
        print("YOUR STRENGTH IS NOW ", character.strength)
        return character

    elif lootdrop == 'Shield':
        character.defence = character.defence + 5
        print('YOU PICKED UP A SHIELD, INCREASING YOUR DEFENCE BY 5!! :)')
        print("YOUR DEFENCE IS NOW ", character.defence)
        return character

    elif lootdrop == 'NOTHING':
        print('OPPS IT IS AN EMPTY BAG BETTER LUCK NEXT TIME .')




#BATTLE STATE
def battle(score):
    enemy=selectenemy(goblin, wolf, orc, bat, beast)
    print("A DANGEROUS", enemy.name, 'HAS APPEARED' )
    print('You have three(3) options, what will you do? ......')
    while enemy.health >0:
        option = input('1.Sword attack\n2.Magic attack\n3.RUN!!!!!\n')
        if option == '1':
            print('YOU ATTACKED THE', enemy.name , 'BY SWINGING YOUR SWORD.')
            hitchance= random.randint(0,10)
            if hitchance >3:
                enemy.health= enemy.health-character.strength
                print('YOU JUST HIT THE', enemy.name, 'THEY HAVE ' ,enemy.health, 'REMAINING')

                if enemy.health>0:
                    character.health= character.health -(enemy.strength/character.defence)
                    print('THE', enemy.name, 'ATTACKED AND HITS YOU, YOU NOW HAVE', character.health, 'REAMINING')
                    gameover(character, score)

                else:
                    if enemy.name == 'Goblin':
                        enemy.health = 50
                        score = score +13
                        #return score

                    elif enemy.name == 'Wolf':
                        enemy.health = 60
                        score = score +10
                        #return score

                    elif enemy.name == 'Orc':
                        enemy.health = 70
                        score = score +15
                        #return score

                    elif enemy.name == 'Bat':
                        enemy.health = 15
                        score = score +5
                        #return score

                    elif enemy.name == 'Beast':
                        enemy.health = 75
                        score = score +20
                        #return score

                    print('YOU HAVE DEFETED THE', enemy.name, )
                    print('LOOKS LIKE IT DROPPED SOMETHING, LETS CHECK IT OUT.')
                    lootdrop = loot()
                    print('WOW, IT IS A ', lootdrop)
                    lootEffect(lootdrop,character)
                    return score
                    break
            else:
                print('OUCH, YOU MISSED!!!!, CAREFUL NEXT TIME.')
                print('THE', enemy.name, 'HITS YOU FOR FULL DAMAGE')
                character.health = character.health -enemy.strength
                print('YOU NOW HAVE', character.health, 'REMANING FROM YOUR HEALTH.')
                print('BECAREFUL NEXT TIME!!!!!')
                gameover(character, score)

        elif option == '2':
            print('YOU ATTACKED THE', enemy.name , 'BY CASTING A MAGIC SPELL.')
            hitchance= random.randint(0,10)
            if hitchance >2:
                enemy.health= enemy.health-character.magic
                print('YOU JUST HIT THE', enemy.name, 'THEY HAVE ' ,enemy.health, 'REMAINING')

                if enemy.health>0:
                    character.health= character.health -(enemy.strength/character.defence)
                    print('THE', enemy.name, 'ATTACKED AND HITS YOU, YOU NOW HAVE', character.health, 'REAMINING')
                    gameover(character,score)

                else:
                    if enemy.name == 'Goblin':
                        enemy.health = 50
                        score = score +13
                        #return score

                    elif enemy.name == 'Wolf':
                        enemy.health = 60
                        score = score +10
                        #return score

                    elif enemy.name == 'Orc':
                        enemy.health = 70
                        score = score +15
                        #return score

                    elif enemy.name == 'Bat':
                        enemy.health = 15
                        score = score +5
                        #return score

                    elif enemy.name == 'Beast':
                        enemy.health = 75
                        score = score +20
                        #return score

                    print('YOU HAVE DEFETED THE', enemy.name, )
                    print('LOOKS LIKE IT DROPPED SOMETHING, LETS CHECK IT OUT.')
                    lootdrop = loot()
                    print('WOW, IT IS A ', lootdrop)
                    lootEffect(lootdrop,character)
                    return score
                    break

            else:
                print('OUCH, YOU MISSED!!!! HOW CAN YOU MISS A MAGIC SPELL?, CAREFUL NEXT TIME.')
                print('THE', enemy.name, 'HITS YOU FOR FULL DAMAGE')
                character.health = character.health -enemy.strength
                print('YOU NOW HAVE', character.health, 'HP REMANING.')
                print('BECAREFUL NEXT TIME!!!!!')
                gameover(character, score)

        elif option == '3':
            print('YOU TRY TO RUN AWAY.......')
            runchance= random.randint(2,10)
            if runchance> 4:
                print('YOU RAN AWAY FROM THE', enemy.name, 'WITHOUT BEEN NOTICED.')
                break
            else:
                print('YOU TRIED TO RUN, BUT THE', enemy.name, 'CAUGHT UP WITH YOU BECAUSE YOU FELL')
                print('YOU TRIED TO DEFEND YOURSELF, BUT CANNOT AND THE', enemy.name, 'HIT YOU FOR FULL DAMAGE :(')
                character.health = character.health -enemy.strength
                print('YOUR HEALTH IS NOW ', character.health, 'HP')
                gameover(character, score)
        else:
            print('ERROR!!!... INVALID INPUT, PLEASE ENTER "1", "2" OR "3".')

character=selecthero()
score = battle(score)
print(score)
score = battle(score)
print(score)
score = battle(score)
print(score)
score= battle(score)
print(score)
score= battle(score)
print(score)



