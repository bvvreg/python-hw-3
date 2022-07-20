import sys
print ("\n********** CALCULATOR ***********")
print ("*     Арифметичні операції      *")
print ("*         (+, -, *, /)          *")
print ("*  з двома цілими аргументами   *")
print ("*     заданими у вигляді:       *")
print ("*         X операція Y          *")
print ("*     в командній стрічці       *")
print ("*********************************\n")

def calc(left_operand, rigth_operand, operation):
    result = ''
    try:
        match operation:
            case "+":
                result = f"Сума чисел: {left_operand} + {rigth_operand} = {int(left_operand)+ int(rigth_operand)}"
            case "-":
                result = f"Різниця чисел: {left_operand} - {rigth_operand} = {int(left_operand) - int(rigth_operand)}"
            case "*":
                result = f"Добуток чисел: {left_operand} * {rigth_operand} = {int(left_operand) * int(rigth_operand)}"
            case "/":
                if int(rigth_operand) == 0:
                   result = "Помилка: ділення на 0!"
                else:
                   result = f"Частка чисел: {left_operand} / {rigth_operand} = {int(left_operand) / int(rigth_operand)}"
            case "%":
                if int(rigth_operand) == 0:
                    result = "Помилка: ділення на 0!"
                else:
                    result = f"Остача від ділення: {left_operand} % {rigth_operand} = {int(left_operand) % int(rigth_operand)}"
    
    except ValueError:
        result = "Помилка: введіть числа!"
    return result


allowed_operations = ['+', '-', '/', '*','%']
operands = sys.argv
del operands[0]

count_operand = len(operands)

if count_operand > 3:
    print ("Помилка: забагато аргументів!")
    print ("\n*********************************")
    sys.exit()

str_operands = ''
MANY_OPERATION = 0
str_operands =''.join(operands)
str_operands.replace(" ", "")
operation = ""

for key in allowed_operations:
        if key in str_operands:
            operands = str_operands.split(key)
            operation = key
            MANY_OPERATION +=1
if MANY_OPERATION > 1:
    print ("Помилка: забагато операцій!")
    sys.exit()
if operation != "":
    print (calc(operands[0], operands[1], operation))
else:
    print ("Помилка: не знайдено операцію!")
print ("\n*********************************")
