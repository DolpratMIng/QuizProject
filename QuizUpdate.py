#Ming commit fkdjsfklajdlk;fj
#List of tuple to store questions and answers
Questions = [
    ("Question 1: What years Hikaru Nakamura was born?\n1. 2025\n2. 2000\n3. 1998\n4. 1987\n",4),
    ("Question 2: What age did Hikaru Nakamura earned his grandmaster title?\n1. 12\n2. 13\n3. 14\n4. 15\n",4),
    ("Question 3: How many U.S. Chess Champion has Hikaru Nakamura achieved?\n1. 2\n2. 3\n3. 4\n4. 5\n",4),
    ("Question 4: How long is the history of chess?\n1. 500 years\n2. 1000 years\n3. 1500 years\n4. 2000 years\n",3),
    ("Question 5: Which country is known to be the origin of chess game?\n1. India\n2. Russia\n3. England\n4. France\n",1),
    ("Question 6: How many squares on the chess board?\n1. 60\n2. 64\n3. 63\n4. 50\n",2),
    ("Question 7: How many possible moves in chess?\n1. 10,000 moves\n2. 1,000,000 moves\n3. 1,000,000,000 moves\n4. more than the atoms in the universe\n",4),
    ("Question 8: Who is the most popular chess streamer in the world?\n1. Hikaru Nakamura\n2. Magnus Carlsen\n3. Levy Rozman\n4. Eric Rosen\n",3),
    ("Question 9: What is the master title Levy Rozman earned?\n1. FM\n2. IM\n3. GM\n4. NM\n",2),
    ("Question 10: What quote Eric rozen usually say?\n1. \"Oh no my queen\"\n2. \"Bing... Bang... Boom\"\n3. \"Wooden shield\"\n4. \"Sacrifice THE ROOK\"\n",1)
]

#Function to reduce the duplication(of taking user input and gather score)
def CreateQuestion(score):
    #for loop to go through each question in the list
    for i in range(len(Questions)):
        answer = -1 
        #input handling for input validation to check for specific data types, range limit
        while answer < 0 or answer > 4:
            #Try except block
            try:
                #user input
                answer = int(input(Questions[i][0]))
                #if the user give the data out of range
                if answer < 0 or answer > 4: 
                    print("Invalid choice. Please enter a choice from 1 to 4.")
            except ValueError: #if the user give the invalid data type
                print("Invalid input. Please enter a valid integer")
        
        #checking for the answer
        if answer == Questions[i][1]:
            score+= 1
            print("The answer is correct. The current score is ",score,"/10.\n")
        else:
            print("The answer is not correct. The current score is ",score,"/10.\n")

    return score

while True:
    #Call the function
    score = CreateQuestion(0)

    #Show the score commentary
    if(score <= 3):
        print("Well done, you have complete the quiz.\nIt's not bad but YOU SHOULD QUIT CHESS THOUGH.")
    elif(score <= 6):
        print("Well done, you have complete the quiz.\nYOU ARE TOO WEAK. PATHETIC.")
    elif(score <= 8):
        print("Well done, you have complete the quiz.\nGood but need to study more.")
    else:
        print("Well done, you have complete the quiz.\nYou are pretty DECENT.")
    
    #restart or exit menu
    while True:
        #Restart or quit
        print()
        exit_restart = input("(R)estart or (E)xit: ")

        exit_restart = exit_restart.upper() # convert it to capital letter
        #Restart
        if(exit_restart == "R" or exit_restart == "RESTART"): 
            break
        #Exit
        elif(exit_restart == "E" or exit_restart == "EXIT"):
            exit()
        #Go back to restart or exit menu
        else:
            print("Invalid input. Please give the input again.")


