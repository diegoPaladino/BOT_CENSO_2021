# f_test

import pyautogui as p

# sexo = input(p.prompt('sexo = '))
sexo = p.prompt('qual o sexo = ')

if sexo == 'f':
    print('foi digitado feminino')
else:
    print('foi digitado masculino')