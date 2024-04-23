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


  
    g.button("Navi")
    g.condition("persistent.unlock_2")
    g.image( "images/example")
   
    g.button("CAIN")
    g.condition("persistent.unlock_3")
    g.image("images/himbo_title_card.png")

    g.button("maid")
    g.image("images/maid_title_card.png")

    g.button("example")
    g.image("images/example")
    g.button("example2")
    g.image("images/example")
    
   

    # The transition used when switching images.
    g.transition = dissolve
