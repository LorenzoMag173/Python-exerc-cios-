from Model import Model

class Control:

    def __init__(self):
        self.modelo = Model()
        self.opcao = 0

    def mostrarMenu(self):
        print ('Escolha uma das opcões abaixo: '+
              '\n1. Sair'                       +
              '\n2. Trocar'                     +
              '\n3. Tabuada'                    +
              '\n4. Exercicio 01'               +
              '\n5. Exercicio 02'               +
              '\n6. Exercicio 03'               +
              '\n7. Exercicio 04'               +
              '\n8. Exercicio 05'               +
              '\n9. Exercicio 06'               +
              '\n10. Exercicio 07'              +
              '\n11. Exercicio 08'              +
              '\n12. Exercicio 09'              +
              '\n13. Exercicio 10'              +
              '\n14. Exercicio 11'              +
              '\n15. Exercicio 12'              +
              '\n16. Exercicio 13'              +
              '\n17. Exercicio 14'              +
              '\n18. Exercicio 15'              +
              '\n19. Exercicio 16'              +
              '\n20. Exercicio 17'              +
              '\n21. Exercicio 18'              +
              '\n22. Exercicio 19'              +
              '\n23. Exercicio 20'              )




    def operacoes(self):
        while(self.opcao != 1):
            self.mostrarMenu()
            self.opcao = int(input('Escolha uma das opções acima: '))
            if self.opcao == 1:
                print('obrigado')
            elif self.opcao == 2:
                valorA = int(input('informe um valor para A'))
                valorB = int(input('informe um valor para B'))
                print(self.modelo.trocar(valorA,valorB))
            elif self.opcao == 3:
                num = int(input('informe um número: '))
                print(self.modelo.tabuada(num))

            elif self.opcao == 4:
                num = int(input("informe um número"))
                print(self.modelo.exercicioUm(num))

            elif self.opcao == 6:
                num = int(input("informe um número"))
                print(self.modelo.exercicioDois(num))

            elif self.opcao == 7:
                print(f'a soma dos números entre 1 e 100 é:{self.modelo.exercicioTres()}')

            elif self.opcao == 8:
                num = int(input("informe um número"))
                print(f'Os multiplos de 5, de 1 a 50 são: \n{self.modelo.exercicioQuatro()}')

            elif self.opcao == 9:
                num = int(input("Informe um número: "))
                print(self.modelo.exercicioCinco(num))

            elif self.opcao == 13:
                num = int(input("Informe um número: "))
                print(f'A soma dos numeros é: {self.modelo.exercicioNove(num)})

            elif self.opcao == 14
            if __name__ == "__main__":
               print(self.exercicioDoze)(1, 20)




            else:
                print('opção escolhida não e válida')

