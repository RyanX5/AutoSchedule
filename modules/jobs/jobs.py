# Module to add jobs

import csv
import os.path



# Jobs -> name, duration, frequency 



class Jobs:

	def __init__(self):

		# self.name = name
		# self.duration = duration
		# self.frequency = frequency
		self.FILENAME = "jobs.csv"

	def add_jobs(self, name, duration, frequency):

		data = [
			[self.name, self.duration, self.frequency]
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


	def assign_jobs(self, name, userName):

		# access users.csv file
		# look for name == row['Name']
		# modify the row['work']


		with open('../users/users.csv', 'r') as csvfile:

			reader = csv.DictReader(csvfile)

			for row in reader:

				print(row)




test = Jobs()
test.assign_jobs("Rohan", "Laundry")