import os
import csv

# Create file name
csvpath = os.path.join('.', 'Resources', 'election_data.csv')

# Declare lists
voter_ids = []
counties = []
candidates = []

# Read/load file into lists
with open(csvpath) as csvfile:
    # Drop header row
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        # Add voter id
        voter_ids.append(row[0])
        # Add county
        counties.append(row[1])
        #Add candidate
        candidates.append(row[2])

    # Total Votes
    total_votes = len(voter_ids)

    #Loop through candidates to count votes
    candidates_votes = dict()
    for candidate in candidates:
        if candidate in candidates_votes:
            candidates_votes[candidate] = candidates_votes[candidate]+1
        else:
            candidates_votes[candidate] = 1

    print(f"Election Results")
    print(f"------------------------------------------")
    print(f"Total Votes: {total_votes}")
    print(f"------------------------------------------")

    for candidate_name, candidate_votes in candidates_votes.items():
        percentage = "{:.0%}".format(candidate_votes/total_votes)
        print(f"{candidate_name}: {percentage} ({candidate_votes})")
    
    print(f"------------------------------------------")
    winner_name, winner_votes = max(candidates_votes.items(), key=lambda k: k[1])
    print(f"Winner: {winner_name}")

# Write new file
f = open("PyPoll.txt", "w")
f.write("Election Results \n")
f.write("--------------------------------------\n")
f.write(f"Total Votes: {total_votes} \n")
f.write("--------------------------------------\n")
for candidate_name, candidate_votes in candidates_votes.items():
    percentage = "{:.0%}".format(candidate_votes/total_votes)
    f.write(f"{candidate_name}: {percentage} ({candidate_votes}) \n")
f.write("--------------------------------------\n")
f.write(f"Winner: {winner_name} \n")
f.write("--------------------------------------\n")
f.close()