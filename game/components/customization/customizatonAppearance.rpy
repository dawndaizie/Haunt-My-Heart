init python: 

    import colorsys


    ## COLOR HELPERS
    def hex_to_rgb(value):
        value = value.lstrip("#")
        return tuple(
            int(value[i:i + 2], 16)
            for i in (0, 2, 4)
        )

    def rgb_to_hex(rgb):
        channels = [
            max(0, min(255, int(round(channel))))
            for channel in rgb
        ]

        return "#{:02x}{:02x}{:02x}".format(*channels)

    def skin_hex(position):
        position = max(0.0, min(1.0, position))
        scaled = position * (len(SKIN_PALETTE) - 1)

        index = min(int(scaled), len(SKIN_PALETTE) - 2)
        fraction = scaled - index

        first = hex_to_rgb(SKIN_PALETTE[index])
        second = hex_to_rgb(SKIN_PALETTE[index + 1])

        mixed = tuple(
            a + (b - a) * fraction
            for a, b in zip(first, second)
        )

        return rgb_to_hex(mixed)

    def hsv_hex(hue, saturation, brightness):
        rgb = colorsys.hsv_to_rgb(
            hue,
            saturation,
            brightness
        )

        return rgb_to_hex(
        tuple(
            channel * 255 
            for channel in rgb)
        )
    
    ## IMAGE PATHS
    def clothing_path(piece, choice, color):
        return (
            "images/characterCustomization/clothes/{}/{}{}_{}.jpg"
            # change to .png once assets are ready !!
        ).format(
            bodyType,
            piece,
            choice,
            color
        )
    
    def thumbnail_path(piece, choice): 
        return (
            "images/characterCustomization/"
            "thumbnails/{}_{}.png"
        ).format(
            piece,
            choice
        )

    ## PLAYER LAYERS
    def mc_layers():

        root = "images/characterCustomization"

        skin = skin_hex(skinColor)

        hair = hsv_hex(
            hairHue,
            hairSaturation,
            hairBrightness
        )

        eyes = hsv_hex(
            eyeHue,
            eyeSaturation,
            eyeBrightness
        )

        return [
            (
                root + "/base/base{}.jpg".format(bodyType), #change to .png
                skin
            ),

            (
                root + "/faceShape/face{}.jpg".format(headShape), #change to .png
                skin
            ),

            (
                clothing_path(
                    "bottom",
                    bottoms,
                    bottomsColor
                ),
                None
            ),

            (
                clothing_path(
                    "top",
                    shirt,
                    shirtColor
                ),
                None
            ),

            (
                root + "/eyeShape/eyes{}.jpg".format(eyeShape), #change to .png
                None
            ),

            (
                root + "/eyeShape/irises{}.jpg".format(eyeShape), #change to .png
                eyes
            ),

            (
                root + "/hair/hair{}.jpg".format(hairStyle), #change to .png
                hair
            ),
        ]



    def mc_displayable():

        parts = []

        for path, tint in mc_layers():

            if not renpy.loadable(path):
                continue

            if tint is None:
                layer = path
            else:
                layer = Transform(
                    path,
                    matrixcolor=TintMatrix(tint)
                )

            parts.extend([
                (0, 0),
                layer
            ])

        if not parts:
            return Null(width=467, height=946)

        return Composite(
            (467, 946),
            *parts
        )


    def missing_mc_layers():
        return [
            path
            for path, tint in mc_layers()
            if not renpy.loadable(path)
        ]

    def mc_dynamic(st, at):
        return mc_displayable(), None



image MC = DynamicDisplayable(mc_dynamic)
    
