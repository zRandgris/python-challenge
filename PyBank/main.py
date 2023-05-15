import os
import csv

csvpath = os.path.join('PyBank', 'Resources', 'budget_data.csv' )

# Setting up values
n= 0
sum = 0
avgchange = 0
count = 0
difference = 0
previous = 0
difflist = []
monthlist = []
maxdiff = 0
mindiff = 0

numbers = []
with open(csvpath, 'r') as csvfile:


    csvreader = csv.reader(csvfile)

    print(csvreader)

    # Skipping Header
    csv_header = next(csvreader)

    for row in csvreader:
        # With each row read, add value to n
        n = n+1

        #Add every value at index 1
        sum = sum + int(row[1])

        #Adding the number into the number list
        numbers.append(row[1])

        #Calculating the difference of current year and previous year
        difference = float(row[1]) - previous

        #updating the previous year with each loop
        previous = float(row[1])
       
        #Saving the difference into a list called difflist       
        difflist.append(difference)
        #Creating a list contains the months for future refferece
        monthlist.append(row[0])
        

    
    # To find the Maximum number in difflist
    maxdiff = max(difflist)
    # To find the Minimum number in difflist
    mindiff = min(difflist)
    
    for x in difflist:
        #To keep track of the list index
        count = count + 1

        if x == maxdiff:          

            # Giving the index to the monthlist to match the maxdiff, -1 is the correct month where it started.
            Maxmonth = monthlist[count-1]
            
        if x == mindiff:
            # Giving the index to the monthlist to match the mixdiff, -1 is the correct month where it started.
            Minmonth = monthlist[count-1]

    #Calculating the Average Change
    avgchange = ((int(numbers[0]) - int(numbers[n-1])) / (n-1))

#--------------------------------------------------------------------------------------------------------------------
#Writing into txt file
outpath = os.path.join('PyBank', 'analysis', 'Result.txt')

with open(outpath, 'w') as wfile:
    wfile.write('Financial Analysis\n\n')
    wfile.write('-----------------------------\n\n')
    wfile.write('Total Months:'+ str(n) + '\n\n' )
    wfile.write('Total: $'+ str(sum) + '\n\n')
    wfile.write('Average Change: $'+ str(round(avgchange, 2))+'\n\n')
    wfile.write('Greatest Increase in Profits: '+ str(Maxmonth)+' ($'+ str(maxdiff)+')\n\n')
    wfile.write('Greatest Decrease in Profits: '+ str(Minmonth)+' ($'+ str(mindiff)+')\n\n')
    


