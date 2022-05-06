nota1 = int(input("Digite a nota do 1º aluno"))
nota2 = int(input("Digite a nota do 2º aluno"))
nota3 = int(input("Digite a nota do 3º aluno"))
nota4 = int(input("Digite a nota do 4º aluno"))
notas_juntas = nota4 + nota3 + nota2  + nota1
media = notas_juntas / 4
listas_alunos = [nota1,nota2,nota3,nota4]
print(f"As notas foram dos alunos foram {listas_alunos} e a media deles foram de {media}")
