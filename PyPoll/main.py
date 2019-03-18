import os
import csv

#variables,list,dict
total_votes = 0
candidate_dict = {}
candidate_list = []


#choose where to read
election_csv = os.path.join('..','election.csv')
#check if file exists
#os.path.exists('election.csv') test returned true

with open(election_csv, newline='') as election:
    reader = csv.DictReader(election, delimiter = ",")

    #count voters
    for row in reader:
        total_votes += 1

        if row['Candidate'] not in candidate_dict:
            candidate_dict[row['Candidate']] = 0
        if row['Candidate'] in candidate_dict:
            candidate_dict[row['Candidate']] += 1

    #list and pair candidates with votes
    candidates = []
    votes = []
    for k, v in candidate_dict.items():
        candidates.append(k)
        votes.append(v)
    
    candidate_list = list(zip(votes, candidates))

#print results 
print("Election Results:")
print("-----------------------")
print(f'Total Votes: {total_votes}')
print(f"\n\
{candidate_list[0][1]}: {format(float(candidate_list[0][0] / total_votes * 100), '.3f')}% ({candidate_list[0][0]})\n\
{candidate_list[1][1]}: {format(float(candidate_list[1][0] / total_votes * 100), '.3f')}% ({candidate_list[1][0]})\n\
{candidate_list[2][1]}: {format(float(candidate_list[2][0] / total_votes * 100), '.3f')}% ({candidate_list[2][0]})\n\
{candidate_list[3][1]}: {format(float(candidate_list[3][0] / total_votes * 100), '.3f')}% ({candidate_list[3][0]})\n\
-------------------------\n\
Winner: {candidate_list[0][1]}\n\
-------------------------")

#output file
txtfile = os.path.join('..','newfile2.txt')

#open file and specify content
with open('newfile2.txt', 'w') as txtfile:
#write to text
    txtfile.write("Election Results:\n")
    txtfile.write("-----------------------\n")
    txtfile.write(f'Total Votes: {total_votes}\n')
    txtfile.write(f"\n\
{candidate_list[0][1]}: {format(float(candidate_list[0][0] / total_votes * 100), '.3f')}% ({candidate_list[0][0]})\n\
{candidate_list[1][1]}: {format(float(candidate_list[1][0] / total_votes * 100), '.3f')}% ({candidate_list[1][0]})\n\
{candidate_list[2][1]}: {format(float(candidate_list[2][0] / total_votes * 100), '.3f')}% ({candidate_list[2][0]})\n\
{candidate_list[3][1]}: {format(float(candidate_list[3][0] / total_votes * 100), '.3f')}% ({candidate_list[3][0]})\n\
-------------------------\n\
Winner: {candidate_list[0][1]}\n\
-------------------------")
    



        
