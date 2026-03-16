from collections import deque

def bfs(przepustowosc, sasiedzi, zrodlo, ujscie, rodzic):
    odwiedzone = [False] * len(przepustowosc)
    kolejka = deque([zrodlo])
    odwiedzone[zrodlo] = True
    rodzic[zrodlo] = -1

    while kolejka:
        u = kolejka.popleft()

        for v in sasiedzi[u]:
            if not odwiedzone[v] and przepustowosc[u][v] > 0:
                odwiedzone[v] = True
                rodzic[v] = u
                kolejka.append(v)

                if v == ujscie:
                    return True

    return False


def edmonds_karp(liczba_wierzcholkow, krawedzie, zrodlo, ujscie):
    przepustowosc = [[0] * liczba_wierzcholkow for _ in range(liczba_wierzcholkow)]
    sasiedzi = [[] for _ in range(liczba_wierzcholkow)]

    for poczatek, koniec, wartosc in krawedzie:
        przepustowosc[poczatek][koniec] += wartosc
        sasiedzi[poczatek].append(koniec)
        sasiedzi[koniec].append(poczatek)

    rodzic = [-1] * liczba_wierzcholkow
    maksymalny_przeplyw = 0

    while bfs(przepustowosc, sasiedzi, zrodlo, ujscie, rodzic):
        przeplyw_sciezki = float("inf")
        v = ujscie

        while v != zrodlo:
            u = rodzic[v]
            przeplyw_sciezki = min(przeplyw_sciezki, przepustowosc[u][v])
            v = u

        v = ujscie
        while v != zrodlo:
            u = rodzic[v]
            przepustowosc[u][v] -= przeplyw_sciezki
            przepustowosc[v][u] += przeplyw_sciezki
            v = u

        maksymalny_przeplyw += przeplyw_sciezki

    return maksymalny_przeplyw


liczba_wierzcholkow = int(input("Podaj liczbę wierzchołków: "))
liczba_krawedzi = int(input("Podaj liczbę krawędzi: "))

krawedzie = []

print("Podawaj krawędzie w formacie: początek koniec przepustowość")
for _ in range(liczba_krawedzi):
    poczatek, koniec, wartosc = map(int, input().split())
    krawedzie.append((poczatek, koniec, wartosc))

zrodlo = int(input("Podaj zródło: "))
ujscie = int(input("Podaj ujście: "))

wynik = edmonds_karp(liczba_wierzcholkow, krawedzie, zrodlo, ujscie)
print("Maksymalny przepływ:", wynik)