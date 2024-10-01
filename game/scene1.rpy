image intro = "images/title.png"

label splashscreen: 
    scene black 
    pause 1.0
    show intro at truecenter, title_size  with fade 
    pause 1.0
    hide intro at truecenter, title_size  with fade 
    return

label start:
play music "sadtheme.mp3" loop 
centered """
A life-changing invitation… \n
Sounds too good to be true, right
    """

jump scene2  
