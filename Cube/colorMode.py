import time as ti
inc = 5

rgb = [ 255,0,0]
def rgbMode(rgb):
        while True:
            # this makes g 255 and then starts to lower R to 0
            if (rgb [0] == 255 and rgb[1] < 255 and rgb[2] == 0):
                rgb[1] += inc
                return rgb

            if rgb [1] == 255 and rgb[0] > 0 :
                rgb[0] -= inc
                return rgb
            #####################################################

            if rgb [1] == 255 and rgb[2] < 255 and rgb[0] == 0 :
                rgb[2] += inc
                return rgb

            if rgb [2] == 255 and rgb[1] > 0 :
                rgb[1] -= inc
                return rgb
            #####################################################

            if rgb [2] == 255 and rgb[0] < 255 and rgb[1] == 0:
                rgb[0] += inc
                return rgb

            if rgb [0] == 255 and rgb[2] > 0 :
                rgb[2] -= inc
                return rgb
            #####################################################
print(rgbMode(rgb))