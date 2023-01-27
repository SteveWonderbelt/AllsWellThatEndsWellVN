#Define characters
define c = Character('Countess', color="#820BDA")
define s = Character('Steward', color=" #7b8014")
define cl = Character('Clown', color=" #ea96e0 ")
define h = Character('Helena', color="#EE44AD")

#Scene starts here
label act1scene3:

    scene act1scene1castlehall
    with dissolve

    show countess neutral
    c "I will hear you now, steward. What do you say of this gentlewoman?"

    #Left-Steward, neutral, right-countess
    s "Madam, I hope you'll recall that I've taken much care to make you happy in the past."
    s "It would be immodest and dishonorable of me to announce my past deeds myself."

    c "Wait, why is this rogue here?"

    #Left- Clown, right, Countess

    c "Begone, slave. I don't believe all the compaints about you, though I know you're foolish enough for them to be true and you have it in you to misbehave in the ways they describe."

    cl "As you know, madam, I am a very poor fellow."

    c "Well, sir."

    cl "No, madam, it's not very well that I am poor, though many who are wealthy are also damned."

    cl "But if I have your ladyship's permission to go out into the world, Isbel the servant girl and I will do what we can."

    c "You'll need to beg?"

    cl "I beg of your good will, my lady, in this case."

    c "In what case?"

    cl "In the case of Isbel and I."

    cl "Servants don't usually build up much of an inheritance."

    cl "I don't think I'll ever have God's blessing untl I've had children, for they say children are blessings."

    c "Why do you want to marry?"

    cl "My poor body requires it, madam."

    cl "I am driven by desires of the flesh and I must heed the devil's commands."

    c "Is that your only reason?"

    cl "As it happens I do have better reasons as well, Madam."

    c "Would it please you to share them?"    

    cl "I have been a wicked creature, madam, as you and anyone of flesh and blood have been. And so I want to marry so I can repent."

    c "You'll repent your marraige before you repent your wickedness."

    cl "I am friendless, madam, and I hope to gain friends for my wife's sake."

    c "Such friends are your enemies, foolish man."

    cl "You don't know much about great friends, madam."
    #center-clown, exit countess
    cl "The rogues come to do things for me that I tire of doing for myself."

    cl "He that takes care of my lands and spares my animals from having to do the work leaves me more time to focus on the harvest."

    cl "If he sleeps with my wife, he'll be my slave."

    cl "You see, he that comforts my wife cherishes my flesh and blood."

    cl "He that cherishes my flesh and blood loves my flesh and blood."

    cl "He that love my flesh and blood is my friend."

    cl "And so, he that kisses my wife is my friend."

    cl "Men are never happy with what they are. That's why they get married."

    cl "Young Charbon the Puritan and old Poysam the Papist, though they have different religions, have the same mind."

    cl "They can knock their horns together like a herd of deer."
    #countess_neutral-right, clown_neutral-left
    c "Will you always be so foul-mouthed and dishonest?"

    cl "I'll be a prophet, madam, and I speak the truth this way:"
    #clown_singing-center
    cl "{i} For I will balad will repeat \n Which men full true shall find \n Your marriage comes by destiny, \n Your cuckoo sings by kind.{/i}"
    #clown_netural-left, countess_neutral-right
    c "Leave, sir."
    c "We'll talk more later."
    #steard_netural-left, countess_neutral-right
    s "If it pleases you, madam, he should tell Helena to come to you. She's the one I need to talk to you about."

    c "Sir, tell my gentlewoman, Helena, that I want to speak with her."
    #clown_singing-center
    cl "{i}Was this fair face the cause, quoth she, \n Why the Grecians sacked Troy? \n Fond done, done fond,\n Was this King Priam's joy? \n With that she sighed as she stood, \n With that she sighed as she stood, \n And gave this sentence then;\n Among nine bad if one be good, \n Among nine bad if one be good, \n There's yet one good in ten. {/i}"

    #clown_neutral-left, countess_neutral-right
    c "One good in ten?"
    c "You've corrupted the song, sir."

    cl "One good woman in ten, madam. This purifies the song."

    cl "If only God would serve the world as I've served the song all year!"

    cl "We'd find nothing bad about the one woman in ten if I were the priest."

    cl "One in ten, I sing!"

    cl "It would help our chances if we could find a good woman once every comet or during an earthquake."

    cl "A man could tear his heart out before finding a good woman."
    #countess_annoyed_right
    c "I command you to leave, rogue."

    cl "Imagine, a woman commanding men and no harm is done by it."

    cl "My character is such that I don't have strict morals, but it will do no harm."

    cl "Like a secret puritan I shall wear my anglican robes over my black gown that shoes my true colors."

    cl "I will now leave and summon Helena here."

    #countess_neutral_right steward_neutral_left
    c "Now, then."

    s "I know that you love Helena, madam."

    c "Yes, I do. Her father left her here in my care and she deserves as much love as she can find, wherever she can find it."

    c "She's owed more than she's paid and she'll be paid more than she'd ever demand."

    s "I was recently nearer to her than I think perhaps she wanted me to be, madam."

    s "She was alone, and speaking to herself seemingly."

    s "I assume she thought that no one else could hear her."

    s "She was talking about how she loves your son, madam."

    s "She said Fortune was no goddess, as she'd put them in such different stations in life."

    s "Love could not be divine if it wouldn't bless the union of two people, regardless of social status."

    s "Diana was no queen of virgins if she'd allow her poor servant to be captured by love without a way to be saved from her passions or to earn her love later."

    s "I've never heard a young maiden speak with such bitter sorrow."

    s "I thought it my duty to share this with you quickly, madam, as I fear much grief may follow. I felt it important for you to know."

    c "You've done your duty, sir, but keep this to yourself."

    c "I've suspected this many times before, but I couldn't be certain enough to believe it nor doubt it."

    c "Leave me, please."

    c "Keep this in your heart and I again thank you for your honest service. We will speak further later."

    #countess_neutral_center
    c "This reminds me of when I was young."

    c "These things are only natural. The thorns of love accompany our rose of youth."

    c "Our blood gives into these passions."

    c "In fact, when a youth experiences love's strong passions, we know nature is running its course."

    c "We remember these as our mistakes, though they didn't seem that way at the time."
    #play footsteps/door open here
    c "Oh, here's Helena now."

    c "I can see lovesickness all over her."

    #helena_neutral_left, countess_concerned_right
    h "You summoned me, madam?"

    c "You know I consider myself a mother to you, Helena."
    #Helena-shocked, suprirsed, afraid
    h "My most honorable mistress."

    c "No, a real mother, I mean, Helena."

    c "Why not a mother?"
    #Helena worried, anxious
    c "You looked like you'd seen a snake when I said \"mother\". What's in \"mother\" that startles you so?"

    c "I say, I am your mother and I count you among the children that I gave birth to."

    c "Adopted children often grow to feel as close to us as biologogical children."

    c "The family we choose can feel just as familiar the family we're born with."

    c "You never put me through labor pains but I can still have a mother's love for you. And I do, Helena."
    #Helena fearful again, crying slightly
    #Countess, irritated, frustrated
    c "For God's sake, young lady!"

    c "Does it really boil your blood to hear me say I am your mother?"
    c "What's so wrong that Iris of the rain clouds brings tears to your eyes?"
    c "Why does being my daughter stir such a reaction in you?"


    h "Because I am not your daughter."
    c "I say, I am your mother."

    h "I'm sorry, madam, but...."
    h "The Count Rousillon cannot be my brother."
    h "I am of humble origins, he from a very honorable family."
    h "My parents are of no notability and his are nobles."
    h "He is my master and my dear lord."
    h "I lives as his servant and will die his subject."
    h "He must not be my brother."

    #countess returns to netural
    c "And I must not be your mother?"
    #Helena, not crying but still anxious
    h "You are my mother, madam. Or..."
    h "Well I wish you were."
    h "If only that didn't mean my lord your son were my brother, I would indeed love to be your daughter."
    h "I'd rather die than you be both of our mothers, for then I'd be his sister."
    h "Is there no way I could be your daughter without him being my brother?"

    c "Of course, Helena."
    c "Be my daughter-in-law."
    #Helena, shocked, pale
    c "God save you from meaning what you said."
    c "\"Daughter\" and \"mother\" make your heart race."
    c "Why do you turn so pale?"
    c "My fear has caught your fondness. This is the root of your loneliness."
    c "Now I see where your tears come from."
    c "It's clear to me that you love Bertram, Helena."
    c "Don't try to deny it, it's written all over your face."
    c "Now, tell me the truth."
    c "Your cheeck's blushing serves as a confession and your eyes are practically shouting it."
    c "Stubborness is sinful, Helena. Only that and your frustration at being discovered keeps you from speaking."
    c "Speak up. Is it true?"
    c "If it is, you've made quite the tangle of things."
    c "If it isn't, then swear it."
    c "Either way, I command you, as God may help me fight for you, tell the truth."

    h "Forgive me, good madam!"
    c "Do you love my son?"
    h "Good madam, please forgive me."
    c "Do you love my son, Helena?"
    h "Don't you love him, madam?"

    c "Don't play games with me, Helena."
    c "My love for you is strong and everyone recognizes it."
    c "Come, tell me of your affections. Your passions have already given you away."
    #maybe a pause here?
    #Helena, on her knees, center
    h "My lady I confess, on my knee, before God and you."
    h "First to you, and then to God."
    h "I do love your son."
    h "Before I came here my friends were poor but honest. Such is my love."
    h "Don't take offense, for he is not harmed to be loved by me."
    h "I don't follow him around claiming anything about him and I wouldn't want to be with him until I'm worthy of him."
    h "Not that I know how I'd ever be worthy of him."
    h "I love him in vain. I am hopeless."
    h "I pour my love like water into a strainer, hoping to catch it, but it evades me."
    h "Like a pagan, I worship the sun while it looks down on me not even knowing I exist."
    h "Please, mada, don't hate me for loving the son you love."
    h "If you- whose honor in older age suggets that you were a virtuous young woman, ever loved chastely and passionately like me, so that Diana of charity and Venus of love were as merged into one-"
    h "Have pity on this girl who could not choose but to give her love to someone who could never return it."
    h "For she is one who will not seek to pursue her love but will keep it, sweetly and secretly, until her death."
    #countess, center, neutral
    c "Did you not recently have a plan? Something about going to paris?"
    c  "Speak truly now, Helena"
    #helena_anxious_left, countess_neutral_right
    h "I did, Madam."
    c "And why was that? The truth now."
    h "I will tell the truth, I swear."
    h "You know that my father left me some rare medicines? He'd collected them because in his experience they were powerful and very useful."
    h "Before he died he taught me about how they could do more than many thought."
    h "So he left them to me for safe-keeping and use."
    h "Among these medicines is one that will cure the terrible sickness that has afflicted the king."
    c "And this was your reason to go to Paris?"
    h "Your son, my lord, gave me the idea. If he hadn't..."
    h "...Paris, the medciine, the king..." 
    h "None of it would have crossed my mind."
    c "Helena, do you think the king would accept your help if you were to offer it?"
    c "He and his physicians are in agreement. He doesn't think they can help him and they thinks he can't be helped."
    c "Don't take this the wrong way, but why would they trust a poor, uneducated maiden when the best doctors have left the sickness to do what it will?"
    h "My hope was that, besides my father's renowned skills, his reputation might bring me good fortune."
    h "And, if your ladyship would give me the chance to attempt success, I'd wager my life on his grace being cured down to the day and hour."
    c "Do you realy believe this, Helena?"
    h "Yes, madam. Absolutely."
    c "Then you have my permission and love."
    #Helena, surprised
    c "I'll provide you everything you need to travel and servants to wait on you."
    c "Send my greetings to my friends at court, please."
    c "I will stay here and pray for your efforts to succeed."
    c "You will leave tomorrow."
    c "And please remember: I shall help you in any way I can."
