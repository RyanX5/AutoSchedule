import csv
import os
from ..jobs.jobs import Jobs
import ast

class Users:

    def __init__(self) -> None:
        self.FILENAME = "./modules/users/users.csv"

    def add_user(self, name, email):
        if not Jobs.user_exists(name, self.FILENAME):
            works = []
            self.add_to_file(name, email, works)

        else:
            print("User already exists: " + name)



    def add_to_file(self, name, email, works):
        header = ["Name", "Email", "Works"]
        data = [name, email, works]

        if os.path.exists(self.FILENAME):
            with open(self.FILENAME, 'a', newline="") as file:
                # file.write(self.name + "," + self.email + ",")
                
                # for work in self.works:
                #     file.write(work + ",")
                
                    csvwriter = csv.writer(file)
                    csvwriter.writerow(data)
        else:
            with open(self.FILENAME, 'w',newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(header)
                csvwriter.writerow(data)

    def add_work(self, work):
        self.works.append(work)

    '''
		Return True when the user is deleted and False if the user doesn't exist
	'''
    def delete_user(self, name):
        if not Jobs.user_exists(name, self.FILENAME):
            return False
		    
        data = []
        
        with open(self.FILENAME, 'r') as file:
            reader = csv.DictReader(file)

            for row in reader:
                if name != row['Name']:
                    data.append(row)

        header = ['Name', 'Email', 'Works']

        if os.path.exists(self.FILENAME):
            with open(self.FILENAME, 'a', newline="") as file:  
                csvwriter = csv.writer(file)
                csvwriter.writerows(data)
        else:
            with open(self.FILENAME, 'w',newline="") as file:
                csvwriter = csv.writer(file)
                csvwriter.writerow(header)
                csvwriter.writerows(data)







