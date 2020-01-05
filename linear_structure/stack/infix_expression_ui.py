from infix_expression import *


def eval_infix_input():
    while True:
        infix = input(">>>")
        if not infix:
            print("Session ended. Thanks for using!")
            break
        try:
            postfix = infix_to_postfix(infix)
            answer = eval_postfix(postfix)
            if int(answer) == answer:
                answer = int(answer)
            print(answer)
        except SyntaxError:
            print("Invalid syntax!")


if __name__ == "__main__":
    eval_infix_input()
