
COLOUR_TO_CODE = {
    "DeepSkyBlue4" : "#00688b",
    "gold3" : "#cdad00",
    "HotPink" : "#ff69b4"
}

user_input = "HotPink"

colour = COLOUR_TO_CODE[user_input]

print("Color code for {} is {}. ".format(user_input, colour))

for colour, code in COLOUR_TO_CODE.items():
    print("Colour {} has code {}".format(colour, code))
