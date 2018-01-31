def leave():
    imp = input('What? ')
    print('Nevermind...')
    return;

input('Imagine you\'re in a castle. How do you feel? ')
input('But what if you\'re trapped behind doors made of steel? ')
imp = input('If I gave you a key, would you try every lock (y/n)? ')
if (imp[0] == 'y' or imp[0] == 'Y'):
    imp = input('If it opened a door, would you continue to walk (y/n)? ')
    if (imp[0] == 'y' or imp[0] == 'Y'):
        imp = input('If a shadow was lurking, would you grab for a sword (y/n)? ')
        if (imp[0] == 'y' or imp[0] == 'Y'):
            imp = input('If the figure was royal, would you replace a lord (y/n)? ')
            if (imp[0] == 'y' or imp[0] == 'Y'):
                imp = input('If you made it to king, would you protect and save (y/n)? ')
                if (imp[0] == 'y' or imp[0] == 'Y'):
                    print('Then it\'s true that the heavens caught a hero so brave!')
                elif (imp[0] == 'n' or imp[0] == 'N'):
                    print('Then you\'ll rot in your playground as always a slave!')
                else:
                    leave()
            elif (imp[0] == 'n' or imp[0] == 'N'):
                print('Then the job will be clean: Kill you by guillotine!')
            else:
                leave()
        elif (imp[0] == 'n' or imp[0] == 'N'):
            imp = input('If the figure promised life, would you trust their reward (y/n)?')
            if (imp[0] == 'y' or imp[0] == 'Y'):
                print('Then you\'ll live to old age as a quaint and wise sage!')
            elif (imp[0] == 'n' or imp[0] == 'N'):
                print('Then you shant again roam with the trap as your home!')
            else:
                leave()
        else:
            leave()
    elif (imp[0] == 'n' or imp[0] == 'N'):
        print('Then it\'s impossible to win if you never begin!')
    else:
        leave()
elif (imp[0] == 'n' or imp[0] == 'N'):
    imp = input('Then there\'s no point in us even trying to talk!')
else:
    leave()