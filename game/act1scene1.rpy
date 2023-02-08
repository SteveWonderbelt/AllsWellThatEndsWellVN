# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define b = Character('Bertram', color="#1E49AD")
define c = Character('Countess', color="#820BDA")
define l = Character('Lafeu', color="#FFC300")
define h = Character('Helena', color="#EE44AD")
define p = Character('Parolles', color="#C3E4F3")
define pa = Character('Page', color="#383729")

# The game starts here.

label act1scene1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene act1scene1castlehall
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    #countess, sad
    show countess neutral at right
    c "Bertram, losing you feels like losing my husband again."

    #Bertram, neutral
    show bertram neutral at left
    b "Yes, I feel the same about leaving, mother...but I must do as the King commands."
    

    #Lafeau, netural at left
    hide bertram neutral at left
    show lafeu at left
    l "The king will be like a husband to you, countess, and as good as a father to you, sir. He's known to be good to all of his subjects. Especially considering who your father was, he is bound to be generous."

    #Countess, neutral
    c "Do we know how likely it is that he'll recover? He's been sick for some time, or so I hear."

    #Lafeu, neutral
    l "It's hard to say, madam..."

    #lafeu, concenred
    l "But I did hear he has turned away his doctors. He's spent a lot of time following their orders, only to find himself losing hope..."

    #Countess, neutral
    c "It reminds me of this young woman here. Her late father..."

    #countess gets choked up at this point, switches to crying
    hide countess neutral at right
    show countess cry at right
    #Bertram, concerned
    hide bertram neutral at left
    show bertram concerned at left
    b "Mother? Are you alright?"

    # Countess, lightly crying
    c "Yes, it's just... " 
    
    # Countess, sad
    hide countess cry at right
    show countess sad at right
    c "Anyway, he was a doctor of considerable skill, and a very good man besides. A miracle worker, truly. If he were still living I don't doubt he could cure the king."

    #Netural
    hide bertram concerned at left
    show lafeu at left
    l "This man, madam, what was his name?"

    #Neutral
    hide countess cry at right
    show countess neutral at right
    c "Oh, he earned every ounce of fame he got, Lafeu. Gerard de Narbon was his name."

    #Sad
    l "Ah, yes, a great man. Just the other day the king was talking about him with admiration and sadness. If knowledge alone could keep a man alive, he'd be with us still."

    #Neutral
    hide lafeu at left
    show bertram neutral at left
    b "This illness the king has, Lafeu, do they know what it is?"

    #Neutral
    hide bertram neutral at left
    show lafeu at left
    l "A fistula, my lord."

    #Neutral
    hide lafeu at left
    show bertram neutral at left
    b "Can't say I've heard of that..."

    #Netural
    hide bertram neutral at left
    show lafeu at left
    l "Don't go spreading that around if you don't mind, my lord. Anyway, this young lady, she's Narbon's daughter, countess?"

    #Neutral
    c "Yes, and his only child, under my care now that her father is gone. She's done very well in school under the circumstances. Good head on her shoulders. Her father taught her to be as honest and good as himself."

    #show Helena crying hysterically
    hide lafeu at left
    show helena at left 
    #concerned
    hide helena at left
    show lafeu at left
    l "I think you've made the poor thing cry, madam"

    #sad
    hide countess neutral at right
    show countess sad at right
    c "Oh, Helena, I'm so sorry. Thinking of your father must be very hard for you right now. Come now, no more. We don't want people thinking you're being performative, do we?"

    #crying
    hide lafeu at left
    show helena at left
    h "I perform only what I feel, madam."

    #Neutral
    hide helena at left
    show lafeu at left
    l "I know it's hard, Helena. But excessive grief does no one any good. We owe our mourning to the dead, but excessive grief is the enemy of the living."

    #sad
    c "If the living is the enemy to grief, too much grief can be lethal."

    #Neutral
    hide lafeu at left
    show bertram neutral at left
    b "Mother, may have your blessing? To leave and attend the king?"

    #Neutral
    hide bertram neutral at left 
    show lafeu at left
    l "What is to be made of that?"
    hide lafeu at left
    show bertram neutral at left

    #Sad
    c "I give you my blessing, Bertram. Follow in your father's footsteps. But please hear this. You will feel your blood and virtue fight within you, but I want you to remember to be good like I've taught you. Love all, trust few, and do right by everyone you meet." 
    
    #Sad
    c "Should you gain power, don't abuse it to win over your enemies, and value your friends as you value your own life. Don't be afraid to speak, but don't speak so much that you make yourself a nuisance." 
    
    #Sad
    c "I hope God sees fit to shower you with many blessings, and that he answers my own prayers."

    #Sad
    c "Farewell now, my lord."

    #Sad
    c "Lafeu, my son is an untrained nobleman yet. Advise him for me, if you please."

    #Neutral
    hide bertram neutral at left
    show lafeu at left
    l "Of course, madam. He'll have only the best advice I can give."

    #Sad
    c "God bless him. Goodbye, Bertram."

    #countess exits
    hide countess sad

    #Neutral
    show bertram neutral at right
    b "I'm hoping for the best for you, Helena. Take care of my mother for me while I'm gone."

    #Neutral
    l "Goodbye, young lady. Remember to maintain your father's reputation."

    # b and l leave
    #Sad
    h "If only that were all...the truth is I'm not thinking of my father. My fake tears do more to honor him than my real ones. It shames me to admit it, but I've forgotten him. The only face I can think of is.."
    #Very sad?
    h "Bertram's..."
    #Sad
    h "I am ruined. Simple as that."
    #Sad
    h "With Bertram gone life is pointless."
    #Sad
    h "Just my luck falling in love with the brightest star in the sky. Admire him all I want, I can never reach him."
    #Dreamy
    h "Until now I've taken comfort in being able to simply bask in his radiance, by just being near him..." 
    #Sad
    h "To love someone so far above me is to see my love die."
    #Sad
    h "The deer that seeks love from the lion must accept death."
    #Dreamy
    h "It was so nice, though agony in a way, to see him all the time, to sit and take in those beautiful eyebrows, those stunning eyes, that lovely skin, to absorb them into my heart."
    #dreamy
    h "I could draw every line and feature of that sweet face by memory alone."
    #dreamy
    h "Not to mention his muscles..."
    #sad
    h "But now he's gone."
    #sad
    h "Now all I can do is hang onto what he's left-" 
    #suprirsed
    h "Wait, who's that?"

    #Parolles enters

    #says this to herself, neutral
    h "Oh he's going away with Bertram. I know Bertram cares for him, so I do as well, but truthfully I think he's a complete liar, fool, and coward. And he probably always will be."
    #thinking
    h "Sometimes it feels like fools like this attain more power than the wise ever do."
    #neutral
    p "Blessings to you, beautiful queen!"
    #amused
    h "And you, monarch!"
    #confused
    p "I'm no monarch."
    #amused
    h "Nor am I."
    #neutral
    p "Thinking of virginity again, aren't you?"
    #neutral
    h "Yes, actually. You're a soldier, right? Man is the enemy of virginity: how can we defend it against him?"
    #neutral
    p "Simple. Keep him out."
    #neutral
    h "Our virginity is too weak to defend against his attacks. You are a great warrior. Share with the court some advice."
    #neutral
    p "There is no resistance, regrettably. Man needs only to sit down in front of you and..."
    #neutral
    p "Well..."
    #neutral
    p "Blow you up."
    #amused
    h "May god bless our poor virginity and defend it from conquerors and blower-uppers, then." 
    #amused
    h "How might virgins blow up men in return?"
    #neutral
    p "Man will quickly be blown down when virginity is blown up."
    #neutral
    p "By blowing him down again, your fortified city has already been lost by the fracture that you yourselves made."
    #neutral
    p "Nature did not intend you to preserve your virginity."
    #neutral
    p "Losing it leads to an increase in population. You can't have virgins without their mothers losing their virginity first. The loss of your virginity can create ten more virgins. "
    #neutral
    p "Keeping your virginity forever would mean there can be no more virgins."
    #neutral
    p "Virginity is a cold friend that is best gotten rid of."
    #amused
    h "I think I'll keep it a while longer. Even if it means I die a virgin."
    #neutral
    p "There's no benefit to that. It's against the laws of nature."
    #neutral
    p "To speak in favor of virginity is to slander your mothers of bad behavior, which is unacceptable disobedience."
    #neutral
    p "A virgin is like a man who commits suicide."
    #neutral
    p "Virginity kills itself and therefore should be buried far outside holy ground, like something that's committed a crime against nature."
    #neutral
    p "Virginity breeds flies like old cheese and, like cheese, becomes moldy, rotting, and eventually dies consuming itself."
    #neutral
    p "Virginity is silly, proud, lazy, and based on self-love, the most forbidden sin."
    #neutral
    p "You gain nothing by keeping your virginity, so get rid of it."
    #neutral
    p "Within ten years, you'll have ten babies, a very respectable increase in value, and the original body won't be much worse off. "
    #neutral
    p "So be gone with it!"
    #amused
    h "Well, how might one lose it to her own liking?"
    #neutral
    p "You'll need to like a man you haven't liked before."
    #neutral
    p "It's something that will only lose its shine as it goes unused. The longer it's kept, the less it's worth. So get rid of it while you can still sell it."
    #neutral
    p "Virginity, like an old nobleman, wears a hat that's completely out of style. It may look nice, but it simply doesn't fit, like the brooch or tooth-pick. Fashionable a few years ago but very much not nowadays."
    #neutral
    p "An old virginity is like an old withered pear, it looks ill and tastes dry."
    #neutral
    p "You can't help but think \"this used to be better, what can I even do with it now?\""
    #amused
    h "I won't give it up just yet I don't think." 
    #sad
    h "Bertram's bound to have a thousand relationships at court, may God protect him. Court is a good place to get an education and he's someone..."
    #sad
    h "..."
    #neutral
    p "He's someone what?"
    #sad
    h "Someone who I wish all the best. It's just a pity that..."
    #neutral
    p "What's a pity?"
    #sad
    h "That wishing someone well is just a thought and not something you can feel. I wish we lower-born people, who only have our dreams for comfort, could go be with our noble friends, and show them how we really feel. But we must keep it to ourselves."

    #page enters
    pa "Monsieur Parolles, my lord calls for you."

    #page exits
    #neutral
    p "Goodbye little Helena. I'll think of you at court."
    #neutral
    p "If I can remember you anyway."
    #amused
    h "Parolles, you were born under a generous star."
    #proud
    p "And under Mars, the God of war."
    #amused
    h "Oh yes, certainly. Especially {i}under{/i} Mars."
    #confused
    p "What do you mean?"
    #amused
    h "Just that you're so occupied by the wars, so you must have been born under Mars."
    #proud
    p "When the star was ascending."
    #amused
    h "When he was descending actually, I suspect."
    #confused
    p "Why?"
    #amused
    h "You have a tendency of running backwards when you fight."
    #neutral
    p "That's strategic. It's to gain advantage."
    #neutral
    h "As is running away, when you're scared so you run to safety. The mixture of bravery and fear has helped you gain an impressively quick run. It suits you."
    #flustered
    p "I'm too busy to answer you fully. When I return I will be the perfect nobleman. Then I'll teach you what I've learned so you can keep up with a nobleman's advice and understand the guidance people give you."
    #neutral
    p "If not, you'll die in your lack of gratitude and be killed by your ignorance."
    #neutral
    p "When you have time, say your prayers. When you don't have time, remember your friends. Find a husband and use him as he uses you. "
    #neutral
    p "Goodbye."

    #Parolles exits
    #thinking
    h "Seems like we often find the solution ourselves, though it seems like heaven sent it to us."
    #thinking
    h "We say God controls us, but we still have free will. Talk of fate can just slow us down and make us too lazy to get what we want."
    #thinking
    h "Who decided to make me love someone so high up above me? Who made me see his beauty but not let me gain his love?"
    #thinking
    h "Just because one person was born high and another born low doesn't mean they can't naturally come together if they're attracted to one another, and then kiss as though they were born equals."
    #thinking
    h "People who think rationally and rigidly about their limits and assume they can't do what others have already done will view certain things as impossible when really they're just difficult."
    #thinking
    h "If a woman successfully shows her merit then she will surely win her love."
    #thinking
    h "The king's disease..."
    #resolute
    h "Maybe I'm misguided, but I've decided what I'm going to do and I will stick to my plan to the end."

  # This ends the game.

    return
