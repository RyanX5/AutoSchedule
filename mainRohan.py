# Main File to run everything
from modules.users import users
from modules.jobs import jobs

def main():
	jobObj = jobs.Jobs()
	userObj = users.Users()

	# if(jobObj.add_jobs("Cooking", "30 mins", "2")):
	# 	print("Successfully added.")
	# else:
	# 	print("Error")

	# jobObj.assign_jobs("Laundry", "Rohan")
	# jobObj.assign_jobs("Laundry", "Rohan")

    jobObj.delete_jobs("Laundry")

	# if(jobObj.add_jobs("Laundry", "30 mins", "2")):
	# 	print("Successfully added.")
	# else:
	# 	print("Error")

	# print(userObj.delete_user("Rohan"))

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
