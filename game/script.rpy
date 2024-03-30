# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# We can change the size and the codename in the future by changing the values in size
# if you wanna change the height of the name box just change the variable define gui.name_ypos = -100 in the gui file
define config.tag_layer = {'bg':'background'}
define config.tag_layer={'bg_obj':'background_item'}

screen screen_interactable:
       imagebutton:
        xpos 0.5
        ypos 0.5
        idle "images/error_screen.png" 
        hover "images/error_screen_highlight.png" 
        action Jump("error_message")
       imagebutton:
        xpos 0.4
        ypos 0.5
        idle "images/running_machine.png" 
        hover "images/running_machine_highlited.png" 
        action Jump("running_machine")
       imagebutton:
        at halfsize
        xpos 0.8
        ypos 0.6
        idle "images/Placeholder_Cain.png" 
        hover "images/Placeholder_Cain_highlighted.png" 
        action Jump("cain_dia")
       imagebutton:
        xpos 0.2
        ypos 0.6
        idle "images/plushies.png"
        hover "images/plushies_highlighted.png"
        action Jump("plushies")
   
init:
    image bg general_area="images/general_area.PNG"
    image bg navigation_room="images/navigation_room.png"
    image flay_neutral="images/Neutral_Flayon.png"
    image flay_smug="images/Neutral_Flayon.png"
    image flay_unamused="images/Flayon_unamused.png"
    image flayon_neutral_deadpan="images/Flayon_neutral_deadpan.jpg"
    image flay_thinking="images/Neutral_Flayon.png"
    image flayon_annoyed_deadpan="images/Flayon_neutral_deadpan.jpg"
    image flayon_glare_annoyed="images/Flayon_glare_annoyed.jpg"
    image flayon_smirk="images/Flayon_smirk.jpg"
    image flayon_excited="images/Neutral_Flayon.png"
    image flayon_confused="images/Neutral_Flayon.png"
    image flay_stunned="images/Neutral_Flayon.png"
    image cain_neutral="images/Placeholder_Cain.png"
    image cain_worried="images/Placeholder_Cain.png"
    image cain_head_empty="images/Placeholder_Cain.png"
    image cain_excited="images/Placeholder_Cain.png"
    image cain_flexing="images/Placeholder_Cain.png"
    image cain_out_of_breath="images/Placeholder_Cain.png"
    image error_screen="images/error_screen.png"

define FLAY = Character("Flayon", who_suffix="\n{size=-15}Ace Pilot"  )

define NAVI  = Character("Navi", who_suffix="\n{size=-15}Code name"  )

define CAIN  = Character("Cain", who_suffix="\n{size=-15}Code name"  )

define DEAN = Character("Dean", who_suffix="\n{size=-15}Code name"  )

define KIT = Character("Kit", who_suffix="\n{size=-15}Code name"  )
#dark light tint matrixcolor TintMatrix("7A7A7B")
# dark tint  matrixcolor TintMatrix("4C4CAA")
# The game starts here.
transform cain_position:
        xalign 0.8
        yalign 0.6
        zoom 0.2
transform  big_size:
        zoom 2.0
transform halfsize:
        zoom 0.2
label start:
    # These display lines of diaslogue.
   

 
    scene bg general_area 
    show flay_neutral at left
    "Ah… Sometimes I think CAIN, our technician, only works here to use the high-tech workout gear we have…\nI'm still not sure they actually know how to work a computer. Still, they have enough energy for the entire team so it's helpful to have them around!"
    
    queue sound "sfx/sliding-door-6758.mp3"
    queue sound "sfx/quick-mechanical-keyboard-14391.mp3"
    
    call screen screen_interactable
label running_machine:
        show flay_neutral at left
        "Cain’s running machine! We spent a whole week working on modding this so it can track every detail of your run, they let me use it whenever I want!"
        call screen screen_interactable
label plushies:
        show flay_smug at left
        "Cute…!"
        call screen screen_interactable
label error_message:
        show flay_neutral at left
        "Hm, something is definitely wrong… I hope we can fix this soon…"
        call screen screen_interactable

