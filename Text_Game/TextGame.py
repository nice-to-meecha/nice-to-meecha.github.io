print("Hmph")

name = input("Who are ye? ")

age_1 = int(input("Alright, " + name + ". How old are ye? "))

print("Come on. Are you actually " + str(age_1) + ", " + name + "?")

age_2 = int(input("How old are you really? "))


if age_1 == age_2:
    print("You'd better be " + str(age_2) + ", " + name + ", or you'll be a liar for the entirety of this game.")
    liar_status = input("Do you want to be a liar? (This is a 'yes' or 'no' question.) ")
else:
    print("You liar! I knew it!!")
    liar_status = "yes"


if liar_status.lower() == "yes":
    print("I knew you were up to no good.")
    print("Well then, " + name + ", if that's even your real name, let's see if you're old enough for this game. If you're older than 18, you'll be fine.")
else:
    print("I don't believe you, but I guess this will have to do.")
    print("Let's see if you're old enough to play this game. You must be at least 18, despite a lack of mature content.")
    

while age_2 < 18:
    print("Scram! You can't play!")
    print("Unless if, of course, you would like to lie about your age.")
    age_2 = int(input("What is your--ahem--age? "))
    liar_status = "yes"

is_older = age_2 >= 18

if is_older:
    print("I convened with my supervisors, and it seems that you are allowed to play this game. Ugh.")
    wants_to_play = input("Well, scallywab. Are you sure you want to embark on this adventure? ")

    if wants_to_play.lower() == "yes":
        print("Alright, then. We shall proceed.")
    else:
        print("Quit wasting my time, sponge.")
