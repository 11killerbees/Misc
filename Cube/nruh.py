import time as ti
rgb = [255,0,0]

def rbg():

    while True:
        for i in range(255):
            rgb[1] += 1
            print(rgb)

        for i in range(255):
            rgb[0] -= 1
            print(rgb)

        for i in range(255):
            rgb[2] += 1
            print(rgb)

        for i in range(255):
            rgb[1] -= 1
            print(rgb)

        for i in range(255):
            rgb[0] += 1
            print(rgb)

        for i in range(255):
            rgb[2] -= 1
            print(rgb)



