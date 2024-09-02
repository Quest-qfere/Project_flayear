# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# We can change the size and the codename in the future by changing the values in size
# if you wanna change the height of the name box just change the variable define gui.name_ypos = -100 in the gui file

default preferences.text_cps = 40

init:
    #backgrounds    
    image bg party_room=im.Scale('images/bg/bg_partyroom.png', 1920, 1200)
    image bg pilot_room=im.Scale('images/bg/bg_pilotroom.png', 1920, 1000)
    image bg navi_cake=im.Scale('images/navi/navi_cakeneutral.png', 1920, 1200)
    image bg gas_station_inside=im.Scale('images/bg/bg_gas_station_inside.png', 1920, 1200)
    image bg gas_station_outside=im.Scale('images/bg/bg_gas_station_outside.png', 1920, 1200)
    #flayon
    image flayon_neutral=im.Scale('images/flayon/flayon_neutral.png', 683, 683)
    image flayon_confused=im.Scale('images/flayon/flayon_confused.png', 300, 400)
    image flayon_excited=im.Scale('images/flayon/flayon_excited.png', 300, 400)
    image flayon_surprised=im.Scale('images/flayon/flayon_surprised.png', 300, 400)
    image flayon_concerned=im.Scale('images/flayon/flayon_concerned.png', 300, 400)
    image flayon_neutral_cropped = Crop((0, 0, 275, 250), "flayon_neutral")
    image flayon_concerned_cropped = Crop((0, 0, 275, 250), "flayon_concerned")
    image flayon_confused_cropped = Crop((0, 0, 275, 250), "flayon_confused")
    image flayon_excited_cropped = Crop((0, 0, 275, 250), "flayon_excited")
    image flayon_surprised_cropped = Crop((0, 0, 275, 250), "flayon_surprised")
    #cain
    image cain_neutral=im.Scale('images/cain/cain_neutral.png', 300, 400)
    image cain_excited=im.Scale('images/cain/cain_excited.png', 300, 400)
    image cain_flex=im.Scale('images/cain/cain_flex.png', 300, 400)
    image cain_neutral_cropped = Crop((0, 0, 275, 250), "cain_neutral")
    image cain_excited_cropped = Crop((0, 0, 275, 250), "cain_excited")
    image cain_flex_cropped = Crop((0, 0, 275, 250), "cain_flex")
    #charli
    image charli_neutral=im.Scale('images/charli/charli_neutral.png', 410, 410)
    image charli_excited=im.Scale('images/charli/charli_excited.png', 300, 400)
    image charli_neutral_cropped = Crop((0, 0, 275, 250), "charli_neutral")
    image charli_excited_cropped = Crop((0, 0, 275, 250), "charli_excited")
    #dean
    image dean_neutral=im.Scale('images/dean/dean_neutral.png', 300, 400)
    image dean_smug=im.Scale('images/dean/dean_smug.png', 300, 400)
    image dean_concern=im.Scale('images/dean/dean_concern.png', 300, 400)
    image dean_facepalm=im.Scale('images/dean/dean_facepalm.png', 300, 400)
    image dean_neutral_cropped = Crop((0, 0, 275, 250), "dean_neutral")
    image dean_smug_cropped = Crop((0, 0, 275, 250), "dean_smug")
    image dean_concern_cropped = Crop((0, 0, 275, 250), "dean_concern")
    image dean_facepalm_cropped=Crop((0, 0, 275, 250), "dean_facepalm")
    #kit
    image kit_neutral=im.Scale('images/kit/kit_neutral.png', 300, 400)
    image kit_excited=im.Scale('images/kit/kit_excited.png', 300, 400)
    image kit_starryeyed=im.Scale('images/kit/kit_starryeyed.png', 300, 400)
    image kit_concerned=im.Scale('images/kit/kit_concerned.png', 300, 400)
    image kit_crying=im.Scale('images/kit/kit_crying.png', 300, 400)
    image kit_neutral_cropped = Crop((0, 0, 275, 250), "kit_neutral")
    image kit_excited_cropped = Crop((0, 0, 275, 250), "kit_excited")
    image kit_starryeyed_cropped = Crop((0, 0, 275, 250), "kit_starryeyed")
    image kit_concerned_cropped = Crop((0, 0, 275, 250), "kit_concerned")
    image kit_crying_cropped = Crop((0, 0, 275, 250), "kit_crying")
    #navi
    image navi_neutral=im.Scale('images/navi/navi_neutral.png', 300, 400)
    image navi_disgusted=im.Scale('images/navi/navi_disgusted.png', 300, 400)
    image navi_worried=im.Scale('images/navi/navi_worried.png', 300, 400)
    image navi_snacks=im.Scale('images/navi/navi_snacks.png', 300, 400)
    image navi_cake_neutral=im.Scale('images/navi/navi_cakeneutral.png', 300, 400)
    image navi_cake_annoyed=im.Scale('images/navi/navi_cakeannoyed.png', 300, 400)
    image navi_neutral_cropped = Crop((0, 0, 275, 250), "navi_neutral")
    image navi_worried_cropped = Crop((0, 0, 275, 250), "navi_worried")

    # props
    image note = "images/props/prologue_note_temp.png"
    image rtrus_screen=im.Scale("images/props/rtrus_screen.png", 300, 300)
    image rtrus_screen_1 = "rtrus_screen"
    image rtrus_screen_2 = "rtrus_screen"
    image rtrus_screen_3 = "rtrus_screen"
    image rtrus_screen_4 = "rtrus_screen"
    image rtrus_screen_5 = "rtrus_screen"
    image error_msg=im.Scale("images/props/error_msg.png", 200, 100)
    image error_1 = "error_msg"
    image error_2 = "error_msg"
    image error_3 = "error_msg"

    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)

