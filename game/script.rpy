# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# We can change the size and the codename in the future by changing the values in size
# if you wanna change the height of the name box just change the variable define gui.name_ypos = -100 in the gui file
define config.tag_layer = {'bg':'background'}
define config.tag_layer={'bg_obj':'background_item'}
define config.default_text_cps = 45
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

define FLAY = Character("Flayon", who_suffix="\n{size=-15}Ace Pilot",what_slow_cps=25  )

define NAVI  = Character("Navi", who_suffix="\n{size=-15}Code name",what_slow_cps=25  )

define CAIN  = Character("Cain", who_suffix="\n{size=-15}Code name",what_slow_cps=25  )

define DEAN = Character("Dean", who_suffix="\n{size=-15}Code name",what_slow_cps=25  )

define KIT = Character("Kit", who_suffix="\n{size=-15}Code name",what_slow_cps=25  )
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
    "{cps=25} Ah… Sometimes I think CAIN, our technician, only works here to use the high-tech workout gear we have…{/cps}"
    extend "{cps=25} I'm still not sure they actually know how to work a computer.{/cps}"
    extend "{cps=25} Still, they have enough energy for the entire team so it's helpful to have them around!{/cps}"
    
    queue sound "sfx/sliding-door-6758.mp3"
    queue sound "sfx/quick-mechanical-keyboard-14391.mp3"
    
    call screen screen_interactable
label running_machine:
        show flay_neutral at left
        "{cps=25} Cain’s running machine! {p} We spent a whole week working on modding this so it can track every detail of your run, they let me use it whenever I want!{/cps}"
        call screen screen_interactable
label plushies:
        show flay_smug at left
        "{cps=25}Cute…!{/cps}"
        call screen screen_interactable
label error_message:
        show flay_neutral at left
        "{cps=25}Hm, something is definitely wrong… I hope we can fix this soon…{/cps}"
        call screen screen_interactable

label cain_dia:
    CAIN "Flay, dude! what’s up!"
    FLAY "Hey Cain, any progress?"
    show cain_worried at cain_position
    CAIN "Nope, sorry man. {p}It’s so weird… I just can't find the error!?\nSomething is definitely fishy about this…"
    show flay_thinking at left
    FLAY "For sure… {p}What about Charli, have you heard anything?"
    show cain_neutral at cain_position
    CAIN "Nope again…"
    extend "{cps=25} Sorry bro… {p}I'm gonna try and focus on getting the systems back online. ASAP!{/cps}"
    show flay_neutral at left
    FLAY "Cool, let me know if you find any information or clues, ok?"
    show cain_head_empty at cain_position
    CAIN "…Clues?"
    FLAY "Yeah!"
    extend "{cps=25} I found a couple of notes and footprints outside. I'm starting to think someone, or something, got into the R-TRUS.{/cps}"
    show cain_excited at cain_position
    CAIN "…Well it’s your lucky day! {p}I found a clue!"
    show flayon_excited at left
    FLAY "…!"
    "{cps=25} Cain holds up a folded piece of paper that literally has the word “CLUE” written on it.{/cps}"
    CAIN "I found it on the floor when I came inside!{p}Woah! A real clue! This is awesome!!!"
    FLAY "Yeah!"
    show cain_neutral at cain_position
    CAIN "…"
    show flay_neutral at left
    FLAY "…"
    show cain_head_empty at cain_position
    CAIN "…"
    FLAY "Sooo… can I have it?"
    show cain_neutral at cain_position
    CAIN "Heh … not so fast buddy!"
    extend "{cps=25} This is the PERFECT opportunity!{/cps}"
    FLAY "Hm? For what?"
    ##play boss fight music
    jump cain_fight
label cain_fight:   
    show cain_flexing at cain_position
    CAIN "… FIGHT ME MACHINA X FLAYON!"
    show flay_stunned at left
    FLAY "You… Want to fight?…{p}Right now ?"
    CAIN "I KNOW I can beat you…{p}Are you scared perhaps…{p}Scared of losing to me!"
    show flay_neutral at left
    FLAY "Fine… you know what… "
    show flayon_excited at left
    extend "BRING IT ON!"
    show cain_excited at cain_position
    CAIN "HAHA! FINALLY!"
    extend "{cps=25} If you win, you can have the clue, ready?{/cps}"
    FLAY "I was born ready, Cain!"
    show cain_flexing at cain_position
    CAIN "COME AT ME!!!" 
    extend "{cps=25}{size=-10} Sorry flay i respect you as a leader and a pilot i just need to fight you it’s a personal urge i have i’m sorry this is all affectionate ok good luck man.{/size}{/cps}"
    "{cps=25} Pick the moves in the correct order to win!{/cps}"
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
       extend"The… {p} {cps=25}I forgot to name my finishing move…{/cps}"
       show cain_flexing at cain_position
       extend "\nTHE COOLEST FINISHING MOVE OF ALL TIME!"
       #unlock cg and show it
       $ persistent.unlock_3=True
       "cg unlocked"
       "Would you like to try again?"
       menu:
                "Yes":
                        jump cain_fight
                "Main menu":
                        return
    elif right_moves==4:
        show cain_out_of_breath at cain_position
        CAIN "Ok… {p} You win Maybe I need some more training…"
        show cain_excited at cain_position 
        extend "THAT WAS SO MUCH FUN!"
        show flay_neutral at left
        FLAY "You put up a good fight!"
        extend "{cps=25} We can train together anytime, okay?{/cps}"
        show cain_neutral at cain_position
        CAIN "Thank you bro…" 
        extend "You're so…" 
        extend "so cool…"
        show cain_excited at cain_position
        CAIN "Here! Hopefully it's helpful!"
        show cain_neutral at cain_position
        CAIN "Thanks for the fight!"
        extend "Good luck finding the other clues!"
        extend "I should get back to the computer now…" 
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
