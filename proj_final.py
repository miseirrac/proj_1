import pandas as pd

# Load the excel file into a data frame at the start of the programme,"make" is used for row index
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

# Define function 1 : display menu
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

# define function 2 :load data set
def load_dataset(): 
  #Call global variable df
  global df
  # read excel file, "Make" is used for row index
  df = pd.read_excel("AnnualCarPopulationbyMake.xlsx", index_col="make")
  # print remarks once excel has been loaded
  print("Dataset has been loaded")

#define function 3 : main programme
def main():
# The choice variable controls the loop and holds the user's menu choice.
    choice = 0
  # repeat the menu until the user chooses option 8 
    while choice != 8:
        # display the menu.
        display_menu()

        # Get the user's choice.
        choice = int(input('Select an option: '))

        # Option 1 : load new excel into the programme.
        if choice == 1:    
          # call for load_data set function to load a new excel into the programme
          load_dataset()
          
        #Option 2 : Display EV records
        elif choice == 2:  
            #Filter to electrical car records only
            ev_records = df[df['fuel_type'] == 'Electric']
            # Display the records found. 
            print(ev_records.to_string())
          
        #Option 3 : Display highest EV population
        elif choice == 3:  
            #Filter to electrical car records only
            electric_cars = df[df['fuel_type'] == 'Electric']
            # Find the row with the highest number
            highest_ev = electric_cars.loc[electric_cars['number'].idxmax()]

            # Display the result
            print("\n===== HIGHEST ELECTRIC VEHICLE POPULATION =====")
            print("Year:", highest_ev['year'])

            print("Fuel Type:", highest_ev['fuel_type'])
            print("Number:", highest_ev['number']
         if electric_cars.empty:
              print("No Electric vehicle records found.")
         else: 
             highest_ev = electric_cars.loc[electric_cars['number'].idxmax()]
      #Option 4 : Display lowest EV population
        elif choice == 4: 
           #Filter to electrical car records only
            electric_cars = df[df['fuel_type'] == 'Electric']
          # Find the row with the highest number
            lowest_ev = electric_cars.loc[electric_cars['number'].idxmin()]
           # Display the result
            print("\n===== LOWEST ELECTRIC VEHICLE POPULATION =====")
            print("Year:", lowest_ev['year'])
            print("Fuel Type:", lowest_ev['fuel_type'])
            print("Number:", lowest_ev['number'])
          if electric_cars.empty:
            print("No Electric vehicle records found.")
         else: 
             highest_ev = electric_cars.loc[electric_cars['number'].idxmin()]

          #Option 5: Search EV Record

        elif choice == 5:

            # Ask user how they would prefer to search
            print("1. Search by Year")
            print("2. Search by Vehicle Make")

            # Input option
            search_choice = int(input("Select search option:"))

            # Option 1: Search by year
            if search_choice == 1:
                search_year = int(input("Enter which year"))

                # Find records by year
                search_result = df[df["year"] == search_year]

                # Display search results
                if search_result.empty:
                    print("No records found")
                else:
                    print(search_result.to_string())

            # Option 2: Search by car make
            elif search_choice == 2:
                search_make = input("Enter the vehicle make:")
                search_result = df[df.index == search_make]

                if search_result.empty:
                    print("No records found")
                else:
                    # CORRECTED: print syntax
                    print(search_result.to_string())

            # CORRECTED: This else belongs to search_choice
            else:
                print("Invalid search option.")


        elif choice == 6:  #Update EV Population
            new_year = input('Enter the year: ')
            new_make = str(input('Enter the make: '))
            new_fueltype = input('Enter the fuel type: ')
            #Only allowing these fuel types
            valid_fueltypes = ['electric', 'petrol']
            if new_fueltype.lower() in valid_fueltypes:
            #confirming input data
                print(f"Confirm New Record: {new_year}, {new_make}, {new_fueltype}")
                new_number = int(input('Enter the population:'))
              # Ensure number is not negative
              if new_number<0:
                print('Population cannot be negative')
            else:
              matching_re[df.index == new_make) & (df['year'] == int(new_year)) & (df['fuel_type'].str.lower() == new_fueltype.lower())]          
                if matching_record.empty:
                  print('Record not found')
                else:
                  print('Current population:'. matching_record['number'].values[0])
                  confirm = input('Update this record:(Yes/No): ')
                  if confirm.lower() == 'yes':
                      df.loc[ (df.index == new_make) & (df['year'] == int(new_year)) & df['(dfuel_type'].str.lower() == new_fueltype.lower()),'number'] = new_number
                      print('Record updated successfully!')
                  else:
                    print('Update cancelled.')
            else:
              print('Please enter a valid fuel type.')

        #Option 7 : save the updated data set
        elif choice == 7:
          #update to excel
          df.to_excel("AnnualCarPopulationNew.xlsx")
          #inform that data has been updated
          print("Data set has been updated!")


        #Option 8 : Exit programme 
        elif choice == 8:
            print('Exiting the program. . .')
        # If user did not select any of the available option, error will be prompted
        else:
            print('Error: invalid selection.')

main()






