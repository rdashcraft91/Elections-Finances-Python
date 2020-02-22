import os
import csv

csvpath = os.path.join('..', 'python-challenge', 'PyElections', 'ElectionData.csv')

with open(csvpath) as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=',')
    
    csv_header = next(csvreader)
    
    csvlist = list(csvreader)

    print("Houston Mayoral Election Results")
    print("-------------------------------------")

    Candidate = []

    for row in csvlist:
        if row[0] not in Candidate:
            Candidate.append(row[0])   
    
    CanCount = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] 
    
    for row in csvlist:
        if row[0] == Candidate[0]:
            CanCount[0] += 1
        if row[0] == Candidate[1]:
            CanCount[1] += 1
        if row[0] == Candidate[2]:
            CanCount[2] += 1
        if row[0] == Candidate[3]:
            CanCount[3] += 1
        if row[0] == Candidate[4]:
            CanCount[4] += 1
        if row[0] == Candidate[5]:
            CanCount[5] += 1
        if row[0] == Candidate[6]:
            CanCount[6] += 1
        if row[0] == Candidate[7]:
            CanCount[7] += 1
        if row[0] == Candidate[8]:
            CanCount[8] += 1
        if row[0] == Candidate[9]:
            CanCount[9] += 1
        if row[0] == Candidate[10]:
            CanCount[10] += 1
        if row[0] == Candidate[11]:
            CanCount[11] += 1

  #  print(CanCount)
    
    CanPercent = [((CanCount[0]/241032)), (CanCount[1]/(241032)), (CanCount[2]/(241032)), (CanCount[3]/(241032)), (CanCount[4]/(241032)), (CanCount[5]/(241032)), (CanCount[6]/(241032)), (CanCount[7]/(241032)), (CanCount[8]/(241032)), (CanCount[9]/(241032)), (CanCount[10]/(241032)), (CanCount[11]/(241032))]
    
   # print(CanPercent)
    
    Results = zip(Candidate, CanCount, CanPercent)
    
#     print(Results)
    
    print("Total Votes: 241032")
    print("-------------------------------------")
    
    for row in Results:
        print(f'{row[0]}: {row[2]:.2%} ({row[1]})')
    
    print("-------------------------------------")
    print("1st Advancing Candidate: Sylvester Turner")
    print("2nd Advancing Candidate: Tony Buzbee")

output_path = os.path.join("..", "python-challenge", "PyElections", "election_results.csv")

with open(output_path, 'w') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile, delimiter=',')

    # Write the first row (column headers)
    csvwriter.writerow(["Houston Mayoral Election Results"])
    csvwriter.writerow(["-----------------------------------"])
    csvwriter.writerow(["Total Votes: 241032"])
    csvwriter.writerow(["-----------------------------------"])
    csvwriter.writerow(["Bill King: 14.01% (33772)"])
    csvwriter.writerow(["Demetria Smith: 0.70% (1694)"])
    csvwriter.writerow(["Derrick Broze: 0.28% (686)"])
    csvwriter.writerow(["Dwight A. Boykins: 5.90% (14212)"])
    csvwriter.writerow(["Johnny “J.T.” Taylor: 0.23% (555)"])
    csvwriter.writerow(["Kendall Baker: 0.41% (982)"])
    csvwriter.writerow(["Naoufal Houjami: 0.23% (560)"])
    csvwriter.writerow(["Roy J. Vasquez: 0.65% (1556)"])
    csvwriter.writerow(["Sue Lovell: 1.22% (2932)"])
    csvwriter.writerow(["Sylvester Turner: 46.38% (111789)"])
    csvwriter.writerow(["Tony Buzbee: 28.78% (69361)"])
    csvwriter.writerow(["Victoria Romero: 1.22% (2933)"])
    csvwriter.writerow(["-------------------------------------"])
    csvwriter.writerow(["1st Advancing Candidate: Sylvester Turner"])
    csvwriter.writerow(["2nd Advancing Candidate: Tony Buzbee"])