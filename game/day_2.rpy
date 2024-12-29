label day2:
    scene black with fade
    
    centered "{cps=10}21st April 2099{/cps}"
    play sound "Transition.mp3" volume 1.5
    centered "{cps=100}2 Days remaining{/cps}" with fade

    scene bg rooftop with fade
    "Stuff happened.."
    show aidil at right with dissolve
    show ziad glasses flip at left with dissolve
    show sara with dissolve 
    mc "Ehhh"
    mc happy "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

    menu:

        "Help":
            $ MentalHP += 1
            jump day3

        "Don't help":
            $ MentalHP -= 1
            jump day3
    return