# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# We can change the size and the codename in the future by changing the values in size
# if you wanna change the height of the name box just change the variable define gui.name_ypos = -100 in the gui file

define config.tag_layer = {'bg':'background'}
define config.tag_layer={'bg_obj':'background_item'}
default preferences.text_cps = 40

define FLAY = Character("Flayon", who_suffix="\n{size=-15}Ace Pilot"  )

define NAVI  = Character("Navi", who_suffix="\n{size=-15}Code name"  )

define CAIN  = Character("Cain", who_suffix="\n{size=-15}Code name"  )

define DEAN = Character("Dean", who_suffix="\n{size=-15}Code name"  )

define KIT = Character("Kit", who_suffix="\n{size=-15}Code name"  )
# The game starts here.

#inventory
init python:
    class item:
        def __init__(self, name, image, hover):
            self.name = name
            self.image = image
            self.imageH = hover

    class inv:
        def __init__(self):
            self.items = []
            self.amount = 0

        def add(self, itemname, itemimage, hover):
            self.items.append(item(itemname,itemimage,hover))
            self.amount += 1

        def add(self, item):
            self.items.append(item)
            self.amount+=1

        def remove(self,item):
            self.items.remove(item)
            self.amount -=1

screen inventory_button:
    textbutton "Inventory" action [ Show("Inven"),Hide("inventory_button")] align (0.95, 0.04)

screen Inven:
    add "gui/main_menu.png" xalign 1
    hbox align (0.95, 0.04)  spacing 20:
        textbutton "Close Inventory" action [Hide("Inven"), Show("inventory_button")]
    if Inventory.amount == 0:
        text "no items :c" at transform:
            align (0.5, 0.1)
    else:
        hbox xfill False spacing 15 xalign 0.5:
            for i in Inventory.items:
                imagebutton:
                    idle i.image 
                    hover i.imageH 
                    action NullAction()
                    tooltip i.name
        $ tooltip = GetTooltip()
        
        if tooltip:
            nearrect:
                focus "tooltip"
                prefer_top True

                frame:
                    xalign 0.5
                    text tooltip


screen phone:
    imagebutton:
        xpos 0.7
        ypos 0.4
        idle  "images/phone.png"

screen closeprints:
    imagebutton:      
        xpos 0.5 
        ypos 0.3
        idle "images/miach.png" 
        
        
        #action [Hide("closeprints"),Show("lookaround"), Jump("looks")]

screen closecloth:
    imagebutton:      
        xpos 0.5 
        ypos 0.5
        idle "images/miach.png" 
        
        
        #action [Hide("closecloth"),Show("lookaround")]

screen closewires:
    imagebutton:      
        xpos 0.5 
        ypos 0.5
        idle "images/miach.png" 

screen closeprints2:
    imagebutton:      
        xpos 0.5 
        ypos 0.5
        idle "images/miach.png" 

screen closecam:
    imagebutton:      
        xpos 0.5 
        ypos 0.5
        idle "images/miach.png" 

screen closepaper:
    imagebutton:      
        xpos 0.5 
        ypos 0.5
        idle "images/miach.png" 

screen fridges:
    imagebutton:      
        xpos 0.5 
        ypos 0.5
        idle "images/miach.png" 

screen box:
    imagebutton:      
        xpos 0.5 
        ypos 0.5
        idle "images/miach.png" 


screen storelooks:
    imagebutton:
        xpos 0.5
        ypos 0.3
        idle "images/fridge.png"
        action [ Hide("storelooks"),Show("fridges"),Jump("fridge")]

    imagebutton:
        xpos 0.7
        ypos 0.3
        idle "images/door.png"
        action [ Hide("storelooks"),Jump("securityRoom")]

    imagebutton:
        xpos 0.3
        ypos 0.3
        idle "images/box.png"
        action [ Hide("storelooks"),Show("box"),Jump("box")]


screen gaslooks:
    imagebutton:
        xpos 0.5
        ypos 0.3
        idle "images/footprints.png"
        action [ Hide("gaslooks"),Show("closeprints2"),Jump("prints2")]

    imagebutton:
        xpos 0.7
        ypos 0.3
        idle "images/secCam.png"
        action [ Hide("gaslooks"),Show("closecam"),Jump("cam")]

    imagebutton:
        xpos 0.3
        ypos 0.3
        idle "images/cpaper.png"
        action [ Hide("gaslooks"),Show("closepaper"),Jump("paper")]

    imagebutton:
        xpos 0
        ypos 0
        idle "images/gas_station_door.png"
        action [ Hide("gaslooks"),Jump("gasstationenter")]

screen gaslooks2:
    imagebutton:
        xpos 0.5
        ypos 0.3
        idle "images/footprints.png"
        action [ Hide("gaslooks2"),Show("closeprints2"),Jump("prints2")]

    imagebutton:
        xpos 0.7
        ypos 0.3
        idle "images/secCam.png"
        action [ Hide("gaslooks2"),Show("closecam"),Jump("cam")]

    imagebutton:
        xpos 0
        ypos 0
        idle "images/gas_station_door.png"
        action [ Hide("gaslooks2"),Jump("gasstationenter")]


