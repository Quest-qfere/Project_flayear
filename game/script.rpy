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
    image bg rtrusExit = "images/bg/bg_rtrus_exit.png"
    #flayon
    image flayon_neutral=im.Scale('images/flayon/flayon_neutral.png', 683, 683)
    image flayon_confused=im.Scale('images/flayon/flayon_confused.png', 683, 683)
    image flayon_excited=im.Scale('images/flayon/flayon_excited.png', 683, 683)
    image flayon_surprised=im.Scale('images/flayon/flayon_surprised.png', 683, 683)
    image flayon_concerned=im.Scale('images/flayon/flayon_concerned.png', 683, 683)
    image flayon_concentrating=im.Scale('images/flayon/flayon_concentrating.png', 683, 683)
    image flayon_smug=im.Scale('images/flayon/flayon_smug.png', 683, 683)
    image flayon_neutral_cropped = Crop((0, 0, 275, 250), "flayon_neutral")
    image flayon_concerned_cropped = Crop((0, 0, 275, 250), "flayon_concerned")
    image flayon_confused_cropped = Crop((0, 0, 275, 250), "flayon_confused")
    image flayon_excited_cropped = Crop((0, 0, 275, 250), "flayon_excited")
    image flayon_surprised_cropped = Crop((0, 0, 275, 250), "flayon_surprised")
    #cain
    image cain_neutral=im.Scale('images/cain/cain_neutral.png', 683, 683)
    image cain_excited=im.Scale('images/cain/cain_excited.png', 683, 683)
    image cain_flex=im.Scale('images/cain/cain_flex.png', 683, 683)
    image cain_worried=im.Scale('images/cain/cain_worried.png', 683, 683)
    image cain_neutral_cropped = Crop((30, 0, 275, 250), im.Scale('images/cain/cain_neutral.png', 410, 410))
    image cain_excited_cropped = Crop((30, 0, 275, 250), im.Scale('images/cain/cain_excited.png', 410, 410))
    image cain_flex_cropped = Crop((30, 0, 275, 250), im.Scale('images/cain/cain_flex.png', 410, 410))
    #charli
    image charli_neutral=im.Scale('images/charli/charli_neutral.png', 683, 683)
    image charli_excited=im.Scale('images/charli/charli_excited.png', 683, 683)
    image charli_neutral_cropped = Crop((30, 0, 275, 250), im.Scale('images/charli/charli_neutral.png', 410, 410))
    image charli_excited_cropped = Crop((30, 0, 275, 250), im.Scale('images/charli/charli_excited.png', 410, 410))
    #dean
    image dean_neutral=im.Scale('images/dean/dean_neutral.png', 683, 683)
    image dean_smug=im.Scale('images/dean/dean_smug.png', 683, 683)
    image dean_concern=im.Scale('images/dean/dean_concern.png', 683, 683)
    image dean_facepalm=im.Scale('images/dean/dean_facepalm.png', 683, 683)
    image dean_neutral_cropped = Crop((30, 0, 275, 250), im.Scale('images/dean/dean_neutral.png', 410, 410))
    image dean_smug_cropped = Crop((30, 0, 275, 250), im.Scale('images/dean/dean_smug.png', 410, 410))
    image dean_concern_cropped = Crop((30, 0, 275, 250), im.Scale('images/dean/dean_concern.png', 410, 410))
    image dean_facepalm_cropped= Crop((30, 0, 275, 250), im.Scale('images/dean/dean_facepalm.png', 410, 410))
    #kit
    image kit_neutral=im.Scale('images/kit/kit_neutral.png', 683, 683)
    image kit_excited=im.Scale('images/kit/kit_excited.png', 683, 683)
    image kit_starryeyed=im.Scale('images/kit/kit_starryeyed.png', 683, 683)
    image kit_concerned=im.Scale('images/kit/kit_concerned.png', 683, 683)
    image kit_crying=im.Scale('images/kit/kit_crying.png', 683, 683)
    image kit_neutral_cropped = Crop((30, 0, 275, 250), im.Scale('images/kit/kit_neutral.png', 410, 410))
    image kit_excited_cropped = Crop((30, 0, 275, 250), im.Scale('images/kit/kit_excited.png', 410, 410))
    image kit_starryeyed_cropped = Crop((30, 0, 275, 250), im.Scale('images/kit/kit_starryeyed.png', 410, 410))
    image kit_concerned_cropped = Crop((30, 0, 275, 250), im.Scale('images/kit/kit_concerned.png', 410, 410))
    image kit_crying_cropped = Crop((30, 0, 275, 250), im.Scale('images/kit/kit_crying.png', 410, 410))
    #navi
    image navi_neutral=im.Scale('images/navi/navi_neutral.png', 683, 683)
    image navi_disgusted=im.Scale('images/navi/navi_disgusted.png', 683, 683)
    image navi_worried=im.Scale('images/navi/navi_worried.png', 683, 683)
    image navi_snacks=im.Scale('images/navi/navi_snacks.png', 683, 683)
    image navi_cake_neutral=im.Scale('images/navi/navi_cakeneutral.png', 683, 683)
    image navi_cake_annoyed=im.Scale('images/navi/navi_cakeannoyed.png', 683, 683)
    image navi_neutral_cropped = Crop((30, 0, 275, 250), im.Scale('images/navi/navi_neutral.png', 410, 410))
    image navi_worried_cropped = Crop((30, 0, 275, 250), im.Scale('images/navi/navi_worried.png', 410, 410))

    # props
    image note = "images/props/act_1/prologue_note_temp.png"
    image rtrus_screen=im.Scale("images/props/act_1/rtrus_screen.png", 300, 300)
    image rtrus_screen_1 = "rtrus_screen"
    image rtrus_screen_2 = "rtrus_screen"
    image rtrus_screen_3 = "rtrus_screen"
    image rtrus_screen_4 = "rtrus_screen"
    image rtrus_screen_5 = "rtrus_screen"
    image error_msg=im.Scale("images/props/act_1/error_msg.png", 200, 100)
    image error_1 = "error_msg"
    image error_2 = "error_msg"
    image error_3 = "error_msg"

    # cg
    image cg1 = "images/cg/cg1.png"
    image cg2 = "images/cg/cg2.png"
    image transition:
        "cg1"                       
        2.9                          
        "cg2" with dissolve       
        2.7
        "#000000" with fade
        1.2

    # game state
    default Inventory = inv()
    default cloth_taken = False
    default cam = False
    default paper_taken = False
    default box = False
    default seenComp = False

      
    #image image=im.Scale('images/char/mode.png', 683, 683)
    #image image=im.Scale('images/char/mode.png', 683, 683)
    #image image=im.Scale('images/char/mode.png', 683, 683)
    #image image=im.Scale('images/char/mode.png', 683, 683)
    #image image=im.Scale('images/char/mode.png', 683, 683)
    #image image=im.Scale('images/char/mode.png', 683, 683)
    #image image=im.Scale('images/char/mode.png', 683, 683)
    #image image=im.Scale('images/char/mode.png', 683, 683)
    #image image=im.Scale('images/char/mode.png', 683, 683)
    #image image=im.Scale('images/char/mode.png', 683, 683)

