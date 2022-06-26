import datetime

class BikeRentalCompany:
    
    def __init__(self,stock=0):

        self.stock = stock

    def displaystock(self):
    #Displays the bikes currently available for rent.
        print("We have currently {} bikes available to rent.".format(self.stock))
        return self.stock

    def BikeOnHour(self, n):
    # Rent bike on Hourly Basis

        if n <= 0:
            print("Please enter a valid number.")
            return None
        
        elif n > self.stock:
            print("Sorry! Available bikes to rent = {}".format(self.stock))
            return None
        
        else:
            now = datetime.datetime.now()                      
            print("You have rented a {} bikes on hourly basis today at {} hours.".format(n,now.hour))
            print("You will be charged ₹50 for each hour per bike.")

            self.stock -= n
            return now      
     
    def BikeOnDaily(self, n):
        # Rent a bike on daily basis

        if n <= 0:
            print("Please enter a valid number.")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None
    
        else:
            now = datetime.datetime.now()                      
            print("You have rented {} bikes on daily basis today at {} hours.".format(n, now.hour))
            print("You will be charged ₹200 for each day per bike.")

            self.stock -= n
            return now
        
    def BikeOnWeekly(self, n):
    # Rent bike on weekly basis
        if n <= 0:
            print("Please enter a valid number.")
            return None

        elif n > self.stock:
            print("Sorry! We have currently {} bikes available to rent.".format(self.stock))
            return None        
        
        else:
            now = datetime.datetime.now()
            print("You have rented {} bike(s) on weekly basis today at {} hours.".format(n, now.hour))
            print("You will be charged ₹1000 for each week per bike.")
            self.stock -= n

            return now
    
    def returnBike(self, request):

        rentalTime, rentalBasis, numOfBikes = request
        bill = 0

        if rentalTime and rentalBasis and numOfBikes:
            self.stock += numOfBikes
            now = datetime.datetime.now()
            rentalPeriod = now - rentalTime
        
            # hourly bill
            if rentalBasis == 1:
                bill = round(rentalPeriod.seconds / 3600) * 50 * numOfBikes
                
            # daily bill
            elif rentalBasis == 2:
                bill = round(rentalPeriod.days) * 200 * numOfBikes
                
            # weekly bill
            elif rentalBasis == 3:
                bill = round(rentalPeriod.days / 7) * 1000 * numOfBikes
            

            print("Thankyou for returning the bike.")
            print("Total Bill: ₹{}".format(bill))
            return bill
        else:
            print("You have not rented any bike with us.")
            return None



class Customer:

    def __init__(self):
        
        self.bikes = 0
        self.rentalBasis = 0
        self.rentalTime = 0
        self.bill = 0

    
    def requestBike(self):
    # Takes request for the number of bikes wanted by the customer
                      
        bikes = input("How many bikes would you like to rent?")
        try:
            bikes = int(bikes)
        except ValueError:
            print("Please enter a valid number.")
            return -1

        if bikes < 1:
            print(" Number of bikes should be greater than zero.")
            return -1
        else:
            self.bikes = bikes
        return self.bikes
     
    def returnBike(self):
    # Return the bike
        if self.rentalBasis and self.rentalTime and self.bikes:
            return self.rentalTime, self.rentalBasis, self.bikes  
        else:
            return 0,0,0
