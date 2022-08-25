
from mimetypes import init


cart = []

def add_cart(addeditem): 
 
    return cart.append(addeditem)


def del_cart(delitem):    
    return cart.remove(delitem)

def showcart(show):
    if len(show) == 0:
        print("You currently have nothing in your cart")
    else:
        for n in show:
            print(f"You currently have a {n} in your cart!")
    




def main():

    while True:
        initial_input = input('Do you want to: Show/Add/Delete or Quit?: ')
        if initial_input == 'Show':
            showcart(cart)
        
        elif initial_input == 'Add':
            addeditem = input("What item would you like to add?: ")
            add_cart(addeditem)
        
        elif initial_input == 'Delete':
            print(cart)
            delitem = input("What item would you like to delete?: ")
            del_cart(delitem)

        else:

             initial_input == 'Quit'
             print("thank you for shopping with us today!")
             print(cart)
             break
                            
    
main()                          
