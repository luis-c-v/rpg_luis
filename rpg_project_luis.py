"""
LUIS' RPG 
Created: Jul 27, 2020
Dyl's Final Assignment
"""

GPA = 3.0

def intro(name):
    """reads the introduction/details of the game"""
    print("\nWelcome back to high school, " + name + "! This game is full of high school wonders, teen-age urges, and countless AP/IB courses! The objective of the game is to finish your first high school year with the highest GPA! (or at least don't get kicked out of school by letting your GPA drop below 2.0) But I warn you!!! Do not let your freshman year go by so quickly! Have fun and explore your adolescence. \nBecause I feel courteous, you will start off with a 3.0 GPA. Good luck, " + name + "! You will need it.")


def check_gpa():
    """prints the gpa of player"""
    if GPA >= 3.0:
        print("\nYour GPA is " + str(GPA) + "!")
    else:
        print("\nYour GPA is " + str(GPA) + ".")
        

def friends_month():
    """runs game through freshman year!"""
    global GPA
    # pulls gpa from main() and makes it useful here!
    print("\nIt's your freshman year in high school! Your are young, immature, and insecure. So lets find some friends!")
    
    # runs Focus on finding friends
    print("You walk into your first high-school class, Biology. You notice there is a single chair left in the front of the classroom. Luckily, the instructor arranged the seating to be divided into groups of four! In your group you have a guy named Jesus, he dresses extremely well but has an edgar haircut, a girl named Cathy, she looks off but she was the first to introduce herself to you, and another girl named Claudia, she has a RBF and hasn't said a single thing all period.\n")
    classmate = {"A": "Jesus", "B": "Cathy", "C": "Claudia"}
    print("You plan to follow-up with one of your classmates after school.")
    for k, v in classmate.items():
        # TYP used for loop to be able to print the options in a clean and neat manner
        print(k + ") " + v)
    fst_friend = input("Who do you want to reach out to? ").upper()    
    #used the users input to later check what theu want to futher investigate (person in this case)
    if fst_friend == "A":
        # runs Jesus
        print("\n{-------- OPTION A --------}\nYou reached out to Jesus!\n\nAt first you questioned his personality. He dressed really nice and came off as 'put-together.' But, boy were you wrong! This man is a mess! He spends all his money on clothes and haircuts. He never has money to buy his own food when you guys hang out! Ohhh, and dont forget he drives his dad's truck and calls it the 'MAMALONA.' Aside from that he is extremely goofy and incredibly fun to be around, especially when you guys aren't dinning out. One major issue is that Jesus doesn't like studying and your Biology instructor asigned the class the first problem set of the year!\n\nThe problem set is due Monday, but Jesus invited you to a truck meet this weekend. You never heard of a truck meet.")
        weekend_1 = {"A": "Go to the truck meet with Jesus", "B": "Stay home and complete the study set", "C": "Go to the truck meet and stay-up late on Sunday to complete the problem-set"}
        for k, v in weekend_1.items():
            print(k + ") " + v)
        choice = input("\nHow do you plan to spend this weekend? ").upper()                 
        if choice == "A":
            # Go to the truck meet with Jesus
            print("\n{-------- OPTION A --------}\nYou didn't want to disappoint Jesus the first time he invited you somewhere!\n\nOn the way to the truck meet, Jesus blasts his truck speakers to some spanish music you've never heard before, he calls them 'Sonideras.' That was an odd start to the night but you ended up liking his music. At the truck meet you got meet a bunch of Jesus' friends! Most of them dress similar to him, and very amiable! They immedately initial dialogue as if you had known them for ages. After countless hours of watching trucks burning tires in the parking lot, the police arrive to the meet. As soon as the sirens went off, Jesus instinctively took off for the 'MaMaLoNa.'\n\nSince you see people running to their cars like crazy you begin to run too but dont remember when Jesus parked!")
            meet = {"A": "Run frantically to the nearest truck", "B": "Call your mom to pick you up"}
            for k, v in meet.items():
                print(k + ") " + v)
            at_meet = input("\nWhat do you plan on doing now? ").upper() 
            if at_meet == "A":
                print("\n{-------- OPTION A --------}\nYou didn't want to call you mom since she would accuse Jesus of being a bad influence.\n\nYou ran to the nearest truck you could find. Luckily, the owner of the truck was one of Jesus' friends you met earlier, Jose. He tells you to jump into the back of his truck and drops you off at a gas station a mile away where Jesus was waiting for you. You and Jesus laugh the whole incident off on the way back home.\nMonday, Jesus can help but pass notes during Bio reminding you about the weekend and how you both forgot to complete the problem set. You laugh it off the entire period and forget to take notes.")
                GPA -= .3
                check_gpa()
            else:
                print("\n{-------- OPTION B --------}\nYou called your mom because you feared that you wouldnt find Jesus.\n\nFortunately your loving mom arrives as swiftly as a bear to her cub in danger. She brings you home, cooks you dinner, and advises that you don't go to truck meets with Jesus anymore. Unfortuately you were so anxious of going to the truck meet that you forgot to complete the problem set. Monday comes and both you and Jesus can't turn in the problem set")
                GPA -= .3
                check_gpa()  
            not_completed_game = "NO"
        elif choice == "B":
            # Stay home and complete the study set
            print("\n{-------- OPTION B --------}\nYou chose to stay home to complete the problem set!\n\nAlthough you do feel bad about not joining Jesus to the truck meet you do feel extremely knowledgeable on the animal and plant cell structure! However, you are still sad that you couldn't go to the meet with Jesus. So you debate wether you should send him a text or wait til Monday to apologize in person.")
            GPA += .3
            check_gpa()                 
            text = {"A": "Send Jesus a message", "B": "Wait til Monday to see him"}
            for k, v in text.items():
                print(k + ") " + v)
            debate = input("\nWhat do you plan on doing? ").upper()                 
            if debate == "A":
                # send him a text
                print("\n{-------- OPTION A --------}\nYou sent Jesus a text message!\n\nHe responds in a couple minutes telling you not to worry about it! He mentioned that he would invite you to the next meet. A week went by of cheerful dialouge with Jesus and he invites you to another truck meet! But this time the Bio instructor handed you an exam.")
                weekend_1 = {"A": "Go to the truck meet with Jesus", "B": "Stay home and complete the study guide", "C": "Go to the truck meet and stay-up late on Sunday to complete the study guide"}
                for k, v in weekend_1.items():
                    print(k + ") " + v)
                choice = input("\nHow do you plan to spend this weekend? ").upper()                 
                if choice == "A":
                    # Go to the truck meet with Jesus
                    print("\n{-------- OPTION A --------}\nYou didn't want to disappoint Jesus the first time he invited you somewhere!\n\nOn the way to the truck meet, Jesus blasts his truck speakers to some spanish music you've never heard before, he calls them 'Sonideras.' That was an odd start to the night but you ended up liking his music. At the truck meet you got meet a bunch of Jesus' friends! Most of them dress similar to him, and very amiable! They immedately initial dialogue as if you had known them for ages. After countless hours of watching trucks burning tires in the parking lot, the police arrive to the meet. As soon as the sirens went off, Jesus instinctively took off for the 'MaMaLoNa.'\nSince you see people running to their cars like crazy you begin to run too but dont remember when Jesus parked!")
                    meet = {"A": "Run frantically to the nearest truck", "B": "Call your mom to pick you up"}
                    for k, v in meet.items():
                        print(k + ") " + v)
                    at_meet = input("\nWhat do you plan on doing now? ").upper() 
                    if at_meet == "A":
                        print("\n{-------- OPTION A --------}\nYou didn't want to call you mom since she would accuse Jesus of being a bad influence.\n\nYou ran to the nearest truck you could find. Luckily, the owner of the truck was one of Jesus' friends you met earlier, Jose. He tells you to jump into the back of his truck and drops you off at a gas station a mile away where Jesus was waiting for you. You and Jesus laugh the whole incident off on the way back home.\nMonday, Jesus can help but pass notes during Bio reminding you about the weekend and how you both forgot to complete the problem set. You laugh it off the entire period and forget to take notes.")
                        GPA -= .3
                        check_gpa()
                    else:
                        print("\n{-------- OPTION B --------}\nYou called your mom because you feared that you wouldnt find Jesus.\n\nFortunately your loving mom arrives as swiftly as a bear to her cub in danger. She brings you home, cooks you dinner, and advises that you don't go to truck meets with Jesus anymore. Unfortuately you were so anxious of going to the truck meet that you forgot to complete the problem set. Monday comes and both you and Jesus can't turn in the problem set")
                        GPA -= .3
                        check_gpa()
                    not_completed_game = "NO"
                elif choice == "B":
                    print("\n{-------- OPTION B --------}\nYou declined Jesus' second offer to join him at the truck meet.\n\nForntuately you studied immensely to exceed the exam Monday! However, you feel sad because while you completed you exam without breaking a sweat, while Jesus slept right through the test. He also ignored you after class :(")
                    GPA += .1
                    check_gpa()     
                else:
                    print("\n{-------- OPTION C --------}\nYou declined Jesus' first offer and you don't want to disappoint him a second time!\n\nYou crammed most of the content for the exam before meeting up with Jesus to go the truck meet. You go and you have an amazing time! You met a ton of his friends, they dress very similar to him and all have the same haircut as he does too! Unfortunately the Police arrived after someone call them because of the screeching tires and all the smake they produced. You had enough time to get a good nights rest before the exam. Monday came around and you didnt do as you would have studied more but study got a 80% on your first exam!")
                    GPA += .1
                    check_gpa() 
                not_completed_game = "NO"
            else:
                # wait until monday
                print("\n{-------- OPTION B --------}\nYou declined Jesus' offer to join him at the truck meet and it's Monday.\n\nYou formally apologize. He says not to worry about it, but you know that deep down both you and him lost a friend. Taking to him feels unnatural, so you avoid people like him from now on. In the bright side of things, you completed the study set!")
                check_gpa()
                not_completed_game = "NO"
        else:
            print("\n{-------- OPTION C --------}\nYou didn't want to disappoint Jesus the first time he invited you somewhere but you also didn't want to blow off your study set!\n\nOn the way to the truck meet, Jesus blasts his truck speakers to some spanish music you've never heard before, he calls them 'Sonideras.' That was an odd start to the night but you ended up liking his music. At the truck meet you got meet a bunch of Jesus' friends! Most of them dress similar to him, and very amiable! They immedately initial dialogue as if you had known them for ages. After countless hours of watching trucks burning tires in the parking lot, the police arrive to the meet. As soon as the sirens went off, Jesus instinctively took off for the 'MaMaLoNa.'\n\nSince you see people running to their cars like crazy you begin to run too but dont remember when Jesus parked!")
            meet = {"A": "Run frantically to the nearest truck", "B": "Call your mom to pick you up"}
            for k, v in meet.items():
                print(k + ") " + v)
            at_meet = input("\nWhat do you plan on doing now? ").upper() 
            if at_meet == "A":
                print("\n{-------- OPTION A --------}\nYou didn't want to call you mom since she would accuse Jesus of being a bad influence.\n\nYou ran to the nearest truck you could find. Luckily, the owner of the truck was one of Jesus' friends you met earlier, Jose. He tells you to jump into the back of his truck and drops you off at a gas station a mile away where Jesus was waiting for you. You and Jesus laugh the whole incident off on the way back home.\nMonday, Jesus can help but pass notes during Bio reminding you about the weekend and how you both forgot to complete the problem set. You laugh it off the entire period and forget to take notes.")
            else:
                print("\n{-------- OPTION B --------}\nYou called your mom because you feared that you wouldnt find Jesus.\n\nFortunately your loving mom arrives as swiftly as a bear to her cub in danger. She brings you home, cooks you dinner, and advises that you don't go to truck meets with Jesus anymore. Unfortuately you were so anxious of going to the truck meet that you forgot to complete the problem set. Monday comes and both you and Jesus can't turn in the problem set") 
            GPA -= .3
            check_gpa() 
            not_completed_game = "NO"
        
    elif fst_friend == "B":
        # runs Cathy
        print("\n{-------- OPTION B --------}\nYou reached out to Cathy!\n\nYou don't know much about her other that she is extremely friendly! She loves to ride horses and her father is the CEO of Bank of America. Consequently, she is a pampered child! She always gets what she wants from her parents and knows the power she has but doesn't show it immedately. You notice it gradually as you begin to knwo more about her. She invited you to her house for brunch this weekend, but the bio instructor mentioned that she would give the a quiz on Monday!")
        cat = {"A": "Join Cathy's brunch invite", "B": "Decline brunch to study at home", "C": "Ask Cathy if she wants to study for the quiz together after brunch"}
        for k, v in cat.items():
            print(k + ") " + v)
        brunch = input("\nWhat do you plan on doing this weekend? ").upper() 
        if brunch == "A":
            print("\n{-------- OPTION A --------}\nYou chose to have Brunch with Cathy!\n\nYou arrive to cathy's home and she has a beautiful home! Porcelin floors, white cabinets, and an elegant stairwell! He home is very well kept, and you can't help but notice every bit of detail in the home. After burnch, which felt more like a three course meal, Cathy asked if you want to take a swim in rooftop pool, but you also remembered you had to study for the quiz on Monday!")
            cat_2 = {"A": "Take a swim", "B": "Go home to study"}
            for k, v in cat_2.items():
                print(k + ") " + v)
            brunch = input("\nWhat do you plan on doing now? ").upper()                 
        elif brunch == "B":
            print("\n{-------- OPTION B --------}\nYou chose to decline Cathy's offer to brunch!\n\nShe now felt the need to make you seem like a rude person. Because she is wealthy, people who tried being her friend now know about you. On the bright side, as everyone was too worried about spreading gossip, you studied for the quiz! Which means that you did really well on the first quiz! However, people continue to talk smack about you!")
            GPA += .3
            check_gpa()                 
        else:
            print("\n{-------- OPTION C --------}\nYou asked Cathy if she would like to study for the quiz after brunch!\n\nShe was flattered at the inquisition! The weekend came and both of you were extremely excited about learning more about each other! Since you both studied, you guys received amazing scores on the quiz! But the instructor assumed you cheated so she separated you.")
            GPA += .2
            check_gpa()
        not_completed_game = "NO"
    else:
        # runs Claudia 
        print("\n{-------- OPTION C --------}\nYou reached out to Claudia.\n\nShe is extreme self-centered. The only things she wanted to talk about was the boys she was interested in and how she looked. She mentioned that she would want to go on a date with Jesus from your bio group. she asked if you wanted to be friends with her.")
        claud = {"A": "Continue talking to her", "B": "May God bless her", "C": "Make her humble >;)"}
        for k, v in claud.items():
            print(k + ") " + v)
        preception = input("\nWhat do you want to do with Claudia? ").upper()  
        if preception == "A":
            print("\n{-------- OPTION A --------}\nYou chose to continue talking to Claudia!\n\nYou are debating whether she is actually pretentious or just trying to scare you off. So you are conflicted whether you want to invite her to lunch or find another friend. ")
            claud_1 = {"A": "Invite her to lunch", "B": "Find another friend"}
            for k, v in claud_1.items():
                print(k + ") " + v)
            dump = input("\nWhat do you want to do with Claudia? ").upper() 
            if dump == "A":
                print("\n{-------- OPTION A --------}\nYou chose to invite Claudia to lunch!\n\nUnfortunately, she declined you offer, rather disrespectfully.\nBecause you chose to invest so much time in Claudia you missed a biology assignment!")
                GPA -= .2
                check_gpa()                  
            else:
                print("\n{-------- OPTION B --------}\nYou chose to find another friend, however, many people saw you talking to Claudia and now they assumed that you are just like her! Now no one wants to be your friend.\nBecause you chose to invest so much time in looking for a friend you miss a biology assignment!")
                GPA -= .2
                check_gpa()
            not_completed_game = "NO"
        elif preception == "B":
            print("\n{-------- OPTION B --------}\nYou chose to let Claudia be Claudia!\n\nYou gave yourself room to read people's intentions before they played you! And this allowed you to focus on your assignments!")
            GPA += .2
            check_gpa() 
            not_completed_game = "NO"
        else:
            print("\n{-------- OPTION C --------}\nYou chose to mess with Claudia, in hopes to humble her down!\n\nYou are considering giving her helpful feedback on her attitude towards others or recording her stuck-upness secretly and uploading it online.") 
            claud_2 = {"A": "Confront her", "B": "Ridicule her online"}
            for k, v in claud_2.items():
                print(k + ") " + v)
            humble = input("What do you say? ")
            if humble == "A":
                print("\n{-------- OPTION A --------}\nYou chose to confront her about her sassy ways!\n\nYou confronted her durning lunch infront of everyone. She didnt like the things you had to say about her toes ;0 So she chose to throw you the slice of pizza she was eating. A piece of pepperoni got stuck to you hair, you pulled it out and threw it back at her. This all broke out to a massive food fight! And you ultimately got suspended :( for telling the truth...")
            else:
                print("\n{-------- OPTION B --------}\nYou chose to record her sassy ways!\n\nAfter uploading her clips, your account received thousands of subscribers! However, Claudia figured you out and sued you for Defamation. You were suspended because of this.")
            not_completed_game = "NO"
    return [GPA] + [not_completed_game]
        


