n = coordenadas
p1 = re.compile('\["1",')
p2 = re.compile('\] -')
m = p1.sub('POINT(',n)
coordenadas = p2.sub('),',m)


def repl(n):
  