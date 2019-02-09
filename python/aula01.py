import os

def gprint(msg):
    w = os.get_terminal_size().columns
    h = os.get_terminal_size().lines
    t = ''
    for i in range(w):
        t = t + '█'
    print(t) 
    g = '█'
    espaco = ((w - len(msg)) - 2)/2       
    for i in range(int(espaco)):
        g = g + ' '
    g = g + msg
    for i in range(int(espaco)):
        g = g + ' '
    g = g + '█'   
    print(g)
    print(t) 

gprint('OLÁ MUNDO!!!')    