define FLAY = Character("Flayon", who_suffix="\n{size=-15}Ace Pilot"  )
define NAVI  = Character("Navi", who_suffix="\n{size=-15}Navigator"  )
define CAIN  = Character("Cain", who_suffix="\n{size=-15}Technician"  )
define DEAN = Character("Dean", who_suffix="\n{size=-15}Medic"  )
define KIT = Character("Kit", who_suffix="\n{size=-15}Weapons"  )
define CHARLI = Character("Charli", who_suffix="\n{size=-15}Mechanic"  )

transform charfarleft:
    xcenter 0.1
    yalign 1.0

transform charfarright:
    xcenter 0.9
    yalign 1.0

transform charright:
    xcenter 0.75
    yalign 1.0

transform charmidright:
    xcenter 0.6
    yalign 1.0

transform charmid:
    xcenter 0.45
    yalign 1.0

transform charmidleft:
    xcenter 0.3
    yalign 1.0

transform charleft:
    xcenter 0.15
    yalign 1.0

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
    xalign 0.83
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
    call screen gas_station_items

screen gas_station_items():
    imagebutton:
        xpos 100
        ypos 300
        idle "images/props/act_1/snack1_idle.png"
        hover "images/props/act_1/snack1_hover.png"
        action Jump("snack_chosen")

    imagebutton:
        xpos 400
        ypos 300
        idle "images/props/act_1/snack2_idle.png"
        hover "images/props/act_1/snack2_hover.png"
        action Jump("snack_chosen")

    imagebutton:
        xpos 700
        ypos 300
        idle "images/props/act_1/door_idle.png"
        hover "images/props/act_1/door_hover.png"
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
    jump act2_start

