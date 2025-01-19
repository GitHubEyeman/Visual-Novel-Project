label findziad:
    scene cafeteria with fade
    mc normal "Hmm. Maybe Ziad is the one that send's the letter. {w}I'm pretty sure he's here for lunch."
    mc "Oh there he is."
    show ziad at left with dissolve
    "Tuah sees Ziad sitting alone eating."
    mc "Oh there he is."
    mc "Hi Ziad."
    show ziad flip
    "Ziad glance at Tuah direction."
    show ziad flip at center with move
    z "Oh Tuah. What do you want?"
    mc "{i}Uhh... his tone shows he's not in a good mood. {w}I should really choose my words here carefully.{/i}"
    mc "Oh, just want to check on you."
    z "Huh? Okay?"
    mc "Well,{w=0.5} how are you? You look stressed out."
    show ziad glasses with dissolve
    z "Oh you think?"
    mc "Oh uhh... Haha maybe. Why are you stressed out then?"
    z "Of course because the recent exam. My marks are so low."
    mc "Oh really? How much did you get?"
    z "Only 91%%."
    mc "{i}What the- That isn't low at all! I barely passed with 43%%{/i}"
    mc "Well, that' doesn't look that low to me."
    
    z "Are you joking me?{w} Yes, it is!{w} I should have gotten at least 99%%.{w} Argh! I'm doomed"
    mc "Do you really need to get full marks?"
    z "Of course!"
    mc "{i} Hmm, I think I get it now.{/i}"
    mc happy "Based on my deduction skills,{w=0.5} I deduct that his parents are pressuring him to get full marks."
    mc "I think understand your situation."
    show ziad side with dissolve
    z "Yeah like I believe you."
    mc "{i}Seems like he's not telling anything more at the moment. Maybe I should try again tomorrow.{/i}"
    mc "Well, I hope you feel better. I'll take my leave for now. See you later."
    z "Yeah, see you later."
    hide ziad side with dissolve
    mc normal "{i}Maybe it really is Ziad, but he's just not ready to tell me.{/i}"
    mc sad "{i}Aaaaaah! I have no idea.{/i}"
    if chooseSara == True:  
        jump day2
    else:
        jump findsara