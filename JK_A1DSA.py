#Jacob Korin #100860365

import time
# function takes file name as input, returns each line in an array
def read_file(my_file):
    data = []

    with open(my_file) as file:
        for line in file:
            data.append([line.strip()])
    return data

# Insertion sort algorithm that sorts an array of arrays by the third element in each subarray(in this case price of each product)
def insertion_sort_by_price(products):
    startTime = time.time()       
    for index in range(1, len(products)):
        current_product = products[index]
        current_price = float(current_product[2])  # Convert price to float for comparison
        position = index - 1

        # Move products with higher prices to the right of the current product
        while position >= 0 and float(products[position][2]) > current_price:
            products[position + 1] = products[position]
            position -= 1
        products[position + 1] = current_product
    
    endTime = time.time()

    return endTime-startTime


def main():
    #reading the raw data
    product_data = read_file("product_data.txt")

    # initializing an array to hold formatted data
    products = []

    # splitting each line in the raw data file into an array
    for i in range(len(product_data)):
        products.append((product_data[i])[0].split(','))
       
    # function to add items
    def create(id, name, price, category):
        products.append([id, name, price, category])
    
    # function to update items
    def update(id, name, price, category):
        for i in range(len(products)):
            if int(products[i][0]) == int(id):
                products[i] = [id, name, price, category]
        print(f"Product successfully updated")

    # function that searches for items by product id
    def search_by_id(id):
        for i in range(len(products)):
            if int(products[i][0]) == int(id):
                print(f"{products[i][0]}, {products[i][1]}, {products[i][2]}, {products[i][3]}")

    # function that searches for items by product name
    def search_by_name(name):
        for i in range(len(products)):
            if (products[i][1]).strip().lower() == name.lower():
                print(f"{products[i][0]}, {products[i][1]}, {products[i][2]}, {products[i][3]}")
    
    # function that deletes items given their id
    def delete(id):
        prod_id = 0
        for i in range(len(products)):
            if int(products[i][0]) == int(id):
                prod_id = i

        products.pop(prod_id)
        print(f"Product {id} successfully deleted")

    # ALL FUNCTIONS BEING USED BELOW, UNCOMMENT TO TEST
    timeToSort = (insertion_sort_by_price(products))
    #delete(93533)
    #create('91032', "Dishwasher DJSPA", '299', "Home & Kitchen")
    #search_by_id(10889)
    #search_by_name("Shirt DNRZU")
    #update("13471", "Knife Set TPCMO", "699", "Home & Kitchen")
    
    #for i in range(len(products)):
        #print(products[i])

    #print("It took",timeToSort,"seconds to sort the data.")
    return 0
main()
