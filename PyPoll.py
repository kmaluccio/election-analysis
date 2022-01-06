# Data to retrieve from file:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Import the datetime class from the datetime module
import datetime as dt
# Use now() attribute on teh datetime class to get the present time.
# now = dt.datetime.now()
# Print the present time.
# print("The time right now is ", now)

# Import csv and os modules
import os
import csv
# Assign a variable for the file to load from a path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Total vote counter
total_votes = 0
# Initialize candidates list
candidate_options = []

# Open the election results, read the file.
with open(file_to_load) as election_data:

    # Read the file object with reader function.
    file_reader = csv.reader(election_data)
    # Read header row.
    headers = next(file_reader)
    
    # Print each row in the CSV file.
    for row in file_reader:
        # print(row)
        # Increment vote counter by 1
        total_votes += 1

        # Print candidate name from each row
        candidate_name = row[2]
        # Check to see if we already added this candidate to our list
        if candidate_name not in candidate_options:
            # Add the candidate name to the list
            candidate_options.append(candidate_name)
        
# Print out total votes, all candidates
print(total_votes)
print(candidate_options)

# Create a filename variable to a path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open function with the w mode to write as a text file.
with open(file_to_save, "w") as txt_file:
    # Write counties to the new file.
    txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")
