import os
import csv



csvpath = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# Setting up values
n = 0
sum = 0
can1 = 0
can2 = 0
can3 = 0

#Reading the csv file
with open(csvpath, 'r') as csvfile:

    csvreader = csv.reader(csvfile)

    print(csvreader)

    # Skipping Header
    csv_header = next(csvreader)
    
    for row in csvreader:
        #each row read is added to n
        n = n + 1
        #If 'Charles Casper Stockham' is matched, then add value to can1

        if row[2] == 'Charles Casper Stockham' :
            can1 = can1+1

        #If 'Diana DeGette' is matched, then add value to can2

        elif row[2]  == 'Diana DeGette' :
            can2 = can2 +1

        #If 'Raymon Anthony Doane' is matched, then add value to can3
        
        elif row[2] == 'Raymon Anthony Doane' :
            can3 = can3 + 1

    # Getting the percentage for each candidate
    pcan1 = can1/n
    pcan2 = can2/n
    pcan3 = can3/n   
   
    # #Creating a dictionary for candidate
    canlist = {'Charles Casper Stockham': can1,'Diana DeGette': can2 , 'Raymon Anthony Doane': can3}
    # For pulling 'key' out of the dictionary with maximum value
    


outpath = os.path.join('PyPoll', 'analysis', 'Result.txt')

#Writing the result into the file at the outpath destination    
with open(outpath, 'w') as wfile:
    
    wfile.write('Election Results\n\n')
    wfile.write('-------------------------\n\n')
    wfile.write('Total Votes : '+ str(n) + '\n\n')
    wfile.write('-------------------------\n\n')
    wfile.write('Charles Casper Stockham:' + f'{pcan1:.3%}'+' ('+ str(can1)+')\n\n')
    wfile.write('Diana DeGette:' + f'{pcan2:.3%}'+' ('+ str(can2)+')\n\n')
    wfile.write('Raymon Anthony Doane:'+f'{pcan3:.3%}'+' ('+ str(can3)+')\n\n')
    wfile.write('-------------------------\n\n')
    #Pulling 'key' out of the dictionary with maximum value
    wfile.write('Winner: '+ max(canlist, key = canlist.get)+'\n\n')
    wfile.write('-------------------------\n\n')

  