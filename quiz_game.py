print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != 'yes':
    quit()

score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == 'central processing unit':
    score += 1
    print('correct!')
else:
    print('Incorrect!')

answer = input("What does RAM stand for? ")
if answer.lower() == 'random access memory':
    score += 1
    print('correct!')
else:
    print('Incorrect!')

answer = input("What does BMW stand for? ")
if answer.lower() == 'bavariyan motor ways':
    score += 1
    print('correct!')
else:
    print('Incorrect!')

answer = input("What does ROM stand for? ")
if answer.lower() == 'read only memory':
    score += 1
    print('correct!')
else:
    print('Incorrect!')

answer = input("What does GPU stand for? ")
if answer.lower() == 'graphics processing unit':
    score += 1
    print('correct!')
else:
    print('Incorrect!')

print(f"You got {score} questions correct!")
print(f"You got {(score/5)*100} {"%."} questions percentage!")