label scene3:
     
menu:
      "It's addressed to"
      "Mx.":
            $ pronoun = "they/them"
            $ Honorific = "Mx."
      "Ms.":
            $ pronoun = "she/her"
            $ Honorific = "Ms."
      "Mr.":
            $ pronoun = "he/him"
            $ Honorific = "Mr."

python:     
      mcname = renpy.input("It has my first name?", length=32)
      mcname = mcname.strip()
      mclast = renpy.input("and last name?", length=32)
      mclast = mclast.strip()
      
      if not mcname:
            mcname = "Lil"
      if not mclast:
            mclast = "Guwapo"

mc "[Honorific] [mcname] [mclast]... I’m reading that correctly, right?"

menu:
      "Yep, no mistaking it.":
            jump scene4 
      "No, let's check again.":
            jump scene3

      
return

