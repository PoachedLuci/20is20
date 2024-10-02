label scene6:
    play music "cute.mp3" loop volume 0.2

    scene bginside1 with dissolve

    play sound ["audio/vfx/steps.wav"] loop

    """Stepping past the threshold and into the mansion,
    you can’t help but gasp at the state of the foyer before you."""

    "Despite the state of its outside, the inside itself is well-maintained."

    """The floorboards, while worn, are swept and washed.
    No cobwebs decorate the corners of the walls or the banister."""

    """With each further step you take, the situation becomes stranger.
    Each step, with its matching echo down the halls, reveals more questions."""

    "Who lived here? Why would they even bother with maintaining a place of this size?"

    stop sound

    "Why stick with this whole haunted-looking mansion schtick?"

    "As your thoughts drift, your new… companion… lets out a low whistle."

    show reaper default with dissolve

    reaper "Pretty impressive…"

    """Despite the deadpan expression, there’s a glint of wonder in his voice.
    His eyes drift the same way yours had."""

    "At least, they do until they meet yours."

    reaper "Like, this place I mean. It’s impressive, yeah?"

    you "It’s ..."

menu:
    "Impressive":
        "You can’t help but agree with him."

        you "I can’t believe how good it looks. It’s clearly been here a while."

        mystery "'A while' may be underselling it."

        mystery "It’s {i}practically prehistoric{/i}."

    "Overwhelming":
        you "Huge."

        you "Like, I don’t remember the last time I’ve set foot in a place this big you know?"

        reaper "I mean, yeah it’s big, but…"

        "He shrugs at you, before saying,"

        reaper "... in the end, the folks who live here are probably the same as anyone else."

        reaper "Folks are all the same in the end, no matter what."

        mystery "Woooow. From anyone else, that would have sounded {i}edgy{/i}."

    "A Dump":
        you "It needs a lot of work."

        you """Like sure, the location’s great and the owner is trying hard,
        but this place has to be filled with I don’t know."""

        you "Asbestos or something?"

        "As your new companion stares at you confused, a high-pitched laugh rang out from nearby."

        mystery "Asbestos? You’re invited to someone’s home, and you say it’s filled with asbestos?"

"That voice grabs hold of your mind, catches your words in your mouth before you can say them."

"There’s a sense of familiarity, a feeling of nostalgia…"

you "... [siren]?"

"Sure enough, as soon as her name passed your lips she stepped forward."

show reaper default at midleft with move

show siren default at midright with dissolve

"Out of the shadows of this mysterious mansion came your childhood friend."

"For a moment, you find yourself wondering if this is real."

you "I’m not losing it, am I?"

show siren laugh

"As if to assuage your fears, [siren] laughed in that pitchy way you remember her by."

siren "I’d be surprised if you hadn't lost it a while ago."

you "[siren] what? What are you doing here? I-"

show siren default

"She looks away from you, and scoffs."

siren "Isn’t it obvious? I’m here to win."

"""[siren] continues to ignore you. Instead, her eyes stop on your new… friend.
As she pauses and gazes up and down, she sing-songs to him."""

show siren exc

siren "I see the competition is… strong."

show reaper con

"""For a moment, he seems to perk up.
That moment is cut short, however, as [siren] drawls."""

siren "And not much else."

show reaper s

"The cruel comment seems to amuse [reaper]."

"""[siren], on the other hand, drums her fingers on her arm.
You’d known her enough to know she was annoyed."""

"But that wasn’t the question, was it? You force the question again."

you "What are you doing here, [siren]?"

show siren default

"Her fingers stop drumming, only to squeeze her arm instead."

you "It’s been ages! Where have you been?"

"You want nothing more than to grill [siren], to get some answers."

"""After all, you had been friends when you were younger.
She disappeared without so much as a goodbye."""

"Why is she here now, of all times? This has to be some sort of sick joke."

show reaper con

"[reaper] furrows his brows and leans close to ask."

reaper "Hey… are you okay?"

"This question, too, finds no answer."

play music "cute.mp3" loop volume 0.1 fadeout 1.0

jump scene7
