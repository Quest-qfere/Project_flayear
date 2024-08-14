# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# We can change the size and the codename in the future by changing the values in size
# if you wanna change the height of the name box just change the variable define gui.name_ypos = -100 in the gui file
init:
    image bg general_area="images/general_area.PNG"
    image bg navigation_room="images/navigation_room.png"
    image flay_neutral:
        "images/Sprites_Flay.png"
        fit "cover"
        xsize 700
    image flay_smug:
        "images/Sprites_Flaypng"
        fit "cover"
        xsize 700
    image flay_unamused:
        "images/Sprites_Flay.png"
        fit "cover"
        xsize 700
    image flayon_neutral_deadpan:
        "images/Sprites_Flay.png"
        fit "cover"
        xsize 700
    image flay_thinking:
        "images/Sprites_Flay.png"
        fit "cover"
        xsize 700
    image flayon_annoyed_deadpan:
        "images/Sprites_Flay.png"
        fit "cover"
        xsize 700
    image flayon_glare_annoyed:
        "images/Sprites_Flay.png"
        fit "cover"
        xsize 700
    image flayon_smirk:
        "images/Sprites_Flay.png"
        fit "cover"
        xsize 700
    image flayon_excited:
        "images/Sprites_Flay.png"
        fit "cover"
        xsize 700
    image flayon_confused:
        "images/Sprites_Flay.png"
        fit "cover"
        xsize 700
    image flay_stunned:
        "images/Sprites_Flay.png"
        fit "cover"
        xsize 700
    image navi:
        "images/Sprites_Navi.png"
        fit "cover"
        xsize 700
    image navi_annoyed:
        "images/Sprites_Navi.png"
        fit "cover"
        xsize 700
    image navi_smug:
        "images/Sprites_Navi.png"
        fit "cover"
        xsize 700
    image navi_confused:
        "images/Sprites_Navi.png"
        fit "cover"
        xsize 700
    image navi_annoyed_borred:
        "images/Sprites_Navi.png"
        fit "cover"
        xsize 700
    image navi_thinking:
        "images/Sprites_Navi.png"
        fit "cover"
        xsize 700
    image navi_smirk_eye_roll:
        "images/Sprites_Navi.png"
        fit "cover"
        xsize 700
    image navi_sigh_annoyed:
        "images/Sprites_Navi.png"
        fit "cover"
        xsize 700
    image navi_eyeroll:
        "images/Sprites_Navi.png"
        fit "cover"
        xsize 700        
    image error_screen:
        "images/error_screen.png"
        
    image bg general_area="images/general_area.png"
    image bg navigation_room="images/navigation_room.png"


define FLAY = Character("Flayon", who_suffix="\n{size=-15}Ace Pilot",what_slow_cps=25  )

define NAVI  = Character("Navi", who_suffix="\n{size=-15}Code name",what_slow_cps=25  )

define CAIN  = Character("Cain", who_suffix="\n{size=-15}Code name"  )

define DEAN = Character("Dean", who_suffix="\n{size=-15}Code name"  )

define KIT = Character("Kit", who_suffix="\n{size=-15}Code name"  )
#dark light tint matrixcolor TintMatrix("7A7A7B")
# dark tint  matrixcolor TintMatrix("4C4CAA")
# The game starts here.
transform  big_size:
        zoom 2.0
label start:
    # These display lines of diaslogue.
    "This is  a super scuffed demo of the scene without the minigame(I'll try to learn how to do that)"
    play sound "sfx/door-bang-1wav-14449.mp3"
 
    scene bg general_area 
    show flay_neutral at left:
                matrixcolor TintMatrix("4C4CAA")
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
    show flay_unamused at left:
        matrixcolor TintMatrix("7A7A7B")
    FLAY "(We all know better by now. Navi’s ego is bigger than the R-TRUS itself.)"
    hide navi
    show navi_smug at right
    NAVI "Very well. It’d be my pleasure to keep you company for a while. I assume you’re…"
    hide navi_smug
    show navi_confused at right
    NAVI "Now that I think about it, what exactly are you doing?"
    with Dissolve(.5)
    scene bg navigation_room at big_size
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

    
    # This ends the game.
    jump card_game
    $ persistent.unlock_2=True
    $ persistent.unlock_1=True
    "..."
    return
label bad_end:
        NAVI"..."
        FLAY"..."
        NAVI "Machina..."
        FLAY "Navi..."
        FLAY "(We have been playing this game for 2 hours with no end in sight. For some strange reason, neither of us have managed to match a single pair of cards.)"
        FLAY "(At this point, I have to wonder…)"
        FLAY "(Is this game cursed, or are we?)"
        "Some say the game between Machina and Navi is still going on to this day, stuck in perpetual limbo, neither side winning or losing"
        "What happened to R-TRUS and Charli?{p}Where are the other Machiroons?{p}Does the power ever come back?{p}Questions we may never find the answers to."
label good_end:
    show Navi_annoyed at right
    show flayon_confused at left
    scene bg navigation_room at big_size
    queue sound "sfx/door-bang-1wav-14449.mp3"
    NAVI "Ugh! You cheated!"
    FLAY "Wh— How even? This is your game"
    NAVI "Then it’s a stupid game!{p}A complete waste of my time!"
    FLAY "(Aaaand there’s the sore loser meltdown.)"
    "Navi stomps across the room as Flayon looks on curiously. They're holding something when they return and shove it towards him"
    NAVI "There! This is what you wanted, right? Now get out!"
    show flayon_surprised at left
    FLAY "Huh? That’s it?"
    "Navi lets out a frustrated sound and starts shoving Flayon out the door."
    NAVI "Get OUT!!!"
    scene bg general_area 
    queue sound "sfx/sliding-noise-v2-83483.mp3"
    NAVI "And DON'T come back!!!"
    show flayon_neutral_deadpan at left
    FLAY "..."
    show flayon_smirk at left
    FLAY "IT WAS NICE HANGING OUT WITH YOU TOO!"
    queue sound "sfx/door-bang-1wav-14449.mp3"
    "There’s a loud thump of something hitting the door on the opposite side"
    "Flayon looks down at the item in his hand.{p}It’s a transparent plastic cup with the straw still inside.{p}There’s some pink liquid at the bottom."
    show flay_neutral at left
    FLAY "Oh, this must be—"
    "Flayon opens the lid.{p}The faintest hint of strawberries wafts into the air."
    FLAY "Strawberry milkshake!{p}Damn, they finished it all."
    FLAY "At least that’s one clue down."
