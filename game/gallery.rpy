init python:
 # Creates the gallery object.
    g = Gallery()
    # Allows navigation in the gallery
    g.navigation=True 
    # Creates the buttons on the side of the screen to progress and go back
    g.span_buttons=True

    # A button with an image that is always unlocked.
    g.button("title")
    g.image("title")

    # by making the same image in the "thumbnail" (reduced imaged) that is on screnns.py. I can create the illusion of an image expansion, and we can resize and move by using the images properties 
    g.button("Machineigh") 
    g.image("Machineigh1","images/7AA453CD-35EE-46E4-872C-8C71F3EEE617.png")
  
    g.button("miach")
    g.image("Miach1", "images/8D95AB33-5623-4129-9D70-D7E040F0588E.png")

    
   

    # The transition used when switching images.
    g.transition = dissolve
