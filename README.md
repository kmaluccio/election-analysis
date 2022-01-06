# Election-Analysis

## Project Overview
A Colorado Board of Elections employee has asked for the following tasks to be completed on the election audit of a recent local congressional election.

1. Calculate the total number of received votes.
2. Get a complete list of candidates who received votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Voter turnout for each county.
7. The percentage of votes from each county out of the total count.
8. The county with the highest turnout


## Resources
- Data Source: All election data can be found in the csv file: [Election Results](https://github.com/kmaluccio/election-analysis/blob/main/Resources/election_results.csv)
- Software: Python3, Visual Studio Code

## Results
The results of the analysis (tasks 1-5) of this election are the following:

- There were 369,711 total votes cast in the congressional election
- The candidates were:
	- Charles Casper Stockham
	- Diana DeGette
	- Raymon Anthony Doane
- The candidate results were:
	- Charles Casper Stockham received 23% of the vote and 85,213 total votes
	- Diana DeGette received 73.8% of the vote and 272,892 total votes
	- Raymon Anthony Doane received 3.1% of the vote and 11,606 total votes
- Therefore, the winner of the election was:
	- Diane DeGette, receiving 73.8% of the vote and 272,892 total votes

The results of the analysis (tasks 6-8) of this election are below:
- There were three counties with voters in this election
- The percentage of vote and total votes per county are:
	- Jefferson County with 10.5% of the vote and 38,855 total votes
	- Denver County with 82.8% of the vote and 306,055 total votes
	- Arapahoe County with 6.7% of the vote and 24,801 total votes
- Therefore, the county with the highest turnout was:
	- Denver County with 82.8% of the vote

## Challenge Overview
The challenge for this project was to complete tasks 6, 7, and 8 found in the project overview. Python script was written in VS code using the data source file with election results. The code for this analysis can be found at: [PyPoll Challenge](https://github.com/kmaluccio/election-analysis/blob/main/PyPoll_Challenge.py). In this challenge, after analyzing the data based on each candidate, the data was analyzed based on each county where the votes took place.

## Challenge Summary
With the data provided for the election, this analysis has clearly found all counties where voters participated, all candidates with their total vote count and percentage of total votes, and lastly a winner of the election. There are a few simple ways to perform a similar analysis on another election using the same code. This is evident since the code pulls data from the CSV file, so as long as the new data is stored in a similar way to the election results given above, we can easily perform an analysis on any election. Two changes that need to be made are saving the new data file to the Resources folder and editing the file name in the script (line 9) to match the new data file name. Then, if you wanted to save this election analysis, you want to change the name of the file that we are writing in (line 11) so that there would be two text files in the analysis folder and we would have access to both analyses. Running this new python script will produce new output for another analysis of a different election. The results would output the counties and voting data from each county, the candidates and voting data for each candidate, and the winner of the election. Thus, this analysis can be done for any election using the same code with some edits to the data file and analysis text file.