def main():
    """This function excutes the entire game!"""
    global GPA
    user_name = input("Greetings lad! What's your name? ").capitalize()
    intro(user_name)
    # started everyone out w/ 3.0 gpa
    GPA = 3.0
    check_gpa()
    color = input("\nBefore we begin what is your favorite color? If your favorite color is my favorite too, then your GPA will start off at 3.2! ")
    print("\nSorry, " + color + " stinks!")
    # implemented this just for fun
    print("\n***** Quick side note, every question defaults to the last option! *****")
    
    not_completed_game = True
    # used a variable to boolean to ensure that our game still has questions and is able to be played
    
    while (GPA > 2.0) and not_completed_game:
        # while loop!
        # one condition should be completing the game (variable that starts out False and changes to True as soon as the game has been completed)
        # second should be while the gpa is > 2.0
        bb_list = friends_month()
        GPA = bb_list[0]
        if bb_list[1] == "NO":
            break
    if GPA > 3.5:
        print("congradulations! " + user_name + ", you have completed your freshmen year in High School with a " + str(GPA) + "! You deserve a cookie!")
    elif GPA < 2.0:
        print("Your high school years must have sucked if you couldn't complete this simple game!")
    else:
        print("Congratulations! " + user_name + ", you passed with a " + str(GPA) + "... at least.")
        
main()