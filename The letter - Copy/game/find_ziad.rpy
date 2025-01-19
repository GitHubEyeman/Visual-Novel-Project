label findziad:
    scene cafeteria with fade
    mc normal "Hmm. Maybe Ziad is the one that send's the letter. I'm pretty sure he's here for lunch."
    mc "Oh there he is."
    "Tuah sees Ziad sitting alone eating."
    mc "Oh there he is."
    mc "Hi Ziad."
    "Ziad glance at Tuah direction."
    show ziad at right with dissolve
    z "Oh Tuah. What do you want?"
    mc "{i}Uhh his tone shows he's not in a good mood. Should really choose my words here.{/i}"
    mc "Oh just want to check on you."
    z "Huh? Okay?"
    mc "Well how are you? You seem stressed."
    show ziad glasses at right with dissolve
    z "Oh you think?"
    mc "Oh uhh. Haha maybe. Why are you stressed then?"
    z "Of course because of my exam. My marks are so low."
    mc "Oh really? How much did you get?"
    z "Only 91%%"
    mc "{i}What the- That isn't low. I barely passed with 43%%{/i}"
    mc "Well, isn't that high?"
    
    z "Are you joking me? No it's not! I should have gotten at least 99%%. Argh! I'm doomed"
    mc "Do you really need to get full marks?"
    z "Of course! I need to."
    mc "{i} Hmm, I think I get it now.{/i}"
    mc happy "Thanks to my deduction skill, I deduct that his parents are pressuring him to get full marks."
    mc "I understand your situation"
    show ziad side at right with dissolve
    z "Yeah like I believe you."
    mc "{i}Seems like he's not telling anything more at the moment. Maybe I should try again tomorrow.{/i}"
    mc "Well, I hope you feel better. I'll take my leave for now. See you later."
    z "Yeah see you later"
    hide ziad side with dissolve
    mc normal "{i}Maybe it really is Ziad, but he's just not ready to tell me{/i}"
    mc "{i}Aaaaaah! I have no idea.{/i}"
    if chooseSara == True:  
        jump day2
    else:
        jump findsara