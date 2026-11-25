import os
import time
import questionary
from questionary import Choice
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
console = Console()

ambition = 0 #character traits and influence on game
caution = 0
confidence = 0
andrea_trust = 0 #character relationships and influence
gabriele_trust = 0
lucia_trust = 0
beatrice_interest = 0
suspicion = 0

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def type_text(text, style="", delay=0.07):
    for char in text:
        console.print(char, style=style, end="")
        time.sleep(delay)
    console.print()

def dialogue(character, text):
    console.print(f"[bold]{character}:[/bold] ", end="")
    type_text(text, style="bold")
    console.print()

def narration(text):
        console.print(f"[italic dim]{text}[/italic dim]")
        if len(text)>70:
            time.sleep(2.2)
        else:
            time.sleep(1.5)

def show_choice(prompt, options):
    return questionary.select(prompt, options).ask()

def memory_note(character, duration=2.0):
    note = f" ◈ {character} will remember this."
    console.print(f"[italic yellow]{note}[/italic yellow]", end="")
    time.sleep(duration)
    console.print()

clear()
title_card = (
    "\n✦  𝕿𝖍𝖊 𝕻𝖆𝖎𝖓𝖙𝖊𝖉 𝕿𝖗𝖆𝖎𝖙𝖔𝖗𝖘  ✦\n"
    "──────────────────────────────────────\n"
    "[dim][ Press ENTER to Start ][/dim]\n"
)
console.print(Align.center(title_card))
input()
clear()

console.print("\n[bold]Chapter I - The Commission[/bold]")
console.print("Florence 12 April 1478")
console.print("[bold]Scene I - The Workshop[/bold]")

narration("\nMorning light enters Master Andrea's workshop. "
    "Tommaso is preparing a wooden panel while Andrea "
    "inspects his work.")

dialogue("ANDREA", "You're pressing too hard. Be patient, Tommaso.")
dialogue("TOMMASO", "I thought you wanted it finished today.")
dialogue("ANDREA", "Finished, yes. Ruined, no.")
narration("Andrea examines the panel.")
dialogue("ANDREA", "Your father was better at this. He understood the value of patience.")
narration("A knock interrupts them. A well-dressed woman enters.")
dialogue("ANDREA", "Madonna Beatrice, what a pleasure!")
dialogue("BEATRICE", "Master Andrea, I need a painting for my household chapel. A Madonna and Child, can you undertake it?")
dialogue("ANDREA", "Of course.")
narration("Beatrice notices Tommaso.")
dialogue("BEATRICE", "And who is this?")
dialogue("ANDREA", "My apprentice, Tommaso.")
dialogue("BEATRICE", "How long have you been learning?")
dialogue("TOMMASO", "Nine years, Madonna.")
dialogue("BEATRICE", "Then I shall see what you can do.")
answer = show_choice(
    "Madonna Beatrice is watching closely. How do you respond?",
    [
        questionary.Choice(
            title = "I still have much to learn, Madonna. My master has taught me well.", 
            value = "humble"
        ),
        questionary.Choice(
            title = "I have some of my own studies, if you'd care to see them.",
            value = "ambitious"
        ),
        questionary.Choice(
            title = [("italic fg:#888888", "Tommaso looks towards Andrea, waiting for his approval.")],
            value = "shy"
        )
    ]
)

if answer == "humble":
    dialogue("BEATRICE", "Modesty is a virtue. Though I hope you have something more than modesty to offer.")
    caution+=1
    andrea_trust += 1
    beatrice_interest+=1

elif answer == "ambitious":
    dialogue("BEATRICE", "Good. I appreciate a young man who takes pride in his work.")
    ambition+=1
    confidence+=1
    andrea_trust-=1
    beatrice_interest+=2
    memory_note("Andrea")
    narration("Andrea scowls at Tommaso")
    

elif answer == "shy":
    caution+=1
    andrea_trust +=2
    dialogue("ANDREA", "He has some promising studies, Madonna. Though he still has much to learn.")
    narration("Beatrice nods, apparently satisfied.")

