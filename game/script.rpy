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
    image bg kit_room="images/insidedoorclosed_wip.png"
    image flay_neutral="images/Neutral_Flayon.png"
    image flay_schocked="images/Neutral_Flayon.png"
    image flay_scared="images/Neutral_Flayon.png"
    image flay_unamused="images/Flayon_unamused.png"
    image flayon_neutral_deadpan="images/Flayon_neutral_deadpan.jpg"
    image flay_thinking="images/Neutral_Flayon.png"
    image flayon_annoyed_deadpan="images/Flayon_neutral_deadpan.jpg"
    image flayon_glare_annoyed="images/Flayon_glare_annoyed.jpg"
    image flayon_smirk="images/Flayon_smirk.jpg"
    image flayon_excited="images/Neutral_Flayon.png"
    image flayon_confused="images/Neutral_Flayon.png"
    image flay_stunned="images/Neutral_Flayon.png"
    image kit_with_grenade="images/placeholder_kit.png"
    image kit_neutral="images/placeholder_kit.png"
    image kit_thinking="images/placeholder_kit.png"
    image kit_laugh="images/placeholder_kit.png"
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
transform dark_transformation:
        matrixcolor BrightnessMatrix(-0.5)
label start:
    # These display lines of diaslogue.
    show flay_neutral at dark_transformation,right
    FLAY "KIT, what is going on?{p}I can’t see anything here.{p}Was the power not rested here?{p}Hold on, where’s that light switch…"
    show kit_with_grenade at left,dark_transformation
    KIT "Welcome welcome everyroon! It's now time to finally get this party started!"
    extend "  Entering the stage for the first time ever, put your parts and paws together for our special guest of the night, the main contestant of our show!"
    KIT "The one that pilots our home and lands in our hearts. The universally loved:Machina X Flayon"
    queue sound "sfx/applause-75314.mp3"
    scene bg kit_room at 
    show flay_schocked at right
    show kit_neutral at left
    FLAY "KIT… Who are you talking to?{p}Where did that sound come from if we’re the only two people in this room?"
    KIT "Eheh, we’re not the only ones here, silly!{p}The other Machiroons are just on the other side and they’re playing along with us right now.{p}It's all just part of the game after all!"
    #queue sound ""
    KIT "Now then, let’s begin the final event of the night.{p}Welcome everyroon to The Most Epic Trivia Quiz of Ultimate Mystery!{p}Or for short TMETQUM!"
    show kit_thinking at left
    KIT "… Name still pending review for more awesomeness."
    show kit_with_grenade at left
    KIT "Anywwaaayyyy…~!{p}This challenge is intended to be your final step in this long journey of helping us Machiroons.{p}Can you face the task head-on and give it your all?"
    KIT  "Will you use every ounce of your mind to unravel the mysteries this journey has brought you to!?{p}Oh wow, I'm so excited!{p}Here, Flayon catch!"
    show flay_scared at right
    FLAY "Huh… HUH-!?{p}W-Why did you toss me a grenade?!{p}I don’t want it!"
    KIT "D’aww, don’t be scared. It's not gonna blow up on you as long as you just don’t drop it! Or pull that silver pin at the top."
    extend   "Oh man, then things will really go off the charts with a sudden BOOM!!" 
    KIT "Just use it when picking your answer, it will be useful! Now, let the games begin!"
    #queue sound"""
    KIT "Alrighty~! The objective of the game is super duper easy, like so simple." 
    extend "{p}Use your brain to guess correctly and win!"
    KIT "There are seven questions in total, and once you finish, you’ll get the final item in our quest and win!" 
    extend "{p}Sounds painless, doesn’t it?"
    FLAY "It does sound simple enough… {p}But what's the catch?{p}No tricks this time?"
    KIT "Ehe, well… not reaaallly! You’ll see why it's called The Most Epic Trivia-!{p}Ah, well you get the point.{p}Onto the game!!"
