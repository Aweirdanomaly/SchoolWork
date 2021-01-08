#
# ps6pr5.py (Problem Set 6, Problem 5)
#
# TT Securities    
#
# Computer Science 111
#

import math

def display_menu():
    """ prints a menu of options
    """  
    print()
    print('(0) Input a new list of prices')
    print('(1) Print the current prices')
    print('(2) Find the latest price')
     ## Add the new menu options here.
    print('(3) Find the average price')
    print('(4) find the standard deviation')
    print('(5) Find the max price and its day')
    print('(6) Test a threshold')
    print('(7) Your investment plan')
    print('(8) Quit')

def get_new_prices():
    """ gets a new list of prices from the user and returns it
    """
    new_price_list = eval(input('Enter a new list of prices: '))
    return new_price_list

def print_prices(prices):
    """ prints the current list of prices
        input: prices is a list of 1 or more numbers.
    """
    if len(prices) == 0:
        print('No prices have been entered.')
        return
    
    print('Day Price')
    print('--- -----')
    for i in range(len(prices)):
        print('%3d' % i, end='')
        print('%6.2f' % prices[i])

def latest_price(prices):
    """ returns the latest (i.e., last) price in a list of prices.
        input: prices is a list of 1 or more numbers.
    """
    return prices[-1]

## Add your functions for options 3-7 below.
def avg_price(vals):
    """ takes in list vals and returns the average of all its values"""
    x = 0
    for i in vals:
        x += i
    return x/ len(vals)

def std_dev(vals):
    """ takes in list of values 'vals' and returns their standard dev. """
    avg = avg_price(vals)
    w = 0
    for i in vals:
        w += ((i - avg)**2)
    w /= len(vals)
    return math.sqrt(w)

def max_day(vals):
    """ takes in a list of values 'vals' and returns the biggest one"""
    i = 0
    w = 0
    while i < len(vals):
        if vals[i] > w:
            w = vals[i]
            ans = i
        i += 1
    return ans

def any_below(vals, tld):
    """ takes in list 'vals' and integer 'tld' and returns a boolean 
    value depending on whether there exist an integer lower than 'tld'
    in 'vals' """
    ans = False
    for i in vals:
        if i < tld:
            ans = True
    return ans
        
def find_plan(vals):
    """takes in list 'vals' as input and returns an optimum investing
    strategy in which a list containing the day to buy, the day to sell,
    and the profit made"""
    w = 0
    for i in range(len(vals)):
        for j in range(len(vals)):
            a = vals[j] - vals[i]
            if a > w and j > i:
                w = a
                m = j
                l = i
    return [l, m, (vals[m] - vals[l])]
            
    
    


def tts():
    """ the main user-interaction loop
    """
    prices = []

    while True:
        display_menu()
        choice = int(input('Enter your choice: '))
        print()

        if choice == 0:
            prices = get_new_prices()
        elif choice == 8:
            break
        elif choice < 8 and len(prices) == 0:
            print('You must enter some prices first.')
        elif choice == 1:
            print_prices(prices)
        elif choice == 2:
            latest = latest_price(prices)
            print('The latest price is', latest)
        ## add code to process the other choices here
        elif choice == 3:
            avg = avg_price(prices)
            print('The average price is', avg)
        elif choice == 4:
            sd = std_dev(prices)
            print('The standard deviation is', sd)
        elif choice == 5:
            max = max_day(prices)
            print('The max price is', prices[max], 'on day', max)
        elif choice == 6:
            td = eval(input('Enter the threshold: '))
            ans = any_below(prices, td)
            if ans == True:
                print('There is at least one price below', td)
            else:
                print('There are no prices below', td)
        elif choice == 7:
            inv_list = find_plan(prices)
            print('Buy on day', inv_list[0], 'at price', prices[inv_list[0]])
            print('Sell on day', inv_list[1], 'at price', prices[inv_list[1]])
            print('Total profit:', inv_list[2])

        else:
            print('Invalid choice. Please try again.')

    print('See you yesterday!')
