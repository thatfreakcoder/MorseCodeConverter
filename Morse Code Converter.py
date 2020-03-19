import sys , time
txt_morse = {
    "A" : ".-" , "B" : "-..." ,
"C": "-.-." , "D": "-.." , "E": "." , "F": "..-." ,
"G": "--." , "H": "...." , "I": ".." , "J": ".---" , 
"K": "-.-" , "L": ".-.." , "M": "--" , "N": "-." , 
"O": "---" , "P": ".--." , "Q": "--.-" , "R": ".-." ,
"S": "..." ,"T": "-" , "U": "..-" , "V": "...-" ,
"W": ".--" , "X": "-..-" , "Y": "-.--" , "Z": "--..", " " : " "

}

morse_txt = {
        ".-" : "A" , "-..." : "B" ,
        "-.-." : "C", "-.." : "D", "." : "E", "..-." : "F",
        "--." : "G" , "...." : "H", ".." : "I", ".---" : "J", 
        "-.-" : "K" , ".-.." : "L" , "--" : "M" , "-." : "N" , 
        "---" : "O" , ".--." : "P", "--.-" : "Q" , ".-." : "R" ,
        "..." : "S" , "-" : "T" , "..-" : "U" , "...-" : "V",
        ".--" : "W" , "-..-" : "X" , "-.--" : "Y" , "--.." :"Z"

}
def text_to_morse():
    global  txt_morse
    txt = str(input("Enter the Word You want to Convert to Morse Code\n"))
    length = len(txt)
    UpperCase = txt.upper()
    for word in UpperCase:
        print(word + "  " + txt_morse[word])
        time.sleep(1)
        
def morse_to_text():
    global morse_txt
    morse = input("Enter the Morse Code (ONLY ALPHABET W/o SPACE) to Convert to Text\n")
    print(str(morse) + " = " + str(morse_txt[morse]))
    time.sleep(1)

def converter():
    selection = input("\nPress 1 to convert TEXT to MORSE CODE\nPress 0 to convert MORSE CODE to TEXT\n")
    if selection == "1":
        text_to_morse()
        Quit()
    elif selection == "0":
        morse_to_text()
        Quit()
    else:
        print("Invalid Input")
        time.sleep(1)
        converter()
def Quit():
    quit = input("\nPress 1 to Convert Again\nPress 0 to Quit\n")
    if quit == "1":
        converter()
    elif quit == "0":
        sys.exit()
    else:
        print("Invalid Input")
        time.sleep(1)
        quit()
        
converter()