console.print("[bold]Scene II - The Yard[/bold]")
narration("Late afternoon. In the small yard behind the workshop, Gabriele grinds azurite against a stone slab.")
dialogue("GABRIELE", "So, Madonna Beatrice was watching you rather closely.")
dialogue("TOMMASO", "She was watching the painting.")
dialogue("GABRIELE", "Naturally, and Andrea looked delighted.")
dialogue("TOMMASO", "Andrea rarely looks delighted.")
dialogue("GABRIELE", "Not when you're involved anyway.")
narration("Gabriele laughs and returns to grinding the pigment.")
narration("Tommaso notices a new leather purse hanging from his belt. It looks considerably better than anything Gabriele usually owns.")
dialogue("TOMMASO", "That's new.")
dialogue("GABRIELE", "What is?")
dialogue("TOMMASO", "The purse.")
dialogue("GABRIELE", "Ah. A little work on the side. Nothing extraordinary.")
dialogue("TOMMASO", "What kind of work?")
dialogue("GABRIELE", "A drawing for a gentleman's man. He needed a quick hand, and I needed the money.")
narration("He pats the purse.")
dialogue("GABRIELE", "Four florins. Not bad for an afternoon, eh?")
answer = show_choice(
    "How do you respond?",
    [
        Choice(
            title = "A gentleman's man? Who was he?",
            value = "cautious"
        ),
        Choice(
            title = "Good. You deserve some luck for once.",
            value = "encouraging"
        ),
        Choice(
            title = "Four florins? You're becoming a wealthy man.",
            value = "confident"
        )
    ]
)
if answer == "cautious":
    dialogue("GABRIELE", "Must I know a man's entire family before accepting his money?")
    dialogue("TOMMASO", "I was only asking.")
    narration("Gabriele returns to his work, a little less cheerful than before.")
    caution+=1
    gabriele_trust-=1
elif answer == "encouraging":
    dialogue("GABRIELE", "Finally, someone who appreciates honest work.")
    dialogue("TOMMASO", "I wouldn't go that far.")
    dialogue("GABRIELE", "Careful. I might start charging you for compliments.")
    narration("He knocks his shoulder against Tommaso's.")
    gabriele_trust+=1
elif answer == "confident":
    dialogue("GABRIELE", "Wealthy? Give me another four and perhaps I'll consider it.")
    narration("He laughs and puts the purse away.")
    dialogue("GABRIELE", "One day, Tommaso. One day I'll have a workshop of my own.")
    confidence+=1
    
console.print("[bold]Scene III - Two Rooms Near Santa Croce[/bold]")
narration("The rooms Tommaso shares with his sister are modest, with little furniture beyond a table, two chairs and a narrow bed.")
narration("Lucia sits by the window, mending a sleeve. A small candle illuminates her work.")
dialogue("LUCIA", "You're late.")
dialogue("TOMMASO", "Andrea kept us working.")
dialogue("LUCIA", "Andrea always keeps you working.")
narration("She puts the needle down.")
dialogue("LUCIA", "I heard Madonna Beatrice visited the workshop today. Did you manage to impress her?")
dialogue("TOMMASO", "I don't know.")
dialogue("LUCIA", "You never know anything.")
narration("She smiles and returns to her sewing.")
dialogue("LUCIA", "The house where I work has been busy. More visitors than usual. The steward has been running about all day, and apparently the master has been entertaining some important guests.")
dialogue("TOMMASO", "Important people?")
dialogue("LUCIA", "Wealthy people, at least. That's usually close enough.")
dialogue("TOMMASO", "Who was visiting?")
dialogue("LUCIA", "I don't concern myself with names. I have enough work as it is.")
narration("She pauses again.")
dialogue("LUCIA", "Besides, I hear enough about the Medici and the Pazzi without ever meeting either family. The servants seem to have an opinion about everything.")
dialogue("TOMMASO", "Best not to get involved with such people.")
dialogue("LUCIA", "I sew their clothes, Tommaso. I hardly think that makes me involved.")
answer = show_choice(
    "What do you tell her?",
    [
        Choice(
            title = "You should find another household. I don't trust those people.",
            value = "precautious"
        ),
        Choice(
            title = "I suppose you hear more than you let on.",
            value="friendly"
        ),
        Choice(
            title = "Their quarrels are none of our concern. We have enough to worry about.",
            value = "cautious"
        )
    ]
)

