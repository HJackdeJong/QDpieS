import pygame
import csv
import numpy as np
import time

shovelImg = pygame.image.load("shovel.png")

pileImg = pygame.image.load("pile.png")
workerImg = pygame.image.load("worker.png")

shovel = [
        (57337.07036067169, 225312.7785964522, 324.3270750954244),
        (56111.7268121729, 229016.55150156975, 91.87869555831124),
        (54848.68657176172, 228714.5165945104, 214.2178093950882),
        (57043.058888960855, 224620.30387730378, 197.71819862657804),
        (58818.24695304147, 228556.1562586717, 90.64628879484441),
        (55584.335708098726, 228643.3326070516, 103.30983900578731),
        (55329.67526628129, 229071.77746152953, 126.55509572980823),
        (55634.16965694022, 228897.2971685805, 95.72231988396189),
        (55907.91450019988, 224492.48414928955, 292.02353991481834)
        ]

dump = [
        (55326.89167814255, 224584.59434623912, 402.82630990406693),    
        (52564.68784339185, 227612.3184463942, 239.65896326785077),
        (53056.94609636884, 227788.6762552661, 238.28288786835236),
        (56055.43835881027, 223804.10620310454, 389.9619407149561),
        (55151.241107882255, 222682.30990526878, 367.7867750371585), 
        (60197.16195376024, 229197.08303932683, 319.505051727804),    
        (56677.320635755146, 225801.24777536737, 178.06205560859232),   
        (60383.14264305079, 229604.81193935624, 330.29807742173216),  
        (55974.1757814635, 227017.5998378733, 210.47617579130508),    
        (56722.89398455073, 227378.29822193738, 180.80984244173158),    
        (56037.75387786484, 226968.23656696462, 215.49659044117675),    
        (56318.3419548814, 226725.51768855014, 225.32281936884513),    
        (55396.06684379293, 222736.87129374265, 372.1580116279071),    
        (56807.7633775774, 227273.37528566128, 174.5504727272697)
        ]
import pygame

# Initialize Pygame
pygame.init()
width = 1100
height = 1100
# Set the window size
window_size = (width, height)


# Create the window
screen = pygame.display.set_mode(window_size)

# Set the background color
bg_color = (255, 255, 255)

# Set the shovel and dump colors
shovel_color = (0, 0, 255)
dump_color = (255, 0, 0)
truck_color = [(100, 20, 199),(12, 127, 166),(17, 37, 189),(19, 191, 111),(11, 143, 29),(173, 7, 15)]

# Set the shovel and dump point sizes
shovel_point_size = 5
dump_point_size = 5
truck_point_size = 3

# Set the scale factors for the north and east values
min_north = min(min(shovel, key=lambda x: x[0]), min(dump, key=lambda x: x[0]))[0]
max_north = max(max(shovel, key=lambda x: x[0]), max(dump, key=lambda x: x[0]))[0]
min_east = min(min(shovel, key=lambda x: x[1]), min(dump, key=lambda x: x[1]))[1]
max_east = max(max(shovel, key=lambda x: x[1]), max(dump, key=lambda x: x[1]))[1]

north_scale = (width-100) / (max_north - min_north)
east_scale = (height-100) / (max_east - min_east)
print(str(north_scale) + "   " + str(east_scale))


# Set the vertical offset for the elev values
elev_offset = 300

# Set the minimum and maximum elev values
min_elev = min(min(shovel, key=lambda x: x[2]), min(dump, key=lambda x: x[2]))[2]
max_elev = max(max(shovel, key=lambda x: x[2]), max(dump, key=lambda x: x[2]))[2]

# Set the elev scale factor
elev_scale = (max_elev - min_elev) / window_size[1]

# Set the running flag
running = True

# Run the game loop
alpha = 0
fade_speed = 4
rate = 1
trucks = np.zeros((69, 1000000, 4))
# screen.fill((139,69,19))
set = 0
type = 0

