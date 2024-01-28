nome = input("Nome do aluno:")
notas1 = float(input("Insira a primeira nota:"))
notas2 = float(input("Insira a segunda nota:"))
notas3 = float(input("Insira a terceira nota:"))
m1 = (notas1 + notas2 + notas3)/ 3

notas4 = float(input("Insira a primeira nota:"))
notas5 = float(input("Insira a segunda nota:"))
notas6 = float(input("Insira a terceira nota:"))
m2 = (notas4 + notas5 + notas6)/ 3

notas7 = float(input("Insira a primeira nota:"))
notas8 = float(input("Insira a segunda nota:"))
notas9 = float(input("Insira a terceira nota:"))
m3 = (notas7 + notas8 + notas9)/ 3
mf = (m1 + m2 + m3) / 3
print("A média final do aluno {} é {:.2f}".format(nome, mf))
