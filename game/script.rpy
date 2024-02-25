# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# We can change the size and the codename in the future by changing the values in size
# if you wanna change the height of the name box just change the variable define gui.name_ypos = -100 in the gui file

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

label start:
    python:
        Inventory = inv()


    # These display lines of dialogue.

    " My name is Machina X Flayon, the pilot of guild Tempus." 
    " As a guild of smart, brave adventurers, we get commissioned for quests often, but today was different; a quest came through for me specifically!
"   
    FLAY "Miach Miach"

    show screen inventory_button
    "Unlocking inventory"
    $Inventory.add("PLACEHOLDER","gui/item_placeholder.png", "gui/item_placeholder_hover.png" )
    "Congratulations, you got one(1) placeholder item!!"
    "see it now"
    $Inventory.add("PLACEHOLDER","gui/item_placeholder.png", "gui/item_placeholder_hover.png")
    "You got the second item, nice"

    "placeholder text 2"
    # This ends the game.

    return