label cain_dia:
    CAIN "Flay, dude! what’s up!"
    FLAY "Hey Cain, any progress?"
    show cain_worried at cain_position
    CAIN "Nope, sorry man. \nIt’s so weird… I just can't find the error!?\nSomething is definitely fishy about this…"
    show flay_thinking at left
    FLAY "For sure… \nWhat about Charli, have you heard anything?"
    show cain_neutral at cain_position
    CAIN "Nope again … Sorry bro …\nI'm gonna try and focus on getting the systems back online. ASAP!"
    show flay_neutral at left
    FLAY "Cool, let me know if you find any information or clues, ok?"
    show cain_head_empty at cain_position
    CAIN "…Clues?"
    FLAY "yeah! I found a couple of notes and footprints outside. I'm starting to think someone, or something, got into the R-TRUS."
    show cain_excited at cain_position
    CAIN "…Well it’s your lucky day!\nI found a clue!"
    show flayon_excited at left
    FLAY "…!"
    "Cain holds up a folded piece of paper that literally has the word “CLUE” written on it."
    CAIN "I found it on the floor when I came inside!\n Woah! A real clue! This is awesome!!!"
    FLAY "Yeah!"
    show cain_neutral at cain_position
    CAIN "…"
    show flay_neutral at left
    FLAY "…"
    show cain_head_empty at cain_position
    CAIN "…"
    FLAY "Sooo… can I have it?"
    show cain_neutral at cain_position
    CAIN "Heh … not so fast buddy! This is the PERFECT opportunity!"
    FLAY "Hm? For what?"
    ##play boss fight music
    jump cain_fight
label cain_fight:   
    show cain_flexing at cain_position
    CAIN "… FIGHT ME MACHINA X FLAYON!"
    show flay_stunned at left
    FLAY "You… Want to fight?…\nRight now ?"
    CAIN "I KNOW I can beat you …\nAre you scared perhaps …\nScared of losing to me !"
    show flay_neutral at left
    FLAY "Fine… you know what … "
    show flayon_excited at left
    extend "BRING IT ON !"
    show cain_excited at cain_position
    CAIN "HAHA! FINALLY! If you win, you can have the clue, ready?"
    FLAY "I was born ready, Cain!"
    show cain_flexing at cain_position
    CAIN "COME AT ME!!! {size=-10}sorry flay i respect you as a leader and a pilot i just need to fight you it’s a personal urge i have i’m sorry this is all affectionate ok good luck man.{/size}"
    "Pick the moves in the correct order to win!"
    $ right_moves = 0
    $ wrong_moves = 0
    jump fight

label fight:
   
    if right_moves+wrong_moves==0:
       "Pick your first move!"
    elif right_moves+wrong_moves==1:
        "Pick your second move!"
    elif right_moves+wrong_moves==2:
       CAIN "Watch this!"
       "CAIN uses SWEEPING KICK"
       "Pick your third move!"
    elif right_moves+wrong_moves==3: 
        CAIN "Don’t hold back!"
        "CAIN uses READY TO STRIKE."
        "Pick your last move!"
        jump fight_choices
    elif  wrong_moves==4 or right_moves<4:
       show cain_excited at cain_position
       CAIN "Heh… Prepare for my finishing move…"
       show  cain_head_empty at cain_position
       extend "THE… "
       show cain_head_empty
       extend"The… \nI forgot to name my finishing move…"
       show cain_flexing at cain_position
       extend "\nTHE COOLEST FINISHING MOVE OF ALL TIME!"
       #unlock cg and show it
       $ persistent.unlock_3=True
       "Would you like to try again?"
       menu:
                "Yes":
                        jump cain_fight
                "Main menu":
                        return
    elif right_moves==4:
        show cain_out_of_breath at cain_position
        CAIN "Ok… You win Maybe I need some more training…"
        show cain_excited at cain_position 
        extend "THAT WAS SO MUCH FUN!"
        show flay_neutral at left
        FLAY "You put up a good fight! We can train together anytime, okay?"
        show cain_neutral at cain_position
        CAIN "Thank you bro… You're so… so cool…"
        show cain_excited at cain_position
        CAIN "Here! Hopefully it's helpful!"
        show cain_neutral at cain_position
        CAIN "Thanks for the fight! Good luck finding the other clues! I should get back to the computer now…" 
        FLAY "See ya, Cain!"
        jump end
label fight_choices:
    menu:
        "ROUNDHOUSE":
                queue sound "sfx/punch-140236.mp3"
                if right_moves+wrong_moves==2:
                        $ right_moves=right_moves+1
                        jump fight
                else:
                        $ wrong_moves=wrong_moves+1
                        jump fight
        "TAIL WHIP":
                queue sound "sfx/punch-140236.mp3"
                if right_moves+wrong_moves==3:
                        $ right_moves=right_moves+1
                        jump fight
                else:
                        $ wrong_moves=wrong_moves+1
                        jump fight
        "SCRATCH":
                   queue sound "sfx/punch-140236.mp3"
                   if right_moves+wrong_moves==0 or right_moves+wrong_moves==1 :
                        $ right_moves=right_moves+1
                        jump fight
                   else:
                        $ wrong_moves=wrong_moves+1
                        jump fight

        "SHIELD PUNCH":
                   queue sound "sfx/punch-140236.mp3"
                   if right_moves+wrong_moves==0 or right_moves+wrong_moves==1:
                        $ right_moves=right_moves+1
                        jump fight
                   else:
                        $ wrong_moves=wrong_moves+1
                        jump fight


label end:
    "unlock cgs"
    $ persistent.unlock_2=True
    $ persistent.unlock_1=True
    "..."
    return
