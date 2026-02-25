questions=(
    ("what is the capital of india? "),
    ("what is the largest city in india? "),
    ("what is the smallest city in india? ") )
options=(
    ("a.new delhi","b.mumbai","c.kolkata","d.chennai"),
    ("a.new delhi","b.mumbai","c.kolkata","d.chennai"),
    ("a.new delhi","b.mumbai","c.kolkata","d.chennai") )
answers=("a","b","c")
guesses=[]
score=0
question_num=0
for question in questions:
    print("------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess=input("answer (a,b,c,d): ").lower()
    guesses.append(guess)
    if guess==answers[question_num]:
        score+=1
        print("correct!")
    else:
        print("incorrect!")
        print(f"{answers[question_num]} is the correct answer")
    question_num+=1
print("-------------")
print("   RESULTS   ")
print("-------------")

print("answers:", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses:", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score=int(score/len(questions)*100)
print(f"your score is: {score}%")
