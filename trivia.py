#!/usr/bin/python3

import html

trivia= {
         "category": "Entertainment: Film",
         "type": "multiple",
         "question": "Which of the following is NOT a quote from the 1942 film Casablanca? ",
         "correct_answer": "&quot;Frankly, my dear, I don&#039;t give a damn.&quot;",
         "incorrect_answers": [
             "&quot;Here&#039;s lookin&#039; at you, kid.&quot;",
             "&ldquo;Of all the gin joints, in all the towns, in all the world, she walks into mine&hellip;&rdquo;",
             "&quot;Round up the usual suspects.&quot;"
            ]
        }

A = html.unescape(trivia['correct_answer'])
B = html.unescape(trivia['incorrect_answers'][0])
C = html.unescape(trivia['incorrect_answers'][1])
D = html.unescape(trivia['incorrect_answers'][2])


print(trivia.get('question'))
print("A. " + A)
print("B. " + B)
print("C. " + C)
print("D. " + D)

answer = input('Answer here: ')

if answer == "A":
    print('That is correct')

else:
    print('Wrong answer')



