Products = {}
Product_list = []
sum = 0

def line():
    return print("=-"*40)

line()
print("Welcome to the goods storeroom control!")
print("Options: 1- Generate a control report\n 2- Append products in the database\n 3- Remove products of the database")
option = int(input("Which option do you want? "))
if option == 1:
    with open("ex17.txt", 'r') as h:
        for i in h.readlines():
            print(" Item   Code     Description       Quantity")
            x = i.replace("}", "").replace("{", "").replace("[", '').replace("]", '').replace(":", "  ").replace("'", "")
            y = x.replace(",", "  ").replace(' "', "     ").replace('" ', " ").replace('\n', "")
            print(y)
            line()
if option == 2:
    option_2 = str(input("Do you want to create a new entry in the dabatase or append more products? "))
    if option_2.lower() in "create":
        while True:
            Products.clear()
            product = str(input("Which product/merchandise do you want to append? "))
            code = int(input("Insert a numerical code: "))
            description = str(input("Describe your product/merchandise: "))
            quantity = int(input("How many of this product/merchandise do you want to append? "))
            Products.update({product: [code,description, "     " , quantity]})
            with open('ex17.txt', 'a') as a:
                a.write(str(f'{Products}\n'))
            answer = str(input("Do you want to continue? Yes or No? "))
            if answer.lower() not in ('yes', 'y'):
                break
        
    
    elif option_2.lower() in 'append':
        option_3 = str(input("Which product do you want to update? "))
        quantity_2 = str(input("How much do you want to add? "))
        with open('ex17.txt', 'r') as b:
            for i in b.readlines():
                x = i.replace('\n', "").replace("\"", " ").replace("' '", " ").replace(",", "  ")
                Product_list.append(x)
        with open('ex17.txt', 'w') as c:
            for i in Product_list:
                if option_3 in i:
                    z = i[-4:-2]
                    sum = int(z) + int(quantity_2)
                    new = i.replace(z,str(sum))
                    i = new
                c.write(f"{i}\n")

elif option == 3:
    option_4 = str(input("Do you want to remove all the data of the product or decrease his stock? "))
    if option_4.lower() in "remove":
        option_5 = str(input("Which product do you want to remove? "))
        with open("ex17.txt", 'r') as d:
            for i in d.readlines():
                x = i.replace('\n', "").replace("\"", "").replace("' '", "   ").replace(",", "  ")
                Product_list.append(x)
        with open("ex17.txt", 'w') as e:
            for i in Product_list:
                if option_5 in i:
                    x = Product_list.remove(i)
                    for v in Product_list:
                        e.write(f"{v}\n")
    
    elif option_4.lower() in "decrease":
        option_6 = str(input("Which product do you want to decrease? "))
        quantity_3 = str(input("How much do you want to decrease? "))
        with open('ex17.txt', 'r') as f:
            for i in f.readlines():
                x = i.replace('\n', "").replace("\"", "").replace("' '", "   ").replace(",", "  ")
                Product_list.append(x)
        with open('ex17.txt', 'w') as g:
            for i in Product_list:
                if option_6 in i:
                    z = i[-4:-2]
                    sum = int(z) - int(quantity_3)
                    if sum <= 0:
                        print("You can't decrease anymore")
                    else:
                        new = i.replace(z,str(sum))
                        i = new
                g.write(f"{i}\n")

            
                
                

   
