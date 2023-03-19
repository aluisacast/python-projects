# Autor: Ana Luisa Castañeda Garce
#   Data Analysis

# Variables 
low_le = 10000000000000000000000
high_le = 0

sum_le = 0
lenght_year = 0

i_high_le = 0
i_low_le = 10000000000000000000000

loop = 'yes'


source = 'James C. Riley (2005) - Estimates of Regional and Global Life Expectancy, 1800–2001. Issue Population and Development Review. Population and Development Review. Volume 31, Issue 3, pages 537–543, September 2005., Zijdeman, Richard; Ribeira da Silva, Filipa, 2015, "Life Expectancy at Birth (Total)", http://hdl.handle.net/10622/LKYT53, IISH Dataverse, V1, and UN Population Division (2019)'
# -------------------------------


print()
print('Welcome to the: ',end='')
print("\033[4m{}\033[00m".format('1543-2019 World'),end='')
print(' Life Expectancy Viewer Program')
print('Data from: OurWorldInData.org, source at the end of the program.\n')

while loop.lower() == 'yes' :

    learn = input('Did you came to learn from a specific YEAR or COUNTRY or from the WORLD? ')

    if learn.lower() == 'year' :
        interest = input('Enter the year you want to learn from. ')

        print()

        with open("life-expectancy.csv") as le_file :
            
            next(le_file) # This skips the first line of the file that indicates
                        # Entity,Code,Year,Life expectancy (years)
            for  line in le_file :

                clean_line = line.strip() # cleans the strings of spaces
                data = clean_line.split(',') # splits each line when there is a ","

                country = data[0] 
                year = data[2]
                le = float(data[3])
            
                
                if year == interest :    
                    sum_le += le
                    lenght_year += 1

                    if le < i_low_le : # finds the lowest life expectancy for that year
                        low_le = le
                        low_country = country

                    if le > i_high_le : # finds the highest life expectancy for that year
                        high_le = le
                        high_country = country
                    
            print('For the year ',interest,':')
            print(f'The average life expectancy across all countries was {(sum_le / lenght_year):.2f}')
            print(f'The max life expectancy was in {high_country} with {high_le}')
            print(f'The min life expectancy was in {low_country} with {low_le}\n')

        loop = input('Do you want to learn more (YES/NO)? ')

    elif learn.lower() == 'country' :
        interest = input('Enter the name of the country you want to learn from. ')

        print()
        
        with open("life-expectancy.csv") as le_file :
            
            next(le_file) # This skips the first line of the file that indicates
                        # Entity,Code,Year,Life expectancy (years)
            for  line in le_file :

                clean_line = line.strip() # cleans the strings of spaces
                data = clean_line.split(',') # splits each line when there is a ","

                country = data[0] 
                year = data[2]
                le = float(data[3])
            
                
                if country.lower() == interest.lower() :    
                    sum_le += le
                    lenght_year += 1

                    if le < i_low_le : # finds the lowest life expectancy for that year
                        low_le = le
                        low_year = year

                    if le > i_high_le : # finds the highest life expectancy for that year
                        high_le = le
                        high_year = year
                    
            print('For the country ',interest,': ')
            print(f'The average life expectancy is of {(sum_le / lenght_year):.2f}')
            print(f'The max life expectancy was in {high_year} with {high_le}')
            print(f'The min life expectancy was in {low_year} with {low_le}\n')

        loop = input('Do you want to learn more (YES/NO)? ')

    elif learn.lower() == 'world' :
        interest = 'world'

        print()

        with open("life-expectancy.csv") as le_file :
            
            next(le_file) # This skips the first line of the file that indicates
                        # Entity,Code,Year,Life expectancy (years)
            for  line in le_file :

                clean_line = line.strip() # cleans the strings of spaces
                data = clean_line.split(',') # splits each line when there is a ","

                country = data[0] 
                year = data[2]
                le = float(data[3])


                if le < low_le : # finds the lowest life expectancy
                    low_le = le
                    low_country = country
                    low_year = year

                if le > high_le : # finds the highest life expectancy
                    high_le = le
                    high_country = country
                    high_year = year
                    
                        
            print(f'The overall max life expectancy in the World during 1543-2019 was: {high_le} from {high_country} in {high_year}')
            print(f'The overall min life expectancy in the World during 1543-2019 was: {low_le} from {low_country} in {low_year}\n')  

        loop = input('Do you want to learn more (YES/NO)? ')

    else :
        'Chose from a year, country or the world, please.'
        loop = 'yes'


else :
    print()
    show = input('Do you want to see the source of the data (YES/NO)? ')
    while show.lower() == 'yes' :
        print('\nData extracted from: ',source,'\n')
        show = 'end'
    else :
        print('\nThank you for using the Life Expectancy Viewer Program.')
        print('This program was made by', "\033[1m{}\033[00m" .format('Ana Luisa Castañeda.'))
        print('Godbye.\n')