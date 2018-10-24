import csv

with open('surveyresults.csv', 'r') as csv_file: #open original file to be read
    csv_reader = csv.reader(csv_file) #creating csv file variable and using method to read file
    for line in csv_reader:
        print(line)




    #with open('new_names.csv', 'w') as new_file: #open new file for writing
       # csv_writer = csv.writer(new_file, delimiter = '-') #csv writer and variable

     #   for line in csv_reader:
         #   csv_writer.writerow(line) #writing from old file into new file with new delimiter









