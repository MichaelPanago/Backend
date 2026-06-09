import json
products = []
try:
    with open("products.json", "r", encoding="utf-8") as file:
        products = json.load(file)
except:
    products = []
def save_products():
    with open("products.json", "w", encoding="utf-8") as file:
        json.dump(products, file, ensure_ascii=False)
while True:
    print("---Αποθήκη---")
    print("1. Προσθληκη Προϊόντων")
    print("2. Δείξε Τα Προϊόντα")
    print("3. Έξοδος")
    print("4. Σύνολο προϊόντων")
    print("5. Αναζήτηση προϊόντος")
    print("6. Διαγραφή προϊόντος")

    choice = input("Κάντε μια επιλογή: ")
    
    if choice =="1":
       product_code = input("Κωδικός Προϊόντος: ")
       name = input("Όνομα Προϊόντος: ")
       quantity = int(input("Ποσότητα: "))
       product = {
        "product_code": product_code,
        "name": name,
        "quantity": quantity
     }
       
       products.append(product)
       save_products()
       print("Το προϊόν προστέθηκε!")

    elif choice == "2":
        print("Προϊόντα: ")
        for product in products:
         print(f"Κωδικός: {product['product_code']}")
         print(f"Όνομα: {product['name']}")
         print(f"Ποσότητα: {product['quantity']}")
         print("------------------")
    
    elif choice == "3":
        print("Αντίο!")
        break
    
    elif choice == "4":
        print(f"Τα συνολικά προϊόντα είναι: {len(products)}")


    elif choice == "5":
        search = input("Ποιο προϊόν ψάχνεις; ")
        for product in products:
         if search == product["name"]:
            print(f"Το προϊόν βρέθηκε με όνομα: {search}")
         else:
            print("Το προϊόν δεν βρέθηκε!")
    
    elif choice == "6":
     delete_product = input("Ποιο προϊόν θέλεις να διαγράψεις; ")

     if delete_product in products:
        products.remove(delete_product)
        print(f"Το προϊόν διαγράφηκε: {delete_product}")
     else:
        print("Το προϊόν δεν υπάρχει!")

    else:
        print("Λάθος Επιλογή!")