label gameshow:
     wrong_ans=0
     "Question 1: What did Flayon cook up for Valentine’s Day in 2023?"
     menu:
          "Special Stream":
                 KIT "Ooh, that wasn’t quite what we were looking for but that’s ok!"
                 wrong_ans=wrong_ans+1
          "Cover":
                 KIT "Talk about beginner’s luck!{p}You got it on the first try~"
          "Machiroons":
                 KIT "Ooh, that wasn’t quite what we were looking for but that’s ok!"
                 wrong_ans=wrong_ans+1
          "Voice Tweet":
                 KIT "Ooh, that wasn’t quite what we were looking for but that’s ok!"
                 wrong_ans=wrong_ans+1
     "Question 2: What was the first game that Flayon and Gavis Bettel collaborated on?"
     menu:
          "Cuphead":
                 KIT "Wrong, sorry~"
                 wrong_ans=wrong_ans+1
          "Resident Evil 6":
                 KIT "Wrong, sorry~"
                 wrong_ans=wrong_ans+1
          "World of Warcraft":
                 KIT "Wrong, sorry~"
                 wrong_ans=wrong_ans+1
          "Ultimate Horse Chicken":
                 KIT "Hey, you got it! Hey, You're not bad!"
     "Question 3: Who out of these Lobotomy Corporation NPCs did Flayon receive first?"
     menu:
          "Poussey":
                 KIT "Ding ding! You got that one really quick. Think your luck will run out?"
          "Joshua":
                 KIT "Nope, you weren’t even close on that! That’s a little embarrassing…"
                 wrong_ans=wrong_ans+1
          "Zayn":
                 KIT "Nope, you weren’t even close on that! That’s a little embarrassing…"
                 wrong_ans=wrong_ans+1
          "Kukuru":
                 KIT "Nope, you weren’t even close on that! That’s a little embarrassing…"
                 wrong_ans=wrong_ans+1
     "Question 4: What is Flayon’s official title in the guild Tempus?"
     menu:
          "Customer service":
                 KIT "Ouch! I thought you would have gotten that easy peasy…"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
          "Customer care":
                 KIT "Ouch! I thought you would have gotten that easy peasy…"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
          "Customer value":
                 KIT "Ouch! I thought you would have gotten that easy peasy…"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
          "Customer support":
                 KIT "Aw man, you got it right. I wonder if I should make these harder!"
     "Question 5: Outside of Vanguard, which HQ member did Flayon have his first collab stream with?"
     menu:
          "Altare":
                 KIT "Hey, you got another one! Are you sure you’re not cheating~"
          "Vesper":
                 KIT "Oh dear… and that was one of our easy questions too…"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
          "Axel":
                 KIT "Oh dear… and that was one of our easy questions too…"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
          "Magni":
                 KIT "Oh dear… and that was one of our easy questions too…"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
     "Question 6: Which of these races did Flayon pick for his character selection in Elder Scrolls IV: Oblivion?"
     menu:
          "Khajiit":
                 KIT "Another successful answer was found!{p}Man, you’re really good at this!"
          "Redguard":
                 KIT "Guess that one was just a bit too hard for you.{p}Let’s give you an easier one~"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
          "Imperial":
                 KIT "Guess that one was just a bit too hard for you.{p}Let’s give you an easier one~"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
          "Orsimer":
                 KIT "Guess that one was just a bit too hard for you.{p}Let’s give you an easier one~"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
     "Question 7: How many members are there in the Tempus Guild, including inactive members?"
     menu:
          "Four":
                 KIT KIT "Ohh, and a fumble on the last question!{p}That isn’t good…~"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
          "Eight":
                 KIT "Holy moly, you got it!"
          "Ten":
                 KIT "Ohh, and a fumble on the last question!{p}That isn’t good…~"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
          "Twelve":
                 KIT "Ohh, and a fumble on the last question!{p}That isn’t good…~"
                 wrong_ans=wrong_ans+1
                 if(wrong_ans>=4):
                     jump bad_end
     FLAY "Alright! That was all of them right, so what’s my prize?"
     KIT "Looks like you got yourself a pretty epic memory there.{p}But is it as good as you think it is?{p}We aren’t finished just yet!"
     FLAY "You… mean there’s more?"
     KIT "Not to worry at all Flayon!{p}You have a pretty awesome memory but were you able to guess what the meaning behind all these answers was?"
     FLAY "I thought you said that there weren’t going to be any trick questions during this quiz!"
     show kit_laugh at left
     KIT "Well, it was a half yes half no kinda answer.{p}We gotta keep you on your toes after all~...{p}Now, the final question is going to make it or break it.{p} Will you overcome or will you fall into despair?!"
     KIT "Oh the horror, oh the humanity!{p}For the final and last question of our ultimate quiz it is-!!"
     final_answer=renpy.input("FINAL: What do all of these answers spell out?", length=32)
     if final_answer.toLowerCase()=="cupcake":
      KIT "Yes, yes, YES!! That is it!{p}You are the winner of TMETQUM!{p}And here is the GRAND FINAL PRIZE for our dearest winner!"
      KIT "Not that we had any other prizes tonight, ehe~"
      KIT "Bring it out!{p}Our delicious, delectable dessert of the night is…!"
      KIT "TA-DA!"
      FLAY "Looks like a normal cupcake to me… is there anything especially grand about this prize?"
      KIT "I poured my heart and soul into making this cupcake, I’ll have you know! HMPH!"
      FLAY "Alright, alright!{p}I admit, it does look pretty tasty…"
      "Flayon brings the cupcake up to his mouth, but Kit promptly grabs his wrist."
      KIT "HEY!{p}That there is your final clue and a masterpiece of fine art, it is not for eating!"
      KIT "Now now, it’s about time you’ve gone out and solved the mystery of the missing Roon once and for all.{p}Finally, all of the pieces will fit into place!"
      KIT "That’s right!{p}Now, shoo, shoo!{p}Off you go!"
      "Kit waves Flayon off and shuts the door with a mischievous giggle."
      FLAY "Their mood doesn’t seem to fit the current situation.{p}I wonder where this final clue will lead me?"
     else:
        jump bad_end
label bad_end:
     KIT "Oh dear oh no!!{p}Looks like you got that one completely wrong.{p}I guess that just means you’ll be stuck here permanently relearning every single thing that you should have known from the very beginning." 
     KIT "How unlucky for you but super duper fun for me! Kyahaha~!!"

      
 

