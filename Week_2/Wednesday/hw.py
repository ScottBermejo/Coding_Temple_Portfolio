class Cart:
    def __init__(self,cat):
        self.category = cat

class CartItem(Cart):
    def __init__(self,cat,item,price):
        super().__init__(cat)
        self.item = item
        self.price = price

    def add_item(self,category,item,price):
        self.category = category
        self.item = item
        self.price = price
        
    def remove_item(self,cart,item):
        for i in cart:
            if i.get_item() == item:
                cart.remove(i)
            
        
    def show_cart(self,num):
        print(self.category.title(),"\n",num,self.item.title(),":",self.price)
    def get_item(self):
        return self.item
        
def show_instructions():
    print("=" * 50)
    print("""Type 'add' to add item to cart.
        Type 'remove' to add item from cart.
        Type 'show' to view all items in your cart.
        Type 'quit' to exit program and show your list.""")
print("=" * 50)
        
shopping_cart = []
item_count = 1
done = False
while not done:
    show_instructions()
    ask = input("What would you like to do?: ").lower()
    
    if ask == 'quit':
        for i in shopping_cart:
            i.show_cart(item_count)
        done = True
    elif ask == 'add':
        cat = input('What category, ex. Meat,Fruit,Vegetable?: ').lower()
        item = input("What's the item's name?: ").lower()
        price = float(input("What's the item's price?: "))
        new_cart = CartItem('','',0.0)
        new_cart.add_item(cat,item,price)
        if new_cart.get_item() == item:
            item_count += 1
        else:
            shopping_cart.append(new_cart)
    elif ask == 'remove':
        item = input("Which item would you like to remove?: ").lower()
        remove_item(shopping_cart, item)
    elif ask == 'show':
        for i in shopping_cart:
            i.show_cart(item_count)
    else:
        print("Invalid, please try again.")
        continue
        
        