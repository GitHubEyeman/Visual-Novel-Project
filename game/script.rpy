# This is the codes for the first day of this VN. There are multiple days split across different files.
# All codes about characters, names, fonts, ects goes to the characters.rpy 
# The code starts here.

# MentalHP variable to determine which ending you'll get at the end.
default MentalHP = 0
default helpAidil = False
label start:

    # Intro scene

    #scene bg rain_rooftop
    #play music "rain.mp3" fadein 0.3 fadeout 0.3
    #"My mind kept going back to that day."
    #"And I kept wondering..."
    #"How things would've turn out if I had done things differently."
    #stop music fadeout 1.0
    #scene black with fade
    
    centered "{cps=10}21th April 2099{/cps}"
    play sound "Transition.mp3" volume 1.5
    #centered "{cps=100}3 Days remaining{/cps}" with fade


    # The First scene at a cafe.
    scene classroom with fade
    #show aidil with dissolve #Make sure it is lowercase even if the original image file has uppercase letters.

    #a "Hi, stuff happened and-"
    "On a ordinary Wednesday morning, the classroom buzzed with the usual chatter and laughter"
    mc sad "Ahh, Morning school time. I hate it. Ugh, so many assignments."
    #show aidil with dissolve
    "Tuah sit down on his spot"
    "As Tuah pulled his notebook from his bag, something fall from his bag"
    mc normal "Huh? What is this?"
    mc "A folded piece of paper? A letter? I never remember having this"
    "Tuah unfolded the letter"
    mc "Ah so it IS a letter"
    "Dear Tuah, one of your classmates is struggling—more than you could ever imagine. They're in pain, but they've hidden it so well that no one sees it, not even you."
    "If you don't act soon, something might happened. I don't expect you to believe me right away, but I ask you to try. Please, look around. Notice the signs."
    "You can make a difference. You have until the end of the week to help them. Please don't ignore this"
    mc "What the? Is this a prank? So weird. This must be a joke."
    mc "But…this letter feels off, especially the last part. Please don't ignore this? Almost desperate."
    mc happy "I can make a difference huh? What's the harm in looking into it? Worst case, it's just a prank, and I'll get to laugh at whoever wrote it later. Best case, I could finally be the hero"
    "Tuah spend his class session thinking of any possible person"

    scene cafeteria with fade
    "Tuah stumble upon Aidil in the Cafeteria"
    show aidil at right with dissolve
    a "Yo Tuah, over here"
    mc happy "Oh Aidil, thanks for saving me the seat."
    a "No problemo, I'm your guy after all."
    mc "How do you get to cafeteria so early?"
    a "The key is to exit class before the class end. Just ask to go to toilet like 11 minutes before class end. Always work"
    mc "Somehow I trust you"
    mc sad "......"
    a "What's with your face, is the fried rice that bad? I mean, me personally would never eat that"
    mc normal "No, it's just…something on my mind"
    a "Well, you can just lay it on me. Disclaimer, I would charge RM5 per hour, Now, tell Dr. Aidil, what's bothering your mind? Love story?"
    mc happy "Haha, you with your jokes."
    mc normal "{i}Should I tell him about the letter? Kinda not wanting to bother him. Wonder what his reaction would be{/i}"

    menu:

        "Tell Aidil about the letter":
            $ helpAidil = True
            mc "Anyway, do you know anyone that with a problem."
            a "Someone with a problem? Well, you could say everyone has their own problem."
            a "You have your own problem, I have my own problem, even the snarky Miss Alissa has her own problem. It's either it's a big problem or a small problem."
            mc "You're not wrong to be fair"
            mc "Alright fine, I got this weird letter today"
            "Tuah explain everything about the letter"
            a "Weird, sounds like melodramatic social experiment. Maybe look around, maybe there's some hidden camera."
            mc "Yeah, but it feels…real you know. Like maybe there is someone asking for help"
            a "Maybe this is the time you become a hero."
            mc "How do you read my mind?"
            a "I'm your best friend. I know everything that you think. Either way. Goodluck on finding that person. Not everyone is good at asking for help."
            mc "So you're saying writing a letter to me is a way of asking for help?"
            a "You could say that."
            mc "Any idea who?"
            a "Hmmm. No actually. I mean you can't actually just know someone's problem just by looking at them."
            mc "Yeah make sense"
            jump continue

        "Keep about the letter to yourself":
            mc "Nevermind. It's just random stuff."
            a "Wow, being secretive now huh? What are you now? Agent OO7?"
            a "Is it about the homework?"
            mc "Not that"
            a "Oh, maybe it's some new crush huh? Who is it?"
            mc "Stop that, no. I haven't even move on from my ex."
            a "What?! HAHAHA. Okay, okay. I'll stop prying. But seriously, don't stress too much, bro. Life's short—gotta enjoy it while we can."
            jump continue
            
            
    return

    #menu:

        #"Help":
            #$ MentalHP += 1
            #jump day2

        #"Don't help":
            #$ MentalHP -= 1
            #jump day2

    #return

label continue:
    mc "Oh yeah, I haven't return your hoodie yet. Follow me back home, I'll give it to you later."
    a "Nah, just take it. It's yours"
    mc "What? But I thought it's your favourite hoodie."
    a "It's okay. Just treat it as your birthday gift, I haven't gift anything yet right?"
    mc "Well if you say so"
    "Tuah excuse himself to find people that may have sent the letter"
    mc "{i}Hmm, so who should I check on to?{/i}"
    
    menu day1choice:

        "Find Sara":
            scene library with fade
            "The library was quieter than usual, with only a few students scattered among the shelves."
            "Sara sat at a corner table by the window, a stack of books next to her and her nose buried in one."
            mc happy "Maybe Sara’s the one who need help. She always alone pretty much all the time. Maybe she’s suffering in silent and don’t know who to tell. And of course she chooses me to tell about her problem. Hehe"
            show sara at right with dissolve
            mc "Hey Sara. Got a moment?"
            s "AH! Oh Tuah, you surprise me. Uh yeah, I do. What is it?"

        "Find Ziad":
            "Blabla"