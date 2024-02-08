# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# We can change the size and the codename in the future by changing the values in size
# if you wanna change the height of the name box just change the variable define gui.name_ypos = -100 in the gui file
init:
    image general_area="images/general_area.PNG"
    image navigation_room="images/navigation_room.png"
    image flay_neutral="images/Neutral_Flayon.png"
    image navi="images/navi.png"
    image navi_annoyed="images/Navi_annoyed.png"
    image flay_unamused="images/Flayon_unamused.png"
    image navi_smug="images/Navi_smug.png"
    image navi_confused="images/Navi_neutral_confused.png"
    image flayon_neutral_deadpan="images/Flayon_neutral_deadpan.jpg"
    image navi_annoyed_borred= "images/Navi_borred_annoyed.png"
    image flayon_annoyed_deadpan="images/Flayon_neutral_deadpan.jpg"
    image navi_thinking="images/Navi_thinking.png"
    image flayon_glare_annoyed="images/Flayon_glare_annoyed.jpg"
    image navi_smirk_eye_roll="images/Navi_smug.png"
    image navi_sigh_annoyed="images/Navi_sigh_annoyed.png"
    image navi_eyeroll="images/Navi_eyeroll.png"
    image flayon_smirk="images/Flayon_smirk.jpg"

define FLAY = Character("Flayon", who_suffix="\n{size=-15}Ace Pilot"  )

define NAVI  = Character("Navi", who_suffix="\n{size=-15}Code name"  )

define CAIN  = Character("Cain", who_suffix="\n{size=-15}Code name"  )

define DEAN = Character("Dean", who_suffix="\n{size=-15}Code name"  )

define KIT = Character("Kit", who_suffix="\n{size=-15}Code name"  )
# The game starts here.
transform big_size:
        zoom 2.0
label start:


    
    # These display lines of dialogue.
    "This is  a super scuffed demo of the scene without the minigame(I'll try to learn how to do that)"
    play sound "sfx/door-bang-1wav-14449.mp3"
    scene general_area at big_size
    show flay_neutral at left
    #" My name is Machina X Flayon, the pilot of guild Tempus." 
    #" As a guild of smart, brave adventurers, we get commissioned for quests often, but today was different; a quest came through for me specifically!
    # all of this  just showing a draf from a machiroon 
    FLAY " (For being the Machiroon in charge of movement and communication, the navigator would rather hole up in their room and limit interaction with the rest of us. If one didn’t know any better, they might call Navi a recluse.) "

    FLAY "(But unfortunately…)"

    play sound "sfx/jixaw-metal-pipe-falling-sound.mp3"
   
    # This ends the game.
    NAVI "Gott verdammt!"
    queue sound "sfx/door-bang-1wav-14449.mp3"
    queue sound "sfx/sliding-noise-v2-83483.mp3"
    show navi_annoyed at right
    NAVI "Machina! I should’ve known it was you! You always pick the worst time to visit me!"
    hide navi_annoyed
    show navi at right
    NAVI "Well… I suppose I can’t fault you for wanting an audience with me. It’s not your fault I’m so captivating."
    hide flay_neutral
    show flay_unamused at left
    FLAY "(We all know better by now. Navi’s ego is bigger than the R-TRUS itself.)"
    hide navi
    show navi_smug at right
    NAVI "Very well. It’d be my pleasure to keep you company for a while. I assume you’re…"
    hide navi_smug
    show navi_confused at right
    NAVI "Now that I think about it, what exactly are you doing?"
    with Dissolve(.5)
    scene navigation_room at big_size
    hide flay_unamused
    show flay_neutral at left
    FLAY"I’d explain it to you, but I’m pretty sure you don’t care."
    hide navi_confused
    show navi_annoyed at right
    "Rude! I’ll have you know that I care plenty about— "
    hide flay_neutral
    show flayon_neutral_deadpan at left
    FLAY "It’s not about you."
    hide navi_annoyed
    show navi_annoyed_borred at right
    NAVI "Ah, then I’ve already lost all interest. You should’ve led with that first, Machina. Less of our time wasted."
    hide flayon_neutral_deadpan
    show flayon_annoyed_deadpan at left
    FLAY "Yeah. I’m starting to think the same thing."
    hide navi_annoyed
    show navi at right
    NAVI "What I’m more curious about is what you’re doing here. You’re not the type to intrude, and I’m not the type to invite."
    hide flayon_annoyed_deadpan
    show flay_neutral at left
    FLAY "I was actually hoping you could make an exception today. With our little power outage emergency and all."
    hide navi
    show navi_thinking at right
    NAVI "When you put it like that…"
    show flayon_glare_annoyed at left
    FLAY "If you say no just to spite me, I will bite you."
    
    show navi_smirk_eye_roll at right
    NAVI "\"All work and no play…\""
    hide flayon_glare_annoyed
    show flay_neutral at left
    FLAY "…"
    hide navi_smirk_eye_roll
    show navi_sigh_annoyed at right
    NAVI "Will you not even humor me, Machina?"
    hide flayon_neutral_deadpan
    show flayon_neutral_deadpan at left
    FLAY "\“...makes Jack a dull boy.” Can I ask you what I want now?"
    hide navi_sigh_annoyed
    show navi_eyeroll at right
    NAVI "Tut, tut, tut! What did I just say? You’re all work and no play!"
    NAVI "So… play a game with me first! If you can beat me, I will assist you in whatever you need out of the endless kindness of my heart."
    hide flayon_neutral_deadpan
    show flayon_smirk at left
    FLAY "Is that a challenge?"
    hide navi_eyeroll
    show navi_smirk_eye_roll at right
    NAVI "Looks like you’re not as half-witted as you seem. Win and you can go back to running around like a headless hakkito in no time!"
    FLAY "You’re on."

    "INSERT MINIGAME"
    "unlock cgs"
    $ persistent.unlock_2=True
    $ persistent.unlock_1=True
    "..."
    return
