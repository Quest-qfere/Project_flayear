# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
# We can change the size and the codename in the future by changing the values in size
# if you wanna change the height of the name box just change the variable define gui.name_ypos = -100 in the gui file

default preferences.text_cps = 40

init:
    #backgrounds    
    image bg party_room=im.Scale('images/bg/bg_partyroom.png', 1920, 1200)
    image bg navi_cake=im.Scale('images/navi/navi_cakeneutral.png', 1920, 1200)
    #flayon
    image flayon_neutral=im.Scale('images/flayon/flayon_neutral.png', 300, 400)
    image flayon_confused=im.Scale('images/flayon/flayon_confused.png', 300, 400)
    image flayon_excited=im.Scale('images/flayon/flayon_excited.png', 300, 400)
    image flayon_surprised=im.Scale('images/flayon/flayon_surprised.png', 300, 400)
    #cain
    image cain_neutral=im.Scale('images/cain/cain_neutral.png', 300, 400)
    image cain_excited=im.Scale('images/cain/cain_excited.png', 300, 400)
    image cain_flex=im.Scale('images/cain/cain_flex.png', 300, 400)
    #charli
    image charli_neutral=im.Scale('images/charli/charli_neutral.png', 300, 400)
    image charli_excited=im.Scale('images/charli/charli_excited.png', 300, 400)
    #dean
    image dean_neutral=im.Scale('images/dean/dean_neutral.png', 300, 400)
    image dean_smug=im.Scale('images/dean/dean_smug.png', 300, 400)
    image dean_concern=im.Scale('images/dean/dean_concern.png', 300, 400)
    #kit
    image kit_neutral=im.Scale('images/kit/kit_neutral.png', 300, 400)
    image kit_excited=im.Scale('images/kit/kit_excited.png', 300, 400)
    image kit_starryeyed=im.Scale('images/kit/kit_starryeyed.png', 300, 400)
    #navi
    image navi_neutral=im.Scale('images/navi/navi_neutral.png', 300, 400)
    image navi_cake_neutral=im.Scale('images/navi/navi_cakeneutral.png', 300, 400)
    image navi_cake_annoyed=im.Scale('images/navi/navi_cakeannoyed.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)
    #image image=im.Scale('images/char/mode.png', 300, 400)

define FLAY = Character("Flayon", who_suffix="\n{size=-15}Ace Pilot"  )

define NAVI  = Character("Navi", who_suffix="\n{size=-15}Code name"  )

define CAIN  = Character("Cain", who_suffix="\n{size=-15}Code name"  )

define DEAN = Character("Dean", who_suffix="\n{size=-15}Code name"  )

define KIT = Character("Kit", who_suffix="\n{size=-15}Code name"  )

define CHARLI = Character("Charli", who_suffix="\n{size=-15}Code name"  )

image note = "images/prologue_note_temp.png"

transform charfarleft:
    xalign 0.10
    yalign 0.6

transform charfarright:
    xalign 0.95
    yalign 0.6

transform charright:
    xalign 0.80
    yalign 0.6

transform charmidright:
    xalign 0.65
    yalign 0.6

transform charmid:
    xalign 0.50
    yalign 0.6

transform charmidleft:
    xalign 0.35
    yalign 0.6

transform charleft:
    xalign 0.20
    yalign 0.6

define fastdissolve = Dissolve(0.2)

screen birthday_button:
    modal True
    button:
        xalign 0.5
        yalign 0.5
        xysize (300, 100)
        text "Make a wish!"
        action Return()
        background "gui/button/choice_idle_background.png"
        hover_background "gui/button/choice_hover_background.png"

# The game starts here.

label start:
    # These display lines of dialogue.
    show bg party_room with fade
    pause 0.5
    show flayon_surprised at charfarleft
    show charli_excited at charfarright
    with fastdissolve
    FLAY "Charli!?"
    CHARLI "Hi Flay! Surprise~"
    hide flayon_surprised
    show flayon_excited at charfarleft
    FLAY "You're okay!"
    CHARLI "Of course I am, silly! Sorry for tricking you, hehe~ How else would we get you to your surprise party?"
    hide flayon_excited
    show flayon_confused at charfarleft
    
    with fastdissolve
    FLAY "Surprise... party...?"
    show cain_excited at charright with fastdissolve
    CAIN "YEAH! Happy birthday, man! Did you really think we forgot?"
    hide flayon_confused
    show flayon_neutral at charfarleft
    with fastdissolve
    FLAY "Honestly, I was so distracted I kind of forgot myself."
    #hide cain_excited with fastdissolve
    show kit_excited at charmidright with fastdissolve
    KIT "Well that's nooooo good! We are gonna make sure you have the BEST party ever!"
    #hide kit_excited with fastdissolve
    show dean_neutral at charmid with fastdissolve 
    DEAN "I did try to advise against the whole \"fake kidnapping\" scenario, by the way."
    CHARLI "You have to admit, I'm a very good actor, right?"
    hide dean_neutral
    show dean_smug at charmid
    with fastdissolve
    DEAN "...Yes. You did well."
    FLAY "So the whole thing was fake?"
    hide kit_excited
    show kit_neutral at charmidright
    with fastdissolve
    KIT "It was! Come on, when would I ever ask to stop for snacks in the middle of a mission?"
    hide cain_excited
    show cain_neutral at charright
    with fastdissolve
    CAIN "Tiny, that is totally something you would do."
    FLAY "You organized all of this, just to surprise me?"
    hide dean_smug
    show dean_neutral at charmid
    with fastdissolve
    DEAN "Correct. We thought you deserved something grand."
    DEAN "...a gas station basement isn't exactly what I had in mind."
    hide charli_excited
    show charli_neutral at charfarright
    with fastdissolve
    CHARLI "We made it work! I think it's purr-fect!"
    FLAY "It's very... well... roon-coded!"
    NAVI "Ahem! Quick! Before the candles go out!"
    hide flayon_neutral
    hide charli_neutral
    hide dean_neutral
    hide cain_neutral
    hide kit_neutral
    with dissolve
    scene bg navi_cake with fade
    call screen birthday_button
    scene bg party_room with fade
    show flayon_neutral at charfarleft
    show navi_cake_neutral at charmidright
    with fastdissolve
    NAVI "Happy birthday, Machina!"
    NAVI "Hopefully you like the cake; I spent a {i}while{/i} decorating it."
    hide navi_cake_neutral 
    show navi_cake_annoyed at charmidright
    with fastdissolve
    NAVI "...I mean. It didn't take that long. It actually took no time at all! Ha!"
    NAVI "..."
    hide navi_cake_annoyed
    show navi_cake_neutral at charmidright
    with fastdissolve
    NAVI "But I do hope you like it. And I hope you have an... {i}adequate{/i} birthday!"
    FLAY "Thank you, Navi! The cake looks great!"
    hide navi_cake_neutral with fastdissolve
    pause 0.1
    show cain_neutral at charmidright with fastdissolve
    CAIN "Happy birthday, boss!"
    CAIN "Sorry about the fighting earlier. I still want a rematch, though!"
    hide cain_neutral
    show cain_excited at charmidright
    with fastdissolve
    CAIN "Enjoy the party, dude! You so totally deserve it! You're like, the best leader ever!"
    CAIN "HIGH FIVE!!!"
    hide window
    pause 0.3
    hide cain_excited with fastdissolve
    pause 0.1
    show dean_neutral at charmidright with fastdissolve
    window show
    DEAN "Machina, happy birthday!"
    DEAN "Like I mentioned, I was against this whole \"Birthday Scavenger Hunt\" situation."
    hide dean_neutral
    show dean_smug at charmidright
    with fastdissolve
    DEAN "But I have to say, it was pretty fun. I hope you had fun too."
    hide dean_smug
    show dean_concern at charmidright
    with fastdissolve
    DEAN "And I promise I will get Cain and Charli to fix the damages on the R-TRUS before we leave. They aren't that bad... {size=-10}I hope.{/size}"
    hide flayon_neutral
    show flayon_confused at charfarleft
    with fastdissolve
    FLAY "Thanks, Dean! Wait, you guys actually damaged it? But---{nw}"
    hide dean_concern
    show kit_excited at charmidright
    with fastdissolve
    KIT "FLAY!"
    KIT "Do you like the decorations?! I put them all up myself!"
    hide kit_excited
    show kit_neutral at charmidright
    with fastdissolve
    KIT "I wanted to do indoor fireworks, but Navi told me no."
    hide kit_neutral
    show kit_starryeyed at charmidright
    with fastdissolve
    KIT "I HOPE YOU HAVE THE BEST BIRTHDAY EVEEEEEEEEEER!"
    KIT "We love you! Don't forget it!"
    hide kit_starryeyed
    show kit_excited at charmidright
    with fastdissolve
    KIT "Let's party! YAYYYYY!"
    hide kit_excited with fastdissolve
    pause 0.1
    show charli_neutral at charmidright 
    show flayon_neutral at charfarleft
    with fastdissolve
    CHARLI "Hiya, Machinya! Sorry for today!"
    CHARLI "This whole thing was my idea and I may have gotten slightly carried away! Hehe..."
    hide charli_neutral
    show charli_excited at charmidright
    with fastdissolve
    CHARLI "But, I just wanted to make sure you had the best party ever! You do so much for us, and we are all so thankful, meow!"
    hide charli_excited
    show charli_neutral at charmidright
    with fastdissolve
    CHARLI "Thank you, Machi! I hope you have the best birthday!"
    FLAY "Charli... everyone... thank you!"
    show navi_neutral at charmidleft
    show cain_neutral at charmid
    show dean_neutral at charright
    show kit_neutral at charfarright
    with fastdissolve
    "Happy birthday, Flayon!"
    NAVI "We hope you had fun!"
    NAVI "Sending you around on a wild goose chase was honestly pretty funny!"
    hide cain_neutral
    show cain_flex at charmid
    with fastdissolve
    CAIN "Next year, how about we do an arm wrestling bracket?"
    CAIN "No? I'll keep training anyway."
    DEAN "It was definitely an {i}interesting{/i} way to show our appreciation..."
    DEAN "But hopefully, we got the message across."
    KIT "Happy birthday, Flayon! Thank you for everything!"
    CHARLI "We love you! Meow and forever~ We couldn't think of anyone better to be our leader!"
    hide charli_neutral
    show charli_excited at charmidright
    with fastdissolve
    CHARLI "Now, time to party!"
    scene black with fade
    hide window
    pause 5.0
    window show
    "THE END."
    return
