# Test file to test jobs.py


import jobs
import csv

class TestJobs:

	def __init__(self):

		pass

	def test_add_jobs(self):

		jobsObj = jobs.Jobs("Cleaning", "30", "twice")
		jobsObj.add_jobs()
		# print("added jobs")

		# self.assertEqual(jobsObj.add_jobs(), 'new CSV file', 'incorrect')


	# def test_csv_read(self):
	# 	strin = ""
	# 	with open("jobs.csv", 'r') as csvfile:
	# 		reader = csv.DictReader(csvfile)
	# 		# print(dir(reader))
	# 		for row in reader:
	# 			strin += row['Name']
		
	# 	li = list(strin)
	# 	print(li)




test = TestJobs()
# test.test_add_jobs()
test.test_csv_read()

