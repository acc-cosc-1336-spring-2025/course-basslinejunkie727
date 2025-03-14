
def get_factorial(num):
    factorial=1
    for i in range(1,num+1):
        factorial*=i
    return factorial

def sum_odd_numbers(num):
    sum_odd=0
    while n<=num:
        sum_odd+=n
        n+=2
    return sum_odd



def main():
    while True:
        print('homework 3 menu')
        print('1-factorial')
        print('2-sum odd numbers')
        print('3-exit')
        choice=input('please input 1,2,or 3')
        if choice=="1":
            while True:
                try:
                    num=int(input('enter a number between 1 to 9 for factoral calculation'))
                    if num >0 and num<10:
                        break
                except ValueError:
                    print('please enter a valid integer')
            print(f'the factorial of {num} is {get_factorial(num)}')
        elif choice=="2":
            while True:
                try:
                    num=int(input('enter a number between 1 and 99 to sum odd numbers'))
                    if num>0and num<100:
                        break
                    else:
                        print('number must be less than 100 and more than 0')
                except ValueError:
                    print('please enter a valid integer')
        elif choice=='3':
            continue_exit=input('do you want to exit yes/no').lower()
            if continue_exit=='yes':
                print('exiting the program')
                break
            else:
                continue
        else:
            print('please enter a valid number')
        exit_choice=input('do you want to exit yes/no').lower()
        if exit_choice=='yes':
            print('exiting the program')
            break
        else:
            continue
        