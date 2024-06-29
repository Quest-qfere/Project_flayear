init python:
 # Creates the gallery object.
    g = Gallery()
    # Allows navigation in the gallery
   
    # Creates the buttons on the side of the screen to progress and go back


    # A button with an image that is always unlocked.
    g.button("title")
    g.image("title")

    # by making the same image in the "thumbnail" (reduced imaged) that is on screnns.py. I can create the illusion of an image expansion, and we can resize and move by using the images properties 
    g.button("Machi") 
    g.condition("persistent.unlock_1")
    g.image("images/Flayon_neutral_deadpan.jpg")
    g.image("images/Flayon_smirk.jpg")
    g.image("images/Flayon_unamused.png")
    g.image("images/Flayon_glare_annoyed.jpg")
    g.image("images/Neutral_Flayon.png")

  
    g.button("Navi")
    g.condition("persistent.unlock_2")
    g.image( "images/Navi_annoyed.png")
    g.image("images/Navi.png")

    g.button("himbo")
    g.image("images/himbo_title_card.png")

    g.button("maid")
    g.image("images/maid_title_card.png")

    g.button("example")
    g.image("images/example")
    g.button("example2")
    g.image("images/example")
    
   

    # The transition used when switching images.
    g.transition = dissolve
