import config
import prefill


print("enter \"help\" for more help")
run = True


while run == True:
    ans = input("Prefilled G Forms QR Code Generator: ").split()
    
    if ans[0] == "exit":
        if len(ans) < 2:
            run = False
        else:
            print("Too many arguments, enter \"help\" for help")
    
    elif ans[0] == "about":
        if len(ans) < 2:
            print("\nPrefilled G Forms QR Code Generator is a program that generates a prefill link of a google form based on a specified excel file. It is then shortened through bitly and turned into a qr code\n")
        else:
            print("Too many arguments, enter \"help\" for help")
        
    
    elif ans[0] == "run":
        if len(ans) < 2:
            prefill.run()
        else:
            print("Too many arguments, enter \"help\" for help")
        
    elif ans[0] == "token":
        if len(ans) < 2:
            print("Not enough arguments, enter \"help\" for help")
        else:
            
            if ans[1] == "list":
                if len(ans) < 3:
                    print(str(config.bitly_token).translate({ord(c): None for c in '][,'}))
                else:
                    print("Too many arguments, enter \"help\" for help")
            
            elif ans[1] == "add":
                if len(ans) > 2:
                    for i in range(len(ans) - 2):
                        config.bitly_token.append(ans[i + 2])
                else:
                    print("Not enough arguments, enter \"help\" for help")
                
            elif ans[1] == "remove":
                if len(ans) > 2:
                    for i in range(len(ans) - 2):
                        config.bitly_token.remove(ans[i + 2])
                else:
                    print("Not enough arguments, enter \"help\" for help")
                
            elif ans[1] == "clear":
                if len(ans) < 3:
                    config.bitly_token = []
                else:
                    print("Too many arguments, enter \"help\" for help")
    
    elif ans[0] == "destination":
        if len(ans) == 1:
            print(config.destination)
        elif len(ans) == 3:
            if ans[1] == "change":
                config.destination = ans[2]
        else:
            print("Too many or not enough arguments, enter \"help\" for help")
                

    
    elif ans[0] == "form":
        if len(ans) == 1:
            print(config.forms_link)
        elif len(ans) == 3:
            if ans[1] == "change":
                config.forms_link = ans[2]
        else:
            print("Too many or not enough arguments, enter \"help\" for help")
    
    elif ans[0] == "help":
        if len(ans) < 2:
            print("\nexit                        exits the program\nabout                       displays program info\nrun                         generates the qr code\ntoken list                  lists all the tokens\ntoken add <token>           adds the specified bitly token/s (you may add multiple tokens at a time)\ntoken remove <token>        removes the specified bitly token/s (you may remove multiple tokens at a time)\ntoken clear                 clears the tokens\ndestination                 displays the current destination folder\ndestination change <path>   changes the destination folder to the specified path\nform                        displays the current google form prefill link\nform change                 changes the google form prefill link to the specified url\n")
        else:
            print("Too many arguments, enter \"help\" for help")
        
    else:
        print("unknown command")