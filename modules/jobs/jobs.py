# Module to add jobs

import csv
import os.path
import ast



# Jobs -> name, duration, frequency 



class Jobs:

	def __init__(self):

		self.FILENAME = "./modules/jobs/jobs.csv"
		self.FILENAME_USERS = "./modules/users/users.csv"




	def add_jobs(self, name, duration, frequency):

		done = False

		data = [name, duration, frequency]
		if os.path.exists(self.FILENAME):

			if not self.work_exists(name):

				self.add_jobs_to_file(data[0], data[1], data[2])
				done = True

			else:

				print("Work already exists")
				self.list_jobs()

		else:

			self.add_jobs_to_file(data[0], data[1], data[2])
			done = True

		return done


	'''
		Adds jobs that can be assigned to users

	'''
	def add_jobs_to_file(self, name, duration, frequency):

		data = [
			[name, duration, frequency]
		]

		

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
				

		
		print("Successfully added job: " + name)




	'''
		Assigns jobs to users.

	'''
	def assign_jobs(self, workName, userName):


		data = self.generate_data(workName, userName)

		if data != []:
			if self.user_exists(userName, "./modules/users/users.csv"):
				self.modify_data(data)
			else:
				self.prompt_no_user()

		else:
			if not self.user_exists(userName, "./modules/users/users.csv"):
				self.prompt_no_user()



	'''
		PRIVATE

		Returns a list containing all the required changes in the CSV file

	'''
	def generate_data(self, workName, userName):

		data = []

		# Checks if the work exists in the database
		if self.work_exists(workName):
			# Opens the users.csv file
			with open(self.FILENAME_USERS, 'r') as csvfile:

				reader = csv.DictReader(csvfile)

				for row in reader:
					# Goes through each row and checks if the names match
					if userName == row['Name']:
						
						# Converts the "Works" string value ("[]") to a list
						li = ast.literal_eval(row['Works'])

						# Appends the given work name to the list
						li.append(workName)

						# Sets the "Works" value of the row to a stringified list again
						row['Works'] = str(li)

					# Appends all the row values in the data list, accumulating changes	
					data.append(row)

		else:
			# If work not found in the database
			self.prompt_no_work()

		return data




	'''
		PRIVATE

		Modifies the users.csv file with the required changes (adding jobs)

	'''

	def modify_data(self, data):

		with open(self.FILENAME_USERS, 'w') as csvfile:
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

		with open(self.FILENAME, 'r') as csvfile:

			reader = csv.DictReader(csvfile)

			for row in reader:
				if name == row['Name']:
					exists = True

		return exists



	'''
		PRIVATE

		Returns a boolean specifying if the given user name exists in the database

	'''

	@staticmethod
	def user_exists(name, fileLocation):

		exists = False

		with open(fileLocation, 'r') as csvfile:

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



	'''
		PRIVATE

		TODO: add action after no work is found in the database, preferably ask to create a new user


	'''

	def delete_jobs(self, name):

		# modify jobs csv
		# go to user
		# check if the user has the job
		# if yes, get its ['works']
		# list it, remove the element
		# stringify it, add it again


		if self.work_exists(name):
			data = []
			with open(self.FILENAME, 'r') as csvfile:
				reader = csv.DictReader(csvfile)

				for row in reader:

					if row['Name'] != name:
						data.append(row)


			with open(self.FILENAME, 'w') as csvf:
				
				headers = ["Name", "Duration", "Frequency"]
				writer = csv.DictWriter(csvf, fieldnames=headers)
				writer.writeheader()
				writer.writerows(data)

			self.delete_work_from_user(name)

			print("Successfully deleted job: " + name)
			self.list_jobs()

		else:

			self.prompt_no_work()




	def list_jobs(self):

		with open(self.FILENAME, 'r') as csvfile:

			reader = csv.DictReader(csvfile)

			for row in reader:

				print(row)



	def delete_work_from_user(self, name):
		
		data = []
		users = []

		with open(self.FILENAME_USERS, 'r') as csvfile:
			reader = csv.DictReader(csvfile)

			for row in reader:

				if name in row['Works']:
					users.append(row['Name'])

					li = ast.literal_eval(row['Works'])
					li = [x for x in li if x!=name]
					row['Works'] = str(li)

				data.append(row)


		with open(self.FILENAME_USERS, 'w') as csvf:

			headers = ["Name", "Email", "Works"]

			writer = csv.DictWriter(csvf, fieldnames=headers)

			writer.writeheader()
			writer.writerows(data)

		for names in users:

			print("Deleted work: " + name + " from " + names)





# "ROhan", "asdasd", "['Cooking', Laundry, Laundry]"
# "ROhan", "asdasd", "['Cooking']"
# "ROhaasdn", "asdasasdd", "['Cooking', Laundry]"











