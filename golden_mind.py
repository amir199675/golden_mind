import random

def main():
    numbers = range(1,10)
    operations = ['-','+']
    result = 0
    input('keep an integer in your mind and press enter!')
    for i in range(4):
        rand_int = random.randint(0,len(numbers)-1)
        selected_number = numbers[rand_int]

        rand_operation = random.randint(0,len(operations)-1)
        selected_operation = operations[rand_operation]
        if selected_operation == '-':
            input(f'{selected_number} subtract from result and press enter!')
            result -= selected_number
        else:
            input(f'{selected_number} sum from result and press enter!')
            result += selected_number
    input('subtract first number that you keep in your mind from result!')
    print(f'result= {result}?')

if __name__ == '__main__':
    main()
