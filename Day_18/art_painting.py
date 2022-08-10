import colorgram

color_extracts = []
colors = colorgram.extract('image.jpg', 20)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    color_extracts.append(new_color)
print(color_extracts)

color_list = [(238, 246, 243), (246, 240, 244), (235, 241, 246), (1, 13, 31), (52, 25, 17), (219, 127, 106), (9, 105, 160), (242, 214, 69), (150, 84, 39), (215, 87, 64), (164, 162, 32), (158, 6, 24), (157, 62, 102), (11, 63, 32), (97, 6, 19), (207, 74, 104), (10, 97, 58), (0, 63, 145), (173, 135, 162)]