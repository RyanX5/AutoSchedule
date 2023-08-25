# Module to add jobs

import csv
import os.path



# Jobs -> name, duration, frequency 



class Jobs:

	def __init__(self, name, duration, frequency):

		self.name = name
		self.duration = duration
		self.frequency = frequency
		self.FILENAME = "jobs.csv"

	def add_jobs(self):

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


