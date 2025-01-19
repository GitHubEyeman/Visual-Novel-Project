label day3:
    scene black with fade
    centered "{cps=10}23rd April 2099{/cps}"
    play sound "Transition.mp3" volume 1.5
    centered "{cps=100}1 Day remaining{/cps}" with fade

    scene bg cafe with fade
    "Some more stuff happened.."

    #menu:

        #"Help":
            #$ MentalHP += 1
            #jump dayfinal

        #"Don't help":
            #$ MentalHP -= 1
            #jump dayfinal
    #return