screen lookaround:
    imagebutton:
        xpos 0.5
        ypos 0.3
        idle "images/footprints.png"
        action [Hide("lookaround"),Show("closeprints"),Jump("foots") ]

    imagebutton:
        xpos 0.7
        ypos 0.3
        idle "images/cloth.png"
        action [Hide("lookaround"),Show("closecloth"),Jump("cloths")]

    imagebutton:
        xpos 0.3
        ypos 0.3
        idle "images/wires.png"
        action [Hide("lookaround"),Show("closewires"),Jump("wires")]

    imagebutton:
        xpos 0
        ypos 0
        idle "images/gas_station_door.png"
        action [ Hide("lookaround"),Jump("gasenter")]

screen lookaroundnocloth:
    imagebutton:
        xpos 0.5
        ypos 0.3
        idle "images/footprints.png"
        action [ Hide("lookaroundnocloth"), Show("closeprints"),Jump("foots")]

    imagebutton:
        xpos 0.3
        ypos 0.3
        idle "images/wires.png"
        action [Hide("lookaroundnocloth"), Show("closewires"),Jump("wires")]

    imagebutton:
        xpos 0
        ypos 0
        idle "images/gas_station_door.png"
        action [Hide("lookaroundnocloth"), Jump("gasenter")]

screen storing:
    vbox:
        align (0.5, 0.5)
        for item in Inventory.items:
            $name = item.name
            textbutton "[name]" action Return(item)   

screen secroom:
    imagebutton:      
        xpos 0.5 
        ypos 0.5
        idle "images/computer.png" 
        action [ Hide("secroom"),Jump("computer")]      
            
transform right2:
    xcenter  0.8
    yalign  1.0

transform right3:
    xcenter  0.65
    yalign  1.0

transform right4:
    xcenter 0.5
    yalign 1.0
                
init:
    image rtrusExit = "images/RTrus_exit.png"
    image gasExit = "images/gas_station_ext.png"
    image store = "images/Store_Background.png"
    image secRoom = "images/SecRoom.png"
    image flay_neutral = "images/Neutral_Flayon.png"
    image flay_think = "images/flay_think.png"
    image flay_worried = "images/flay_worried.png"
    image flay_shock = "images/flay_shock.png"
    image flay_excite = "images/flayconcentrate.png"
    image flay_smug = "images/flaysmug.png"
    image flay_concentrate = "images/flayshock/png"
    image navi_neutral = "images/Navi.png"
    image cain_neutral = "images/Placeholder_Cain.png"
    image dean_neutral = "images/Dean.png"
    image kit_neutral = "images/kit.png"
    image cain_worried = "images/Placeholder_Cain_worried.png"
    image dean_worried = "images/Dean_worried.png"
    image navi_worried = "images/Navi_worried.png"
    image kit_worried = "images/kit_worried.png"
    image cain_flex = "images/cain_flex.png"

    image cg1 = "images/cg1.png"
    image cg2 = "images/cg2.png"



    default Inventory = inv()
    default feets = False
    default cloth = False
    default wires = False
    default cloth_taken = False
    default feets2 = False
    default cam = False
    default paper = False
    default paper_taken = False
    default box = False

    image transition:
        "cg1"                       
        2.9                          
        "cg2" with dissolve       
        2.7
        "#000000" with fade
        1.2
      

label start:
    python:
        Inventory = inv()
        feets = False
        cloth = False
        wires = False
        cloth_taken = False
        feets2 = False
        cam = False
        paper = False
        paper_taken = False
        box = False

       


    # These display lines of dialogue.
    scene rtrusExit
    show flay_neutral at left
    show dean_worried at right
    show kit_worried at right2
    show navi_worried at right3
    show cain_neutral at right4

    " My name is Machina X Flayon, the pilot of guild Tempus." 
    " As a guild of smart, brave adventurers, we get commissioned for quests often, but today was different; a quest came through for me specifically!
"   
    show screen inventory_button
    DEAN "Weird… I swear I saw Charli just before you two left?"

    NAVI "Yeah, and I didn't hear anyone else leave?"

    KIT "Where are they? Did they receive your message, Flayon?"
    hide dean_worried
    hide kit_worried
    hide navi_worried
    hide cain_neutral

    queue sound "sfx/quick-mechanical-keyboard-14391.mp3"
    show screen phone

    

    FLAY "..."
    show flay_think at left
    FLAY "This doesn't look good."
    
    hide screen phone
    show dean_worried at right
    show kit_worried at right2
    show navi_worried at right3
    show cain_neutral at right4

    CAIN "How about you have a look around Flay? We can stay back and work on trying to repair the R-TRUS, yeah?"