if answer == "precautious":
    narration("Lucia puts the sleeve down.")
    dialogue("LUCIA", "And where would you have me work instead?")
    dialogue("TOMMASO", "I'll find something.")
    dialogue("LUCIA", "Sure, you'd do. I can look after myself, you know?")
    narration("She picks up the needle again, somewhat irritated.")
    caution+=1
    lucia_trust-=1
    memory_note("Lucia")
elif answer == "friendly":
    dialogue("LUCIA", "Perhaps. People talk rather freely when they think nobody is listening.")
    dialogue("TOMMASO", "And you listen?")
    dialogue("LUCIA", "Someone has to. You certainly don't say much.")
    narration("She laughs softly.")
    lucia_trust+=1
elif answer == "cautious":
    dialogue("Lucia", "Perhaps you're right.")
    narration("She returns to her sewing.")
    caution+=1

console.print("[bold]The next day[/bold]")
narration("The following morning, Tommaso arrives at the workshop to find Andrea reading a small letter.")
dialogue("ANDREA", "Madonna Beatrice has sent word. She wishes you to return to her house on the fourteenth. Apparently, she has another task for you.")
dialogue("TOMMASO","Has she said what it is?")
dialogue("ANDREA", "No.")
narration("Andrea folds the letter and puts it away. He returns to his painting.")
time.sleep(0.7)
narration("Tommaso looks towards the unfinished panel.")
dialogue("TOMMASO", "Two days then.")
console.print("[bold]End of Chapter I[/bold]")
console.print()
time.sleep(0.7)
console.print("[bold]Chapter II - The Drawing[/bold]")
console.print("Florence 14 April 1478")
console.print("[bold]Scene IV - The Chapel[/bold]")
narration("Tommaso arrives at Beatrice's house carrying a small wooden case of drawing materials. The steward leads him through the courtyard, past a fountain and into a modest chapel.")
dialogue("TOMMASO", "Madonna Beatrice, you asked for me?")
dialogue("BEATRICE", "I did. Come look at this.")
narration("She gestures towards a painting near the altar. It depicts the Madonna holding the infant Christ. The figures are beautifully arranged, though their expressions are somewhat lifeless.")
dialogue("BEATRICE", "What do you think?")
narration("Tommaso studies it carefully.")
dialogue("TOMMASO", "It's very well executed.")
dialogue("BEATRICE", "That's not quite what I asked.")
dialogue("TOMMASO", "The figures seem distant. As if they're looking at something beyond us.")
dialogue("BEATRICE", "Interesting, you noticed.")
narration("She approaches the table and takes a sheet of parchment.")
dialogue("BEATRICE", "I have commissioned your master to paint something similar. A Madonna and Child for this chapel. But I wonder whether there is room for something a little different.")
narration("She hands him the parchment.")
dialogue("BEATRICE", "Draw me a face. Not a finished painting. Just something of your own.")
answer=show_choice(
    "What do you draw?",
    [
        Choice(
            title="A serene Madonna, much like the one in the painting.",
            value="talented"
        ),
        Choice(
            title = "A Madonna with a more human expression, gentle but weary.",
            value="confident"
        ),
        Choice(
            title="A Madonna whose gaze is directed towards the viewer, almost challenging them.",
            value="ambitious"
        )
    ]
)
if answer == "talented":
    narration("Tommaso draws carefully, paying attention to proportion and expression.")
    dialogue("BEATRICE", "A familiar choice.")
    dialogue("TOMMASO", "I thought it appropriate for a chapel.")
    caution+=1
    andrea_trust+=1

