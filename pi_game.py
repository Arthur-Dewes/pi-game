
def main():
    
    def gibbons_lamberts_pi():
        """
        Este é um gerador de dígitos de pi usando um algoritmo spigot.

        A função produz os dígitos de pi sequencialmente, um de cada vez.
        O algoritmo usa operações de aritmética inteira, o que significa
        que não requer cálculos de ponto flutuante de alta precisão.
        
        O algoritmo baseia-se numa série de cálculos que geram os dígitos
        de pi de forma iterativa, e é caracterizado pela sua simplicidade e
        baixo consumo de memória.

        A função usa as seguintes variáveis:
            q: um acumulador
            r: um resto
            t: um divisor
            k: um incremento
            n: um dígito de pi
            l: um incremento

        A cada iteração, verifica-se se 4 * q + r - t é menor que n * t.
        Se verdadeiro, o algoritmo produz um dígito de pi (n) e atualiza
        as variáveis q, r, n, etc. para a próxima iteração. Caso contrário,
        o algoritmo atualiza as mesmas variáveis com uma fórmula diferente.

        O algoritmo continua a produzir dígitos de pi indefinidamente.
        """
        q, r, s, t, n, i = 0, 4, 1, 0, 4, 1
        while True:
            if n == (q * (5 * i - 2) + 2 * r) // (s * (5 * i - 2) + 2 * t):
                yield n
                q, r, s, t, n, i = (10 * q - 10 * n * s, 10 * r - 10 * n * t, s, t,
                                (10 * ((q - n * s) * (2 * i - 1) + r - n * t)) // (
                                    s * (2 * i - 1) + t), i)
            else:
                q, r, s, t, n, i = ((2 * i - 1) * q + r, i * i * q,
                                (2 * i - 1) * s + t, i * i * s,
                                ((5 * i * i - 1) * q + (2 * i + 1) * r) // (
                                    (5 * i * i - 1) * s + (2 * i + 1) * t), i + 1)

    print("Bem-vindo ao jogo! Digite os dígitos de π. O jogo para quando você errar.")
    nome = input("Digite seu nome: ")
    pi = gibbons_lamberts_pi()
    count = 0
    digit = next(pi) # inicializa o gerador com o primeiro número de pi

    while True:
        try:
            guess = input(f"Digite o próximo dígito de π: ")
            
            if len(guess) != 1 or not guess.isdigit():
                raise ValueError("Digite apenas um único número entre 0 e 9.")
            
            guess = int(guess)
            
        except ValueError as e:
            print(f"Erro: {e}")
            continue
        except Exception as e:
            print(f"Erro: {e}")
            break

        if guess == digit:
                print("Correto!")
                count += 1
                digit = next(pi) # atualiza para o próximo número de pi
        else:
            print(f"Errado! O próximo dígito de π é {digit}.")
            print(f"Você digitou {count} dígitos de π.")
            break

if __name__ == "__main__":
    main()

