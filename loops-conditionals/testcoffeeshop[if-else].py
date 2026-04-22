#sample barista

menu = 'Black Coffee, Espresso, Latte, Cappucino'
price = 8

print("Welcome to the Coffee Shop! Thank you for coming in today!")
name = input("What is your name?\n")

if name == "Ben":
    print("You're blacklisted in our coffee shop," + name)
else:
    print('\nHello '+ name + '!' + ' what would you like from our menu today? Here is what we are serving, all of them are priced at $8\n') 

order = input(menu + '\n')
#order = input('What would you like to order?\n')
#order = input('Your order is:\n')

print('How many orders of ' + order + ' would you like?')
quantity = input()
total = price * int(quantity)
print("Thank you " + name + ', your total is:$' + str(total))
print("Sounds good " + name + ", we'll have your " + quantity + ' ' + order + ' ready for you in a moment.')

if 4 > 3:
    print("Yep, it's true")
    print("It's still true")
else:
    print("Nope, not true")
