# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# We can change the size and the codename in the future by changing the values in size
# if you wanna change the height of the name box just change the variable define gui.name_ypos = -100 in the gui file

default preferences.text_cps = 40

define FLAY = Character("Flayon", who_suffix="\n{size=-15}Ace Pilot"  )

define NAVI  = Character("Navi", who_suffix="\n{size=-15}Code name"  )

define CAIN  = Character("Cain", who_suffix="\n{size=-15}Code name"  )

define DEAN = Character("Dean", who_suffix="\n{size=-15}Code name"  )

define KIT = Character("Kit", who_suffix="\n{size=-15}Code name"  )

# The game starts here.

label start:
    # These display lines of dialogue.
    "My name is Machina X Flayon, the pilot of guild TEMPUS!" 
    "As a guild of brave, smart adventurers, we get commissioned for quests quite often."
    "But, today was {i}different...{/i} a quest came through, addressed to me specifically!"
    "I wouldn't usually find this strange, but the note attached was... interesting."
    FLAY "So, I recruited five of the strongest people in my team, also known as the Machiroons!"
    FLAY "And we traveled in none other than my giant mech, the R-TRUS! He's pretty cool!"
    FLAY "We all got ready and set off towards the coordinates..."
    # This ends the game.

    return
