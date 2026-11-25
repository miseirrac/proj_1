import pandas as pd

# Load the excel file into a data frame
df = pd.read_excel("AnnualCarPopulationbyMake.xlsx", index_col="make")

#to print preview (first 5 and last 5 data)
#print(df)

#To print entire excel file
#print(df.to_string())

# SELECTION BY COLUMN #
#print(df["year"].to_string())
#print(df["make"].to_string())
#print(df["fuel_type"].to_string())
#print(df["number"].to_string())
#print(df[["year", "make", "fuel_type", "number"]].to_string()) #to display entire data

# SELECTION BY ROWS
# print(df.loc[0])

# To add new column
#df["new column name here"] = ["values under the new column must be in order, by rows"]

# To add new rows
#new_rows = pd.dataFrame([{"year": XXXX, "make": BRAND, "fuel_type": ABCD, "number": 1234},
                        #{"year": XXXX, "make": BRAND, "fuel_type": ABCD, "number": 1234}])
#df = pd.concat([df, new_row])


def display_menu():
    print("")
    print('==============================================')
    print('      SMART EV ADOPTION ANALYTICS SYSTEM   ')
    print('==============================================')
    print('1. Load EV Dataset')
    print('2. Display EV Records')
    print('3. Display Highest EV Population')
    print('4. Display Lowest EV Population')
    print('5. Search EV Records')
    print('6. Update EV Population')
    print('7. Save Updated Dataset')
    print('8. Exit')
    print("")

#def load_dataset(load_all):
    # print(df.to_string())


def main():
# The choice variable controls the loop and
# holds the user's menu choice.
    choice = 0

    while choice != 8:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Select an option: '))

        # Perform the selected action.
        if choice == 1:    #Load EV Dataset (dk whats the diff between option 1 and 2)
            print(df.to_string())

        elif choice == 2:  #Display EV records
            ev_records = df[df["fuel_type"] == "Electric"]
            print(ev_records.to_string())

        elif choice == 3:   #Display highest EV population
            # Filter only Electric vehicles
            electric_cars = df[df['fuel_type'] == 'Electric']

            # Find the row with the highest number
            highest_ev = electric_cars.loc[electric_cars['number'].idxmax()]

            # Display the result
            print("\n===== HIGHEST ELECTRIC VEHICLE POPULATION =====")
            print("Year:", highest_ev['year'])

            print("Fuel Type:", highest_ev['fuel_type'])
            print("Number:", highest_ev['number'])

        #elif choice == 4:  #Display Lowest EV population
            ##

        #elif choice == 5:   #Search EV Records
           ##

        elif choice == 6:  #Update EV Population
            new_year = input('Enter the year: ')
            new_make = str(input('Enter the make: '))
            new_fueltype = input('Enter the fuel type: ')
            if new_fueltype.lower() in ('electric', 'petrol'):
                print(f"Confirm New Record: {new_year}, {new_make}, {new_fueltype}")
            else:
                print('Please enter a valid fuel type')

        #elif choice == 7:  #(Save updated Dataset)
            #



        elif choice == 8:
            print('Exiting the program. . .')
        else:
            print('Error: invalid selection.')

main()






