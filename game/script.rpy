# This is the codes for the first day of this VN. There are multiple days split across different files.
# All codes about characters, names, fonts, ects goes to the characters.rpy 
# The code starts here.

# MentalHP variable to determine which ending you'll get at the end.
default MentalHP = 0
default tellAidil = False
default chooseSara = False
default chooseZiad = False

label start:
    
    #Stops the main menu music
    stop music fadeout 2.0
    
    #Inline text references
    # {w}  -  pauses the dialogue and requiring click to continue. (Alternatively use extend for a new line)
    # {cps=10}INSERT TEXT HERE{/cps}  -  Change typing speed.
    # {color=#f00}Red{/color}  -  changes text colors
    # {b}{/b} for bold

    #centered "{color=#ffff}{cps=10}21th April{/cps}{/color}"
    #play sound "Transition.mp3" volume 0.5
    
    play music "bgm2.mp3" volume 2 fadein 1.0 fadeout 1.0
    # Starts the scene at Classroom.
    scene classroom with fade
    #show aidil with dissolve #Make sure it is lowercase even if the original image file has uppercase letters.

    
    "On an ordinary morning, the classroom buzzed with the usual chatter and laughter."
    mc sad "Ahh, Morning school time. " 
    extend "I hate it. {w}Ugh, so many assignments."
    "Tuah sit down on his spot"
    "As Tuah pulled out his notebook, {w}something fell off from his bag."
    mc normal "Huh? What's this?"
    mc "A folded piece of paper? {w}A letter? {w}I never remember having this in my bag..."
    "Tuah unfolds the letter..."
    mc "Ah so it IS a letter"
    "Dear Tuah, one of your classmates is struggling more than you could ever imagine. They're in pain, but they've hidden it so well that no one sees it, not even you."
    "If you don't act soon, something might happened. I don't expect you to believe me right away, but I ask you to try. Please, look around. Notice the signs."
    "You can make a difference. You have until the end of the week to help them. Please don't ignore this."
    mc "What the? Is this a prank?{w} So weird. This must be a joke."
    mc "But… {w}this letter feels off, especially the last part. {w}Please don't ignore this? {w}Almost sounds desperate."
    mc happy "I can make a difference, huh?" 
    mc "Oh well, what's the harm in looking into it? Worst case scenario, it's just a prank, and I'll get to laugh at whoever wrote it later.{w} Best case, I could finally be the hero."
    "Tuah then spends most of his class session thinking of any possible person."

    scene cafeteria with fade
    "Tuah stumble upon Aidil in the Cafeteria."
    show aidil at center with dissolve
    a "Yo Tuah, over here!"
    mc happy "Oh Aidil, thanks for saving me the seat."
    show aidil 2
    a "No problemo, I'm your guy after all."
    show aidil 
    mc "How do you get to cafeteria so early?"
    a "The key is to exit right before the class ends. {w}Just ask permission to go to the toilet like around 11 minutes before the class ends. {w}It always works. {w}Heh."
    mc "Somehow, I feel like I could trust you on that."
    mc sad "......"
    a "What's with your face, is the fried rice that bad? I mean, me personally would never eat that."
    mc normal "No, it's just…something on my mind."
    show aidil 2
    a "Well, you can just lay it on me. Disclaimer, I would charge RM5 per hour, Now, tell Dr. Aidil, what's bothering your mind? Love story?"
    mc happy "Haha, you with your jokes."
    mc normal "{i}Should I tell him about the letter? Kinda not wanting to bother him. Wonder what his reaction would be{/i}"

    menu:

        "Tell Aidil about the letter":
            $ tellAidil = True
            mc "Anyway, do you know anyone that with a problem."
            a "Someone with a problem? {w}Well, you could say everyone has their own problem."
            a "You have your own problem, I have my own problem, even the snarky Miss Alissa has her own problem. It's either it's a big problem or a small problem."
            mc "You're not wrong to be fair."
            mc "Alright fine, I got this weird letter today."
            "Tuah explain everything about the letter"
            a "Weird, sounds like melodramatic social experiment. Maybe look around? {w}Perhaps there's some sort of hidden camera in the corner of the room."
            mc "Yeah, but it does feels… real you know. {w}Like maybe there is someone asking for help."
            a "Maybe this is the time you become a hero."
            mc "How do you read my mind?"
            show aidil 2 
            a "I'm your best friend. I know everything that you think. {w}Either way, goodluck on finding that person. {w}Not everyone is good at asking for help."
            show aidil 
            mc "So you're saying writing a letter to me is a way of asking for help?"
            a "You could say that."
            mc "Any idea who?"
            a "Hmmm... {w}Not really. {w}I mean, you can't actually just know someone's problem just by looking at them."
            mc "Yeah make sense."
            jump continue

        "Keep about the letter to yourself":
            mc "Nevermind. {w}It's just thinking some random stuff."
            a "Wow, being secretive now huh? What are you now? Agent OO7?"
            show aidil thinking
            a "Is it about the homework?"
            mc "Not that."
            show aidil 
            a "Oh, maybe it's some new crush, huh? Who is it?"
            mc "Stop that, no. {w}I haven't even move on from my ex."
            a "What?! HAHAHA! Okay, okay. I'll stop prying. {w}But seriously, don't stress too much, bro. {w}Life's short—gotta enjoy it while we can."
            jump continue
            
    return



label continue:
    mc "Oh yeah, I haven't return your hoodie yet. Follow me back home after school, I'll give it to you later."
    a "Nah, just take it. It's yours."
    mc "What? But I thought it's your favourite hoodie."
    show aidil 2
    a "It's okay. Just treat it as your birthday gift, I haven't gift anything yet right?"
    show aidil 
    mc "Well if you say so..."
    "Tuah excuses himself to find people that may have sent the letter."
    mc "{i}Hmm, so who should I check on to?{/i}"
    mc "{i}There's two people that I think maybe the one who have a problem. It's either Sara or Ziad.{/i}"
    mc "{i}I've always seen Sara sitting alone and Ziad always looked stressed out."
    mc "{i}Hmmm... {w}I wonder... {w}Which one should I approach first?"
    menu day1choice:

        "Find Sara":
            $ chooseSara = True
            jump findsara

        "Find Ziad":
            $ chooseZiad = True
            jump findziad



label main_menu:
    # Fade in the music when the menu starts
    $ renpy.music.play(config.main_menu_music, loop=True, fadein=2.0, fadeout=2.0)
    
    # Show the default main menu
    $ renpy.pause(0.5)  # Small pause before showing the menu, just for smoothness

    call screen main_menu 