# creating a quiz with the help of dictionary
print(""" 
  ▄▄█▀▀██▄               ██          
▄██▀    ▀██▄                         
██▀      ▀██▀███  ▀███ ▀███  █▀▀▀███ 
██        ██  ██    ██   ██  ▀  ███  
██▄      ▄██  ██    ██   ██    ███   
▀██▄    ▄██▀  ██    ██   ██   ███  ▄ 
  ▀▀████▀▀    ▀████▀███▄████▄███████ 
      ███                            
       ▀████▀ """)
print("""RULES:\n 
      1)This quiz will contain 5 questions
      2)You can skip any questions(marks will not be provided) 
      3)You can Quit the quiz at an time
      4)4 marks will be given for each right answer and 1 mark will be deducted for every wrong answer
      """)
questions = ["1)The first mechanical computer designed by Charles Babbage was called ?\nA. Abacus\nB. Analytical Engine\nC. Calculator\nD. Processor",
                 "2)Which of the following is the most powerful type of computer ?\nA.Super–micro\nB.Super conductor\nC.Super computer\nD.Megaframe",
                 "3)Which is a single integrated circuit?\nA. Gate\nB. Mother Board\nC. Chip\nD. CPU",
                 "4)C is ?\nA. A third generation high level language\nB. A machine language\nC. An assembly language\nD. All of the above",
                 "5)Web pages are written using ?\nA. FTP\nB. HTTP\nC. HTML\nD. URL"]
answers ={
    questions[0] : 'B',
    questions[1] : 'C',
    questions[2] : 'A',
    questions[3] : 'A',
    questions[4] : 'C'
}
start = input("Do you want to take a quiz(YES/NO): ").lower()
if start == 'yes':
    score = 0
    name = input("Enter your name: ").title()
    print(f"Welcome {name}, You can start the quiz")
    for question in questions:
        print(question)
        proposal = input("Do You want to skip this question(yes/no): ").lower()
        if proposal == 'yes':
            continue
        else:
            ans = input("Enter your answer(option): ").upper()
            if ans == answers[question]:
                score = score+4
                print(f"Your score is {score}")
            else:
                score = score-1
                print(f"Your score is {score}")
        choice = input("Do You want to quit(yes/no): ").lower()
        if choice == 'yes':
            print("You QUIT")
            break
        else:
            continue
print(f"You final score is {score}")
if score >=10:
    print("Good")
else:
    print("Practice more")