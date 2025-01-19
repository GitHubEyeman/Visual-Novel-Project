label findsara:
    scene library with fade
    "The library was quieter than usual, with only a few students scattered among the shelves."
    "Sara sat at a corner table by the window, a stack of books next to her and her nose buried in one."
    mc happy "Maybe Sara's the one who need help. She always alone pretty much all the time. Maybe she’s suffering in silent and don’t know who to tell. And of course she chooses me to tell about her problem. Hehe"
    show sara at right with dissolve
    mc "Hey Sara. Got a moment?"
    s "AH! Oh T-Tuah, you surprise me."
    mc "Sorry about that. Doesn't mean to sneak up on you."
    s "It's okay, I'm just caught up to this book."
    mc "What are you reading?"
    s "Oh it's just some story novel. Nothing special."
    mc "How you're doing?"
    s "I'm good. Well uhh, thank you for asking."
    s "Umm..Do you need something?"
    mc "I always see you sitting here and alone. Are you alright?"
    s "Uhh. Why do you ask?"
    mc "Oh I'm just checking on you."
    s "Well thanks. I'm fine, really. I just like the quiet here. It's... calming."

    menu sara1:
        "{i}Her voice is calm yet there's hesitation. Should I press even further?{/i}"
        "Press her for more details.":
            mc normal "Are you sure you're okay? You don't have any problem?"
            s "Y-yeah. Trust me. I'm okay."
            mc "If you have a problem, you should really tell me you know."
            show sara normal
            s normal "Umm. I really appreaciate you asking me but really, I'm fine. I promise."
            mc happy "Alright. Just remember that I'm always here if you need anything."
            s "Well... Thanks. That means a lot."
            mc "I'll take my leave. Bye Sara"
            s "Bye Tuah."
            jump continue_investigation

        "Back off and change topic.":
            mc "Fair enough. I didn't mean to pry."
            show sara normal
            s "You're not prying. It's just... hard to explain."
            mc "Got it. By the way, how's the novel you're reading?"
            s "It's really good. It's about a princess that become an assasin and try to juggle her life"
            "After awhile, Tuah says goodbye and take his leave."
            jump continue_investigation

label continue_investigation:
    hide sara normal with dissolve
    mc "I couldn’t shake the feeling that Sara was holding something back."
    mc "Hmmm maybe I read too much into it."
    if chooseZiad == True:
        jump day2
    else:
        jump findziad
        
    