default helpAidil = False
default helpSara = False
default helpZiad = False
label day2:
    scene black with fade
    
    centered "{color=#ffff}{cps=10}22nd April 2099{/cps}{/color}"
    centered "{color=#ffff}{cps=10}After School{/cps}{/color}"
    #play sound "Transition.mp3" volume 1.5

    scene classroom with fade
    mc normal "Argh! School has already ended and I barely have any progress on this."
    mc "Hmmm, a day has passed and I'm still not sure. Especially when tomorrow is the deadline. {w}Hmm... I should really choose who I should help today."
    mc "Either it's Sara or Ziad."
    mc "Hmmm.."
    if tellAidil:
        mc normal "Wait, what if Aidil is the one who needs my help? {w}Maybe he's the one who wrote me that letter. {w}Perhaps, the one who needs my help always have been right under my nose."
        mc sad "What if he really did had a problem he couldn't express it to me..."
    mc "I think I have time to meet one last person."
    mc "Hmmm... {w=0.5} Who should I choose to help?"

    # This will lead to chooseoption.rpy
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
