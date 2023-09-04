import csv
with open("dados.csv", "r", newline="") as file:
                
                reader = csv.reader(file)
                for row in reader:
                        print(row[0])
