# CHARACTERS
define p = Character("Pheobe")
define f = Character("Felix")
define m = Character("Milo")
define l = Character("Luka")
define unknown = Character("???")
define yn = Character("[name]")

# NPCs 

define r1 = Character("Reporter 1")
define r2 = Character("Reporter 2")
define r3 = Character("Reporter 3")


# VARIABLES
default felixAffinity = 0
default miloAffinity = 0
default lukaAffinity = 0
default exorcismPoints = 0

# BACKGROUNDS

# SPRITES

# The game starts here.

label splashscreen:
    
    return 

label start:

    $ name = renpy.input("what would you like to be called?")
    $ name = name.strip()
    if name == "":
        $ name = "Eve"

label prologue: 

    scene bg room

    "{i}I've always been able to see ghosts.{/i}"
    "{i}Whether they've died due to some freak accident..{/i}"
    "{i}Passed away in their old age...{/i}"
    "{i}Or has even been a ghost longer than a human...{/i}"
    "{i}I've been able to see them.{/i}"
    "{i}But it really doesn't make me special. Because so can everyone else.{/i}"


    r1 "BREAKING NEWS! There have been alarming number of reports of 'ghost sightings', where eyewitnesses state they are seeing and even able to intereact with individuals who were confirmed dead!"

    r2 "Story now developing, reporters on the scene state in the past five years,  there has been an increase in so-called paranormal activity, but within the last two days, hospitals, places of residence, and even morgues have reported...well, ghosts!"

    r3 "Scientists have been trying to understand this strange phenomena...even employing the help of the undead!"

    "{i}The merge of the living and undead plane happened long before I was born.{/i}"
    "{i}It happened almost exponentially, according to my grandparents. At first, there was random sightings here and there, until just a rush of ghosts occurred, almost like the veil between worlds had given out and the world's population doubled overnight.{/i}"
    "{i}It stirred quite alot of chaos, leading to humans and ghosts fighting over every little thing...{/i}"
    "{i}But family and friends reconnected. History was uncovered. Technology advanced, alongside our understanding of the human consciousness and vulnerability.{/i}"
    "{i}After many years, many people came to accept ghosthood as a second phase of life.{/i}"
    "{i}But despite it all, there were still some quarrels on both sides.{/i}"
    "{i}This lead tot he creation of the Mortem-Mortal Devision, an organization facilitating the smooth transition and coexistence between humans and ghosts.{/i}"
    "{i}And as a proud trainee of this depatement, I think we do a good job.{/i}"

    "Your useless alarm rings, pulling you away from your monologue. The sun beats through the curtains, illuminating your room in a bright, joyous mood. Perhaps similar to your mood. It's quite infectious, honestly."
    "After getting hired for your dream job 3 months ago, you moved into a new apartment in Lithe - one of the largest ghost cities on the continent. Boxes litter your room, remnants of your childhood home that you have yet tp unpack."
    "You jump out of bed, unnaturally excited for the day."
    "{i}Time to get ready for work!{/i}"
    








label day1:


label day2:



    if ((felixAffinity > miloAffinity) and (felixAffinity >lukaAffinity)):
        jump fday3
    
    if ((lukaAffinity > felixAffinity) and (lukaAffinity > miloAffinity)):
        jump lday3

    if ((miloAffinity > lukaAffinity) and (miloAffinity > felixAffinity)):
        jump mday3


    if (lukaAffinity == felixAffinity == miloAffinity):
        jump commonRoute
    return
