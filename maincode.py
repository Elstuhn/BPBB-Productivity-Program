import time
import platform
import typing
from datetime import datetime
import pickle
class User:
    def __init__(self, username : str):
		self.user = username
		self.companion = "Pypy The Python"
		self.productivity = 0
		self.weeklyproductivity = [0]*7
		self.lastweekproductivity = 0
		self.title = "Lazy and fat"
		self.check = False
		
def calcstats():
	sumofproductivity = sum(user.weeklyproductivity)
	compareweek = (sumofproductivity//user.lastweekproductivity)*100
	print(f"Your productivity this week was {compareweek}% of last week's productivity.")
	
	
		
def timecheck():
	global check #check for if weekly stats have been printed out yet or not
	now = datetime.now()
	day = int(now.strftime("%w"))-1
	if day != 0:
		user.check = False
	elif check:
		return
	else:
		user.check = True
		print(f"{user.companion}: Hey {user.user}! The weekly statistics are ready!")
		
		
	
		
try:
	open("userinfo", "x")
	open("userinfo", "x").close()
	username = input("It seems like you are new here! Please enter your name.\n")
	user = User(username)
	print(f"{user.companion}: Hello {user.user}! I shall be your companion for now until you get enough tokens and get a new one! ^_^"
	print(f"{user.companion}: This is a program to make you productive! I shall be here to help you whenever you need help!")
	print(f"{user.companion}: You can see all the commands later, but I'll tell you some things first, whenever you do something productive, you get an amount of tokens depending on different conditions\
	, you can use those tokens to get stuff like companions, eggs and titles")
	
except:
	with open("userinfo", "rb") as fileread:
		user = pickle.load(fileread)

print("Hello
