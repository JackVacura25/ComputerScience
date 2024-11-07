import os

name = input("Before we begin would you please enter a name?\n>)")

def start():  
    print("There was once a professional boxer fighting for the world heavyweight title.")

    print(f"And his name was {name}")

    print(f"it a week out from the fight and {name} was leaving the gym after a hard training session. suddenly a shady looking man approached him and spoke of some buisness oppurtunity and handed {name} a slip of paper with an adress on it and the time 24:00, and a message instructinghim to come alone, and then walked away")

    print("You arrive back to your home and are faced with a decision")
    print("1. go to the buisness oppppurtunity")
    print("2. stay home for the night and rest")
    print("3. contact the police")

    choice1 = input(">")
    if choice1 == "1":
        meeting()
    elif choice1 == "2":
        stayhome()
    elif choice1 == "3":
        callpolice()
    else:
        start()

def meeting():
    print(f"{name} decided they want to go to the meeting and figured out that the adress is a couple blocks away from his building")
    print("1. Walk to meeting")
    print("2. Get a cab")

    choice2 = input(">")
    if choice2 == "1":
        walk()
    elif choice2 == "2":
        taxi()

def stayhome():
    print(f"{name} chose to skip the meeting and get some rest. {name} was sound asleep when suddely there was a knock at the door")
    print("1. answer the door")
    print("2. Ignore it")

    choice3 = input(">")
    if choice3 == "1":
        opendoor()
    elif choice3 == "1":
        ignoredoor()

def callpolice():
    print(f"{name} decides to call thge police and tells them that a man handed him a piece of paper the then tell you that its not serious (nice try)")
    os.system('cls' if os.name == 'nt' else 'clear')
    start()

def walk():
    print(f"{name} decided they wanted to walk to the meeting. when {name} arrives the building is old and abandoned. Inside the building was two big beefy fellas and an old man who says to sit down")
    print(f"after sitting down the old man explains that he is a mob boss and his oppurtunity for {name} to take a loss in his upcoming fight on purpose and the reward from the boss will be five times the pay of the fight itself")
    print(f"So what will it be the boss says")
    print("1. yes")
    print("2. no")

    choice3 = input(">")
    if choice3 == "1":
        yes()
    elif choice3 == "2":
        no()
    
def taxi():
    print(f"{name} catches a cab and the driver is confused with the location and asks why anyone would want to be there at midnight")
    print("1. laugh it off and pay")
    print("2 .explain yourself")

    choice4 = input(">")
    if choice4 == "1":
        laugh()
    elif choice4 == "2":
        explain()

def opendoor():
    print(f"{name} gets up and opens the door outside the door are two men dressed in all black")
    print("1. swing")
    print("2. ask if you can help them")

    choice5 = input(">")
    if choice5 == "1":
        swingdoor()
    elif choice5 == "2":
        canihelp()

def ignoredoor():
    print(f"{name} ignores the knock and shuts their eyes. But 5 seconds later there is another knock")
    print("1. ignore again")
    print("2. answer dooor")

    choice6 = input(">")
    if choice6 == "1":
        ignore2()
    elif choice6 == "2":
        opendoor()

def yes():
    print("I was hoping you would say that. now the plan is that you simply take a beating in the first round and when you fall you dont get up. you can meet me back in the locker room for cash upfront of if you break the deal we will be waiting for you ringside")
    print("1. sounds good")
    print("2. on second thought i dont like this idea")
    print("3. I can do it but i want the money upfront")
    choice7 = input(">")
    if choice7 == "1":
        finalise()
    elif choice7 == "2":
        secthought()
    elif choice7 == "3":
        negotiate()

def no():
    print(f"well heres the thing {name}, your opponent has too much pride to take a dive he has been the champ for ten years. but you are replaceable if you decline this we can make you go away and we will find somebodey else")
    print("1. nope I cant do it")
    print("2. okay fine")
    print("3. okay, but i want the money upfront")

    choice8 = input(">")
    if choice8 == "1":
        decline()
    elif choice8 == "2":
        finalise()
    elif choice8 == "3":
        negotiate()

def laugh():
    print(f"{name} just laughs at the question and gives the cash to the driver and he mutters creep")
    os.system('cls' if os.name == 'nt' else 'clear')
    cabend()

