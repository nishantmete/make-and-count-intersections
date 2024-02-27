# class excercieses
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



"""plane_image = [[(0, 0, 0)]* 100 for i in range(100)]


def make_a_square(plane_image, row, col, side):
    try: 
        for j in range(col, col + side + 1):
            plane_image[row][j] = (255, 255, 255)
            plane_image[row + side][j] = (255, 255, 255)
        
        for i in range(row, row + side + 1):
            plane_image[i][col] = (255, 255, 255)
            plane_image[i][col + side] = (255, 255, 255)
    except IndexError:
            print("Sqaure doesn't fit the image! ")

    images.save(plane_image, "plane_image.png")
make_a_square(plane_image, 80, 80, 19)"""




"""count = 0 
def count_the_length(a_string):
    """
