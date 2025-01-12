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
    imagebutton:      
        xpos 0.4 
        ypos 0.25
        idle "images/inv.png" 
    if Inventory.amount == 0:
        text "{color=#f00}no items :c{/color}" at transform:
            align (0.5, 0.365)
    else:
        hbox align (0.5,0.)
        $count = 0
        for i in Inventory.items:
            textbutton "{color=#f00}[i.name]{/color}":
                action NullAction()
                text_hover_strikethrough True
                xpos 0.445
                yalign 0.365+  count * 0.03
            $count +=1

        $ tooltip = GetTooltip()
        
        if tooltip:
            nearrect:
                focus "tooltip"
                prefer_top True

                frame:
                    xalign 0.5
                    text tooltip

#               hover "{s}{i.name}{/s}"
#
init:
    default Inventory = inv()

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
    default pl1 = item("PLACEHOLDER","gui/item_placeholder.png", "gui/item_placeholder_hover.png" )
    $Inventory.add(pl1)
    "Congratulations, you got one(1) placeholder item!!"
    "see it now"

    default pl2 = item("PLACEHOLDER 222","gui/item_placeholder.png", "gui/item_placeholder_hover.png" )

    $Inventory.add(pl2)
    "You got the second item, nice"

    "placeholder text 2"
    # This ends the game.

    return
                

   




