## All images are placeholders FOR NOW while I draw them. Please enjoy the many photos of chiikawa instead sighhhhh
## VARIABLES 
default name = ""
default pronouns = "she/her" # (she/her/hers), (he/him/his), (they/them/theirs), custom
default customSubject = ""
default customObject = ""
default customPossessive = ""
default pluralVerb = False

default bodyType = "Slender" # slender, curvy, broad, lanky
default headShape = 1 # longer face, shorter face

default skinColor = 0.5 
default skinDetails = None

default hairStyle = 1 # 10 for now sigh
default hairHue = 0.07
default hairSaturation = 0.67
default hairBrightness = 0.34

default eyeShape = 1 # 3 types
default eyeHue = 0.07
default eyeSaturation = 0.67
default eyeBrightness = 0.34

default casualShirt = 1 # 4 types for now, 2 colorways for each, account for bodytype
default casualShirtColor = 1

default workShirt = 1
default workShirtColor = 1

default casualBottoms = 1 #3 types for now, 3 colorways for each, account for bodytype
default casualBottomsColor = 1

default workBottoms = 1 
default workBottomsColor = 1

default accessories = None # 10 different accessories
default bag = None # 4 different bags


init python: 

    BODY_TYPES = (
        "Slender",
        "Curvy",
        "Broad",
        "Lanky",
    )

    HEAD_COUNT = 2
    HAIR_COUNT = 10
    EYE_COUNT = 3

    SKIN_PALETTE = (
        "#F6DECF",
        "#E8BEA2",
        "#D39A75",
        "#B77954",
        "#945C3B",
        "#6B402B",
        "#42271E",
        "#1F0D07",
        "#130703"
    )

    OUTFIT_COUNTS = (
        "casual": {
            "tops": 4,
            "bottoms": 3,
            "top_colors": 2,
            "bottom_colors": 3,
        },

        "work": {
            "tops": 4,
            "bottoms": 3,
            "top_colors": 2,
            "bottom_colors": 3,
        },

    )