import csv
import os 


csvfile = os.path.join("..", "python-challenge","PyPoll", "election_data.csv")   
Analysis = os.path.join ("..", "python-challenge","PyPoll","election_analysis.txt") 
# Declare Variables 
total_votes = 0 
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0


with open(csvfile,newline="", encoding="utf-8") as elections:

    csvreader = csv.reader(elections,delimiter=",") 

    
    header = next(csvreader)     

    
    for row in csvreader: 

      
        total_votes +=1

        
        if row[2] == "Khan": 
            khan_votes +=1
        elif row[2] == "Correy":
            correy_votes +=1
        elif row[2] == "Li": 
            li_votes +=1
        elif row[2] == "O'Tooley":
            otooley_votes +=1

 
candidates = ["Khan", "Correy", "Li","O'Tooley"]
votes = [khan_votes, correy_votes,li_votes,otooley_votes]


dict_candidates_and_votes = dict(zip(candidates,votes))
key = max(dict_candidates_and_votes, key=dict_candidates_and_votes.get)


khan_percent = (khan_votes/total_votes) *100
correy_percent = (correy_votes/total_votes) * 100
li_percent = (li_votes/total_votes)* 100
otooley_percent = (otooley_votes/total_votes) * 100

report = (
 f"Election Results \n"
 
 f"Total Votes: {total_votes}\n"
 
 f"Khan: {khan_percent:.3f}% ({khan_votes})\n"
 f"Correy: {correy_percent:.3f}% ({correy_votes})\n"
 f"Li: {li_percent:.3f}% ({li_votes})\n"
 f"O'Tooley: {otooley_percent:.3f}% ({otooley_votes})\n"
 
 f"Winner: {key}\n")

with open (Analysis , "w")as txt_file:
    txt_file.write(report)
