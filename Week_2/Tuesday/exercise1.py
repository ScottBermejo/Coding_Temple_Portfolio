#from IPython.display import clear_output

shop_list = []
d_list = []

done = False
while not done:
    u_input = input("Would you like to add, delete, show\nor quit your current shopping list: ").lower()
    #clear_output()
    
    if u_input == 'quit':
        done = True
    elif u_input == 'show':
        for item in shop_list:
            print(f"{item['category'].title()} : {item['item'].title()}")
    elif u_input == 'add':
        c_name = input("What category, ex. Meat, Vegetable, Fruit, etc.: ").lower()
        i_name = input("What item, ex. Apple, Broccoli, Chicken: ").lower()
        
        cart = {
            'category': c_name,
            'item': i_name
        }
        shop_list.append(cart)
    elif u_input == 'delete':
        dc_name = input("Which category to delete?: ").lower()
        dc_item = input("Which item to delete?: ").lower()
        
        for item in shop_list:
            if dc_name != item['category'].lower() and dc_item != item['item'].lower():
                d_list.append(item)
        shop_list = d_list
    else:
        print("You typed something else, Try reading the instructions.")
        continue
        
for i in shop_list:
    print(f"{i['category'].title()} : {i['item'].title()}")