def cabend():  
    print(f"when {name} arrives the building is old and abandoned. Inside the building was two big beefy fellas and an old man who says to sit down")
    print(f"after sitting down the old man explains that he is a mob boss and his oppurtunity for {name} to take a loss in his upcoming fight on purpose and the reward from the boss will be five times the pay of the fight itself")
    print(f"So what will it be the boss says")
    print("1. yes")
    print("2. no")

    choice3 = input(">")
    if choice3 == "1":
        yes()
    elif choice3 == "2":
        no()

def explain():
    print(f"{name} explains that a shady fella told you to come here and the taxi calls {name} an idiot")
    os.system('cls' if os.name == 'nt' else 'clear')
    cabend()

def swingdoor():
    print(f"{name} throws a heavy right hook at the man on the right. The blow lands clean on the mans chin and he instantly goes to sleep")
    print(f"then the other man starts digging in his coat pocket")
    print("1. front kick")
    print("2. left hook")
    print("3. tackle")

    choice9 = input(">")
    if choice9 == "1":
        frontkick()
    elif choice9 == "2":
        lefthook()
    elif choice9 == "3":
        tackle()

def canihelp():
    print(f"The man on the left says hello {name}, would you mind if we come in?")
    print("1. sure")
    print("2. swing on him")

    choice10 = input(">")
    if choice10 == "1":
        lethimin()
    elif choice10 == "2":
        swingdoor()

def ignore2():
    print(f"{name} decides that it is smart to just stay in bed and let them go away. But all of a sudden the sound of the front door swinging open makes {name}'s eyes shoot open")
    print(f"{name} runs out of the bedroom and ses two large men walking into the apartment they approach and ask {name} to come over and talk")
    print("1. go and talk to the men")
    print("2. Walk over and swing on the men")
    choice11 = input(">")
    if choice11 == "1":
        aptconvo()
    elif choice11 == "2":
        swingdoor()

def finalise():
    print(f"the boss says alright now be ready we will see you back in the locker room after the fight")
    b4fightnight()

def secthought():
    print(f"the boss says well thats sad to hear he then pulls a handgun out and kills {name}. the end")
    start()

def negotiate():
    print("alright fine you can have the money now i figured you might want it now he then pulls reveals a large briefcase full of cash. 5 million dollars. alright i will see you after the fight pal")
    b4fightnightplus()

def decline():
    print(f"the boss says well thats sad to hear he then pulls a handgun out and kills {name}. the end")
    start()

def frontkick():
    print(f"{name} turns to the other man and horribly telegraphs a slow front kick that the man dodges easily and fires his handgun at {name}. remember {name} is Heavyweight boxer not a kickboxer. the end")
    start()

def lefthook():
    print(f"{name} turns to the other man and cracks him with a swift left hook to the temple and the man crumples to the floor")
    print("1. get to safetey as fast as possible")
    print("2. grab a gun and go to the meeting adress")
    print("3. call the police")

    choice12 = input(">")
    if choice12 == "1":
        fleenocash()
    elif choice12 == "2":
        raidmeeting()
    elif choice12 == "3":
        callpolice2()

def tackle():
    print(f"{name} turns to the other man and shoots a tackle with bad form {name} gets hiptossed into a wall and shot and killed. remember {name} is a heavyweight boxer not a football player")
    start()

def lethimin():
    print(f"the men come into the apartment and walk invite you to sit at the kitchen table")
    print(f"after sitting down the old man explains that he is a mob boss and his oppurtunity for {name} to take a loss in his upcoming fight on purpose and the reward from the boss will be five times the pay of the fight itself")
    print(f"So what will it be the boss says")
    print("1. yes")
    print("2. no")

    choice13 = input(">")
    if choice13 == "1":
        yes()
    elif choice13 == "2":
        no()

def aptconvo():
    print(f"the men sit down at the table and tell you to have a seat")
    print(f"after sitting down the old man explains that he is a mob boss and his oppurtunity for {name} to take a loss in his upcoming fight on purpose and the reward from the boss will be five times the pay of the fight itself")
    print(f"So what will it be the boss says")
    print("1. yes")
    print("2. no")

    choice14 = input(">")
    if choice14 == "1":
        yes()
    elif choice14 == "2":
        no()

def b4fightnight():
    print(f"It was the night beore the fight and {name} had finished a jog and thought it might not be too late to back out of this deal")
    print("1. follow through with the plan")
    print("2. flee the country")

    choice15 = input(">")
    if choice15 == "1":
        fightday()
    elif choice15 == "2":
        fleenocash()

