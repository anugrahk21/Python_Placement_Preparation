# MCQ forum
questions=["What is python?","How to install python?","What are python data types?","What is a function in python?","How to handle exceptions in python?"]
answer=["a","c","d","b","e"]
answer_number=[0,1,2,3,4]
options=[["a. A programming language","b. A snake","c. A car","d. A fruit","e. A movie"],
         ["a. From the command line","b. From a CD","c. From the official website","d. From a book","e. From a friend"],
         ["a. Integer, Float, String","b. List, Tuple, Set","c. Dictionary, Boolean","d. All of the above","e. None of the above"],
         ["a. A variable","b. A block of reusable code","c. A data type","d. An operator","e. A module"],
         ["a. Using if-else statements","b. Using loops","c. Using functions","d. Using classes","e. Using try-except blocks"]]
marks=0
for i in range(len(questions)):
    print(f"Q{i+1}: {questions[i]}")
    for j in options[i]: # For accessing the elements of nested list.[[]]
        print(j)
        ans=input("Enter your answer (a/b/c/d/e): ").lower()
    if (ans==answer[i]):
        marks+=1
        print("Correct!\n")
    elif(ans not in answer):
        print("Enter a valid answer (a/b/c/d/e)")
    else: 
        print(f"Wrong!, The correct answer is option: {options[i][answer_number[i]]}\n")
print(f"Your total score is {marks} out of {len(questions)}.")

    