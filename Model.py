class Model:
    def  __init__(self):
        self.num1 = 0
        self.num2 = 0

    def trocar(self, valorA, valorB):
        valorC = valorA
        valorA = valorB
        valorB = valorC
        return f'Valor A: {valorA}  \nValor B: {valorB}'

    def tabuada(self, num):
        resultado = "" #variavel string
        for i in range(0, 11, 1):
            resultado += f'{num} * {i} = {num * i}\n'
        return resultado

    def exercicioUm(self, num):
        resultado = ""
        for i in range(0, 11, 1):
            resultado += f'{i}\n'
        return resultado

    def exercicioDois(self, num):
        resultado = ""
        for i in range(0, 20, 2):
            resultado += f'{i}\n'
        return resultado

    def exercicioTres(self):
        soma = 0
        for i in range(101):
            soma += i
        return soma

    def exercicioQuatro(self):
        resultado = ""
        for i  in range(0, 51, 5):
            resultado += f'{i}\n'
        return resultado

    def exercicioCinco(self, num):
        if num %2 == 0:
            return f'0 número {num} é par'
        else:
            return f'O número é impar'

    def exercicioNove(selfself, num):
        soma = 0
        for i in range(1, num+1, 1):
            soma += i
        return soma

    def exercicioDez(self):
        resultado = "2\n3\n5"
        for i in range(5, 21, 1):
            if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
                resultado += f; \n{i}
        return resultado

    def exercicioOnze(self,num):
        if num == 2 or num == 3 or num == 5:
            return f'0 |{num} é primo'
        elif num % 2 != 0 and num % 3 != 0 and num % 5 != 0:
                return f'{num} é primo'
        else:
            return f'0 {num} não é primo'


    def exercicioDoze(num):
            """Verifica se um número é primo."""
            if num <= 1:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True

        def exercicioDoze(start, end):
            """Imprime os números primos em um intervalo específico."""
            primes = []
            for num in range(start, end + 1):
                if is_prime(num):
                    primes.append(num)
            print("Números primos de", start, "a", end, ":", primes)


    def exercicioTreze(self,num):





