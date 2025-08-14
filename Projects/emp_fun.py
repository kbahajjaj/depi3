# Import required modules & functions
import csv
import os.path
import gc # Garbage Collector module to free up memory


def search_employee(id):
    with open('employees.csv', 'r') as f:
        reader = csv.reader(f)
        header = f.readline().strip().split(",")
        #next(reader) # skip header row
        found = False # default state of search
        for row in reader:
            if id == int(row[0]):
                found = True
                print(f"{'-' * 100}")
                print(f"{header[0].ljust(5)}{header[1].ljust(25)}{header[2].ljust(25)}{header[3].ljust(10)}{header[4]}")
                print(f"{'-' * 100}")
                print(f"{row[0].ljust(4)}{row[1].ljust(25)}{row[2].ljust(25)}{row[3].ljust(10)}{row[4]}")
                break
        if not found:
            print(f"Employee ID: [{id}] not found in database")

def view_employees():
    with open('employees.csv', 'r') as f:
        
        # create a csv.reader object
        csv_reader = csv.reader(f)
        header = f.readline().strip().split(",")
        #print(csv_reader)

        # use a loop to iterate over each row in the csv file
        #employee_rows = []
        print(f"{'-' * 100}")
        print(f"{header[0].ljust(5)}{header[1].ljust(25)}{header[2].ljust(25)}{header[3].ljust(10)}{header[4]}")
        print(f"{'-' * 100}")
        for row in csv_reader:
            print(f"{row[0].ljust(5)}{row[1].ljust(25)}{row[2].ljust(25)}{row[3].ljust(10)}{row[4]}")            

def clear_all_data():
    filename = "employees.csv"
    f = open(filename, "w+")
    f.close()
    print("DataBase content has been TOTALLY cleared!\nThank You")

def delete_employee(id):
    with open('employees.csv', 'r', newline='') as f:
        f.seek(0)
        header = f.readline().strip().split(",")
        reader = csv.reader(f)
        found = False # default state of search
        rows = [header] # keep the header for the output file
        
        for row in reader:
            if id == int(row[0]):
                found = True
            else:
                rows.append(row)
        #print(rows)
    with open('employees.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(rows)
                #print(f"{header[0].ljust(4)}{header[1].ljust(25)}{header[2].ljust(25)}{header[3].ljust(10)}{header[4]}")
                #print(f"{row[0].ljust(4)}{row[1].ljust(25)}{row[2].ljust(25)}{row[3].ljust(10)}{row[4]}")
    if not found:
        print(f"Can't Delete Employee ID: [{id}], not found in database")
    else:
        print(f"Employee ID: [{id}] was successfuly deleted from database")

    # Clear memory:
    del reader
    del header
    del rows
    del writer
    gc.collect()

def update_employee(id, updates):
    updates.insert(0, id)
    with open('employees.csv', 'r', newline='') as f:
        f.seek(0)
        header = f.readline().strip().split(",")
        reader = csv.reader(f)
        found = False # default state of search
        rows = [header] # keep the header for the output file
        
        for row in reader:
            if id == int(row[0]):
                found = True
                if "" in updates:
                    index_of_empty = updates.index("")
                    updates[index_of_empty] = row[index_of_empty]
                rows.append(updates)
            else:
                rows.append(row)

    with open('employees.csv', 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(rows)
                #print(f"{header[0].ljust(4)}{header[1].ljust(25)}{header[2].ljust(25)}{header[3].ljust(10)}{header[4]}")
                #print(f"{row[0].ljust(4)}{row[1].ljust(25)}{row[2].ljust(25)}{row[3].ljust(10)}{row[4]}")
    if not found:
        print(f"Can't Update Data for Employee ID: [{id}], not found in database")
    else:
        print(f"Employee ID: [{id}] data was successfuly updated in database")

    # Clear memory:
    del reader
    del header
    del rows
    del writer
    del updates
    gc.collect()