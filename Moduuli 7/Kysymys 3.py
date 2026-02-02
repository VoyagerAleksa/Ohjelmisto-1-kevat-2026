airports = {}
while True:
    print ("\nAirport Data Management \n1. Enter a new airport \n2. Fetch airport information \n3. Quit ")
    new_aeroport_str = input("Please choose an option (1-3): ")
    if new_aeroport_str == "1":
        icao_code_str = input("Enter the ICAO code: ")
        airport_name_str = input("Enter the airport name: ")

        airports.update({icao_code_str: airport_name_str})

        print(f"Airport {airport_name_str} with ICAO code {icao_code_str} has been added. ")

    elif  new_aeroport_str == "2":
        icao_code_str = input("Enter the ICAO code: ")
        airport_name = airports.get(icao_code_str, "unknown")
        if airport_name == "unknown":
            print(f"No airport found with ICAO code {icao_code_str}. ")
        else:
            print(f"The airport with ICAO code {icao_code_str} is {airport_name}. ")
    elif new_aeroport_str == "3":
        print("Thank you for using the Airport Data Management system. Goodbye! ")
        break


