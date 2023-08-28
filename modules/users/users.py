import csv
import os
from ..jobs.jobs import Jobs
import ast

class Users:

    def __init__(self) -> None:
        self.FILENAME = "./modules/users/users.csv"

    def add_user(self, name, email):
        works = []
        if os.path.exists(self.FILENAME):
            if not Jobs.user_exists(name, self.FILENAME):
                
                self.add_to_file(name, email, works)

            else:
                print("User already exists: " + name)

        else:
            self.add_to_file(name, email, works)
        




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
                
        print("User successfully added: " + name)

    def add_work(self, work):
        self.works.append(work)

    '''
		Return True when the user is deleted and False if the user doesn't exist
	'''
    def delete_user(self, name):
        if not Jobs.user_exists(name, self.FILENAME):
            return "User doesn't exist: " + name

        else:    
            data = []
            
            with open(self.FILENAME, 'r') as file:
                reader = csv.DictReader(file)

                for row in reader:
                    if name != row['Name']:
                        data.append(row)

            with open(self.FILENAME, 'w') as file:
                fieldnames = ["Name", "Email", "Works"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(data)

            return "User successfully removed: " + name

    def list_users(self):

        print("\n\nLIST OF USERS: \n")

        with open(self.FILENAME, 'r') as csvfile:

            reader = csv.DictReader(csvfile)

            for row in reader:

                print(row)







