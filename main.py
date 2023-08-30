from modules.users import users
from modules.jobs import jobs

def main():

	jobObj = jobs.Jobs()
	jobObj.list_jobs()


	userObj = users.Users()
	userObj.list_users()

if __name__ == "__main__":

	main()
