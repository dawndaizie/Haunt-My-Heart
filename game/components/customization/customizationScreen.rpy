screen number_choices(title, variable, count):

    vbox:
        spacing 8

        text title:
            size 26
            color "#FFFFFF"

        hbox:
            spacing 8
            box_wrap True

            for number in range(1, count + 1):

                textbutton str(number):

                    action SetVariable(
                        variable,
                        number
                    )

                    selected (
                        getattr(renpy.store, variable) == number
                    )


## COLOR CONTROLS
screen color_controls(title, hue_var, sat_var, bright_var):

    vbox:
        spacing 8

        text title:
            size 28
            color "#FFFFFF"

        text "Hue":
            size 22
            color "#DDD3E3"

        bar value VariableValue(hue_var, range=1.0):
            xsize 580

        text "Saturation":
            size 22
            color "#DDD3E3"

        bar value VariableValue(sat_var, range=1.0):
            xsize 580

        text "Brightness":
            size 22
            color "#DDD3E3"

        bar value VariableValue(bright_var, range=1.0):
            xsize 580

        $ swatch = hsv_hex(
            getattr(renpy.store, hue_var),
            getattr(renpy.store, sat_var),
            getattr(renpy.store, bright_var)
        )

        add Solid(swatch):
            xysize (90, 35)


## CLOTHING SELECTION
screen clothing_choices(title, piece, variable, count):

    vbox:
        spacing 8

        text title:
            size 28
            color "#FFFFFF"

        hbox:
            spacing 12
            box_wrap True

            for number in range(1, count + 1):

                $ thumbnail = thumbnail_path(
                    piece,
                    number
                )

                button:
                    xysize (125, 145)
                    padding (10, 10)

                    background Solid("#302B39")
                    hover_background Solid("#51445F")
                    selected_background Solid("#76618D")
                    selected_hover_background Solid("#947BAD")

                    action SetVariable(
                        variable,
                        number
                    )

                    selected (
                        getattr(renpy.store, variable) == number
                    )

                    if renpy.loadable(thumbnail):

                        add thumbnail:
                            xysize (105, 125)
                            fit "contain"
                            align (0.5, 0.5)

                    else:

                        text str(number):
                            align (0.5, 0.5)
                            size 30
                            color "#FFFFFF"



## EDITABLE FIELDS
screen text_field(title, input_value):

    vbox:
        spacing 8

        text title:
            size 26
            color "#FFFFFF"

        button:
            xsize 580
            yminimum 60
            padding (12, 10)

            background Solid("#302B39")
            hover_background Solid("#51445F")

            action input_value.Enable()

            input:
                value input_value

                length 24
                exclude "{}[]\n\r"

                xsize 550
                color "#FFFFFF"
                size 26


