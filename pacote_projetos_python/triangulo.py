'''co = float(input(' Digite o cateto oposto : '))
ca = float(input(' Digite o cateto adjacente: '))
hi = (co ** 2 + ca ** 2) ** (1/2)
print(' a hipotenuza vai medir {:.2f} '.format(hi))'''

import math
co = float(input(' digite o cateto oposto : '))
ca = float(input(' digite o cateto adjacente: '))
hi = math.hypot(co,ca)
print(' a hipotenusa vai medir {:.2f}'.format(hi))
