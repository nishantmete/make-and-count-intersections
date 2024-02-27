import images
import random
in_image  = images.load("in.png")
plane = images.load("plane_image.png")




image = [[(0, 0, 0)] * 50 for _ in range(50)]

random_1 = random.randrange(0, 51)
random_2 = random.randrange(0, 51)
random_3 = random.randrange(0, 51)
random_4 = random.randrange(0, 51)
random_5 = random.randrange(0, 51)

image = [[(0, 0, 0)] * 50 for _ in range(50)]

image[random_1] = [(255, 255, 255)] * 50
image[random_2] = [(255, 255, 255)] * 50
image[random_3] = [(255, 255, 255)] * 50
image[random_4] = [(255, 255, 255)] * 50
image[random_5] = [(255, 255, 255)] * 50

for row in range(random_1):
    image[row][random_5] = (255, 255, 255)
    image[row][random_1] = (255, 255, 255)
    image[row][random_3] = (255, 255, 255)
    image[row][random_2] = (255, 255, 255)


images.save(image, "intersection.png")


def count_the_intersections(image):
    intersections_set = set()
    intersections = 0
    
    for row_index, row in enumerate(image):
        for pixel_index, pixel in enumerate(row):
            if image[row_index][pixel_index] != (0, 0, 0):
                try:
                    if image[row_index - 1][pixel_index - 1] == (0, 0, 0) and image[row_index - 1][pixel_index + 1] == (0, 0, 0):
                        if image[row_index + 1][pixel_index - 1] == (0, 0, 0) and image[row_index + 1][pixel_index + 1] == (0, 0, 0):
                            if image[row_index - 1][pixel_index] == pixel and image[row_index + 1][pixel_index] == pixel:
                                if image[row_index][pixel_index - 1] == pixel and image[row_index][pixel_index + 1] == pixel:
                                    intersections += 1
                                    intersections_set.add((row_index,pixel_index))
                except IndexError:
                    continue

    return intersections
print(count_the_intersections(image))