label act2_start:
    python:
        Inventory = inv()
        cloth_taken = False
        cam = False
        paper_taken = False
        box = False
        seenComp = False
    scene bg rtrusExit with fade
    show flayon_neutral at charfarleft
    show dean_concern at charmid
    show kit_concerned at charmidright
    show navi_worried at charright
    show cain_neutral at charfarright
    show screen inventory_button
    DEAN "Weird… I swear I saw Charli just before you two left?"
    NAVI "Yeah, and I didn't hear anyone else leave?"
    KIT "Where are they? Did they receive your message, Flayon?"
    hide dean_concern
    hide kit_concerned
    hide navi_worried
    hide cain_neutral
    with fastdissolve 
    queue sound "sfx/quick-mechanical-keyboard-14391.mp3"
    show screen phone
    with fastdissolve
    FLAY "..."
    hide flayon_neutral
    show flayon_confused at charfarleft
    with fastdissolve
    FLAY "This doesn't look good."
    hide screen phone
    show dean_concern at charmid
    show kit_concerned at charmidright
    show navi_worried at charright
    show cain_neutral at charfarright
    CAIN "How about you have a look around Flay? We can stay back and work on trying to repair the R-TRUS, yeah?"
    menu:
        "Ok! Sounds like a plan.":
            CAIN "Let us know if you need any help!"
            hide cain_neutral
            show cain_flex at charfarright
            with fastdissolve
            jump act2_scene2
        "Hey… are you sure none of you heard anything weird?":
            KIT "Nope!"
            hide kit_concerned
            show kit_neutral at charmidright
            with fastdissolve
            DEAN "Nothing at all."
            hide dean_concern
            show dean_neutral at charmid
            with fastdissolve
            FLAY "Got it..."
            hide flayon_confused
            show flayon_concerned
            with fastdissolve
            jump act2_scene2

label act2_scene2:
    hide kit_neutral
    hide kit_concerned
    hide dean_neutral
    hide cain_neutral
    hide navi_worried
    hide cain_flex
    hide kit_worried
    hide dean_concern
    hide flayon_confused
    hide flayon_concerned
    with fastdissolve
    FLAY "Hmm, maybe I should check outside first?"
    hide flayon_concerned at charfarleft
    show flayon_neutral at charfarleft 
    with fastdissolve
    jump looks

label foots:
    FLAY "They look like they are heading towards the gas station. But, these aren't my footprints. Does Navi wear shoes like this?"
    hide screen closeprints
    jump looks

label cloths:
    FLAY "Oh?"
    hide flayon_neutral at charfarleft
    show flayon_surprised at charfarleft

menu:
    "I remember someone wearing orange…":
        FLAY "Wasn't Charli wearing Orange?!"
        FLAY "I should take this… this might be important evidence!"
        "Orange Cloth added to Inventory"
        $cloth_taken = True
        
        default c = item("Orange Cloth","gui/item_placeholder.png", "gui/item_placeholder_hover.png")
        $Inventory.add(c )
        hide screen closecloth
        jump lookrshock

    "I don't think this belongs to any of us?":
        FLAY "Weird, I don't remember seeing anyone else around here?"
        hide flayon_surprised at charfarleft
        show flayon_neutral at charfarleft
        FLAY "Who could this belong to!"
        hide screen closecloth
        jump looks