define FLAY = Character("Flayon", who_suffix="\n{size=-15}Ace Pilot"  )
define NAVI  = Character("Navi", who_suffix="\n{size=-15}Navigator"  )
define CAIN  = Character("Cain", who_suffix="\n{size=-15}Technician"  )
define DEAN = Character("Dean", who_suffix="\n{size=-15}Medic"  )
define KIT = Character("Kit", who_suffix="\n{size=-15}Weapons"  )
define CHARLI = Character("Charli", who_suffix="\n{size=-15}Mechanic"  )

transform charfarleft:
    xalign 0.07
    yalign 1.0

transform charfarright:
    xalign 0.95
    yalign 0.6

transform charright:
    xalign 0.80
    yalign 0.6

transform charmidright:
    xalign 0.65
    yalign 0.6

transform charmid:
    xalign 0.50
    yalign 0.6

transform charmidleft:
    xalign 0.35
    yalign 0.6

transform charleft:
    xalign 0.20
    yalign 0.6

transform rtrus_screen_topleft:
    xalign 0.35
    yalign 0.17

transform rtrus_screen_bottommidleft:
    xalign 0.47
    yalign 0.59

transform rtrus_screen_topmid:
    xalign 0.65
    yalign 0.17

transform rtrus_screen_bottommidright:
    xalign 0.47
    yalign 0.59

transform rtrus_screen_topright:
    xalign 0.95
    yalign 0.17

define fastdissolve = Dissolve(0.2)

# The game starts here.

label start:
    # These display lines of dialogue.
    jump intro_sequence

label show_interactive_items:
    show screen gas_station_items
    with fastdissolve
    "Click on an item to interact with it."
    pause

screen gas_station_items():
    imagebutton:
        xpos 100
        ypos 300
        idle "images/props/snack1_idle.png"
        hover "images/props/snack1_hover.png"
        action Jump("snack_chosen")

    imagebutton:
        xpos 400
        ypos 300
        idle "images/props/snack2_idle.png"
        hover "images/props/snack2_hover.png"
        action Jump("snack_chosen")

    imagebutton:
        xpos 700
        ypos 300
        idle "images/props/door_idle.png"
        hover "images/props/door_hover.png"
        action Jump("door_chosen")

