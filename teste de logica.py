def check(number):
    fibonacciSequence = 1
    lastValue = 1
    while fibonacciSequence <= number:
        if number == fibonacciSequence or number == 0:
            return 'O número informado pertence a sequência.'
        assistantChange = fibonacciSequence
        fibonacciSequence += lastValue
        lastValue = assistantChange
    return 'O número informado não pertence a sequência.'


number = int(input("Digite um número para saber se pertence a sequência de Fibonacci: "))

print(check(number))
