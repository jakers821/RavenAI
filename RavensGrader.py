# DO NOT MODIFY THIS FILE.
#
# Any modifications to this file will not be used when grading your project.
# If you have any questions, please email the TAs.
#
#

import os
import sys
import csv
from Agent import Agent
from ProblemSet import ProblemSet

# Returns whether your Agent's answer is the correct answer. Your agent
# does not need to use this method; it is used to identify whether each
# problem is correct in main().
#
# Your agent does not need to use this method.
def outcome(truth, answer):
    if truth==answer:
        return "Correct"
    elif answer < 0:
        return "Skipped"
    else:
        return "Incorrect"

def something():
    answer_filename = "Problems" + os.sep + self.name + os.sep + problemName + os.sep + "ProblemAnswer.txt"

    with open(answer_filename) as fd:
        correctAnswer=int(self.getNextLine(fd))    

# The main driver file for Project2. You may edit this file to change which
# problems your Agent addresses while debugging and designing, but you should
# not depend on changes to this file for final execution of your project. Your
# project will be graded using our own version of this file.
def main():
    answers_file = sys.argv[1]

    answers = {}

    with open(answers_file) as fd:
        reader = csv.DictReader(fd)
        for row in reader:
            if row['ProblemSet'] in answers:
                answers[row['ProblemSet']][row['RavensProblem']] = int(row["Agent's Answer"])
            else:
                answers[row['ProblemSet']] = {row['RavensProblem']: int(row["Agent's Answer"])}


    results=open("ProblemResults.csv","w")
    results.write("Problem,Agent's Answer,Correct?,Correct Answer\n")

    setResults=open("SetResults.csv","w")      
    setResults.write("Set,Correct,Incorrect,Skipped\n")

    with open(os.path.join("Problems", "ProblemSetList.txt")) as fd0:
        for line0 in fd0:
            line0 = line0.rstrip()
            totals = {"Correct": 0, "Skipped": 0, "Incorrect": 0}
            with open(os.path.join("Problems", line0, "ProblemList.txt")) as fd1:
                for line1 in fd1:
                    line1 = line1.rstrip()
                    with open(os.path.join("Problems", line0, line1, "ProblemAnswer.txt")) as fd2:
                        truth = int(fd2.read())
                        ans = answers[line0][line1]
                        results.write("%s,%d,%s,%d\n" % (line1, ans, outcome(truth, ans), truth))
                        totals[outcome(truth, ans)] += 1
            setResults.write("%s,%d,%d,%d\n" % (line0, totals["Correct"], totals["Incorrect"], totals["Skipped"]))

    results.close()
    setResults.close()

if __name__ == "__main__":
    main()