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
        position = max(0.0. min(1.0, position))
        scaled = position * (len(SKIN_PALETTE) - 1)

        index = min(int(scaled), len(SKIN_PALETTE) - 2)
        fraction = scaled - index

        first = hex_to_rgb(SKIN_PALETTE[index])
        second hex_to_rgb(SKIN_PALETTE[index + 1])

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
    def clothing_path(outfit, piece, choice, color):
        return (
        "images/characterCustomization/"
        "{}/{}/{}_{}_{}.jpg" # change to .png once assets are ready !!
        ).format(
            outfit,
            
        )