elif answer=="confident":
    narration("Tommaso works slowly, allowing the imperfections of the face to remain.")
    dialogue("BEATRICE", "She looks almost as though she has lived a life.")
    dialogue("TOMMASO", "Perhaps that is what makes her worth looking at.")
    narration("Beatrice studies the drawing for a moment before placing it beside her.")
    memory_note("Beatrice")
    confidence+=1
    beatrice_interest+=1

elif answer == "ambitious":
    narration("The drawing is unconventional. Her expression is neither entirely peaceful nor sorrowful.")
    dialogue("BEATRICE", "You have given her quite a commanding presence.")
    dialogue("TOMMASO", "I thought she ought to be more than an ornament.")
    dialogue("BEATRICE", "I see.")
    memory_note("Beatrice")
    ambition+=1
    beatrice_interest+=1

dialogue("BEATRICE", "Your master has a good eye. Though I suspect you have one of your own.")
narration("She walks towards the chapel entrance.")
dialogue("BEATRICE", "That will be all for today. Tell Andrea I shall expect the panel soon.")
console.print("[bold]Scene V - The Commission[/bold]")
narration("Late afternoon. The workshop is unusually quiet.")
dialogue("ANDREA", "How was Madonna Beatrice?")
dialogue("TOMMASO", "She asked me to draw something.")
dialogue("ANDREA", "And what did you draw?")
dialogue("TOMMASO", "A face.")
dialogue("ANDREA", "That much I gathered. Did she mention anything about the commission?")
dialogue("TOMMASO", "She expects the panel soon.")
dialogue("ANDREA", "Then we had better not disappoint her.")
narration("He speaks again.")
dialogue("ANDREA", "There is something you ought to understand. A patron may admire your work today and forget your name tomorrow. Do not mistake their attention for friendship.")
answer=show_choice(
    "How do you respond?",
    [
        Choice(
            title="I understand, Master. I have much to learn.",
            value="humble"
        ),
        Choice(
            title="Perhaps. But without patrons, there would be little work for painters.",
            value="ambitious"
        ),
        Choice(
            title="I thought you wanted me to make something of myself.",
            value = "confidence"
        )
    ]
)
if answer == "humble":
    dialogue("ANDREA", "You do good to remember that. Now, prepare the pigments, we have work to do.")
    andrea_trust+=1
elif answer == "ambitious":
    dialogue("ANDREA", "You are not wrong. But there is a difference between earning a living and seeking approval.")
    narration("Andrea turns back to the panel.")
    ambition+=1
elif answer == "confidence":
    dialogue("ANDREA", "I do. But I would rather you became a good painter than a man who spends his life chasing the favour of others.")
    confidence+=1

narration("Suddenly, Gabriele enters carrying a rolled sheet of parchment.")
dialogue("GABRIELE", "Well, I've had a productive afternoon.")
dialogue("ANDREA", "Have you? Then perhaps you can be productive enough to finish grinding that pigment.")
dialogue("GABRIELE", "Always a pleasure, Master.")
narration("Gabriele places the parchment on the bench and begins unrolling it.")
dialogue("TOMMASO", "Another commission?")
dialogue("GABRIELE", "Something of the sort.")
dialogue("ANDREA", "What is this?")
dialogue("GABRIELE", "A study of the cathedral. A man wanted it for a glass-painter.")
narration("The drawing shows the interior of Santa Maria del Fiore.")
dialogue("ANDREA", "Not bad. Though this arch is too narrow. You have mistaken the perspective.")
narration("Gabriele frowns.")
dialogue("GABRIELE","I measured it twice.")
dialogue("ANDREA", "Then you measured it twice incorrectly")
answer=show_choice(
    "You notice the disappointment in your friend's eyes.",
    [
        Choice(
            title=[("italic fg:#888888", "Defend Gabriele's artistic judgement.")],
            value="friendly"
        ),
        Choice(
            title=[("italic fg:#888888", "Agree with Andrea's criticism.")],
            value="critical"
        ),
        Choice(
            title=[("italic fg:#888888", "Stay silent and let Gabriele answer for himself.")],
            value="indifferent"
        )
    ]
)
if answer=="friendly":
    dialogue("TOMMASO", "I think Gabriele has captured the space rather well. The proportions aren't as far off as you suggest.")
    gabriele_trust+=1
    memory_note("Gabriele")
