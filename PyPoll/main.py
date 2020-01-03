import os
import csv

#create funtion that will show three decimals on a calculation
def three_decimals(number):
    return ('%.3f' % (number))

#find file with important information
csvdir = os.chdir('/Users/ethan_martin95/Documents/Georgia-Tech-Bootcamp-PULL/GT-ATL-DATA-PT-12-2019-U-C/Homework/03-Python/Instructions/PyPoll/Resources')
csvpath_r = os.path.join('election_data.csv')

#read in csv file
with open(csvpath_r, newline='') as csvfile_r:
    csvreader = csv.reader(csvfile_r, delimiter=',')
#identify the header
    csvheader = next(csvreader)

#initialize variables and lists
    voter_counter = 0
    candidate_list = []
    vote_count_list = []

#loop through csv file
    for row in csvreader:
#tally the total number of voters
        voter_counter += 1

#if you see a new candidate, create a new entry for them in the candidate list and start a tally for their Votes
        if row[2] not in candidate_list:
            candidate_list.append(row[2])
            vote_count_list.append(1)
#If you see a "captured" candidate, add a tally to their place in the vote list
        else:
            index = candidate_list.index(row[2])
            vote_count_list[index] += 1

#Print results
    print('Election Results')
    print('-------------------------')
    print(f'Total Votes: {voter_counter}')
    print('-------------------------')

    for entry in range(len(candidate_list)):
        print(f'{candidate_list[entry]}: {three_decimals(100*vote_count_list[entry]/voter_counter)}% ({vote_count_list[entry]})')

    print('-------------------------')
    print(f'Winner: {candidate_list[vote_count_list.index(max(vote_count_list))]}')
    print('-------------------------')

#create new text file
    textdir = os.chdir('/Users/ethan_martin95/Documents/Georgia-Tech-Bootcamp-PUSH/Python-Challenge/PyPoll')
    textpath_w = os.path.join('Py_Poll_Output.txt')

#write data to the new text file
    with open(textpath_w, 'w') as textfile_w:
        textfile_w.write('Election Results\n')
        textfile_w.write('-------------------------\n')
        textfile_w.write(f'Total Votes: {voter_counter}\n')
        textfile_w.write('-------------------------\n')

        for entry in range(len(vote_count_list)):
            textfile_w.write(f'{candidate_list[entry]}: {three_decimals(100*vote_count_list[entry]/voter_counter)}% ({vote_count_list[entry]})\n')

        textfile_w.write('-------------------------\n')
        textfile_w.write(f'Winner: {candidate_list[vote_count_list.index(max(vote_count_list))]}\n')
        textfile_w.write('-------------------------\n')
