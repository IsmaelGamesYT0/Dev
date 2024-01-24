print("Quero meu primeiro emprego!")

#Nome -->"Gabriel" = #Str
#Idade --> "33" = #int
#Altura --> "1.75" = #float

#boolean
is_python = True
is_java = False

#Armazenando condicoes
ingresso = 50
compradores = 250
tem_ingresso_suficiente = (ingressos >= compradores) #false
print(tem_ingresso_suficiente)

#Input = Armazena entrada de dados do usuário
#Conversão (Ou cast)

#Idade = int
#Peso = float(decimal)

#Exemplo (Input)-(int)-(float)

nome = input("Digite seu nome:")
idade = int( input("Digite sua idade: ")
peso = float( input("Digite o seu peso")

print(nome)
print(idade)
print(peso)

#Operadores
Soma = (+)
multiplicacao = (*)
divisao = (/)
potencia = (**)

#Exemplo (Operadores)

soma = 1 + 1
multiplicacao = 4 * 4
divisao = 30 / 3
potencia = 7 ** 2

print("soma", soma)
print("multiplicacao", multiplicacao)
print("divisao", divisao)
print("potencia", potencia)

#Exemplo aleatório

n1 =int(input("Primeiro número:") )

n2 =int(input("Segundo Número:") )

s = n1 + n2

print('soma igual', s)

#Condicionais

#Exemplo (Condicionais)

valor1 = 10
valor2 = 50

if valor1 > valor2:
    print(valor1, "é maior que", valor2)
else:
    print(valor2, "é maior que", valor1)

#Exemplo 2 (Condicionais)

idade =int( input("Informe sua idade: ") )

if idade >= 18:
    print("PERMITIDO!")
else:
    print("BLOQUEADO!") 

#Exemplo com salário

salario = float(input("Informe o salário: "))

if salario <= 3000:
    print("programador junior")
elif salario > 3000 and salario <= 6000:
    print("programador pleno")
elif salario > 6000 and salario <= 15000:
    print("programador senior")
else:
    print("gerente de projetos")

#Listas

#Exemplo 1 (Listas)

lista_numeros  = [1, 2, 3]
         index:   0, 1, 2 

print(lista_numeros[0])
print(lista_numeros[1])
print(lista_numeros[2])    

#Exemplo 2 (Listas)

lista_vazia = []

lista_vazia.append("Olá")
lista_vazia.append("Mundo")

print(lista_vazia)

#Exemplos de Listas

Métodos|Parâmetros|Resultado|Descrição
append = item     = mutador = #Acrescenta um novo item no final da lista
insert = posição/ = mutador = #Insere um novo item na posição dada
         item 
pop    = nenhum   = híbrido = #Remove e returno o último item
pop    = posição  = híbrido = #Remove e retorna o item da posição
sort   = nenhum   = mutador = #Ordena a lista
reverse= nenhum   = mutador = #Ordena a lista em ordem reversa
index  = item     = retorna = #Retorna a posição da primeira ocorrência do item
                      idx
count  = item     = retorna = #Retorna o número de ocorrências do item
                       ct
remove = item     = mutador = #Remove a primeira ocorrência do item

#Exemplo 3 (Listas)

numeros = [10, 9, 8, 7, 6]

print( "total:", len(numeros) )
print( "menor valor:", min(numeros) )
print( "maior valor:", max(numeros) )

#Repetições

For   = #Loop que percorre sequências,repetindo ações para cada elemento.
While = #Loop que executa ações enquanto a condição for verdadeira.

#Exemplo (While) = #Repetições

while (True):
    print("Se eu rodar o script meu pc morre") 

#Exemplo 2 (Repetições)

notas = []

codigo_aluno = input("RM: ")
nota = float(input("Nota: "))
resultado = [codigo_aluno, nota]
notas.append(resultado)

#Exemplo 3 (Simplificado) - (Repetições)

notas = []

for x in range(3):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print( "quantidade de notas", len(notas) )

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O RM", codigo_aluno, "tirou a nota", nota)


#Exemplo com o (While)

notas = []

contador = 1

while contador <= 5:
    codigo_aluno = n[0]
    nota = n[1]
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    #alternativa: contador += 1
    contador = contador + 1

print( "quantidade de notas", len(notas) )


#Exemplo 4(Repetições)]

for x in range(5)

x = #valor alterado para cada repetição
    #pode ser usada apenas dentro do bloco de repetição

-range(5) = [0, 1, 2, 3, 4]
-nesse caso,possui 5 itens


#Dicionários(ou objetos) - [Objetos/Dict]

pessoa = {
    "nome": "Programador Python",
    "Idade": 17,
    "peso": 53.3
}

print( pessoa['nome'] )
print( pessoa['idade'] )
print( pessoa['peso'] )

#Dicionais usam chave e valor para armazenar informações

variavel = {
    "chave": "valor",
}

#Exemplo em jogo


# informações do jogar
player = {
    "nome": "Ismael",
    "level": 1,
    "hp": 100,
    "exp": 0,
    "dano": 5,
}

#lista de inimigos
npcs = [
    { "nome": "Monstrinho", "dano": 2, "hp": 50, "exp": 5},
    { "nome": "Monstro", "dano": 5, "hp": 100, "exp": 10},
    { "nome": "Monstrão", "dano": 10, "hp": 150, "exp": 15},
    { "nome": "Chefão", "dano": 25, "hp": 200, "exp": 20},
]
