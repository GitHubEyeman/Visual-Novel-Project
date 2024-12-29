# This is the codes for the first day of this VN. There are multiple days split across different files.
# All codes about characters, names, fonts, ects goes to the characters.rpy 
# The code starts here.

# MentalHP variable to determine which ending you'll get at the end.
default MentalHP = 0

label start:

    # Intro scene

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


    # The First scene at a cafe.
    scene bg cafe with fade
    show aidil with dissolve #Make sure it is lowercase even if the original image file has uppercase letters.

    a "Hi, stuff happened and-"
    mc happy "Really?"
    show aidil with dissolve
    mc "I don't care"


    menu:

        "Help":
            $ MentalHP += 1
            jump day2

        "Don't help":
            $ MentalHP -= 1
            jump day2

    return
