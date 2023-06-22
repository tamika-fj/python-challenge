import os
import csv

#path to collect data from the pybank folder
election_data_csv = os.path.join('PyPoll', 'Resources', 'election_data.csv')

# A list to capture the names of candidates
candidates = []

# A list to capture the number of votes each candidate receives
num_votes = []

# A list to capture the percentage of total votes each candidate garners
percent_votes = []

# A counter for the total number of votes
total_votes = 0


# Displaying resultheader
def result_title():
    print("Election Results\n\n")

#Display dividing lines
def result_divide():
    print("-----------------------------\n\n")

#read election_data .csv file and skip header
with open(election_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)

    #select values to loop through 
    for row in csvreader:
        # Add to our vote-counter, 1 vote for each row after the header
        total_votes += 1

        '''
        If the candidate is not on the list, add his/her name to the list, along with
        a vote in his/her name.
        If he/she is already in the list, add a vote in his/her
        name
        '''
        if row[2] not in candidates:
            candidates.append(row[2])
            index = candidates.index(row[2])
            num_votes.append(1)
        else:
            index = candidates.index(row[2])
            num_votes[index] += 1

    # Add to percent_votes list
    for votes in num_votes:
        percentage = (votes/total_votes) * 100
        percentage = "%.3f%%" % percentage
        percent_votes.append(percentage)

    # Find the winning candidate
    winner = max(num_votes)
    index = num_votes.index(winner)
    winning_candidate = candidates[index]


#Display results on screen

result_title()
result_divide()

#Display total votes cast
print(f"Total Votes: {str(total_votes)}\n\n")
result_divide()

#Display all candidates and votes
for i in range(len(candidates)):
    print(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")

result_divide()

#Display winning candidate
print(f"Winner: {winning_candidate}")
result_divide()

#Set variable for output file
output_file = os.path.join('Pypoll', 'analysis', 'pypoll_calculations.csv')

#open the output file
with open(output_file, "w") as datafile:
    writer = csv.writer(datafile, delimiter = "\t")
    

    #write title 
    writer.writerow("Election Results")

    #write header to file 
    writer.writerow("----------------------------------")
    
    #write calculated values
    for i in range(len(candidates)):
        writer.writerow(f"{candidates[i]}: {str(percent_votes[i])} ({str(num_votes[i])})")
    
    #write header to file 
    writer.writerow("----------------------------------")

    #write winning candidate
    writer.writerow(f"Winner: {winning_candidate}")

    #write header to file 
    writer.writerow("----------------------------------")