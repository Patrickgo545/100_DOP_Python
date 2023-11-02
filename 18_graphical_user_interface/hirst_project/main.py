import colorgram

colors_extract = colorgram.extract('hirst.jpg', 12)
colors_list = []
colors_list_specific = []

# for color in colors_extract:
#     rgb = colors_extract[color]
#     colors_list.append(rgb)

print(colors_extract.r)

# for i in colors_list:
#     r = colors_list[i].r
#     g = colors_list[i].g
#     b = colors_list[i].b
    
#     rgb = (r, g, b)
#     colors_list_specific.append(rgb)

# print(colors_list_specific)
# first = colors_list[0]
# test = first.r

# print(test)