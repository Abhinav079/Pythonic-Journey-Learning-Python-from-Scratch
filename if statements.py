#if statements - this is to choose one of two conditions if the condition is true further the statement gets executed
age=int(input())
if age<18:
    print("You are a small boy")
elif age>=18:
    print("You are an adult")
elif age<0:
    print("you hadn't born")
            