label lookrshock:
    hide flayon_surprised at charfarleft
    show flayon_neutral at charfarleft
    jump looks 

label wires:
    queue sound "sfx/sliding-door-6758.mp3"
    FLAY "!?!?!?"
    hide flayon_neutral at charfarleft
    show flayon_surprised at charfarleft
    FLAY "This has clearly been tampered with!"
    FLAY "Listen, If you're gonna tamper with someone's mech, at least hide it better!"
    hide flayon_surprised at charfarleft
    show flayon_neutral at charfarleft
    hide screen closewires
    jump looks

label enterlooks:
    scene rtrusExit
    show flayon_neutral at charfarleft
    jump looks

label looks:

    if (cloth_taken):
        jump looks2

    show screen lookaround
    FLAY "  "
    jump looks

label looks2:
    show screen lookaroundnocloth
    FLAY "  "
    jump looks2

label gasenter:
    scene gasExit
    show flayon_neutral at charfarleft
    jump gaslooks


label gaslooks:
    if (paper_taken):
        show screen gaslooks2
        FLAY "  "
        jump gaslooks
    show screen gaslooks
    FLAY "  "
    jump gaslooks 


label prints2:
    hide flayon_neutral
    show flayon_confused at charfarleft
    FLAY "Oh? These look the same?"
    FLAY "But these are... going away from the front doors?"
    FLAY "...?"
    hide flayon_confused
    show flayon_neutral at charfarleft
    hide screen closeprints2
    jump  gaslooks

label cam:
    FLAY "Oh! They have security cameras!"
    FLAY "I wonder if I can access the footage somehow?"
    $cam = True
    hide screen closecam
    jump gaslooks

label paper:
    FLAY "...hm!"
    queue sound "sfx/door-bang-1wav-14449.mp3"
    hide flayon_neutral
    show flayon_confused at charfarleft
    FLAY "Should I keep this...?"
menu:
    "Keep the note":
        "Crumpled Note added to Inventory"
        $paper_taken = True   
        default p = item("Crumpled Note","gui/item_placeholder.png", "gui/item_placeholder_hover.png" )
        $Inventory.add(p)
        hide screen closepaper
        hide flayon_confused
        show flayon_neutral at charfarleft
        jump gaslooks
    "Discard the note":
        hide screen closepaper
        hide flayon_confused
        show flayon_neutral at charfarleft
        jump gaslooks

label gasstationenter:
    scene store
    show flayon_neutral at charfarleft
    show screen storelooks

label store:
    show screen storelooks
    FLAY "  "
    jump store 


label fridge:
    FLAY "This isn't the time for snacks…"
    hide screen fridges
    jump store

label box:
    if (box):
        hide screen box
        jump placeitem

    $box = True
    if (paper_taken):
        hide flayon_neutral
        show flayon_confused at charfarleft
        FLAY "Hm? This box seems familiar"
        hide flayon_confused
        show flayon_neutral at charfarleft
        hide screen box
        jump placeitem
    else:
        FLAY "A box."
        FLAY "An empty box."
        hide screen box
        jump placeitem

label placeitem:
    hide flayon_neutral
    if (Inventory.amount != 0):
        "Store An Item?"
        menu:
            "Yes":
                call screen storing
                $stored = _return
                $Inventory.remove(stored)
            "No":
                show flayon_neutral at charfarleft
                jump store       
         
    show flayon_neutral at charfarleft
    if (Inventory.amount == 0):
        FLAY "There is nothing to put in the box"
    
    jump store


