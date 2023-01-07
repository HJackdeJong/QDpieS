import json
count = 0.0

for i in range(10):
    with open(f"C:\\Users\\kalel\\OneDrive\\Desktop\\data_group{i}.json", 'r') as file:
        data = json.load(file)

    # print(len(data['TIMESTAMP']), end=" | ")
    # print(len(data['GPSNORTHING']), end=" | ")
    # print(len(data['GPSEASTING']), end=" | ")
    # print(len(data['GPSELEVATION']), end=" | ")
    # print(len(data['FUEL_RATE']), end=" | ")
    # print(len(data['STATUS']), end=" | ")
    # print(len(data['PAYLOAD']), end=" | ")
    # print(len(data['TRUCK_ID']), end=" | ")
    # print(len(data['TRUCK_TYPE_ID']), end=" | ")
    # print(len(data['SHOVEL_ID']), end=" | ")
    # print(len(data['DUMP_ID']))  


    for i in range(len(data['PAYLOAD'])):
        if str(i) in data['PAYLOAD']:
            if type(data['PAYLOAD'][str(i)]) == float:
                count += data['PAYLOAD'][str(i)]
                print(data['PAYLOAD'][str(i)])
                print(count)

            print(data['TIMESTAMP'][str(i)], end=" | ")
            print(data['GPSNORTHING'][str(i)], end=" | ")
            print(data['GPSEASTING'][str(i)], end=" | ")
            print(data['GPSELEVATION'][str(i)], end=" | ")
            print(data['FUEL_RATE'][str(i)], end=" | ")
            print(data['STATUS'][str(i)], end=" | ")
            print(data['PAYLOAD'][str(i)], end=" | ")
            print(data['TRUCK_ID'][str(i)], end=" | ")
            print(data['TRUCK_TYPE_ID'][str(i)], end=" | ")
            print(data['SHOVEL_ID'][str(i)], end=" | ")
            print(data['DUMP_ID'][str(i)])