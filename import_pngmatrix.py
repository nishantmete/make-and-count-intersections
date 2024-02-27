import pngmatrix

listjust = pngmatrix.load_png8("black.png")

print(listjust)
"""
thematrix = []

for i in range(100):
    thematrix.append([(0, 0, 0)] * 100)
thematrix[0] = [(227, 6, 19)] * 100
thematrix[-1] = [(227, 6, 19)] * 100



rows = len(thematrix)
column = len(thematrix[0])

for row, index in zip(thematrix, range(len(thematrix[0]))):
    row[index] = (255, 255, 255)

for row, index in zip(thematrix, range(len(thematrix[0]) - 1, -1, -1)):
    row[index] = (255, 255, 255)

thematrix[49] = [(0, 191, 99)] * 100

for row in thematrix:
    row[49] = (0, 191, 99)

for row in thematrix:
    row[0] = (227, 6, 19)
    row[-1] = (227, 6, 19)

for a_list in thematrix:
    for element in range(len(row)):
        if a_list[element] == (0, 0, 0):
            a_list[element] = (255, 255, 255)
        elif a_list[element] == (255, 255, 255):
            a_list[element] =(0, 0, 0)
thematrix[len(thematrix)//2][len(thematrix[0])//2] = (238, 191, 138)
print(thematrix[1])
pngmatrix.save_png8(thematrix, "black.png")"""