label scene7:
    scene bginside1

    show siren default at midright

    show reaper default at midleft

    show layer master at night

    play music "distorted-easy.mp3" loop fadein 1.0

    define they = Pronoun("they", "she", "he", custom = "they")

    define person = Term("person", "woman", "man", id = "person")

    play sound ["audio/vfx/heartbeat.wav"]

    """A chill runs through your bones, as the room grows noticeably darker.
    Those ‘going to get murdered’ vibes you had earlier are suddenly returning …"""

    play sound "audio/vfx/whispers.wav" volume 0.1

    show layer master at night

    """Voices start to come from the walls. Lights flicker. You almost expect
    ghosts to start popping out but instead, the walls themselves feel almost alive."""

    mystery "Are you ready to find the answers you seek?"

    stop sound

    queue sound ["audio/vfx/bang.wav"]

    show bginside1 with hpunch

    show siren default at midright with hpunch

    show reaper default at midleft with hpunch

    you "!!!"

    stop sound

    show reaper con

    reaper "That wasn't a good noise."

    show reaper default

    siren "Yea, no shit. Sounds like we’re all stuck here."

    you "Nope, not worth it anymore."

    """You spin around and try yanking the door open, it feels as though
    it’s being tied together from the outside. Each pull only holds the door tighter."""

    menu:
        "Yup this is it. I’m going to die here.":
            "You sit down on the floor in defeat and stare at the door."

            show siren laugh

            siren "Well [they_ve] officially lost it."

        "Continue yanking on the door.":
            "You continue trying to escape but to no avail."

            """No amount of tugging makes the door budge.
            You feel as though somehow trying to open them made them want to stay shut even more."""

        "Pull out your cell phone.":
            "Your phone! Duh. In times like this, you could always count on technology."

            """Yet when you try calling for help, you soon realize you’re in the most backwater,
            isolated, no-one-will-ever-find-my-body part of town."""

            "Of {i}course{/i} there's no reception."

    "As if to tempt fate, your new companion calls out to the void."

    show reaper con

    reaper """Is this how most competitions are run?
    Where’s the host? Who’s going to grant me my wish?"""

    mystery "Remember: the goal of this competition is for you to find out."

    mystery "I’m sure you’d all love to get started if you’re ready for the rules."

    "No matter where you whip your head, there’s no sign of where this voice was coming from."

    play sound ["audio/vfx/heartbeat.wav"] volume 1.0

    "At this rate, you’re sure your heart will beat out your chest."

    """Why did you ever agree to this stupid game? You’re trapped,
    you’re with a stranger and an old friend, and the doors would not budge."""

    """In a moment of wide-eyed panic, you look to your companions.
    Surely they are as freaked out as you are–"""

    show siren exc

    siren "Hell yeah!"

    """She looks almost bursting with excitement.
    Like someone who’s about to watch their favorite show's new season."""

    "Is this for real?!"

    reaper "Ready."

    show reaper s

    """As for the other guy, he smiles straight ahead and
    responds to the voice as if they are straight in front of him."""

    "There may have been some confusion there, but he seemed all for this too."

    "It looks like you were alone in being afraid. Great. That totally made you feel better."

    "Resigned to your possible fate of being a horror movie's final [person], you let out a shaky sigh and grumble."

    you "Fine, just… get on with it."

    play sound "audio/vfx/whispers.wav" volume 0.1

    mystery "Gladly!"

    "This voice was far too happy about this for your tastes."

    """mystery "To keep things nice and fair between you four is by
    having you compete in little trials. That should keep things interesting."""

    "Wait, four?"

    mystery """There will be a total of three trials, each one leading you to learn things about each other.
    Who knows? Perhaps you’ll learn some things about yourself!"""

    mystery """Learning about each other is imperative here,
    so some trials will require teamwork. Be sure to stick together."""

    mystery "In these trials, you will only be allowed to work in pairs and no more."

    mystery """Whoever can find the host by 11 PM on Halloween night will
    be granted whatever their heart desires, as promised."""

    mystery """The first trial will start in 1 hour upstairs, at the first door on the left.
    Discuss who will be partners amongst the four of you."""

    show layer master

    stop sound

    "Again with this fourth person… who were they? Where were they?"

    show reaper default

    show siren default

    reaper "I wonder where this fourth person is…"

    "Thank god. At least someone is wondering the same thing you are."

    show siren laugh

    "As for [siren], she only scoffs and states."

    siren "Hopefully they can provide some interesting competition… or companionship."

    show siren default

    siren "Well, we can at least hope they follow instructions well. Shall we head upstairs?"

    menu:
        "About the fourth person":
            you "I mean if they never show up, I guess that’d be less competition…"

            show reaper con

            reaper "But then we wouldn’t be able to pair up…"

            "He sounds almost disappointed. Bless his soul."

        "About the staircase":
            """I don’t know about this… These stairs look totally unstable.
            I bet they’ll just fall apart when we go up or something.."""

            """[siren] rolls her eyes at you, before stepping close
            enough beside you to shove your back slightly."""

            show siren exc

            siren "Don’t be a wuss. Come on."

    """Well, it looks like you all are now committed to this.
    Whether you want to or not, you may as well roll with it."""

jump scene8