label securityRoom:
    if (cam and not seenComp):
        hide flayon_neutral
        show flayon_excited at charfarleft
        FLAY "Oh! Maybe I can find the footage from the cameras outside here?"
        FLAY "Maybe my tail will work? Let me just…"

        "HE PICKS THE LOCK (CG???)"
        queue sound "sfx/door-bang-1wav-14449.mp3"
        hide flayon_excited
        show flayon_smug at charfarleft
        FLAY "Heh, easy."
        $seenComp = True
        jump securityRoomEnter
    if (cam and seenComp):
        jump securityRoomEnter2
    if (not cam):
        "NO DIALOGUE, JUST SAYS SAME TEXT AS  EARLIER BUT WHAT IS SAID EARLIER IDK PLACEHOLDER HELP"
        jump store

label securityRoomEnter:
    scene secRoom
    show screen secroom
    #hide flayon_smug
    show flayon_smug at charfarleft
    " "
    jump securityRoomEnter

label securityRoomEnter2:
    scene secRoom
    show screen secroom
    #hide flayon_smug
    show flayon_neutral at charfarleft
    " "
    jump securityRoomEnter

label computer:
    hide flayon_smug
    show flayon_concentrating at charfarleft

    FLAY "Let's see..."

    show transition
    $ renpy.pause(7.8, hard=True)
    "END OF ACT"
    jump act_4