# Set up the font
font = pygame.font.Font(None, 36)

# Set up the clock
clock = pygame.time.Clock()

# Set up the start time
start_time = time.mktime(time.strptime("Sun, Apr 3, 2022 12:01:00 AM", "%a, %b %d, %Y %I:%M:%S %p"))

# Set up the game variables
game_running = True
current_time = start_time

for p in range(1,2):
    print(p)
    set = 0
    with open(f'cleaned_trucks\\cleaned_truck{p}.csv', 'r') as input_file:
        reader = csv.reader(input_file)
        for i, row in enumerate(reader):
            trucks[p,i,0] = int(((float(row[2])-min_east)*east_scale))+50
            trucks[p,i,1] = int(((float(row[1])-min_north)*north_scale))+50
            if row[5] == "Empty" or row[5] == "Hauling" or row[5] == "Dumping" or row[5] == "Truck Loading" or row[5] == "Wenco General Production":# or row[5] == "NON_PRODUCTIVE":
                value = 0
            else:
                value = 1
            trucks[p,i,2] = value
            if set == 0:
                trucks[p,i,3] = int(row[8])
                type = int(row[8])
                set = 1
            else:
                trucks[p,i,3] = type
i = -1
while True:
    i+=1
    # Check for events
    if i%rate == 0:
        for event in pygame.event.get():
            # Quit if the window is closed
            if event.type == pygame.QUIT:
                running = False

        # Create a new surface with the same size as the screen
        fade_surface = pygame.image.load("bg.png").convert_alpha()
        # fade_surface = pygame.Surface((1100, 1100))

        # Set the alpha value of the fade_surface
        fade_surface.set_alpha(alpha)
        # fade_surface.fill((0, 0, 0))

        # Blit the fade_surface onto the screen
        screen.blit(fade_surface, (0, 0))

        # Decrease the alpha value by the fade speed
        alpha = max(0, alpha - fade_speed)
        if alpha == 0:
            alpha = 10

        # Draw the shovel points
        for shovel_point in shovel:
            screen.blit(shovelImg, (int(((shovel_point[1]-min_east)*east_scale)+35), int(((shovel_point[0]-min_north)*north_scale))+40))
            # pygame.draw.circle(screen, shovel_color, (int(((shovel_point[1]-min_east)*east_scale)+50), int(((shovel_point[0]-min_north)*north_scale))+50), shovel_point_size)
        # Draw the dump points

        for dump_point in dump:
            screen.blit(pileImg, (int(((dump_point[1]-min_east)*east_scale)+40), int(((dump_point[0]-min_north)*north_scale))+40))
            # pygame.draw.circle(screen, dump_color, (int(((dump_point[1]-min_east)*east_scale)+50), int(((dump_point[0]-min_north)*north_scale))+50), dump_point_size)
        
        # pygame.draw.circle(screen,truck_color,(int(((float(row[2])-min_east)*east_scale)+50), int(((float(row[1])-min_north)*north_scale))+50),truck_point_size)
        for p in range(69):
            try:
                if trucks[p,i,2] == 1:
                    pygame.draw.circle(screen,truck_color[5],(trucks[p,i,0],trucks[p,i,1]),truck_point_size)
                else:
                    pygame.draw.circle(screen,truck_color[1],(trucks[p,i,0],trucks[p,i,1]),truck_point_size)
            except:
                print(trucks[p,i,3])
            # pygame.draw.circle(screen,(222,255,255),(trucks[p,i,0],trucks[p,i,1]),truck_point_size)
            # screen.blit(workerImg, (trucks[p,i,0],trucks[p,i,1]))
        time_text = time.strftime("%a, %b %d, %Y %I:%M", time.localtime(current_time))
        time_label = font.render(time_text, 1, (255, 255, 255))
        screen.blit(time_label, (10, 10))
        pygame.display.flip()
        # Update game state
        current_time += 2
        clock.tick(60)

# Quit Pygame
pygame.quit()


