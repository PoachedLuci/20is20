label scene8:

menu:
    "With an uneasy heart, and a deep concern for your future well-being, you..."

    "Go down the hallway.":
        you """Might as well take a peak around this mansion and
        gather information on where I’ve been kidnapped."""

    "Take a look around the current room.":
        """You find that there is nothing here you haven’t already noticed.
        Same paintings, same stairs, same people."""

        """Well. No point in exploring it any further.
        Seeing a musty painting isn’t going to change the fact that you’re
        possibly doomed."""

        "May as well start exploring elsewhere."

    "Go upstairs.":
        show siren default

        siren "Yeah I don’t think going up is a smart move."

        you "Didn’t you just say–"

        siren "And? I’ve changed my mind!"

        show siren exc

        "She gives you a pointed look."

        show siren default

        siren """Look. Not that I care if I lose my competition, but if they think
        you’re trying to get an upper hand at the trial before they’re ready…"""

        you "... I could get like. I don’t know, ghost blasted or something?"

        siren "You’ve got it."

        "Probably not the best idea to go up there then. You hate it when she’s right."

hide siren default

hide reaper default

"Feeling like there’s no other option. You go down the barely lit hallway."

scene vginside with dissolve

show layer master at night

play music "sneaky.mp3" loop

"Are you imagining things, or does the lighting feel dimmer in this part of the mansion?"

"""At the same time, it feels warmer here than at the entrance.
Weird, considering that it is growing darker and darker."""

"""As you walk through, despite the eerie nature of this mansion,
the actual layout could be cozy under the right conditions."""

"""There are nooks to sit in, and beautiful floral designs
tched into the doors and painted on the walls."""

"If you weren’t so certain this place would kill you, you would even like this area."

mystery "Oh hello."

"Like that, out of nowhere, you hear a soft voice from one of the nooks."

scene vginside with hpunch

show layer master at night

you "AAAAAH!"

show plant default with dissolve

play sound ["audio/vfx/heartbeat.wav"] volume 1.0

"Nope. Nope nope nope nope, even this place is trying to kill you."

"""Nope, they have people hiding to jump out and scare you. Nope, screw this place!
Your first instinct is to try and find something to defend yourself with."""

"There! Books on a nearby shelf!"

"""As you scramble to grab one of the books,
you hear someone yawn in the background and eeke out."""

show plant nerv

mystery "Oh please don’t do that… it could be a limited print…"

you "SCREW your limited print or whatever! Eat book, idiot!"

"You fling the book at the mysterious stranger, who was starting to shamble your way and–"

play sound ["audio/vfx/thud.wav"]

"""… aaaaand it lands with a pathetic whump at their feet.
Gingerly, they reach down to pick up the tome, cradling it to their chest."""

show plant default

"They furrow their brows, looking over the book with deep care."

mystery "I don’t think it’s damaged…"

play sound ["audio/vfx/heartbeat.wav"] volume 1.0

"""Despite it all, despite your heart wanting to jump out your chest and into your throat,
this person doesn’t seem dangerous."""

"Just kind of strange."

"Come to think of it, didn’t the weird voice say there was supposed to be a fourth person here?"

"With trembling words, you inch towards them."

you "Who are you?"

show plant nerv

"They look up from their book and murmur."

plant "[plant]. Hi…"

"[plant]. Okay cool."

you "Are you… here for the competition?"

"They nod, holding the book to their chest before trying to speak up a little louder."

plant "Yes um… I was trying to find a way out, but I heard voices and well, I didn’t know if they were friend or foe so I um…"

plant "Hid in… that nook there."

"Wow. Okay. You’re the jerk here, kinda. Great."

"Not that you could have known, of course. It’s a haunted freaking mansion or whatever. But at least you feel a little calmer now."

you "Yeah… yeah okay, cool. I’m [mcname] [mclast]."

plant "Nice to meet you, [Honorific] [mcname] [mclast]."

show plant default

