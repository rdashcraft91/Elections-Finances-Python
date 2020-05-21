import os
import csv

csvpath = os.path.join('..', 'python-challenge', 'PyElections', 'ElectionData.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    csvlist = list(csvreader)

    # print(csvlist)

    #Total Vote Counter
    total_votes = 0
    
    #Candidate Options and Vote Counter
    candidate = []
    candidate_votes = {}

    # For each row...
    for vote in csvlist:

        # Add to the total vote count
        total_votes = total_votes + 1

        # Extract the candidate name from each row
        candidate_name = vote[0]

        # If the candidate does not match any existing candidate...
        # (In a way, our loop is "discovering" candidates as it goes)
        if candidate_name not in candidate:

            # Add it to the list of candidates in the running
            candidate.append(candidate_name)

            # And begin tracking that candidate's voter count
            candidate_votes[candidate_name] = 0

        # Then add a vote to that candidate's count
        candidate_votes[candidate_name] = candidate_votes[candidate_name] + 1

    sorted_cands = sorted(candidate_votes.items(), key=lambda kv: kv[1], reverse=True)

    def election_list():
        for key, value in sorted_cands:
            print(f'{key}: {"{:.2%}".format(value/total_votes)}% ({value})')

    def election_data():
        for key, value in sorted_cands:
            f'{key}: {"{:.2%}".format(value/total_votes)}% ({value})'

    def print_election(): 
        election_results = (
            f"\n\nElection Results\n"
            f"-------------------------\n"
            f"Total Votes: {total_votes}\n"
            f"-------------------------\n"
            )
        print(election_results, end="")
        election_list()
        print("-------------------------")
        print(f"Advancing First Candidate: {sorted_cands[0][0]}")
        print(f"Advancing Second Candidate: {sorted_cands[1][0]}")
    
    print_election()

output_path = os.path.join("..", "python-challenge", "PyElections", "election_results.csv")

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(['candidate', 'vote_percentage', 'vote_total'])
    for key, value in sorted_cands:
        csvwriter.writerow([key, "{:.2%}".format(value/total_votes), value])