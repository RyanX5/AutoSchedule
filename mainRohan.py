# Main File to run everything
from modules.users import users
from modules.jobs import jobs

def main():
	jobObj = jobs.Jobs()
	userObj = users.Users()

	userObj.add_user("Rohan", "rohaniam777@gmail.com")

	if(jobObj.add_jobs("Cooking", "30 mins", "2")):
		print("Successfully added.")
	else:
		print("Error")

	# if(jobObj.add_jobs("Laundry", "5 mins", "1")):
	# 	print("Successfully added.")
	# else:
	# 	print("Error")

	# if(jobObj.add_jobs("Dishwashing", "15 mins", "1")):
	# 	print("Successfully added")
	# else:
	# 	print("Error")


	# jobObj.assign_jobs("Cooking", "Swoyam")
	# jobObj.assign_jobs("Laundry", "Swoyam")
	# jobObj.assign_jobs("Dishwashing", "Rohan")


if __name__ == "__main__":
	main()