elif answer=="critical":
    dialogue("TOMMASO", "Master Andrea is right. The perspective does seem a little narrow.")
    gabriele_trust-=1
    andrea_trust+=1
elif answer=="indifferent":
    dialogue("TOMMASO", "You should show it to the glass-painter before changing anything. He may see it differently.")
    caution+=1
dialogue("ANDREA", "Do not let a little money make you careless.")
dialogue("GABRIELE", "I wouldn't dream of it.")
narration("Tommaso notices that several small figures have been marked near the choir.")
dialogue("TOMMASO", "You went to the cathedral to draw this?")
dialogue("GABRIELE", "Naturally. Where else would I draw it?")
dialogue("TOMMASO", "And the man was satisfied?")
dialogue("GABRIELE", "Very. He even asked about the light during Mass. Apparently, it matters for the glass.")
narration("Gabriele puts the drawing away.")
dialogue("GABRIELE", "Anyway, four florins are four florins.")
console.print("[bold]Scene VI - An Ordinary Evening[/bold]")
narration("Andrea extinguishes the candles while Tommaso gathers his things.")
narration("Gabriele is still at the bench, attempting to repair a damaged wooden frame.")
dialogue("GABRIELE", "Tommaso, wait! Tell me honestly, does this look crooked?")
dialogue("TOMMASO", "It does.")
dialogue("GABRIELE", "Wonderful. I was hoping you'd say that.")
narration("He puts down the drawing and stretches.")
dialogue("GABRIELE", "Come on. Let's get something to eat before the taverns fill up.")
answer = show_choice(
    "Gabriele is waiting for your answer. What do you do?",
    [
        Choice(
            title="All right. You can tell me more about that commission.",
            value ="inquisitive"
        ),
        Choice(
            title = "Perhaps tomorrow. I promised Lucia I'd be home early.",
            value = "brotherly"
        ),
        Choice(
            title="You should be careful with these commissions. Not everyone deserves your trust.",
            value = "aggressive"
        )
    ]
)
if answer=="inquisitive":
    dialogue("GABRIELE", "Still thinking about my four florins?")
    dialogue("TOMMASO", "I was curious.")
    dialogue("GABRIELE", "The man was polite enough. Needed a drawing, paid well. I see no reason to complain.")
    gabriele_trust+=1
elif answer=="brotherly":
    dialogue("GABRIELE", "Your sister keeps better hours than the rest of us.")
    dialogue("TOMMASO", "Someone has to.")
    dialogue("GABRIELE", "Very well. Another evening, then.")
    lucia_trust+=1
elif answer=="aggressive":
    dialogue("GABRIELE", "And here I thought you were the sensible one.")
    dialogue("TOMMASO", "I'm serious.")
    dialogue("GABRIELE", "So am I. I did a drawing, Tommaso. Nothing more.")
    caution+=1
    gabriele_trust-=1