menu:

    "Ok! Sounds like a plan.":
        CAIN "Let us know if you need any help!"
        show cain_flex at right4

    "Hey… are you sure none of you heard anything weird?":
        KIT "Nope!"
        hide kit_worried
        show kit_neutral at right2
        DEAN "Nothing at all."
        hide dean_worried
        show dean_neutral at right
        FLAY "Got it..."
        hide flay_think
        show flay_worried at left


label scene2:
    hide kit_neutral
    hide dean_neutral
    hide cain_neutral
    hide navi_worried
    hide cain_flex
    hide kit_worried
    hide dean_worried
    hide flay_think
    FLAY "Hmm, maybe I should check outside first?"
    hide flay_worried at left
    show flay_neutral at left 
    

    jump looks

label foots:

    FLAY "They look like they are heading towards the gas station. But, these aren't my footprints. Does Navi wear shoes like this?"
    $feets = True
    hide screen closeprints
    jump looks

label cloths:
    FLAY "Oh?"
    hide flay_neutral at left
    show flay_shock at left
    $cloth = True

menu:
    #ask do we need to get the cloth to go ahead

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
        hide flay_shock at left
        show flay_neutral at left
        FLAY "Who could this belong to!"
        hide screen closecloth
        jump looks


label lookrshock:
    hide flay_shock at left
    show flay_neutral at left
    jump looks 

label wires:
    queue sound "sfx/sliding-door-6758.mp3"
    FLAY "!?!?!?"
    hide flay_neutral at left
    show flay_shock at left
    $wires = True
    FLAY "This has clearly been tampered with!"
    FLAY "Listen, If you're gonna tamper with someone's mech, at least hide it better!"
    hide flay_shock at left
    show flay_neutral at left
    hide screen closewires
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
    if (wires and cloth and feets):
        scene gasExit
        show flay_neutral at left
        show screen gaslooks
        jump gaslooks
    if (not (wires and cloth and feets)):
        FLAY "I think there is still something here to find."
    if (cloth_taken):
        jump looks2
    jump looks

label gaslooks:
    

    if (paper_taken):
        FLAY "  "
        show screen gaslooks2
        jump gaslooks
    FLAY "  "
    show screen gaslooks
    jump gaslooks 


label prints2:
    hide flay_neutral
    show flay_think at left
    FLAY "Oh? These look the same?"
    FLAY "But these are... going away from the front doors?"
    FLAY "...?"
    $feets2 = True
    hide flay_think
    show flay_neutral at left
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
    $paper = True
    hide flay_neutral
    show flay_think at left
    FLAY "Should I keep this...?"
menu:

    "Keep the note":
        "Crumpled Note added to Inventory"
        $paper_taken = True
        
        default p = item("Crumpled Note","gui/item_placeholder.png", "gui/item_placeholder_hover.png" )
        $Inventory.add(p)
        hide screen closepaper
        hide flay_think
        show flay_neutral at left
        jump gaslooks





    "Discard the note":
        hide screen closepaper
        hide flay_think
        show flay_neutral at left
        jump gaslooks

label gasstationenter:
    scene store
    show flay_neutral at left
    show screen storelooks

label store:
    FLAY "  "
    show screen storelooks
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
        hide flay_neutral
        show flay_think at left
        FLAY "Hm? This box seems familiar"
        hide flay_think
        show flay_neutral at left
        hide screen box
        jump placeitem
    else:
        FLAY "A box."
        FLAY "An empty box."
        hide screen box
        jump placeitem

label placeitem:
    hide flay_neutral
    if (Inventory.amount != 0):
        "Store An Item?"
        menu:
            "Yes":
                call screen storing
                $stored = _return
                $Inventory.remove(stored)
            "No":
                show flay_neutral at left
                jump store                
    show flay_neutral at left
    jump store


label securityRoom:
    if (cam):
        hide flay_neutral
        show flay_excite at left
        FLAY "Oh! Maybe I can find the footage from the cameras outside here?"
        FLAY "Maybe my tail will work? Let me just…"

        "HE PICKS THE LOCK (CG???)"
        queue sound "sfx/door-bang-1wav-14449.mp3"
        hide flay_excite
        show flay_smug at left
        FLAY "Heh, easy."
        jump securityRoomEnter
    if (not cam):
        "Unreachable currently. What is the previous dialogue"
        jump Store

label securityRoomEnter:
    scene secRoom
    show screen secroom
    #hide flay_smug
    show flay_smug at left
    " "
    jump securityRoomEnter

label computer:
    hide flay_smug
    show flay_concentrate at left

    FLAY "Let's see..."

    show transition
    $ renpy.pause(7.8, hard=True)
    "END OF ACT"


        



#   $Inventory.add("PLACEHOLDER","gui/item_placeholder.png", "gui/item_placeholder_hover.png" )
#    "Congratulations, you got one(1) placeholder item!!"
#    "see it now"
#    $Inventory.add("PLACEHOLDER","gui/item_placeholder.png", "gui/item_placeholder_hover.png")
#    "You got the second item, nice"

#    "placeholder text 2"

    # This ends the game.



