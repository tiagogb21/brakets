#!/bin/python3

# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING brackets as parameter.

def compare_brackets(open, close):
    brackets_open = {
        '{': '}',
        '(': ')',
        '[': ']',
    }
    # Verifica qual o bracket no dicionário e se esse corresponde ao close
    if brackets_open[open] == close:
        return True
    else:
        return False

def isBalanced(brackets):
  # Verificamos se o tamanho é ímpar, se sim, retornamos 'NO'
    if(len(brackets) % 2 != 0):
        return 'NO'
    # Criamos uma pilha (stack):
    stack = []
    # Armazenamos os brackets de abertura em um dicionário:
    brackets_open_store = ['{', '(', '[']
    # Iteramos por cada elemento do parâmetro brackets:
    for char in brackets:
        # Verificamos se o elemento é de abertura
        if char in brackets_open_store:
            # Empurramos para o final da pilha
            stack.append(char)
        # Se não for, será de fechamento
        else:
            # Verificamos se a pilha está vazia
            if len(stack) == 0:
                return 'NO'
            # Retiramos o elemento mais alto da pilha
            top_element = stack.pop()
            # Comparando se os elementos são correspondentes entre si
            if not compare_brackets(top_element, char):
                return 'NO'
    if len(stack) != 0:
        return 'NO'
    return 'YES'


if __name__ == '__main__':

    t = int(input().strip())

    results = []
    for t_itr in range(t):
        brackets = input()

        results.append(isBalanced(brackets))

    print(*results, sep='\n')
