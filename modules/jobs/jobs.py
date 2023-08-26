# Module to add jobs

import csv
import os.path
import ast



# Jobs -> name, duration, frequency 



class Jobs:

	def __init__(self):

		self.FILENAME = "jobs.csv"



	'''
		Adds jobs that can be assigned to users

	'''
	def add_jobs(self, name, duration, frequency):

		data = [
			[name, duration, frequency]
		]

		done = False

		if not os.path.exists(self.FILENAME):

			with open(self.FILENAME, 'w', newline='') as jobscsv:
				csv_writer = csv.writer(jobscsv)
				csv_writer.writerow(["Name", "Duration", "Frequency"])
				csv_writer.writerows(data)
				done = True

		else:

			with open(self.FILENAME, 'a', newline='') as jobscsv:
				csv_writer = csv.writer(jobscsv)
				csv_writer.writerows(data)
				done = True

		
		return done



	'''
		Assigns jobs to users.

	'''
	def assign_jobs(self, workName, userName):


		data = self.generate_data(workName, userName)

		if data != []:
			if self.user_exists(userName):
				self.modify_data(data)
			else:
				self.prompt_no_user()

		else:
			if not self.user_exists(userName):
				self.prompt_no_user()



	'''
		PRIVATE

		Returns a list containing all the required changes in the CSV file

	'''
	def generate_data(self, workName, userName):

		data = []
		if self.work_exists(workName):
			with open('../users/users.csv', 'r') as csvfile:

				reader = csv.DictReader(csvfile)
				for row in reader:
					if userName == row['Name']:
						
						li = ast.literal_eval(row['Works'])
						li.append(workName)

						row['Works'] = str(li)

					data.append(row)
		else:
			self.prompt_no_work()

		return data




	'''
		PRIVATE

		Modifies the users.csv file with the required changes (adding jobs)

	'''

	def modify_data(self, data):

		with open('../users/users.csv', 'w') as csvfile:
			fieldnames = ["Name", "Email", "Works"]
			writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
			writer.writeheader()
			writer.writerows(data)

		print("Changed required data!")




	'''
		PRIVATE

		Returns a boolean specifying if the given work name exists in the database

	'''

	def work_exists(self, name):

		exists = False

		with open('./jobs.csv', 'r') as csvfile:

			reader = csv.DictReader(csvfile)

			for row in reader:
				if name == row['Name']:
					exists = True

		return exists



	'''
		PRIVATE

		Returns a boolean specifying if the given user name exists in the database

	'''
	def user_exists(self, name):

		exists = False

		with open('../users/users.csv', 'r') as csvfile:

			reader = csv.DictReader(csvfile)

			for row in reader:
				if name == row['Name']:
					exists = True

		return exists



	'''
		PRIVATE

		TODO: add action after no work is found in the database, preferably ask to create work

	'''

	def prompt_no_work(self):

		print("No work found")



	'''
		PRIVATE

		TODO: add action after no work is found in the database, preferably ask to create a new user


	'''

	def prompt_no_user(self):

		print("No user found")





test = Jobs()
test.assign_jobs("Laundry", "Swoyam")