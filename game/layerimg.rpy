init python:
    def layered_image_topdown(base, top):
        base_width, base_height = renpy.image_size(base)
        top_width, top_height = renpy.image_size(top)
        
        # Crop the top image to match the base image's height
        cropped_top = Crop((0, 0, top_width, min(top_height, base_height)), top)
        
        # Create a composite image
        return Composite(
            (base_width, base_height),
            (0, 0), base,
            (0, 0), cropped_top
        )