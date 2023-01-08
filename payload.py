import csv


payload = 0
flag = 0
lastrow = ""
count = 0

with open(f'cleaned_data2.csv', 'r') as input_file:#, open(f"shovel{i}.csv", 'w', newline='') as output_file:
    reader = csv.reader(input_file)
    for row in reader: 
        
        if row[5] == "Hauling" and row[6]!= '' and flag == 0 and row[6] != '0.0':
            
            if (float(row[6]) > (280+280) or float(row[6]) < 280/4):
                print(row)
            payload += float(row[6]) 
            flag = 1
            count += 1
        elif row[5] == "Dumping":
            flag = 0
            
            
print(str(payload) + " | " + str(payload/count))
            
    

          
          
