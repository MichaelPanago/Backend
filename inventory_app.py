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
       product = input("Όνομα Προϊόντος: ")
       products.append(product)
       save_products()
       print("Το προϊόν προστέθηκε!")

    elif choice == "2":
        print("Προϊόντα: ")
        for product in products:
            print(product)
    
    elif choice == "3":
        print("Αντίο!")
        break
    
    elif choice == "4":
        print(f"Τα συνολικά προϊόντα είναι: {len(products)}")


    elif choice == "5":
        search = input("Ποιο προϊόν ψάχνεις; ")
        if search in products:
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