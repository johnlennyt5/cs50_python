from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    
    if len(sys.argv) == 1:
        randomFont = True
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        randomFont = False
    else:
        sys.exit(1)

    figlet.getFonts()
        
    if randomFont == False:
        try:
            figlet.setFont(font=sys.argv[2]) 
        except:
            print("Invalid font name")
            sys.exit(1)
    else:
        font = random.choice(figlet.getFonts())
        figlet.setFont(font=font) 
        
    text = input("Input: ")
   
    
    print('Output:')
    print(figlet.renderText(text))

if __name__ == '__main__':
    main()
