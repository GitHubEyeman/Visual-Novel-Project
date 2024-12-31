label day2:
    scene black with fade
    
    centered "{cps=10}21st April 2099{/cps}"
    play sound "Transition.mp3" volume 1.5
    centered "{cps=100}2 Days remaining{/cps}" with fade

    scene bg rooftop with fade
    "Stuff happened.."
    window show dissolve
    mc "Hmmm..."
    show aidil at right with dissolve
    show ziad glasses flip at left with dissolve
    show sara with dissolve 
    
    mc "Ehhh..."

    show ziad glasses:
        xalign 0.0
        ease 1.0 xalign 1.0
        
    show aidil flip:
        xalign 1.0
        ease 1.0 xalign 0.0
    
    pause 0.8
    show ziad with dissolve
    show aidil thinking flip with dissolve
    show sara 2 with dissolve 


    mc happy "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea."

    menu:

        "Help":
            $ MentalHP += 1
            jump day3

        "Don't help":
            $ MentalHP -= 1
            jump day3
    return