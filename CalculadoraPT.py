from pystyle import *
import pynput
from pynput.keyboard import Key, Listener
banner = '''
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
| 1 1 1 0 ╔══════════════════════════════════════════════╗ 1 0 0 1 |
| 0 1 1 0 ║ Calculadora 1.0.0.0                          ║ 0 1 0 1 |
| 0 1 0 1 ║                     Coded By Francisco Sousa ║ 1 1 0 1 |
| 1 1 0 0 ║ Instagram: francisco._sousa_                 ║ 1 0 0 0 |
| 1 0 1 1 ╚══════════════════════════════════════════════╝ 0 0 0 1 |
||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||          
'''
print(Colorate.Horizontal(Colors.red_to_green, Center.XCenter(banner)))
op=int(input('Escolha uma opcao: \n 1- Soma\n 2- Subtracao\n 3- Divisao\n 4- Media\nSua resposta: '))
if op==1:
    banner=''' 
█▀▀▀█ █▀▀▀█ █▀▄▀█ █▀▀█
▀▀▀▄▄ █░░▒█ █▒█▒█ █▄▄█
█▄▄▄█ █▄▄▄█ █░░▒█ █░▒█'''

    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
    limite_da_soma = int(input('\nQuantos numeros quer somar: '))
    for numero_da_soma in range (1, limite_da_soma+1):
        numeros = int(input('Escreve o {} numero'.format(numero_da_soma)))
        soma_dos_numeros= numero_da_soma + numeros - 1
    print('A soma dos numeros é {}'.format(soma_dos_numeros))
elif op==2:
    banner = ''' 
█▀▀▀█ █░▒█ █▀▀█ ▀▀█▀▀ █▀▀█ █▀▀█ █▀▀█ █▀▀█ █▀▀▀█
▀▀▀▄▄ █░▒█ █▀▀▄ ░▒█░░ █▄▄▀ █▄▄█ █░░░ █▄▄█ █░░▒█
█▄▄▄█ ▀▄▄▀ █▄▄█ ░▒█░░ █░▒█ █░▒█ █▄▄█ █░▒█ █▄▄▄█'''
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
    limite_da_sub = int(input('\nQuantos numeros quer subtrair: '))
    for numero_da_sub in range(1, limite_da_sub + 1):
        numeros_da_sub = int(input('Escreve o {} numero'.format(numero_da_sub)))
        sub_dos_numeros = numero_da_sub - numeros_da_sub - 1
    print('A subtracao dos numeros é {}'.format(sub_dos_numeros))
elif op==3:
    banner = ''' 
█▀▀▄ ▀█▀ █░░▒█ ▀█▀ █▀▀▀█ █▀▀█ █▀▀▀█
█░▒█ ░█░ ▒█▒█░ ░█░ ▀▀▀▄▄ █▄▄█ █░░▒█
█▄▄▀ ▄█▄ ░▀▄▀░ ▄█▄ █▄▄▄█ █░▒█ █▄▄▄█'''
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
    limite_da_div = int(input('\nQuantos numeros quer dividir: '))
    div=int(input('Por qual numero quer dividir: '))
    for numero_da_div in range(1, limite_da_div + 1):
        numeros_da_div = int(input('Escreve o {} numero'.format(numero_da_div)))
        div_dos_numeros = numero_da_div + numeros_da_div - 1
        div2=div_dos_numeros/div
    print('A divisao dos numeros é {}'.format(div2))
else:
    banner = ''' 
 █▀▄▀█ █▀▀▀ █▀▀▄ ▀█▀ █▀▀█
 █▒█▒█ █▀▀▀ █░▒█ ░█░ █▄▄█
 █░░▒█ █▄▄▄ █▄▄▀ ▄█▄ █░▒█'''
    print(Colorate.Horizontal(Colors.blue_to_purple, Center.XCenter(banner)))
    limite_da_media = int(input('\nQuantas notas quer inserir: '))
    soma_da_media = 0
    for numero_da_media in range (1, limite_da_media + 1):
        notas = int(input('Escreve a {} nota'.format(numero_da_media)))
        soma_da_media = soma_da_media + notas
    resposta_da_media = soma_da_media / limite_da_media
    print('A média das notas é {}'.format(resposta_da_media))
