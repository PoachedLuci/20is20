label scene8:
menu:
    "With an uneasy heart, and a deep concern for your future well-being, you"
    "Go down the hallway.":
        you "Might as well take a peak around this mansion and 
        gather information on where I’ve been kidnapped."
    "Take a look around the current room.":
        "You find that there is nothing here you haven’t already noticed. 
        Same paintings, same stairs, same people."
        "Well. No point in exploring it any further. 
        Seeing a musty painting isn’t going to change the fact that you’re 
        possibly doomed."
        "May as well start exploring elsewhere."
    "Go upstairs.":
        siren "Yeah I don’t think going up is a smart move."
        "Your line of sight is drawn to Vivi’s finger, 
        which points from the steps to what you can see of the upstairs landing."
        "Probably not the best idea to go up there since they are probably 
        getting it ready for the first trial."
        
hide siren default
hide reaper default

"Feeling like there’s no other option. You go down the barely lit hallway." 

scene vginside with dissolve

play music "sneaky.mp3" loop 

"Lights feel dimmer in this part of the mansion and the moon seems to be missing."

"Going further down the hallway you feel it’s warmer here than at the entrance."

"It even feels cozy with nooks to sit by windows and lots of floral notes 
in the decorations from the doors to the paintings on the walls. "

mystery "Oh hello."

"You jump, somehow not noticing there was someone further down by one of the windows. "

you "Hey, are you the mysterious fourth person the voice mentioned?"

show plant default

mystery "I'm assuming you know where everyone else is then?"

mystery "I was just lost and heard the voices so I was going to check them out… 
but decided to try and find a way out..." 

menu:
    you "Did you"
    "'Hear the announcement?'":
        mystery "I did but I didn’t understand it. 
        I was hoping to talk to everyone to decide how to move forward."
    "'Find a way out?'":
        mystery "Unfortunately all the windows feel glued shut and 
        the back door leads to a beautiful greenhouse."
        mystery "Unless you plan on smashing through the glass you wouldn’t be able to get out."
    "'Want to join everyone at the main entrance?'":
        mystery "Yup, that sounds good."

you "{i}how could anyone wander around on their own around here?{/i}"

scene bginside1 
play music "cute.mp3" loop 

"You walk back into the main entrance area with the last person and look to find the other two, 
Vivi looking almost uncomfortable talking to him alone."

show siren default 
show reaper default at right 
show plant default at left 

siren "And who’s this? Already found someone to replace me?"

you "{i}Wait. How could I go through that whole conversation, and forget to ask their name?{/i}"

you "Uhhh, well you see…"

mystery "My name is Marlowe… What is everyone's plan?" 

"You notice everyone starts looking around trying to decide what their next move is."

reaper "I’m still here to win so I’ll take anyone as my partner for the paired trials. 
I don’t think we have to pick until the trials start though."

siren "I’m going to win so I’ll only have someone who doesn’t plan on getting in my way." 

menu: 
    "Vivi seems like the safest bet.":
        "I just don’t have to get in her way and we already know each other. 
        Teamwork will be easy if we just work to each other's strengths."
        you "Vivi, want to team up? I know you missed me."
        siren "Exactly who I wanted."
    "Marlowe seems nice.":
        "They already looked around the mansion so they would have good info."
        "They also seem to have pretty good composure all things considered."
        you "If you don’t have anyone in mind Marlowe. I think we would make a good team."
        plant "I would like that a lot."
    "Diesel seems like he won't get in my way.":
        "I can still get the prize at the end even with just his help."
        "He also seems like a good team player, something about him screams teamwork."
        you "If you’re fine with anyone, then I’ll be your partner Diesel."
        reaper "Perfect! Things are starting to look up."

"Now with your partner set. You feel as though these trials can’t be that bad… "

"Hopefully… "

jump scene9 



