# Import required modules & functions
import csv
import os.path
import gc # Garbage Collector module to free up memory

class EmployeeManager:
    # constructor
    def __init__(self, id, name, position, salary, email):
        self.id = id
        self.name = name
        self.position = position
        self.salary = salary
        self.email = email

    def add_employee(self):        
        # save employee object to dictionary
        employee = {'ID' : self.id, 'Name' : self.name,'Position' : self.position,
                    'Salary' : self.salary, 'Email' : self.email}

        # open csv file and add a header if there is no header
        header = ['ID', 'Name', 'Position', 'Salary', 'Email']   
        
        with open('employees.csv', 'a+', newline='') as f:
            # check csv for header
            f.seek(0)
            csv_header = f.readline().strip().split(",")
            #print(csv_header)

            # Write header (if it doesn't exist) and data into csv file    
            writer = csv.DictWriter(f, fieldnames=header)
            
            # add header if it doesn't exist
            if csv_header != header:
                writer.writeheader()    
            
            # write data row to the csv file if the ID entry isn't duplicated
            employee_ids = []
            reader = csv.reader(f)
            for row in reader:
                employee_ids.append(int(row[0]))
                #print(employee_ids)
            
            if employee['ID'] in employee_ids:
                print(f"Employee ID: [{employee['ID']}] aready exists\nNot added to database")
            else:
                writer.writerow(employee)
                print(f"Employee ID: [{employee['ID']}] data is added to database")

        # Clear memory:
        del employee
        del header
        del csv_header
        del writer
        del employee_ids
        gc.collect()