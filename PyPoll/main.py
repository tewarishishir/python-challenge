import os
import csv

inputelectiondata = os.path.join('Resources', 'election_data.csv')

def read_election_data_csv(inputelectiondata):
    with open(inputelectiondata, 'r') as electiondatacsv:
        csvreader = csv.reader(electiondatacsv, delimiter = ',')
        next(electiondatacsv, None)

        total_votes = 0
        votedict = {}

        for row in csvreader:
            total_votes += 1
            if row[2] in votedict:
                votecount = votedict[row[2]]
                votedict[row[2]] = votecount+1
            else:
                votedict[row[2]] = 1
    
    winner_value = max(votedict.values())
    winner_name = {key for key, value in votedict.items() if value == winner_value }

    return votedict, winner_name, total_votes

def print_votes(dictoutput, calc = None):
    for key,value in dictoutput.items():
        print(key+":", "{0:.3f}%".format(value*100.0/calc),"("+str(value)+")")
        
def write_output_csv(outputcsv):
    with open(outputcsv, 'w') as outputfile:
        outputfile.write("Election Results"+ os.linesep)
        outputfile.write("--------------------------------"+ os.linesep)
        outputfile.write("Total Votes: "+ str(vote_count)+ os.linesep)
        outputfile.write("--------------------------------"+ os.linesep)
        for key,value in votedictout.items():
            outputfile.write(key+": "+ "{0:.3f}%".format(value*100.0/vote_count)+" ("+str(value)+")"+ os.linesep)
        outputfile.write("--------------------------------"+ os.linesep)
        outputfile.write("Winner: " + list(winner)[0]+ os.linesep)
        outputfile.write("--------------------------------"+ os.linesep)
        outputfile.close()


outputcsv = "output_election.txt"
votedictout, winner, vote_count = read_election_data_csv(inputelectiondata)
print('Election Results')
print("--------------------------------")
print('Total Votes: '+ str(vote_count))
print("--------------------------------")
print_votes(votedictout, vote_count)
print("--------------------------------")
print("Winner: " + list(winner)[0])
print("--------------------------------")
write_output_csv(outputcsv)