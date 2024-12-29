label dayfinal:
    scene black with fade
    
    centered "{cps=10}23rd April 2099{/cps}"
    play sound "Transition.mp3" volume 1.5
    centered "{cps=100}Dawn of the final day{/cps}" with fade
   
    
    scene bg rooftop with fade
    show aidil with dissolve
    a "Oh, I'm so depressed, I wanna jump!"
    mc sad "(What should I do?)"

    menu:

        "Never give up on saving them":
            $ MentalHP += 1
            mc sad "Wait, don't jump!"
            a "Why?"
            mc "Because I'm your friend."
            if MentalHP > 1:
                jump ending1
            else:
                jump ending2

        "Give up on saving them":
            jump ending3

    return

label ending1:
    a "Oh okay I won't"
    mc "Cool!"

    scene black with fade
    stop music
    "I'm glad I was able to stop them."
    "Their mental health did get better overtime."
    "Though..."
    "My mind kept going back to that day."
    "And I kept wondering..."
    "How things would've turn out if I had done things differently."

    return

label ending2:
    a "No"
    hide aidil concerned with dissolve
    play sound "ImpactFall.wav" volume 1.0
    "They jumped anyways"
    scene bg rain_rooftop with dissolve
    play music "rain.mp3" volume 0.1 fadein 0.3 fadeout 1.0
    mc sad "Man, that sucks..."

    scene black with fade
    "I've failed..."
    "..."
    play audio "special.mp3" volume 1.0
    "After all these years, this guilt, this feeling...\n{w}It never left me."

    "My mind kept going back to that day."
    "And I kept wondering..."
    "How things would've turn out if I had done things differently."
    return

label ending3:
    a "If you have nothing to say then, byeeee!"
    hide aidil concerned with dissolve
    play sound "ImpactFall.wav" volume 1
    "(They jumped off....)"
    scene bg rain_rooftop with dissolve
    play music "rain.mp3" volume 0.1 fadein 0.3 fadeout 1.0
    mc "..."
    mc sad "What have I done..."

    scene black with fade

    "I've failed..."
    "..."
    play audio "special.mp3" volume 1.0
    "All these years, this guilt, this feeling...\n{w}It never left me."

    "My mind kept going back to that day."
    "And I kept wondering..."
    "How things would've turn out if I had done things differently."
    return