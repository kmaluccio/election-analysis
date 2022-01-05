# The data we need to retrieve:
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

# Open the election results, read the file.
with open(file_to_load) as election_data:

    # Read the file object with reader function.
    file_reader = csv.reader(election_data)
    # Read and print header row.
    headers = next(file_reader)
    print(headers)

# Create a filename variable to a path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Use the open function with the w mode to write as a text file.
with open(file_to_save, "w") as txt_file:
    # Write counties to the new file.
    txt_file.write("Counties in the Election\n----------------------\nArapahoe\nDenver\nJefferson")
