import sys , time
quit = False
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
        ".--" : "W" , "-..-" : "X" , "-.--" : "Y" , "--.." :"Z", " " : " "

}
def text_to_morse():
    global  txt_morse
    txt = str(input("Enter the sentence or word to Convert to Morse Code\n"))
    length = len(txt)
    UpperCase = txt.upper()
    for word in UpperCase:
        print(word + "  " + txt_morse[word])
        time.sleep(0.3)
        
def morse_to_text():
    global morse_txt
    morse_code = list(map(str, input("Enter Morse Code (separate words by ' / ')\n").split(' / ')))
    for sentence in morse_code:
        for morse in sentence:
            print(morse_txt[morse] + "  " + morse)
            time.sleep(0.3)


def converter():
    while not quit:
        selection = input("\nPress 1 to convert TEXT to MORSE CODE\nPress 2 to convert MORSE CODE to TEXT\n\nPress 0 to Exit\n")
        if selection == "1":
            text_to_morse()
        elif selection == "2":
            morse_to_text()
        elif selection == "0":
            Quit()
        else:
            print("Invalid Input")
            time.sleep(1)

def Quit():
    global quit
    quit = True
        
converter()