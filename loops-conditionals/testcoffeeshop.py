#sample barista

print('Welcome to the Coffee Shop!')
name = input('What is your name?\n')

menu = 'Black Coffee, Espresso, Latte, Cappucino'
print('\nHello '+ name + '!' + ' what would you like from our menu today? Here is what we are serving, all of them are priced at $8\n') 
order = input(menu + '\n')
#order = input('What would you like to order?\n')
#order = input('Your order is:\n')
price = 8

print('How many orders of ' + order + ' would you like?')
quantity = input()
total = price * int(quantity)
print("Thank you " + name + ', your total is:$' + str(total))
print("Sounds good " + name + ", we'll have your " + quantity + ' ' + order + ' ready for you in a moment.')

