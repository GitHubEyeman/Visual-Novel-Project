label findsara:
    scene library with fade
    "The library was quieter than usual, with only a few students scattered among the shelves."
    "Sara sat at a corner table by the window, a stack of books next to her and her nose buried in one."
    mc happy "Maybe Sara's the one who needs help. {w}She always alone pretty much all the time. {w}Maybe she's suffering in silent and doesn't know who to tell. And of course she choose me to tell about her problem. {w=0.5}Hehe..."
    show sara flip at right with dissolve
    mc "Hey Sara. Got a moment?"
    show sara with dissolve
    s "AH! Oh T-Tuah, you surprise me."
    mc "Sorry about that. Doesn't mean to sneak up on you."
    s "It's okay, I'm just caught up to this book."
    show sara at center with move
    mc "What are you reading?"
    s "Oh it's just some story novel. Nothing special."
    mc "How you're doing?"
    s "I'm good. Well uhh, thank you for asking."
    s "Umm... {w=0.5}Do you need something?"
    mc "I always see you sitting here and alone. Are you alright?"
    s "Uhh. Why do you ask?"
    mc "Oh I'm just checking on you."
    s "Well thanks. I'm fine, really. I just like the quiet here. It's... calming."

    menu sara1:
        "{i}Her voice is calm yet there's hesitation. Should I press even further?{/i}"
        "Press her for more details.":
            mc normal "Are you sure you're okay? You don't have any problems, {w=0.5}do you?"
            s "Y-yeah. Trust me. I'm okay."
            mc "If you have a problem, you should really tell me you know."
            show sara normal
            s normal "Umm. I really appreaciate you asking me but really, {w=0.5}I'm fine.{w=0.5} I promise."
            mc happy "Alright. Just remember that I'm always here if you need anything."
            s "Well... Thanks. That means a lot."
            mc "I'll take my leave. Bye Sara."
            s "Bye Tuah."
            jump continue_investigation

        "Back off and change topic.":
            mc "Fair enough. {w}I didn't mean to pry."
            show sara normal
            s "You're not prying. {w}It's just... hard to explain."
            mc "Got it. By the way, how's the novel you're reading?"
            s "It's really good. It's about a princess that become an assasin and try to juggle her life then they-"
            "Sara talks about the novel she is reading. {w}After a while,{w=0.5} Tuah says goodbye and takes his leave."
            jump continue_investigation

label continue_investigation:
    hide sara normal with dissolve
    mc "I couldn’t shake the feeling that Sara was holding something back."
    mc "Hmmm maybe I'm read too much into it."
    if chooseZiad == True:
        jump day2
    else:
        jump findziad
        
    