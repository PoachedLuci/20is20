label scene5: 
scene houseoutside_d1 with dissolve 

play sound ["audio/vfx/cardoorcloses.wav"]

"And so, after a long drive to the listed address, 
as well as a walk up some unnecessarily long pavement- you stood in front of a mansion."

"From what you see, the curtains in the windows are drawn with no light visible."

"A healthy mess of plants decorates the ground and threatens to take over the plaster-cracked walls."

"The dark of the night only highlights the fact that it is barely visible among the growing trees."

"You can barely see the door, let alone anyone else in the immediate area."

you "Is this even the right address?"

"You kept your invitation tucked away in your back pocket, 
only pulling it out now to confirm you are in the right place."

you "Yep… this has to be it."

you "..."

you "I feel like I’m going to get murdered…"

play sound ["audio/vfx/wind.wav"]

"As soon as the morbid thought crosses your mind, a chilly wind passes your way."

mystery "Hello!"

"The sudden exclamation cutting through the silence of the night startles you."

stop sound fadeout 1.0

scene houseoutside_d1 with hpunch

you "AH-"

"A man comes into your view, waving casually with a hand tucked into his pocket."

show reaper default

mystery "I assume you’re here for the competition as well?"

menu: 
    "Yes, I am":
        show reaper s 
        mystery "Awesome, Me too."
        you "Thank goodness, at least I’m not going in alone…"
    "No, I am not.":
        show reaper s 
        "He gives a cheeky smile at your statement."
        mystery "It’s obvious you’re lying."
        you "Wha- how?!"
        mystery "You wouldn’t be able to enter this area if you weren’t."
        you "I’m not some kind of vampire."
        show reaper con
        mystery "Then what are you?"
        you "{i}What is this guy talking about…{/i}"

show reaper default
mystery "So, have you been here long?"

you "No, I just got here."

mystery "Ahh… well…"

"The two of you fall into awkward silence as neither of you seem to know how to progress the conversation."

you "It’s kind of spooky, huh?"

"You internally cringe at your poor attempt at small talk."

mystery "Spooky? I mean… I guess."

mystery "If you’re scared there’s no need to be."

you "Pff, scared? A-as if."

"The tremor in your voice betrays your front."

show reaper con

mystery "Wait, you're actually scared?" 

show reaper s 

mystery "It’s gonna be alright, trust me. These places only seem spooky ‘cause you’re seeing it at night."

mystery "I bet if you were to come here in the day you’d just think it was a shitty old shed."

"His lighthearted smile makes you feel a little bit better." 

you "Thanks… I’m [you] by the way."

mystery "Diesel."

you "Should we head inside now?"

reaper "As long as you’re feeling alright, let’s go."

jump scene6