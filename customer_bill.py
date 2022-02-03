import logging

# initialize the logger :
logger = logging.getLogger(__name__)
file_handler = logging.FileHandler("customer_bill.log")
formatter = logging.Formatter('[%(asctime)s] %(levelname)s [%(message)s]')

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.DEBUG)

print("Welcome to Food in a Jiffy!")

food_options = {
  "H": {
    "name": "Hamburger",
    "price": 2.49
    },
  "C": {
    "name": "Cheeseburger",
    "price": 4.99
    },
  "F": {
    "name": "Fries",
    "price": 2.50
    },
  "D": {
    "name": "Drink",
    "price": 1.99
    },
  "E": {
    "name": "End Order",
    "price": 0.00
    }
}

def menu():
  for i in food_options:
    line = "[{title}] {name}: ${price}".format(title = i, name = food_options[i]['name'], price = food_options[i]['price'])
    print(line)

menu()
cost = 0
termination = False


choice = input("Please enter the code you want to buy: ").upper()
while not termination:
    if choice in food_options.keys():
        for i in food_options:
            if choice == i and choice != 'E':
                try:
                  num = int(input('How many items do you want to order?'))
                except ValueError:
                  logger.debug("not input digital number")  # logger 
                  num = int(input('Please input a digital number:'))
                finally:
                  logger.info('The customer buy {num} {name}'.format(num = num, name = food_options[i]['name'])) # logger
                  price = food_options[i]['price']
                  print("Your order is {number} {name}, about ${price}.".format(number = num, name = food_options[i]['name'], price = round(num*price,2)))
                  cost += num*price
                  choice = input("Please enter the code you want to buy: ").upper()


            elif choice == 'E':
                logger.info("end order") # logger

                print("\n--------End order---------")
                print("Your total cost is ${money}.".format(money = cost))
                pay = int(input("How much do you want to pay for?"))
                if pay > cost:
                    logger.info('customer pay {pay}, the cost is {cost}, payment success!'.format(pay = pay, cost = cost)) # logger
                    
                    pay_back = pay - cost
                    print("Wait a second, I will pay back for ${pay_back}.".format(pay_back = round(pay_back, 2)))
                else:
                    logger.warning("not enough money") # logger
                    
                    print("Not enough money, can't complete the order.")
                termination = True
                break

    else:
        logger.error('not input the right code') # logger

        choice = input("The code doesn't appear in the menu, please enter again:").upper()
 
print("\nWelcome you again")          

# ------------- The level of logger ------------
'''
1. logger.debug()
2. logger.info()
3. logger.warning()
4. logger.error()
5. logger.critical()
'''
