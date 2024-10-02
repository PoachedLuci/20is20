label scene3:

label pronounSelection:
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
      label firstName:
            mcname = renpy.input("It has my first name?", length = 32).strip().capitalize()

            if not mcname:
                  "enter a real name this time stinky"

                  jump firstName

      label LastName:
            mclast = renpy.input("and last name?", length = 32).strip().capitalize()

            if not mclast:
                  "enter a real last name this time stinky"

                  jump LastName

mc "[Honorific] [mcname] [mclast]... I’m reading that correctly, right?"

menu:
      "Yep, no mistaking it.":
            jump scene4
      "No, let's check again.":
            jump scene3

return
