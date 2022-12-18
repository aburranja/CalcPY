import pyautogui as posicaoMouse
import pyautogui as tempoEspera

#Tempo de espera para o computador pensar
tempoEspera.sleep(2)

#Movendo o mouse até o botão iniciar
posicaoMouse.moveTo(x=670, y=1056)
tempoEspera.sleep(2)

#Clicando na posição
posicaoMouse.click(x=670, y=1056)
tempoEspera.sleep(2)

#Escrevendo a palavra Calc
posicaoMouse.typewrite('calc')
tempoEspera.sleep(1)

#Clicando na calculadora
posicaoMouse.click(x=756, y=487)
tempoEspera.sleep(2)

print(posicaoMouse.position())