## MAIN SCREEN
screen characterCustomizer():

    modal True
    default stage = 1

    default name_input = VariableInputValue(
        "name",
        default=False
    )

    default subject_input = VariableInputValue(
        "customSubject",
        default=False
    )

    default object_input = VariableInputValue(
        "customObject",
        default=False
    )

    default possessive_input = VariableInputValue(
        "customPossessive",
        default=False
    )

    $ stage_title = {
        1: "1 / 2 - Appearance and outfit",
        2: "2 / 2 - Identity and confirmation",
    }[stage]

    add Solid("#17131D")

    text stage_title:
        xpos 70
        ypos 35
        size 42
        color "#FFFFFF"


    ## CHOICE PANEL
    frame:
        xpos 60
        ypos 110
        xysize (800, 825)

        padding (25, 25)
        background Solid("#241E2C")

        viewport:
            id "customizer_options"

            mousewheel True
            draggable True
            scrollbars "vertical"

            vbox:
                xsize 700
                spacing 25

                if stage == 1:

                    text "Appearance":
                        size 34
                        color "#FFFFFF"

                    text "Body type":
                        size 26
                        color "#FFFFFF"

                    hbox:
                        spacing 8
                        box_wrap True

                        for body in BODY_TYPES:

                            textbutton body:

                                action SetVariable(
                                    "bodyType",
                                    body
                                )

                                selected bodyType == body

                    use number_choices(
                        "Head Shape",
                        "headShape",
                        HEAD_COUNT
                    )

                    text "Skin Tone":
                        size 28
                        color "#FFFFFF"

                    bar value VariableValue(
                        "skinColor",
                        range=1.0
                    ):
                        xsize 580

                    add Solid(skin_hex(skinColor)):
                        xysize (90, 35)

                    use number_choices(
                        "Hairstyle",
                        "hairStyle",
                        HAIR_COUNT
                    )

                    use color_controls(
                        "Hair color",
                        "hairHue",
                        "hairSaturation",
                        "hairBrightness"
                    )


                    # Eyes

                    use number_choices(
                        "Eye Shape",
                        "eyeShape",
                        EYE_COUNT
                    )

                    use color_controls(
                        "Eye Color",
                        "eyeHue",
                        "eyeSaturation",
                        "eyeBrightness"
                    )

                    text "Outfit":
                        size 34
                        color "#FFFFFF"

                    use clothing_choices(
                        "Top",
                        "top",
                        "shirt",
                        OUTFIT_COUNTS["tops"]
                    )

                    use number_choices(
                        "Top Colorway",
                        "shirtColor",
                        OUTFIT_COUNTS["top_colors"]
                    )

                    use clothing_choices(
                        "Bottoms",
                        "bottom",
                        "bottoms",
                        OUTFIT_COUNTS["bottoms"]
                    )

                    use number_choices(
                        "Bottoms Colorway",
                        "bottomsColor",
                        OUTFIT_COUNTS["bottom_colors"]
                    )

                else:

                    text "Identity":
                        size 34
                        color "#FFFFFF"

                    use text_field(
                        "Name",
                        name_input
                    )

                    text "Pronouns":
                        size 32
                        color "#FFFFFF"

                    hbox:
                        spacing 10
                        box_wrap True

                        textbutton "She / her":

                            action [
                                DisableAllInputValues(),
                                SetVariable("pronouns", "she")
                            ]

                            selected pronouns == "she"

                        textbutton "He / him":

                            action [
                                DisableAllInputValues(),
                                SetVariable("pronouns", "he")
                            ]

                            selected pronouns == "he"

                        textbutton "They / them":

                            action [
                                DisableAllInputValues(),
                                SetVariable("pronouns", "they")
                            ]

                            selected pronouns == "they"

                        textbutton "Custom":

                            action [
                                DisableAllInputValues(),
                                SetVariable("pronouns", "custom")
                            ]

                            selected pronouns == "custom"

                    if pronouns == "custom":

                        use text_field(
                            "Subject - e.g. they",
                            subject_input
                        )

                        use text_field(
                            "Object - e.g. them",
                            object_input
                        )

                        use text_field(
                            "Possessive adjective - e.g. their",
                            possessive_input
                        )

                        textbutton "Plural-style verbs: [customPlural]":
                            action ToggleVariable("customPlural")

                        text "True: they are / they have. False: she is / she has.":
                            size 20
                            color "#DDD3E3"
                            xmaximum 650

                    text "Ready for work?":
                        size 28
                        color "#FFFFFF"
                        xmaximum 650

                    text "Use Back for any last minute changes.":
                        size 22
                        color "#DDD3E3"
                        xmaximum 650


                    if not name.strip():

                        text "Please enter a name before confirming.":
                            size 22
                            color "#E9B2B2"
                            xmaximum 650

                    elif (
                        pronouns == "custom"
                        and not (
                            customSubject.strip()
                            and customObject.strip()
                            and customPossessive.strip()
                        )
                    ):

                        text "Please fill in all three custom pronoun fields.":
                            size 22
                            color "#E9B2B2"
                            xmaximum 650


    ## CHARACTER PREVIEW
    frame:
        xpos 920
        ypos 110
        xysize (940, 825)

        padding (20, 20)
        background Solid("#211B29")

        fixed:

            add mc_displayable():
                align (0.5, 0.5)
                zoom 0.78

            $ missing_layers = missing_mc_layers()
            $ missing_count = len(missing_layers)



    ## NAVIGATION
    hbox:
        xpos 60
        ypos 965
        spacing 30

        if stage > 1:

            textbutton "Back":

                action [
                    DisableAllInputValues(),
                    SetScreenVariable("stage", 1)
                ]

        if stage < 2:

            textbutton "Next":

                action [
                    DisableAllInputValues(),
                    SetScreenVariable("stage", 2)
                ]

        else:

            textbutton "Confirm character":

                sensitive (
                    bool(name.strip())
                    and (
                        pronouns != "custom"
                        or (
                            bool(customSubject.strip())
                            and bool(customObject.strip())
                            and bool(customPossessive.strip())
                        )
                    )
                )

                action [
                    DisableAllInputValues(),
                    Return(True)
                ]


##ENTRY
label customize_mc:

    window hide

    call screen characterCustomizer

    $ name = name.strip()

    if pronouns == "custom":
        $ customSubject = customSubject.strip()
        $ customObject = customObject.strip()
        $ customPossessive = customPossessive.strip()

    window auto

    jump day1