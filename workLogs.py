#general data JSON
#analyze data 

"""
daily = {
	date : "1/21/2020"
	action : "base"
	misc : ""
}
"""
import json, os, pickle
import matplotlib.pyplot as plt 
from os import path
from datetime import date
from termcolor import colored, cprint

# def terminalGraph(data):
# 	tfig = tpl.figure()
# 	x_Values = [0, 1, 2, 3, 4, 5]
# 	tfig.hist(x_Values, data, grid=[30, 55], force_ascii=True)
# 	tfig.show()

def drawPie(data):
	labels = ('downtime', 'passion projects', 'AWS', 'Meetings', 'Networking', 'Not related team work')
	explode=(0, 0, 0.1, 0, 0, 0)
	fig1, ax1 = plt.subplots()
	ax1.pie(data, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow=True, startangle=90)
	ax1.axis('equal')
	plt.savefig('charts/' + date.today().isoformat() + "pie.png")

def dumpList(hList):
	with open('hours.pkl', 'wb') as f:
		pickle.dump(hList, f)

def dailyWork():
	cprint(date.today(), "yellow")
	print("""
	Data General Guide 
	0: Downtime
	1: Unrelated Work, "Passion Project"
	2: AWS (Team Work)
	3: Meetings
	4: Networking
	5: Not Related Team Work
		""")
	cprint("Ex: 024 \nSo you had downtime, aws and Networking", 'magenta', attrs=['bold'])
	action = input("Enter Actions as an array: ")
	if action == 9: #9 for manual reset
		os._exit(0)
	options = [0] * 6
	#Creates Iterable
	for num in action:
		options[int(num)] += 1
	if(path.exists("hours.pkl")): 
		with open("hours.pkl", 'rb') as f:
			savedHours = pickle.load(f)
		newHours = [x + y for x, y in zip(options, savedHours)]
		dumpList(newHours) #check overWrite
	else:
		dumpList(options)
		print("\nFile Doens't Exist, created file hours.txt")

def writeJson():
	cprint("Busy day huh?", "green")
	tasks = input("What did you do today: ")
	goal = input("Future goals: ")
	misc = input("Any other things: ")
	dailyInput = {
		'work' : tasks,
		'goals' : goal,
		'miscs' : misc
	}
	today = date.today().isoformat()
	with open('jsonFiles/' + today + ".json", 'w') as f:
		json.dump(dailyInput, f)

def titleScreen():
	os.system('clear')
	text = colored("""*********************************************************** Another Day of Work Done ***********************************************************""", 'green', attrs=['blink', 'underline'])
	print(text)


titleScreen()
cprint("Enter '0' to quit \n", 'red')
choice = -1
while choice != '0':
	if choice == 1:
		cprint("What did you do at work today?", "green")
		dailyWork()
	elif choice == 2:
		writeJson()
	elif choice == 3:
		cprint("Generating Graphs...", "green", attrs=['blink'])
		with open("hours.pkl", 'rb') as f:
			data = pickle.load(f)
		drawPie(data)
	elif choice == 0:
		exit()
	choice = int(input("Enter 1 to enter daily work: \n \nEnter 2 for more detailed entry:\n \nEnter 3 to show general usuage time \n"))







