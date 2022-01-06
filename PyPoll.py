# Import the datetime class from the datetime module
# import datetime as dt
# Get and print the present time
# now = dt.datetime.now()
# print("The time right now is ", now)

# Import csv and os modules
import os
import csv
# Assign a variable for the file to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Create a filename variable to a path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Total vote counter
total_votes = 0
# Initialize candidates list
candidate_options = []
# Declare empty dictionary for total votes per candidate and to print all results
candidate_votes = {}
candidate_results = ()
# Initialize variables for winning candidate and count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results, read the file
with open(file_to_load) as election_data:

    # Read the file object with reader function
    file_reader = csv.reader(election_data)
    # Read header row
    headers = next(file_reader)

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

with open(file_to_save, "w") as txt_file:
    # print out election results and write it to the file
    election_results = (
        f"\nElection Results\n"
        f"------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file
    txt_file.write(election_results)

    # Determine the percentage of votes for each candidate
    # Iterate through candidate list
    for candidate_name in candidate_votes:
        # Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # Calculate percentage of votes
        vote_percentage = float(votes) / float(total_votes) * 100
        # Store candidate name and percentage of votes
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
        # Print each candidate, voter count, and percentage of votes
        print(candidate_results)
        # Save the candidate results to text file
        txt_file.write(candidate_results)
        # Determine if the vote count is greater than the winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_percentage = vote_percentage
            # Set winning candidate equal to the candidate name
            winning_candidate = candidate_name
    # Store winning candidate info
    winning_candidate_summary = (
    f"-----------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-----------------------\n")
    print(winning_candidate_summary)
    # Save winning info to text file
    txt_file.write(winning_candidate_summary)
# These prints check total votes, all candidates, total votes per candidate
# print(total_votes)
# print(candidate_options)
# print(candidate_votes)