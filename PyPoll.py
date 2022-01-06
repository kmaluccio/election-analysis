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
# Declare empty dictionary for total votes per candidate
candidate_votes = {}
# Initialize variables for winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

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
            # Begin tracking that candidate's number of votes
            candidate_votes[candidate_name] = 0

        # Add one vote for this candidate
        candidate_votes[candidate_name] += 1

        
# Print out total votes, all candidates, total votes per candidate
print(total_votes)
print(candidate_options)
print(candidate_votes)

# Determine the percentage of votes for each candidate by looping
# Iterate through candidate list
for candidate_name in candidate_votes:
    # Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    # Calculate percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100
    # Print candidate name and percentage of votes
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine if the vote count is greater than the winning count
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_percentage = vote_percentage
        # Set winning candidate equal to the candidate name
        winning_candidate = candidate_name
winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------\n")
print(winning_candidate_summary)

# Create a filename variable to a path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open function with the w mode to write as a text file.
with open(file_to_save, "w") as txt_file:
    # Write counties to the new file.
    txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")
