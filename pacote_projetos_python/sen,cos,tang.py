import math
an = float(input(' Digite um angulo: '))
seno = math.sin(math.radians(an))
print('O angulo de {} o seno desse angilo e {:.2f} '.format(an,seno))
cosseno = math.cos(math.radians(an))
print('O angulo de {} tem o cosseno {:.2f} '.format(an,cosseno))
tan = math.tan(math.radians(an))
print(' O angulo de {} tem a tangente de {:.2f}'.format(an,tan))