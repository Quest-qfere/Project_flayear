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

define CHARLI = Character("Charli", who_suffix="\n{size=-15}Code name"  )

image note = "images/prologue_note_temp.png"

# The game starts here.

label start:
    # These display lines of dialogue.
    pause 2.0
    FLAY "Charli!?"
    CHARLI "Hi Flay! Surprise~"
    FLAY "You're okay!"
    CHARLI "Of course I am, silly! Sorry for tricking you, hehe~ How else would we get you to your surprise party?"
    FLAY "Surprise... party...?"
    CAIN "YEAH! Happy birthday, man! Did you really think we forgot?"
    FLAY "Honestly, I was so distracted I kind of forgot myself."
    KIT "Well that's nooooo good! We are gonna make sure you have the BEST party ever!"
    DEAN "I did try to advise against the whole \"fake kidnapping\" scenario, by the way."
    CHARLI "You have to admit, I'm a very good actor, right?"
    DEAN "...Yes. You did well."
    FLAY "So the whole thing was fake?"
    KIT "It was! Come on, when would I ever ask to stop for snacks in the middle of a mission?"
    CAIN "Tiny, that is totally something you would do."
    FLAY "You organized all of this, just to surprise me?"
    DEAN "Correct. We thought you deserved something grand."
    DEAN "...a gas station basement isn't exactly what I had in mind."
    CHARLI "We made it work! I think it's purr-fect!"
    FLAY "It's very... well... roon-coded!"
    NAVI "Ahem! Quick! Before the candles go out!"
    hide window
    pause 3.0
    window show
    NAVI "Happy birthday, Machina!"
    NAVI "Hopefully you like the cake; I spent a {i}while{/i} decorating it."
    NAVI "...I mean. It didn't take that long. It actually took no time at all! Ha!"
    NAVI "..."
    NAVI "But I do hope you like it. And I hope you have an... {i}adequate{/i} birthday!"
    FLAY "Thank you, Navi! The cake looks great!"
    CAIN "Happy birthday, boss!"
    CAIN "Sorry about the fighting earlier. I still want a rematch, though!"
    CAIN "Enjoy the party, dude! You so totally deserve it! You're like, the best leader ever!"
    CAIN "HIGH FIVE!!!"
    hide window
    pause 0.5
    window show
    DEAN "Machina, happy birthday!"
    DEAN "Like I mentioned, I was against this whole \"Birthday Scavenger Hunt\" situation."
    DEAN "But I have to say, it was pretty fun. I hope you had fun too."
    DEAN "And I promise I will get Cain and Charli to fix the damages on the R-TRUS before we leave. They aren't that bad... {size=-10}I hope.{/size}"
    FLAY "Thanks, Dean! Wait, you guys actually damaged it? But---{nw}"
    KIT "FLAY!"
    KIT "Do you like the decorations?! I put them all up myself!"
    KIT "I wanted to do indoor fireworks, but Navi told me no."
    KIT "I HOPE YOU HAVE THE BEST BIRTHDAY EVEEEEEEEEEER!"
    KIT "We love you! Don't forget it!"
    KIT "Let's party! YAYYYYY!"
    CHARLI "Hiya, Machinya! Sorry for today!"
    CHARLI "This whole thing was my idea and I may have gotten slightly carried away! Hehe..."
    CHARLI "But, I just wanted to make sure you had the best party ever! You do so much for us, and we are all so thankful, meow!"
    CHARLI "Thank you, Machi! I hope you have the best birthday!"
    FLAY "Charli... everyone... thank you!"
    hide window
    pause 2.0
    window show
    "Happy birthday, Flayon!"
    NAVI "We hope you had fun!"
    NAVI "Sending you around on a wild goose chase was honestly pretty funny!"
    CAIN "Next year, how about we do an arm wrestling bracket?"
    CAIN "No? I'll keep training anyway."
    DEAN "It was definitely an {i}interesting{/i} way to show our appreciation..."
    DEAN "But hopefully, we got the message across."
    KIT "Happy birthday, Flayon! Thank you for everything!"
    CHARLI "We love you! Meow and forever~ We couldn't think of anyone better to be our leader!"
    CHARLI "Now, time to party!"
    hide window
    pause 5.0
    window show
    "THE END."

    return
