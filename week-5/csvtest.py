import csv
file_path = "C:/Users/ipinu/OneDrive/Documents/S.YusufCOS102/week-5/GIG-logistics.csv"
with open(file_path, 'r') as csv_file:
    csv_reader = csv.reader(csv_file) 
    next(csv_reader)
    for line in csv_reader:
        print (line[0],line[1],line[2],line[3])