label act_4:
        # These display lines of dialogue.
    show bg party_room with fade
    pause 0.5
    show flayon_surprised at charfarleft
    show charli_excited at charfarright
    with fastdissolve
    FLAY "Charli!?"
    CHARLI "Hi Flay! Surprise~"
    hide flayon_surprised
    show flayon_excited at charfarleft
    FLAY "You're okay!"
    CHARLI "Of course I am, silly! Sorry for tricking you, hehe~ How else would we get you to your surprise party?"
    hide flayon_excited
    show flayon_confused at charfarleft
    
    with fastdissolve
    FLAY "Surprise... party...?"
    show cain_excited at charright with fastdissolve
    CAIN "YEAH! Happy birthday, man! Did you really think we forgot?"
    hide flayon_confused
    show flayon_neutral at charfarleft
    with fastdissolve
    FLAY "Honestly, I was so distracted I kind of forgot myself."
    #hide cain_excited with fastdissolve
    show kit_excited at charmidright with fastdissolve
    KIT "Well that's nooooo good! We are gonna make sure you have the BEST party ever!"
    #hide kit_excited with fastdissolve
    show dean_neutral at charmid with fastdissolve 
    DEAN "I did try to advise against the whole \"fake kidnapping\" scenario, by the way."
    CHARLI "You have to admit, I'm a very good actor, right?"
    hide dean_neutral
    show dean_smug at charmid
    with fastdissolve
    DEAN "...Yes. You did well."
    FLAY "So the whole thing was fake?"
    hide kit_excited
    show kit_neutral at charmidright
    with fastdissolve
    KIT "It was! Come on, when would I ever ask to stop for snacks in the middle of a mission?"
    hide cain_excited
    show cain_neutral at charright
    with fastdissolve
    CAIN "Tiny, that is totally something you would do."
    FLAY "You organized all of this, just to surprise me?"
    hide dean_smug
    show dean_neutral at charmid
    with fastdissolve
    DEAN "Correct. We thought you deserved something grand."
    DEAN "...a gas station basement isn't exactly what I had in mind."
    hide charli_excited
    show charli_neutral at charfarright
    with fastdissolve
    CHARLI "We made it work! I think it's purr-fect!"
    FLAY "It's very... well... roon-coded!"
    NAVI "Ahem! Quick! Before the candles go out!"
    hide flayon_neutral
    hide charli_neutral
    hide dean_neutral
    hide cain_neutral
    hide kit_neutral
    with dissolve
    scene bg navi_cake with fade
    call screen birthday_button
    scene bg party_room with fade
    show flayon_neutral at charfarleft
    show navi_cake_neutral at charmidright
    with fastdissolve
    NAVI "Happy birthday, Machina!"
    NAVI "Hopefully you like the cake; I spent a {i}while{/i} decorating it."
    hide navi_cake_neutral 
    show navi_cake_annoyed at charmidright
    with fastdissolve
    NAVI "...I mean. It didn't take that long. It actually took no time at all! Ha!"
    NAVI "..."
    hide navi_cake_annoyed
    show navi_cake_neutral at charmidright
    with fastdissolve
    NAVI "But I do hope you like it. And I hope you have an... {i}adequate{/i} birthday!"
    FLAY "Thank you, Navi! The cake looks great!"
    hide navi_cake_neutral with fastdissolve
    pause 0.1
    show cain_neutral at charmidright with fastdissolve
    CAIN "Happy birthday, boss!"
    CAIN "Sorry about the fighting earlier. I still want a rematch, though!"
    hide cain_neutral
    show cain_excited at charmidright
    with fastdissolve
    CAIN "Enjoy the party, dude! You so totally deserve it! You're like, the best leader ever!"
    CAIN "HIGH FIVE!!!"
    hide window
    pause 0.3
    hide cain_excited with fastdissolve
    pause 0.1
    show dean_neutral at charmidright with fastdissolve
    window show
    DEAN "Machina, happy birthday!"
    DEAN "Like I mentioned, I was against this whole \"Birthday Scavenger Hunt\" situation."
    hide dean_neutral
    show dean_smug at charmidright
    with fastdissolve
    DEAN "But I have to say, it was pretty fun. I hope you had fun too."
    hide dean_smug
    show dean_concern at charmidright
    with fastdissolve
    DEAN "And I promise I will get Cain and Charli to fix the damages on the R-TRUS before we leave. They aren't that bad... {size=-10}I hope.{/size}"
    hide flayon_neutral
    show flayon_confused at charfarleft
    with fastdissolve
    FLAY "Thanks, Dean! Wait, you guys actually damaged it? But---{nw}"
    hide dean_concern
    show kit_excited at charmidright
    with fastdissolve
    KIT "FLAY!"
    KIT "Do you like the decorations?! I put them all up myself!"
    hide kit_excited
    show kit_neutral at charmidright
    with fastdissolve
    KIT "I wanted to do indoor fireworks, but Navi told me no."
    hide kit_neutral
    show kit_starryeyed at charmidright
    with fastdissolve
    KIT "I HOPE YOU HAVE THE BEST BIRTHDAY EVEEEEEEEEEER!"
    KIT "We love you! Don't forget it!"
    hide kit_starryeyed
    show kit_excited at charmidright
    with fastdissolve
    KIT "Let's party! YAYYYYY!"
    hide kit_excited with fastdissolve
    pause 0.1
    show charli_neutral at charmidright 
    show flayon_neutral at charfarleft
    with fastdissolve
    CHARLI "Hiya, Machinya! Sorry for today!"
    CHARLI "This whole thing was my idea and I may have gotten slightly carried away! Hehe..."
    hide charli_neutral
    show charli_excited at charmidright
    with fastdissolve
    CHARLI "But, I just wanted to make sure you had the best party ever! You do so much for us, and we are all so thankful, meow!"
    hide charli_excited
    show charli_neutral at charmidright
    with fastdissolve
    CHARLI "Thank you, Machi! I hope you have the best birthday!"
    FLAY "Charli... everyone... thank you!"
    show navi_neutral at charmidleft
    show cain_neutral at charmid
    show dean_neutral at charright
    show kit_neutral at charfarright
    with fastdissolve
    "Happy birthday, Flayon!"
    NAVI "We hope you had fun!"
    NAVI "Sending you around on a wild goose chase was honestly pretty funny!"
    hide cain_neutral
    show cain_flex at charmid
    with fastdissolve
    CAIN "Next year, how about we do an arm wrestling bracket?"
    CAIN "No? I'll keep training anyway."
    DEAN "It was definitely an {i}interesting{/i} way to show our appreciation..."
    DEAN "But hopefully, we got the message across."
    KIT "Happy birthday, Flayon! Thank you for everything!"
    CHARLI "We love you! Meow and forever~ We couldn't think of anyone better to be our leader!"
    hide charli_neutral
    show charli_excited at charmidright
    with fastdissolve
    CHARLI "Now, time to party!"
    scene black with fade
    hide window
    pause 5.0
    window show
    "THE END."
    return