console.print("[bold]End of Chapter II[/bold]")
console.print()
time.sleep(0.7)
console.print("[bold]Chapter III - The Drawing[/bold]")
console.print("Florence 17 April 1478")
console.print("[bold]Scene I - The Loggia[/bold]")
narration("Gabriele is waiting outside the workshop when Tommaso steps out.")
dialogue("GABRIELE", "There you are. Come along.")
dialogue("TOMMASO", "Where?")
dialogue("GABRIELE", "Does it matter? I've been waiting for you.")
dialogue("TOMMASO","Andrea expects us back.")
dialogue("GABRIELE","Andrea always expects us back. Come, it's only a short walk.")
narration("Gabriele leads him through the busy streets, towards a quiet loggia not far from the cathedral. A man is waiting beneath its arches, dressed plainly, though his clothes are of good quality.")
dialogue("GABRIELE", "Messere, as promised. This is the drawing.")
narration("The man takes the parchment and carefully unrolls it. It depicts the interior of Santa Maria del Fiore, this time viewed from the choir.")
dialogue("MAN", "Very good.")
narration("He studies it for a moment longer.")
dialogue("MAN", "You have a good eye. Particularly for the arrangement of the figures.")
dialogue("GABRIELE", "I thought it important to show the scale of the building.")
dialogue("MAN", "Quite right. My master's glass-painter will appreciate the detail.")
dialogue("GABRIELE", "Will there be further work, then?")
dialogue("MAN", "Perhaps. There is always work for a capable hand.")
narration("He reaches into his purse and counts six florins into Gabriele's palm.")
dialogue("GABRIELE", "Six? Messer, this is more than we agreed.")
dialogue("MAN", "You have done good work. Consider it an advance on what may follow.")
narration("The man rolls the parchment and returns it to Gabriele.")
dialogue("MAN", "And this is your friend?")
dialogue("GABRIELE", "Tommaso, we work together.")
narration("The man turns towards Tommaso.")
dialogue("MAN", "See that Gabriele comes to Mass on Sunday morning. A man who knows the cathedral so well ought to see it when it is full.")
answer=show_choice(
    "How do you respond to the man?",
    [
        Choice(
            title="Of course, Messere. I'll see that he comes.",
            value="agreeing"
        ),
        Choice(
            title="Why is it so important that he be there?",
            value="questioning"
        ),
        Choice(
            title=[("italic fg:#888888", "Say nothing. Observe the man carefully.")],
            value="silent"
        )
    ]
)
if answer=="agreeing":
    dialogue("MAN", "Very good. I shall look forward to it.")
elif answer=="questioning":
    narration("The man pauses. His expression remains pleasant, although his eyes settle more firmly on Tommaso.")
    dialogue("MAN", "My master has taken an interest in the work. He would like to see the young man in the place he has drawn.")
    dialogue("TOMMASO", "I see.")
    dialogue("MAN", "Good day to you both.")
    narration("As the man walks away, Gabriele turns towards Tommaso.")
    dialogue("GABRIELE", "Must you question everyone? He's paying me, isn't he?")
    suspicion+=1
    man_noticed_you=True
elif answer=="silent":
    narration("Tommaso says nothing. Instead, he watches the stranger as he gathers the parchment.")
    narration("There is a ring on his right hand, its stone turned inward against his palm. He seems conscious of where Tommaso's eyes have settled, and closes his hand.")
    narration("The man offers a final nod before leaving.")
    dialogue("GABRIELE", "Well? What do you make of him?")
    dialogue("TOMMASO","Nothing. I was merely looking.")
    dialogue("GABRIELE", "Then look at these instead.")
    narration("He raises the coins again, smiling.")
    suspicion+=1
    noticed_ring=True

narration("On their way back, Gabriele becomes quieter. He unrolls a second sheet of parchment.")
dialogue("GABRIELE", "Here. Could you keep this for me?")
dialogue("TOMMASO", "Another drawing?")
dialogue("GABRIELE", "An earlier study of the cathedral. Andrea wasn't particularly fond of it, as you might remember.")
narration("Is the drawing Gabriele had worked on before.")
dialogue("GABRIELE", "I might need it if the glass-painter asks for changes. And I would rather not leave it at home. My landlady has a habit of using old parchment to start her fire.")
narration("He hands Tommaso the parchment.")
answer=show_choice(
    "What do you do?",
    [
        Choice(
            title=[("italic fg:#888888", "Take the drawing and put it away safely.")],
            value="take it"
        ),
        Choice(
            title="Keep it yourself. I would rather not be responsible for it.",
            value="don't take it"
        )
    ]
)
if answer=="take it":
    dialogue("TOMMASO", "Very well. I'll keep it in the workshop.")
    dialogue("GABRIELE", "Thank you. I'll collect it when I need it.")
    holds_drawing=True

else:
    dialogue("TOMMASO", "Keep it yourself, Gabriele. I have enough things to worry about.")
    dialogue("GABRIELE", "Fine.")
    holds_drawing=False
