# The game and the first day starts here.
# All codes about characters, names, fonts, ects goes to the characters.rpy 
# name of the character.
# The game starts here.
default MentalHP = 0
label start:

    scene bg rain_rooftop
    play music "rain.mp3" fadein 0.3 fadeout 0.3
    "My mind kept going back to that day."
    "And I kept wondering..."
    "How things would've turn out if I had done things differently."

    stop music fadeout 1.0
    scene black with fade
    
    centered "{cps=10}20th April 2099{/cps}"
    play sound "Transition.mp3" volume 1.5
    centered "{cps=100}3 Days remaining{/cps}" with fade


    scene bg cafe with fade


    show victim happy with dissolve

    # These display lines of dialogue.

    v "Hi, stuff happened and-"
    mc "Really?"
    mc angry "I don't care"

    # This is the first choice.

    menu:

        "Help":
            $ MentalHP += 1
            jump day2

        "Don't help":
            $ MentalHP -= 1
            jump day2

    return
