from bikeRental import BikeRentalCompany, Customer

def main():
    shop = BikeRentalCompany(100)
    customer = Customer()

    while True:
        print("""
        ============== Bike Rental ===============
        1. Display available bikes
        2. Rent a bike on hourly basis @ ₹50
        3. Rent a bike on daily basis @ ₹200
        4. Rent a bike on weekly basis @ ₹1000
        5. Return a bike
        6. Exit
        ==========================================
        """)
        
        choice = input("Enter choice: ")
        
        try:
            choice = int(choice)
        except ValueError:
            print("That's not an int!")
            continue
        
        if choice == 1:
            shop.displaystock()
        
        elif choice == 2:
            customer.rentalTime = shop.BikeOnHour(customer.requestBike())
            customer.rentalBasis = 1

        elif choice == 3:
            customer.rentalTime = shop.BikeOnDaily(customer.requestBike())
            customer.rentalBasis = 2

        elif choice == 4:
            customer.rentalTime = shop.BikeOnWeekly(customer.requestBike())
            customer.rentalBasis = 3

        elif choice == 5:
            customer.bill = shop.returnBike(customer.returnBike())
            customer.rentalBasis, customer.rentalTime, customer.bikes = 0,0,0        
        elif choice == 6:
            break
        else:
            print("Invalid input. Please check the menu again.")        
    print("Thank you for using the bike rental system.")


if __name__=="__main__":
    main()