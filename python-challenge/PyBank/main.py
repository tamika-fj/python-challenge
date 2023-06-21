import csv
import os

#path to collect data from the pybank folder
budget_data = os.path.join('Resources', 'budget_data.csv')

#display title on screen
def display_title():
    print("Financial Analysis\n\n")

#display header on screen
def display_header():
    print("----------------------------------\n\n")


#Read the entire .csv file and skip header
with open(budget_data, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    next(csvreader)

    #create list to store data in the profit/losses column, used to the total sum of Profit/losses
    budget = []

    #create list to store data in the data column to count the number of months
    date = []

    #create list to store comparison of current row with previous row in the profit/losses column
    budget_change = []

    for row in csvreader:

        #calculate the total sum of Profit/losses
        budget.append(int(row[1]))

        #return the number of months
        date.append(row[0])

    #display the title and header
    display_title()
    display_header()

    #display the number of months and total profit/loss
    print("Total Months:", len(date),'\n\n')
    print("Total: $", sum(budget),'\n\n')


    for i in range(1,len(budget)):
        #compare current row with previous row in the profit/losses column
        budget_change.append(budget[i] - budget[i-1])
        
        #calculate the total profit/loss change, then calculate the average budget change by dividing the total profit/loss change by the number of months
        avg_budget_change = sum(budget_change)/len(budget_change)

        #get rows that contain the maximum and minimum budget change
        max_budget_change = max(budget_change)
        min_budget_change = min(budget_change)

        #assign the date to the row containing the maximum budget change, skip the first month 
        max_budget_change_date = str(date[1:][budget_change.index(max(budget_change))])

        #assign the date to the row containing the minimum budget change
        min_budget_change_date = str(date[1:][budget_change.index(min(budget_change))])

    #display the average profit/losses, greatest increase and greatest decrease in profit/losses
    print("Average Change: $", round(avg_budget_change),'\n\n')
    print("Greatest Increase in Revenue:", max_budget_change_date,"($", max_budget_change,")",'\n\n')
    print("Greatest Decrease in Revenue:", min_budget_change_date,"($", min_budget_change,")")


#Set variable for output file
output_file = os.path.join('analysis', 'pybank_calculations.csv')

#open the output file
with open(output_file, "w") as datafile:
    csv_writer = csv.writer(datafile, delimiter = "\t" )
    
    #write title to the file
    csv_writer.writerow("Financial Analysis")

    #write header to file 
    csv_writer.writerow("----------------------------------")

    #display Summary Budget Information to a .csv file
    csv_writer.writerow(["Total Months: ", len(date)])
    csv_writer.writerow(["Total: $ ", sum(budget)])
    csv_writer.writerow(["Average Change: $", round(avg_budget_change)])
    csv_writer.writerow(["Greatest Increase in Revenue: ", max_budget_change_date,"($", max_budget_change,")"])
    csv_writer.writerow(["Greatest Decrease in Revenue: ", min_budget_change_date,"($", min_budget_change,")"])