menu:
    you "Did you"
    "… hear the instructions earlier?":
        plant "I did but um… I didn’t quite understand it."

        plant "If I met up with the other three, maybe they’d know?"

    "… find a way out?":
        "They shake their head."

        plant"All the windows feel glued shut and the back door leads to a greenhouse."

        plant "Unless you plan on smashing through the glass you won’t be able to get out."

        you "Okay well, looks like we’re breaking a greenhouse."

        show plant nerv

        "In a sudden panic, Marlowe cries out."

        plant "Oh please don’t! It’s beautiful there!"

        "There’s a beat of silence before they add."

        plant "Plus I already tried. That wouldn’t break, either."

        show plant default

        "Great."

    "… want to join everyone at the main entrance?":
        show plant s

        "The thought seems to perk them up a little, and they give a vigorous nod."

        plant "Oh yes, please!"

        show plant default

play sound ["audio/vfx/movement.wav"]

"As [plant] puts the book back on the shelf, you shake your head and ask yourself."

you "{i}How the hell could they have wandered off over here on their own?{/i}"

"Mysterious [plant]. It doesn’t matter right now."

scene bginside1 with dissolve

play music "cute.mp3" loop

show siren exc with dissolve

show reaper default at right with dissolve

show plant default at left with dissolve

"Instead, you walk back into the main entrance area with them to look for the other two."

"Indeed, they are right where you left them. Strangely, [siren] looks almost uncomfortable."

"[reaper] did not seem affected, but she immediately jumped on the opportunity to snip at you."

siren "And who’s this? Already found someone to replace me?"

you "Uhhh, well you see…"

show siren default

"In a surprising turn of events, the newest member of the group speaks up."

show plant s

plant "My name is [plant]… What are your names?"

"Oh. That’s right. Introductions. They wouldn’t know anyone here."

"The first person you’d met today raises a hand and says."

show reaper s

reaper "[reaper]. Nice to meet’cha."

"Of course he’d be so nice about this."

show reaper default

"On the other hand, your childhood friend refuses to answer, instead turning her head to scoff."

show plant default

siren "Does it matter? I’m here to win, so there’s no point in telling everyone."

you "That’s [siren]."

show siren exc

siren "HEY!"

show plant s

"[plant] smiles a little at her, despite how uneasy [siren] looks."

plant "Nice to meet you, [siren]. Let’s all do our best."

"With a despondent grumble, she replies."

show siren laugh

siren "If I did my best, you’d all be doomed."

"Everyone’s looking at each other, and you realize you should start deciding your next move."

show reaper s

reaper "Nice to meet you. Even if I’m here to win, I’m sure you’d all make great partners."

"""How sportsmanlike– oh wait. Yeah. Partners.
You have to pick a partner for the trials. But how should you choose?"""

show siren default

show reaper con

siren "Whoever mine is, I hope they don’t plan on getting in my way."

"[plant] says nothing, but seems to shrink at that comment. They still smile softly."

show plant default

menu:
    "Who should you choose…"

    "[siren] seems like the safest bet.":
        """I just don’t have to get in her way and we already know each other.
        Teamwork will be easy if we just work to each other's strengths."""

        "Better the devil you know, right?"

        you "[siren], want to team up?"

        """She looks at you and for once, she looks more confused than anything.
        A perfect opportunity to quip at her."""

        you "You know you missed me!"

        show siren laugh

        "With a snort, she rolls her eyes and steps to stand side by side with you."

        siren "Yeah yeah, fine. Just don’t get in my way."

        show siren default

    "[plant] seems nice.":
        "They were already looking around the mansion so they will have good info."

        "They also seem to have pretty good composure, despite being timid."

        "Maybe it’d be good to have someone knowledgeable and observant."

        you "If you don’t have anyone in mind, Marlowe. I think we would make a good team."

        show plant s

        "This seems to surprise them, but Marlowe’s shock mellows out into a smile."

        plant "I would like that a lot."

    "[reaper] seems like good company.":
        "I can still get the prize at the end, with just his help."

        "He also seems like a good team player. Something about him {i}screams{/i} teamwork."

        "Besides, he has been kind this whole time. It may be nice to have moral support."

        you "[reaper]? Would you do me the honors?"

        show reaper s

        "[reaper] smiles at you, and steps to your side to wrap an arm around your shoulder."

        reaper "Perfect! I’d be glad to."

        reaper "Things are {i}finally{/i} starting to look up."

        show reaper default

"Chosen partner nearby, for the first time tonight you begin to feel some hope."

"With your partner set, maybe the trials won’t be so bad."

"… one could hope."

stop music fadeout 0.2

jump scene9 
