''' Rouletteomat
Inhaltliches Ziel ist die Wahrscheinlichkeiten zu möglichen Einsätzen im Roulettespiel aufzuzeigen.
'''
alleZahlen = 37
einsatz = -1
auszahlung = input('Möchten Sie auf eine Zahl setzen?(Ja/Nein)')

if auszahlung == 'Ja':
    auszahlung = 36
    benZahlen = 1
else:
    auszahlung = 1
    benZahlen = 18

gewinnwahrscheinlichkeit = benZahlen / alleZahlen
verlustwahrscheinlichkeit = (alleZahlen - benZahlen) / alleZahlen
gewinnerwartung = (gewinnwahrscheinlichkeit * auszahlung) + (verlustwahrscheinlichkeit * einsatz)

print(f'Ihre Gewinnerwartung ist: {gewinnerwartung}\n Die Gewinnwahrscheinlichkeit ist: {gewinnwahrscheinlichkeit}\n Die Verlustwahrscheinlichkeit ist: {verlustwahrscheinlichkeit} ')