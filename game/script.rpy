# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# We can change the size and the codename in the future by changing the values in size
# if you wanna change the height of the name box just change the variable define gui.name_ypos = -100 in the gui file

define config.tag_layer = {'bg':'background'}
define config.tag_layer={'bg_obj':'background_item'}

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
            item.name = name
            item.image = image
            item.imageH = hover

    class inv:
        def __init__(self):
            self.items = []
            self.amount = 0

        def add(self, itemname, itemimage, hover):
            self.items.append(item(itemname,itemimage,hover))
            self.amount += 1
    

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
            for item in Inventory.items:
                imagebutton:
                    idle item.image 
                    hover item.imageH 
                    action NullAction()
                    tooltip item.name
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
        ypos 0.3
        idle "images/miach.png" 
        
        
        #action [Hide("closecloth"),Show("lookaround")]

screen closewires:
    imagebutton:      
        xpos 0.5 
        ypos 0.3
        idle "images/miach.png" 

screen closeprints2:
    imagebutton:      
        xpos 0.5 
        ypos 0.3
        idle "images/miach.png" 

screen closecam:
    imagebutton:      
        xpos 0.5 
        ypos 0.3
        idle "images/miach.png" 

screen closepaper:
    imagebutton:      
        xpos 0.5 
        ypos 0.3
        idle "images/miach.png" 


screen gaslooks:
    imagebutton:
        xpos 0.5
        ypos 0.3
        idle "images/footprints.png"
        action [Show("closeprints2"),Jump("prints2"), Hide("gaslooks")]

    imagebutton:
        xpos 0.7
        ypos 0.3
        idle "images/secCam.png"
        action [Show("closecam"),Jump("cam"), Hide("gaslooks")]

    imagebutton:
        xpos 0.3
        ypos 0.3
        idle "images/cpaper.png"
        action [Show("closepaper"),Jump("paper"), Hide("gaslooks")]


screen lookaround:
    imagebutton:
        xpos 0.5
        ypos 0.3
        idle "images/footprints.png"
        action [Show("closeprints"),Jump("foots"), Hide("lookaround")]

    imagebutton:
        xpos 0.7
        ypos 0.3
        idle "images/cloth.png"
        action [Show("closecloth"),Jump("cloths"), Hide("lookaround")]

    imagebutton:
        xpos 0.3
        ypos 0.3
        idle "images/wires.png"
        action [Show("closewires"),Jump("wires"), Hide("lookaround")]
                
            
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
    image flay_neutral = "images/Neutral_Flayon.png"
    image flay_think = "images/flay_think.png"
    image flay_worried = "images/flay_worried.png"
    image flay_shock = "images/flay_shock.png"
    image navi_neutral = "images/Navi.png"
    image cain_neutral = "images/Placeholder_Cain.png"
    image dean_neutral = "images/Dean.png"
    image kit_neutral = "images/kit.png"
    image cain_worried = "images/Placeholder_Cain_worried.png"
    image dean_worried = "images/Dean_worried.png"
    image navi_worried = "images/Navi_worried.png"
    image kit_worried = "images/kit_worried.png"
    image cain_flex = "images/cain_flex.png"




label start:
    python:
        Inventory = inv()
        feets = False
        cloth = False
        wire = False

       


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
        show flay_worried at left


label scene2:
    hide kit_neutral
    hide dean_neutral
    hide cain_neutral
    hide navi_worried
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
        $Inventory.add("Orange Cloth","gui/item_placeholder.png", "gui/item_placeholder_hover.png" )
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
    FLAY "!?!?!?"
    hide flay_neutral at left
    show flay_shock at left
    $wire = True
    FLAY "This has clearly been tampered with!"
    FLAY "Listen, If you're gonna tamper with someone's mech, at least hide it better!"
    hide flay_shock at left
    show flay_neutral at left
    hide screen closewires
    jump looks



label looks:
    show screen lookaround
    FLAY "  "

    if (feets and wire and cloth):
        jump gaslooks

    jump looks

label gaslooks:
    show screen gaslooks


label prints2:
    "UNDER CONSTRUCTION"

label cam:
    
    "UNDER CONSTRUCTION"

label paper:
    
    "UNDER CONSTRUCTION"

#prints2 cam paper



#   $Inventory.add("PLACEHOLDER","gui/item_placeholder.png", "gui/item_placeholder_hover.png" )
#    "Congratulations, you got one(1) placeholder item!!"
#    "see it now"
#    $Inventory.add("PLACEHOLDER","gui/item_placeholder.png", "gui/item_placeholder_hover.png")
#    "You got the second item, nice"

#    "placeholder text 2"

    # This ends the game.



