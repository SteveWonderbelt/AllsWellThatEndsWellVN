#countess neutral image
image countess neutral:
    "countess_neutral"
    pause 5.0
    "countess_neutral_blink" with Dissolve(0.3)
    pause 0.3
    "countess_neutral" with Dissolve(0.3)
    pause 0.3
    repeat 

#countess sad image
image countess sad:
    "countess_sad"
    pause 5.0
    "countess_sad_blink" with Dissolve(0.3)
    pause 0.3
    "countess_sad" with Dissolve(0.3)
    pause 0.3
    repeat

#countess crying image
image countess cry:
    "countess_tears"

#Bertram neutral image
image bertram neutral:
    "bertram_neutral"
    pause 5.0
    "bertram_neutral_blink" with Dissolve(0.3)
    pause 0.3
    "bertram_neutral" with Dissolve(0.3)
    pause 0.3
    repeat

#Bertram concerned image
image bertram concerned:
    "bertram_concerned"
    pause 5.0
    "bertram_concerned_blink" with Dissolve(0.3)
    pause 0.3
    "bertram_concerned" with Dissolve(0.3)
    pause 0.3
    repeat

image lafeu = Placeholder("boy")
image helena = Placeholder("girl")