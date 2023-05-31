import wikipedia

while(True):
    try:
        user_input = input("What would like like to know more about?\n")
        sr = wikipedia.page(user_input)
        print(sr.title)
        print(sr.content)
        break
    except wikipedia.exceptions.PageError:
        print("This page does not exist")
    except:
        print("Something went wrong")
