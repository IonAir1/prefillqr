import prefill
from configparser import ConfigParser


config = ConfigParser()
run = True


config.read('config.ini')
if not config.has_section('main'):
    config.add_section('main')
    
if config.has_option('main','excel_file'):
    excel_file = config.get('main', 'excel_file')
else:
    excel_file = ""
        
if config.has_option('main','forms_link'):
    forms_link = config.get('main', 'forms_link')
else:
    forms_link = ""
    
if config.has_option('main','destination'):
    destination = config.get('main', 'destination')
else:
    destination = "exports/"

if config.has_option('main','bitly_token'):
    bitly_token = config.get('main', 'bitly_token').split(",")
else:
    bitly_token = []
    

def save(key, value):
    if key == "bitly_token":
        val = ",".join(value)
    else:
        val = value
    if not config.has_section('main'):
        config.add_section('main')
    config.read('config.ini')
    config.set('main', str(key), val)
    with open('config.ini', 'w') as f:
        config.write(f)


print("enter \"help\" for more help")


while run == True:
    ans = input("Prefilled G Forms QR Code Generator: ").split()
    
    if ans[0] == "exit" or ans[0] == "quit":
        run = False

    elif ans[0] == "about":
        print("\nPrefilled G Forms QR Code Generator is a program that generates a prefill link of a google form based on a specified excel file. It is then shortened through bitly and turned into a qr code\n")
    
    elif ans[0] == "run":
        prefill.run(excel_file, forms_link, bitly_token, destination)
        
    elif ans[0] == "token":
        if len(ans) < 2:
            print(str(bitly_token).translate({ord(c): None for c in '][,'}))
        else:
            if ans[1] == "add":
                if len(ans) > 2:
                    for i in range(len(ans) - 2):
                        if not ans[i+2] in bitly_token:
                            bitly_token.append(ans[i + 2])
                            save('bitly_token',bitly_token)
                else:
                    print("Invalid arguments, enter \"help\" for help")
                
            elif ans[1] == "remove":
                if len(ans) > 2:
                    for i in range(len(ans) - 2):
                        if ans[i+2] in bitly_token:
                            bitly_token.remove(ans[i + 2])
                            save('bitly_token',bitly_token)
                else:
                    print("Invalid arguments, enter \"help\" for help")
                
            elif ans[1] == "clear":
                    bitly_token = []
                    save('bitly_token',bitly_token)

    elif ans[0] == "excel":
        if len(ans) == 1:
            print(excel_file)
        elif len(ans) == 2:
            excel_file = ans[1]
            save('excel_file', excel_file)
        else:
            print("Invalid arguments, enter \"help\" for help")
            
            
    elif ans[0] == "destination":
        if len(ans) == 1:
            print(destination)
        elif len(ans) == 2:
            destination = ans[1]
            save('destination', destination)
        else:
            print("Invalid arguments, enter \"help\" for help")
                

    
    elif ans[0] == "form":
        if len(ans) == 1:
            print(forms_link)
        elif len(ans) == 2:
            forms_link = ans[1]
            save('forms_link', forms_link)
        else:
            print("Invalid arguments, enter \"help\" for help")
    
    elif ans[0] == "help":
        print("""
        'exit'  or  'quit'     exits the program
        'about'                displays program info
        'run'                  generates the qr code
        'token'                lists all the tokens
        'token add <token>'    adds the specified bitly token/s (you may add multiple tokens at a time)
        'token remove <token>' removes the specified bitly token/s (you may remove multiple tokens at a time)
        'token clear'          clears the tokens
        'destination'          displays the current destination folder
        'destination <path>'   changes the destination folder to the specified path
        'form'                 displays the current google form prefill link
        'form <path>'          changes the google form prefill link to the specified url
        'excel'                displays the current selected excel file
        'excel <path>'         changes the excel file to the specified path
        """)
        
    else:
        print("unknown command")