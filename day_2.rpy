label day2:
    scene black with fade
    
    centered "{cps=10}21st April 2099{/cps}"
    play sound "Transition.mp3" volume 1.5
    centered "{cps=100}2 Days remaining{/cps}" with fade

    scene bg rooftop with fade
    "Stuff happened.."
    show aidil at left with dissolve
    show ziad at right with dissolve
    show sara with dissolve
    "Ehhh"


    menu:

        "Help":
            $ MentalHP += 1
            jump day3

        "Don't help":
            $ MentalHP -= 1
            jump day3
    return