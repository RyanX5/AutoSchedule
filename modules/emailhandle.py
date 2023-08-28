import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import csv
import ast

class EmailHandler:

	def __init__(self):

		self.FILENAME_CRED = "./modules/creds.txt"
		self.FILENAME_USERS = "./modules/users/users.csv"

	def start(self):
		

		_id = "autoschedule1@gmail.com"
		password = self.get_password()
		username = "AutoSchedule Bot"

		_to = self.get_recipients()
		subject = "You've got the following jobs assigned!"
		body = self.generate_content()

		

		for i in range(len(body)):

			msg = MIMEText(body[i], 'html')
			msg['Subject'] = subject
			msg['From'] = username
			msg['To'] = _to[i]

			server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
			server.ehlo()
			server.login(_id, password)
			server.sendmail(username, _to[i], msg.as_string())
			server.close()

			print("Email succesfully sent to: " + _to[i])

	def get_password(self):

		password = ""

		if not os.path.exists("./creds.txt"):
			print("Creds file not found. Set a password!")
			passw = str(input("Enter your password for the email address: "))

			with open("./creds.txt", 'w') as file:
				file.write(passw)

		with open("./creds.txt", 'r') as fileread:
			password = fileread.readline()

		print("Password: " + password)
		return password


	def get_recipients(self):

		emails = []

		if os.path.exists("./users/users.csv"):

			with open("./users/users.csv", 'r') as csvfile:

				reader = csv.DictReader(csvfile)

				for row in reader:

					emails.append(row['Email'])

		else:

			print("Error, no users found")

		print(emails)
		return emails


	def generate_content(self):

		content = []
		final_content = []

		if os.path.exists("./users/users.csv"):

			with open("./users/users.csv", 'r') as csvfile:

				reader = csv.DictReader(csvfile)

				for row in reader:

					content.append(ast.literal_eval(row['Works']))

		for work_list in content:
			to_add = "Following are the tasks assigned to you today: <br><br>"

			for work in work_list:
				to_add += "<b>" + work + "</b>" + '<br>'

			final_content.append(to_add)

	

		else:

			print("Error, no users found")

		#content = [["Laundry", "Work"], ["Cooking", "Laundry"]]
		#final = ["You've got the following: "]
		print(final_content)
		return final_content


		




e = EmailHandler()
e.start()


