import csv
import os

class Users:

    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email
        self.works = []
        self.FILENAME = "./modules/users/users.csv"
        self.add_to_file()

    # def __init__(self, name, email) -> None:
    #     self.name = name
    #     self.email = email

    def add_to_file(self):
        header = ["Name", "Email", "Works"]
        data = [self.name, self.email, self.works]

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




