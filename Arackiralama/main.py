from rent import carRent, BikeRent, Customer


bike = BikeRent(100)
car = carRent(10)
customer = Customer()
main_menu = True
while True:

    if main_menu:
        print('''
                ***** Vehicle Rental Shop *****
                A. Bike Menu
                B. Car Menu
                Q. Exit
                ''')
        main_menu = False
        choice = input(" enter Choice: ")
        if choice == "A" or choice == "a":
            print("""
                    ***** BIKE MENU *****
                    1. Display avaible bikers
                    2. Request a bike on hourly basis $ 5
                    3. Request a bike on daily basis $ 84
                    4. Return a Bike
                    5. Main Menu
                    6. Exit
                    """)
            choice = input(" Enter Choice : ")

            try:
                choice = int(choice)
            except ValueError:
                print("error")
                continue
            if choice == 1:
                bike.displayStock()

                print(" -------------------------- ")
                choice = "A"
            elif choice == 2:
                customer.rentaltime_b = bike.rentHourly(customer.requestVehicle("bike"))
                customer.rentalBasis_b = 1
                main_menu = True
                print(" -------------------------- ")
            elif choice == 3:
                customer.rentaltime_b = bike.rentDaily(customer.requestVehicle("bike"))
                customer.rentalBasis_b = 2
                main_menu = True
                print(" -------------------------- ")
            elif choice == 4:
                customer.bill = bike.returnVehicle(customer.requestVehicle("bike"),"bike")
                customer.rentalBasis_b, customer.rentaltime_b, customer.bikes = 0,0,0
                main_menu = True
            elif choice == 5:
                main_menu = True
            elif choice == 6:
                break
            else:
                print("Invalid input. Please enter a number between 1-6")
                main_menu = True
        elif choice == "b" or choice == "B":
            print("""
                    ***** BIKE MENU *****
                    1. Display avaible CARS
                    2. Request a CAR on hourly basis $ 5
                    3. Request a CAR on daily basis $ 84
                    4. Return a CAR
                    5. Main Menu
                    6. Exit
                    """)
            choice = input(" Enter Choice : ")

            try:
                choice = int(choice)
            except ValueError:
                print("error")
                continue
            if choice == 1:
                car.displayStock()
                choice = "B"
                print(" -------------------------- ")
            elif choice == 2:
                customer.rentaltime_c = car.rentHourly(customer.requestVehicle("car"))
                customer.rentalBasis_c = 1
                main_menu = True
                print(" -------------------------- ")
            elif choice == 3:
                customer.rentaltime_c = car.rentDaily(customer.requestVehicle("car"))
                customer.rentalBasis_c = 2
                main_menu = True
                print(" -------------------------- ")
            elif choice == 4:
                customer.bill = car.returnVehicle(customer.requestVehicle("car"),"car")
                customer.rentalBasis_c, customer.rentaltime_c, customer.cars = 0,0,0
                main_menu = True
            elif choice == 5:
                main_menu = True
            elif choice == 6:
                break
            else:
                print("Invalid input. Please enter a number between 1-6")
                main_menu = True
            if choice == "q" or choice == "Q":
                break
        else:
            print("invalid Input. Please Enter A-B-Q")
            main_menu = True
            print('Thank u for rental shop')