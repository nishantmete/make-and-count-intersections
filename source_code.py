import images

in_image  = images.load("in.png")
plane = images.load("plane_image.png")




image = [[(0, 0, 0)] * 50 for _ in range(50)]

image[0] = [(255, 255, 255)] * 50
image[15] = [(255, 255, 255)] * 50
image[19] = [(255, 255, 255)] * 50
image[34] = [(255, 255, 255)] * 50
image[41] = [(255, 255, 255)] * 50

for row in range(len(image)):
    image[row][0] = (255, 255, 255)
    image[row][20] = (255, 255, 255)
    image[row][35] = (255, 255, 255)
    image[row][45] = (255, 255, 255)

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