label intro_sequence:
    "My name is Machina X Flayon, the pilot of guild TEMPUS!" 
    "As a guild of brave, smart adventurers, we get commissioned for quests quite often."
    "But, today was {i}different...{/i} a quest came through, addressed to me specifically!"
    "I wouldn't usually find this strange, but the note attached was... interesting."
    hide window
    show note:
        alpha 0.00
        xalign 0.5
        yalign 0.5
        easein 1.0 alpha 1.00
    pause 1.0
    window show
    FLAY "So, I recruited five of the strongest people in my team, also known as the Machiroons!"
    FLAY "And we traveled in none other than my giant mech, the R-TRUS! He's pretty cool!"
    FLAY "We all got ready and set off towards the coordinates..."
    show bg pilot_room with fade
    pause 1
    show flayon_neutral at charfarleft
    with fastdissolve
    FLAY "{shaky}Status check, everyone!{/shaky} How's it going?"
    show rtrus_screen at rtrus_screen_topleft
    show navi_neutral_cropped at rtrus_screen_topleft
    with fastdissolve
    pause 0.3
    NAVI "We're getting closer now. ETA is one hour!"
    show rtrus_screen_1 at rtrus_screen_bottommidleft
    show cain_neutral_cropped at rtrus_screen_bottommidleft
    with fastdissolve
    pause 0.3
    CAIN "All systems are looking cool! No problems here, boss!"
    show rtrus_screen_2 at rtrus_screen_topmid
    show dean_smug_cropped at rtrus_screen_topmid
    with fastdissolve
    pause 0.3
    DEAN "To be honest, this whole operation has gone a lot smoother than I imagined."
    show rtrus_screen_3 at rtrus_screen_bottommidright
    show charli_neutral_cropped at rtrus_screen_bottommidright
    with fastdissolve
    pause 0.3
    CHARLI "Yup! Everything's all clear from my side too-nya~"
    show rtrus_screen_4 at rtrus_screen_topright
    show kit_concerned_cropped at rtrus_screen_topright
    with fastdissolve
    KIT "Uhh... guys! We have a biiig problem!"
    hide flayon_neutral
    show flayon_concerned at charfarleft
    with fastdissolve
    FLAY "Huh? What's wrong?"
    hide kit_concerned_cropped
    show kit_crying_cropped at rtrus_screen_topright
    with fastdissolve
    KIT "..."
    KIT "I'm suuuuuuuuuuper hungry!"
    KIT "Can we stop for snacks? Please?"
    hide dean_smug_cropped
    show dean_facepalm_cropped at rtrus_screen_topmid
    with fastdissolve
    DEAN "Seriously..."
    hide flayon_concerned
    show flayon_neutral at charfarleft
    with fastdissolve
    FLAY "Sure, we have time! There must be a place nearby."
    NAVI "Sending coordinates now!"
    pause 0.5
    FLAY "Nice! There's a gas station right here? How convenient!"
    FLAY "Ok guys, let's stop here! This won't take too long."
    hide kit_crying_cropped
    show kit_starryeyed_cropped at rtrus_screen_topright
    KIT "Yay!" 
    hide flayon_neutral
    hide kit_starryeyed_cropped
    hide navi_neutral_cropped
    hide dean_facepalm_cropped
    hide cain_neutral_cropped
    hide charli_neutral_cropped
    hide rtrus_screen
    hide rtrus_screen_1
    hide rtrus_screen_2
    hide rtrus_screen_3
    hide rtrus_screen_4
    with dissolve
    scene bg gas_station_outside with fade
    pause 1.5
    show flayon_concerned at charfarleft
    show navi_disgusted at charfarright
    with dissolve
    NAVI "Eww... this place needs some major redecorating..."
    FLAY "Yeah... let's just be quick, okay?"
    hide navi_disgusted
    hide flayon_concerned
    with fastdissolve
    scene bg gas_station_inside with fade
    pause 1.0
    show flayon_neutral at charfarleft
    with fastdissolve
    FLAY "Huh, everything seems pretty old. And what's with this lighting?"
    show navi_disgusted at charfarright
    with fastdissolve
    NAVI "Gross! Everything's dusty!"
    NAVI "...oh... Look?"
    FLAY "Hmm?"
    hide navi_disgusted
    show navi_neutral at charfarright
    with fastdissolve
    NAVI "Nobody is behind the register? Is... anyone here?"
    hide flayon_neutral
    show flayon_confused at charfarleft
    with fastdissolve
    FLAY "{i}Hm... they're right... that's strange. Why are the lights on if no one is working?{/i}"
    FLAY "{i}Actually, there were no people outside either...{/i}"
    hide navi_neutral
    show navi_worried at charfarright
    with fastdissolve
    NAVI "Let's just grab some snacks and go. This place is seriously freaking me out."
    hide flayon_confused
    show flayon_neutral at charfarleft
    with fastdissolve
    FLAY "Alright, let's see here..."
    hide flayon_neutral
    hide navi_worried
    jump show_interactive_items

label snack_chosen:
    hide screen gas_station_items
    with fastdissolve
    show flayon_neutral at charfarleft
    with fastdissolve
    FLAY "OK, I'm ready! Let's go!"
    show navi_snacks at charfarright
    with fastdissolve
    NAVI "Finally! Time to get back on track!"
    hide flayon_neutral
    hide navi_snacks
    with fastdissolve
    pause 1.0
    jump offline

label door_chosen:
    hide screen gas_station_items
    with fastdissolve
    show flayon_surprised at charfarleft
    with fastdissolve
    FLAY "Looks like it's locked right now..."
    hide flayon_surprised with fastdissolve
    jump show_interactive_items

label offline:
    scene bg pilot_room with fade
    show flayon_neutral at charfarleft
    with fastdissolve
    FLAY "Alright, time to take off!"
    pause 2.0
    show error_1 at rtrus_screen_topleft
    show error_2 at rtrus_screen_bottommidleft
    show error_3 at rtrus_screen_topright
    show error_msg at rtrus_screen_bottommidright
    with fastdissolve
    pause 2.0
    hide flayon_neutral
    show flayon_surprised at charfarleft
    with fastdissolve
    FLAY "What?! RTRUS? What's going on?"
    hide flayon_surprised
    show flayon_confused at charfarleft
    with fastdissolve
    FLAY "Hello? Anyone there?"
    pause 2.0
    hide flayon_confused
    show flayon_concerned at charfarleft
    with fastdissolve
    FLAY "Machiroons, if you can hear this, meet me outside ASAP!"
    hide flayon_concerned with fastdissolve
    pause 0.5
    return