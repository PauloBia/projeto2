# RPG
import random
import time
#Listas
nomes = ('Paulo', 'Luis', 'Eduardo')
classe = ('Mago', 'Arqueiro', 'Guerreiro')
elemento = ('Agua', 'Fogo', 'Ar')

#Perfil
nome_perfil = str(input('Digite o nome do personagem: '))
classe_perfil = random.choice(classe)
elemento_perfil = random.choice(elemento)

#Computador
nome_cpu = random.choice(nomes)
classe_cpu = random.choice(classe)
elemento_cpu = random.choice(elemento)

#História
print(f'''
Olá caro viajante, você está fora de sua realidade
seu objetivo será derrotar o vilão e resgatar a 
gema mágica de GoldenVille.
Primeiro, você se chama {nome_perfil} e você já irá saber sobre 
sua classe e seu elemento.''')
time.sleep(1.5)
print('Prepare-se...')
time.sleep(1.5)

print('''
Você está em um palácio, lugar esse onde tudo começa
seu objetivo será descobrir seu elemento
Fale com o mago supremo para descobrir qual 
elemento você herdou.''')
time.sleep(1.5)

print('''
Você terá 3 opções!
[1] Ir ao salão
[2] Ir ao patio
[3] Ir ao calabouço''')
escolha1 = int(input('Qual sua escolha: '))

if escolha1 == 1:
    print('Você foi ao salão e encontrou o rei, mas nada do mago supremo')
    print('Fale com o rei')
    print('''Suas opções de fala são
    [1] Onde está o mago supremo?
    [2] Sabe onde se encontra o mago supremo?''')
    fala1 = int(input('Qual sua opção: '))

    if fala1 == 1:
        print('Assim que falas com o rei?')
        print('Você perdeu!')

    elif fala1 == 2:
        print('Sim, ele está no calabouço, desça até lá')
        time.sleep(1.5)
        print(f'''Olá, vejo que me encontrou, me chamo Dormammu, O Conquistador Multidimensional
    está atrás de saber o seu elemento não é mesmo?
    primeiro segure essa taça e concentre seu poder nela

    Seu elemento é {elemento_perfil}''')
        time.sleep(1.5)
        print('Vá até a taberna gelada e descubra sua classe')

    else:
        print('Opção inválida')

elif escolha1 == 2:
    print('Você chega no pátio mas não encontra nada, desça para o calabouço!')

elif escolha1 == 3:
    print(f'''Olá, vejo que me encontrou, me chamo Dormammu, O Conquistador Multidimensional
    está atrás de saber o seu elemento não é mesmo?
    primeiro segure essa taça e concentre seu poder nela
    
    Seu elemento é {elemento_perfil}''')

    time.sleep(1.5)

    print('Vá até a taberna gelada e descubra sua classe')

else:
    print('Opção inválida')

print(f'''
Chegando a taberna...
Taberneiro: Olá, o que você deseja?
Guia: Quero saber qual a classe que esse jovem aprendiz pertence
Taberneiro: Ok, a classe desse rapaz é {classe_perfil}''')
