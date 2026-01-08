def main():
    num_alunos = int(input("Digite o número de alunos na turma: "))

    alunos_aprovados = 0
    alunos_reprovados = 0
    soma_geral = 0
    
    print("\n" + "="*60)
    
    for i in range(num_alunos):
        print(f"\n--- Aluno {i+1} de {num_alunos} ---")
        
        nome = input(f"Digite o nome do aluno {i+1}: ")
        notas = []

        for j in range(3):

            nota = float(input(f"Digite a nota {j+1} de {nome}: "))
            while nota < 0 or nota > 10:
                print("Nota inválida!")
                nota = float(input(f"Digite a nota {j+1} de {nome}: "))
            notas.append(nota)
        
        media_aluno = sum(notas) / len(notas)
        soma_geral += media_aluno
        
        situacao = "APROVADO" if media_aluno >= 7.0 else "REPROVADO"
        
        if media_aluno >= 7.0:
            alunos_aprovados += 1
        else:
            alunos_reprovados += 1
        
        print("\n" + "-"*40)
        print(f"NOME: {nome}")
        print(f"NOTAS: {notas[0]:.1f}, {notas[1]:.1f}, {notas[2]:.1f}")
        print(f"MÉDIA: {media_aluno:.1f}")
        print(f"SITUAÇÃO: {situacao}")
        print("-"*40)
    
    if num_alunos > 0:
        media_geral = soma_geral / num_alunos
    else:
        media_geral = 0
    
    print("\n" + "="*60)
    print("RESUMO FINAL DA TURMA")
    print("="*60)
    print(f"Total de alunos: {num_alunos}")
    print(f"Alunos aprovados: {alunos_aprovados}")
    print(f"Alunos reprovados: {alunos_reprovados}")
    print(f"Média geral da turma: {media_geral:.2f}")
    if num_alunos > 0:
        if media_geral >= 9.0:
            classificacao = "EXCELENTE"
        elif media_geral >= 7.0:
            classificacao = "BOA"
        elif media_geral >= 5.0:
            classificacao = "REGULAR"
        else:
            classificacao = "FRACA"
        print(f"Classificação da turma: {classificacao}")
    
    print("="*60)

if __name__ == "__main__":
    main()


