label scene4:

you "Is this some kind of glitter bomb?"

queue sound ["audio/vfx/paper.wav"] 

"You shook the envelope around, hearing nothing outright sinister."

"You stared down with tired eyes, conflicted whether you should open it or 
chuck it back into the pile of letters you tell yourself you’d read later but eventually throw out."

"The royal blue wax seal was oddly familiar but you chalk that up to sleep-deprived delusion. 
It taunted you to open it, and when you ran your fingers over the intricate design you felt your 
heart suddenly racing."

you "..."

menu:
    "Chuck it into the pile":
        you "I’m not in the mood to be pranked by some punk kid right now…"
        "You carelessly threw the letter into the pile, ignoring the nagging feeling in the back of your mind."
        "The rest of the day, you tried to go back to your daily routine,"
        "Spending hours in front of your monitor- searching through bare cupboards to find an ounce of sustenance- 
        laying in bed cursing at the world."
        "Through it all, you couldn’t get the letter out of your mind."
        you "It could be money…"
        "You smiled slightly at the thought, though the reality of the decorated envelope probably 
        containing nothing more than parchment wiped it off quickly."
        "You found yourself back in the living room, staring at the pile with deep contempt."
        "You picked up the letter."
    "Open it":
        you "If this is a prank, I swear…"

queue sound ["audio/vfx/letter.wav"]

"Your finger ran over the edge of the seam-and with bated breath you carefully lifted the seal."

you "..."

you "What the HELL is this?!"

show letter at truecenter, half_size 

show layer master at night

"Congratulations!"

"You have been personally selected to take part in a competition leading up to Halloween night."

"The first competitor to find out who I am, will win. The prize is whatever your heart deeply desires!"

"To participate in this competition simply show up at the not spooky mansion at the edge of town in the forest."

"We hope to see you there,"

"Host"

jump scene5 





