default helpAidil = False
default helpSara = False
default helpZiad = False
label day2:
    scene black with fade
    
    centered "{cps=10}22nd April 2099{/cps}"
    centered "{cps=10}After School{/cps}"
    play sound "Transition.mp3" volume 1.5
    #centered "{cps=100}2 Days remaining{/cps}" with fade

    #scene bg rooftop with fade
    #"Stuff happened.."
    #show aidil at right with dissolve
    #show ziad glasses flip at left with dissolve
    #show sara with dissolve 
    #mc "Ehhh"
    #mc happy "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat."

    #menu:

        #"Help Aidil":
            #$ MentalHP += 1
            #jump day3

        #"Help Sara":
            #$ MentalHP += 1
            #jump day3
        
        #"Help Ziad":
            #$ MentalHP += 1
            #jump day3
    #return
    scene classroom with fade
    mc normal "Argh! School already ended but I barely do any progress"
    mc "Hmmm, a day has passed and I'm still not sure. Especially when tomorrow is deadline. Hmm I should really choose who I should help today."
    mc "Either Sara or Ziad."
    mc "Hmmm.."
    if tellAidil:
        mc normal " Wait, what if Aidil is the one who need help. Maybe the one who wrote me that letter, the one who need my help always have been right under my nose"
        mc normal "What if he really had a problem"
    mc "I can only choose 1 person I need to dedicate helping."
    mc "Hmmm. Who should I choose?"

    if tellAidil == True:
        menu help:
        
            "Help Aidil":
                $ helpAidil = True
                jump helpaidil
        
            "Help Sara":
                $ helpSara = True
                jump helpsara
        
            "Help Ziad":
                $ helpZiad = True
                jump helpziad
    else:
        menu helpnoaidil:
            "Help Sara":
                $ helpSara = True
                jump helpsara
        
            "Help Ziad":
                $ helpZiad = True
                jump helpziad
#pls work