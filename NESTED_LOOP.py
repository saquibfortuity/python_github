print('welcome to bank atm')
restart = ('y')
chances = 3
balance = 88542.22
pinn = 8585
while chances >= 0:
    pin = int(input('enter your 4 digit pin :'))
    if pin == (8585):
        print('you entered your pin correctly')
        while restart not in ('n','NO','no','N'):
            print('enter 1 for balance :')
            print('enter 2 for withdrawl :')
            print('enter 3 for pay in :')
            print('enter 4 for return card :')
            options = int(input('choose any options'))
            #for option one
            if options == 1:
                print('your balance is',balance)
                restart = input('would you like to go back')
                if restart in ('n','NO','N','no'):
                    print('thank you')
                    break
            # for option two
            elif options == 2:
                options2 = ('y')
                withdrawl = float(input('how much you would like to withdrawl'))
                if withdrawl in [100,200,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500]:
                    balance = balance - withdrawl
                    print('ypur balance is ',balance)
                    restart = input('would you like to go back')
                    if restart in ('n', 'NO', 'N', 'no'):
                        print('thank you')
                        break
                elif withdrawl != [100,200,500,1000,1500,2000,2500,3000,3500,4000,4500,5000,5500,6000,6500]:
                    print('Invalid amount, Please re-try')
                    restart =('y')
                elif withdrawl == 1:
                    withdrawl = float(input('enter the amount :'))
            # for option three
            elif options == 3:
                pay_in = float(input('how much would you like to pay in '))
                balance = balance - pay_in
                print('your balance is :',balance)
                restart = input('would you like to go back ?')
                if restart in ('N','NO','no','N'):
                    print('Thank you')
                    break
            #for option four
            elif options == 4:
                print('thank you for using this ATM :')
                break
            else:
                print('please enter a correct number :')
    elif pin != ('8585'):
        print('incorrect password')
    chances = chances-1
    if chances == 0:
        print('no mopre tries')
        break

















