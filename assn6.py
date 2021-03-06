#!/usr/bin/env python
"""
ITS 3210 Introduction to Scripting Languages
Governor's State University
David Shelton

Assignment 6

Create a script that performs the following tasks:

1. Ask the user for a numeric score using raw_input()
2. Convert the user-supplied score into an integer
3. Return the letter grade for the score in a user-friendly sentence (use the grading
   scale in the syllabus)
4. Modify the code you wrote in steps 1-3 so that the script continues asking for a 
   score until the user types 'end' instead of a score
5. Every time the user enters a score, save the score in a list
6. Convert step 1 into its own function that it returns the user input
7. Convert step 3 into its own function so that it returns the letter grade
8. Modify the program so that the user can enter as many scores as they'd like (until
   they type 'end'), and instead of showing the letter grade immediately, wait until
   the user has typed all of the scores then return formatted output showing each score
   and its letter grade at the end. Sort the list from low to high scores before 
   displaying them. The final output should look similar to this (with the scores you
   enter). Be sure to test entering the minimum and maximum scores for different grades
   such as 90, 79, and 60:

Score  Grade
-----  -----
    0      F
   72      C
   84      B
   91      A
  100      A
  
9. Print the lowest score and corresponding letter grade in a user-friendly sentence.
10. Create a dictionary with student names and scores, similar to this (use any names
    and scores you want):
    
student_dictionary = {
    "John Doe": 65,
    "Jane Doe": 77,
    "Bob Smith": 100,
    "Amy Jones": 99
}

11. Using the function created in step 7, loop through the dictionary and print a 
    user-friendly sentence with each student's name, score, and corresponding letter grade
"""
import sys

run = True
Allgrades = []
students = {
    "Eric Bloom": 81,
    "Buck Dharma": 77,
    "Richie Castellano": 100,
    "Jules Radino": 99,
	"Kasim Sulton": 85
}

def ask():
	print "Please enter a score: "
	score = raw_input("> ")
	if score == "end":
		return False
	else:
		GetPutValue(score)

def GetPutValue(x):	
	row = []
	x = int(x)
	grade(x)
	z = grade(x)
	row.append(x)
	row.append(z)
	Allgrades.append(row)
	
	
def grade(score):
	if score >=90:
		letter = 'A'
	elif score >=80:
		letter = 'B'
	elif score >=70:
		letter = 'C'
	elif score >=60:
		letter = 'D'
	elif score >=0:
		letter = 'F'
	else: 
		print "Invalid score."
		ask()
	return letter

def SortIt(x):
	for i,j in sorted(x):
		print "%5s  %5s" % (i,j)	

while run != False:
	ask()
	run = ask()

print "\nScore  Grade"	
print "-----  -----"
SortIt(Allgrades)	

p,q = min(Allgrades)
print "The lowest score is %s %s.\n" % (p,q)

it = iter(sorted(students.iteritems()))

def StudentGrades():
	L = "Students"
	print "%-18s Score Grade" % L 
	print "-" * 18, "----- -----"
	for i in students:
		a,j = it.next()
		grade(j)
		z = grade(j)
		print "%-18s %5s %5s" % (a,j,z)

StudentGrades()
print "\n"
	
	


