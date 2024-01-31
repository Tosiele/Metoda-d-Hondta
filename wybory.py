mandatyA = 0
mandatyB = 0
mandatyC = 0
mandatyD = 0

dzielenieA = 1
dzielenieB = 1
dzielenieC = 1
dzielenieD = 1

A = 47
B = 30
C = 12
D = 15

partie = [['A', 'B', 'C', 'D'], [A, B, C, D]]
dzielenie = [dzielenieA, dzielenieB, dzielenieC, dzielenieD]
mandaty = [mandatyA, mandatyB, mandatyC, mandatyD]


ileMandatow = int(input("Podaj liczbę dostępnych mandatów: "))

for i in range(1, ileMandatow + 1):
    print("\nteraz rozdamy " + str(i) + " mandat")
    
    idMax = partie[1].index(max(partie[1])) #znajdujemy partię z największą ilocią poparcia i pobieramy jej indeks
    
    print(str(i) + " madat dostaje partia " + partie[0][idMax])
    
    dzielenie[idMax] += 1 #zwiększamy dzielenie o 1
    
    partie[1][idMax] = partie[1][idMax] / dzielenie[idMax] #liczbę poparcia parti z maksymalną ilocią głosów dzielimy na tyle na ile jeszcze nie była dzielona
    
    
    mandaty[idMax] += 1 #przydzielamy mandat
    
print("\nA: " + str(mandaty[0]) + " B: " + str(mandaty[1]) + " C " + str(mandaty[2]) + " D " + str(mandaty[3]))
