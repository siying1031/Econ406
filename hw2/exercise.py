"""
Siying homework2 Q2
"""
# Q2.a
def prisoners_dilemma():
    '''Asks both players their strategies of cooperate or defect, and prints the payoff.
       If players choose differing strategies, continue the game.
       If players choose the same strategy, game end and return the number of rounds played.

    Returns
    -------
    counter:int
    The number of rounds player A and player B played.

    '''
    counter = 0
    list_answer = []
    while True:
        counter += 1
        a_input = input('Player A, do you defect? Press Y or N \n')
        b_input = input('Player B, do you defect? Press Y or N \n')
        list_answer.append([a_input,b_input])
        if a_input == 'Y' and b_input == 'Y':
            print('The payoffs of both A and B are -10. \n')
            #print('It takes' + str(counter) + 'rounds for A & B choose the same strategy')
            print(counter)
            break
        elif a_input == 'N' and b_input == 'Y':
            print('The payoff of player A is -20，The payoff of player B is 0.\n')
        elif a_input == 'Y' and b_input == 'N':
            print('The payoff of player A is 0，The payoff of player B is -20.\n')
        else:
            print('The payoffs of both A and B are -3 \n')
            #print('It takes' + str(counter) + 'rounds for A & B choose the same strategy.')
            # Both line 30 & 33 are correct, but line 33 fits the requirement of the homework.
            print(counter)
            break

# Q2.b
def factorial(num: int):
    '''
    Calculates factorial of n and​ returns 𝑛! ​for any positive integers.

    Parameters
    ----------
    num : int
        quantity of numbers.

    Returns
    -------
    n! for any positive integers.

    '''
    res = 1
    if num < 0:
        print("The input number has to greater or equal to 0! \n")
    elif num == 0:
        print("0! = 1")
    else:
        for i in range(1,num + 1):
            res = res*i
        print("Factorial of %d is %d" %(num,factorial))

# Q3.c
word_list = ['sklearn','AI','data analysis',
             'Caffe','AI','sklearn','AI','Computatoinal Economics',
             'Tensorflow','sklearn','Keras','data science','numpy',
             'amazon aws server','AI']
def compute_frequency(words):
    '''takes a list of strings and returns a dictionary of
       how many times each unique string has appeared.

    Parameters
    ----------
    words : list
        a list of strings.

    Returns
    -------
    dic: dictionary.
    how many times each unique string has appeared.

    '''
    dic = {}
    for word in words:
        if word not in dic:
            dic[word] = 1
        else:
            dic[word] = dic[word] +1
    print(dic)
