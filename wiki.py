import wikipedia

while(True):
    try:
        user_input = input("What page would you like to see?\n")
        sr = wikipedia.page(user_input)
        print(sr.title)
        print(sr.content)
        break
    except wikipedia.exceptions.PageError:
        print("That page does not exist")
    except:
        print("Something went wrong")