def b4fightnightplus(): 
    print(f"It was the night beore the fight and {name} had finished a jog and thought it might not be too late to back out of this deal they could just take the all the cash and get a plane ticket across the country then figure the rest out")
    print("1. follow through with the plan")
    print("2. flee the country")

    choice16 = input(">")
    if choice16 == "1":
        fightnightplus()
    elif choice16 == "2":
        fleecountrycashfail()

def fleenocash():
    print(f"{name} catches a cab and gets a ride to the nearest airport and takes the next flight out of town and then contacts police and is placed in protective custody. {name} never boxed again as they feared for their life. the end")
    start()

def raidmeeting():
    print(f"{name} knows who sent these men so they work up the courage to storm the building mentioned in the note.")
    print("1. enter through front")
    print("2. Break a window and crawl in")
    print("find emergency exit")

    choice17 = input(">")
    if choice17 == "1":
        front()
    elif choice17 == "2":
        window()
    elif choice17 == "3":
        emergencyexit()

def callpolice2():
    print(f"with the two men knocked unconsious on the floor {name} leaves the building and calls the police and explains the situation. when the police arrive the men are placed in cutody and {name} is taken into protective custody. {name} went on to fight for 20 world titles and was considered the greatest of all time by the time they retired. the end")
    start()

def fightday():
    print(f" it is the night of the fight {name} is about to walk out against the champion and take a loss and return to the locker room")
    print(f"{name} steps into the ring and after the fighters have been introduced the bell rings for round one")
    print("1. Get knocked out")
    print("2. swing for the fences")

    choice18 = input(">")
    if choice18 == "1":
        palooka()
    elif choice18 == "2":
        gooutfighting()

def fightnightplus():
    print(f" it is the night of the fight {name} is about to walk out against the champion and take a loss and return to the locker room. But then an idea is sparked. the money is already at {name}'s apartment. if {name} gets a first round KO they could flee the arena immediatley and sneak back into the apartment to grab the cash and get out of town")
    print(f"{name} steps into the ring and after the fighters have been introduced the bell rings for round one")
    print("1. Get knocked out")
    print("2. swing for the fences")

    choice19 = input(">")
    if choice19 == "1":
        palooka()
    elif choice19 == "2":
        goodending()

def front():
    print(f"{name} walks into the building through the front door and is shot immeiatley. the end")

def window():
    print(f"{name} smashes a window and crawls in the mobsters in the building hear it and two fly around the corner")
    print("1. shoot at them")
    print("2. surrender")

    choice20 = input(">")
    if choice20 == "1":
        shootdie()
    elif choice20 == "2":
        surrender()

def emergencyexit():
    print(f"{name} sneaks into the building throgh the back and finds his way into an office where ther are two gaurds holding machine guns and a man in a fancy suit")
    print("1. shoot them")
    print("2. announce yourself")

def palooka():
    print(f"all {name} can remember about that night was waking up in the locker room surrounded by mobsters and trainers. {name}'s deal with the mobsters was discovered and {name} recieved a permenant ban from all boxing promotions and never fought again. the end")
    start()

def fleecountrycashfail():
    print(f"As {name} was leaving the apartment a car rooled the window down and gunned down {name}. the end")
    start()

def gooutfighting():
    print(f"{name} does something crazy and starts teeing off on the opponent it only takes about 20 seconds for the champion to fall")
    print(f"after tho official decision {name} returns to the locker room and meets the boss")
    print(f"the boss says that he does not appreciate when people go back on their word and {name} gets whacked. the end")
    start()

def goodending():
    print(f"{name} does something crazy and starts teeing off on the opponent it only takes about 20 seconds for the champion to fall")
    print(f"before the belt can be wrappped {name} runs out of the arena and catches a cab out of town {name} goes to a stash and retrives the cash and heads to a private runway and pays a pilot to take him across the country where they live a quiet life off the grid. the end")
    start()

def shootdie():
    print(f"{name} gets one shot off and drops the one gaurd and is then torn to shreds by a tommy gun. the end")
    start()

def surrender():
    print(f"{name} drops his weapon and throws their hands up in the air. the gaurds then say they know what happened at the aprtment and shred {name} with machine guns. the end")
    start()







start()

