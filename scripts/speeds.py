"""
    This script will take a csv and calculate the
    speed at which the truck is travelling

    This data is not representative of the speed you would
    see on the spedometer since it is not taking into account
    the elevation change
"""
import math
import csv


# Example usage\
# [[northing_prev, easting_prev, elevation_prev], [northing_cur, easting_cur, elevation_cur]]
coords = [[0, 0, 0], [0, 0, 0]] 

# time_prev, time_cur
time = [0, 0]



for t_file_i in range(69):
    def run():
        with open(f"/home/justin/Desktop/BCIT Share/repos/QDpieS/truck_data/truck{t_file_i}.csv") as read_file:
            with open(f"/home/justin/Desktop/BCIT Share/repos/QDpieS/out/speeds.csv", "w") as out_file:
                csvreader = csv.reader(read_file)
                top_speeds = [0] * 100
                for i, row in enumerate(csvreader):
                    try:
                        coords[1][0] = float(row[1]) # northing
                        coords[1][1] = float(row[2]) # easting
                        coords[1][2] = float(row[3]) # elevation
                        time[1] = int(row[0]) # time utc
                        if time[1] - time[0] == 0:
                            continue


                    except:
                        continue

                    time_delta = (time[1] - time[0]) / 2000
                    speed = calculate_speed(coords, time_delta) * 3.6
                    print(speed)
                    out_file.write(str(speed) + ",")

                    # if speed > top_speeds[0] and time_delta == 2:
                    #     top_speeds.pop()
                    #     top_speeds.insert(0, speed)

                    # print("northing delta: ", coords[1][0] - coords[0][0])
                    # print("easting delta: ", coords[1][1] - coords[0][1])
                    # print("delevation delta: ", coords[1][2] - coords[0][2])
                    # print("time delta: ", time_delta)
                    # print("")



                    coords[0][0] = coords[1][0]
                    coords[0][1] = coords[1][1]
                    coords[0][2] = coords[1][2]
                    time[0] = time[1]
                    # print("\n\n")

                # print(top_speeds)



# calcualtes the speed in meteres/second
def calculate_speed(coords, time):
  # Initialize variables to store the total distance traveled and the starting coordinates
  distance = 0
  start_coords = coords[0]

  # Iterate over the list of coordinates
  for coord in coords[1:]:
    # Calculate the distance between the current coordinates and the starting coordinates
    delta_northing = coord[0] - start_coords[0]
    delta_easting = coord[1] - start_coords[1]
    delta_elevation = coord[2] - start_coords[2]
    distance += math.sqrt(delta_northing**2 + delta_easting**2 + delta_elevation**2)

    # Update the starting coordinates
    start_coords = coord

  # Calculate the speed by dividing the distance traveled by the time
  speed = distance / time

  return speed




if __name__ == "__main__":
    run()