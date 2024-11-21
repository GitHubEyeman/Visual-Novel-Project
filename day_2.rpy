label day2:
    scene black with fade
    
    centered "{cps=10}21st April 2099{/cps}"
    play sound "Transition.mp3" volume 1.5
    centered "{cps=100}2 Days remaining{/cps}" with fade

    scene bg rooftop with fade
    "Stuff happened.."

    menu:

        "Help":
            $ MentalHP += 1
            jump day3

        "Don't help":
            $ MentalHP -= 1
            jump day3
    return