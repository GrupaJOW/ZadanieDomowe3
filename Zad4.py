def dfs(graf, i, ujscie, obecny_przeplyw, odwiedzone):
    # Warunek stopu - dotarlismy do ujscia
    if i == ujscie:
        return obecny_przeplyw

    odwiedzone.add(i)

    # Przeszukujemy sasiadow wierzcholka i
    for j, przepustowosc in graf[i].items():
        # Szukamy nieodwiedzonego sasiada z wolna przepustowoscia
        if j not in odwiedzone and przepustowosc > 0:
            
            min_przepustowosc = min(obecny_przeplyw, przepustowosc)
            przeplyw = dfs(graf, j, ujscie, min_przepustowosc, odwiedzone)

            # Aktualizacja przepustowosci (siec resztkowa)
            if przeplyw > 0:
                graf[i][j] -= przeplyw
                graf[j][i] += przeplyw
                return przeplyw

    return 0

def ford_fulkerson(graf, zrodlo, ujscie):
    # Dodanie krawedzi powrotnych o przepustowosci 0
    for i in list(graf.keys()):
        for j in list(graf[i].keys()):
            if j not in graf:
                graf[j] = {}
            if i not in graf[j]:
                graf[j][i] = 0 

    max_przeplyw = 0
    
    # Glowna petla szukajaca sciezek
    while True:
        odwiedzone = set()
        przeplyw = dfs(graf, zrodlo, ujscie, float('inf'), odwiedzone)
        
        # Koniec, gdy brak sciezki powiekszajacej
        if przeplyw == 0:
            break
            
        max_przeplyw += przeplyw

    return max_przeplyw

# --- PRZYKLAD UZYCIA ---

graf_slownik = {
    0: {1: 16, 2: 13},
    1: {2: 10, 3: 12},
    2: {1: 4, 4: 14},
    3: {2: 9, 5: 20},
    4: {3: 7, 5: 4},
    5: {} 
}

graf_2 = {
    0: {1: 10, 2: 5},
    1: {2: 15, 3: 10},
    2: {3: 10},
    3: {}
}

graf_3 = {
    0: {1: 100, 2: 100},
    1: {2: 1, 3: 100},
    2: {3: 100},
    3: {}
}

wynik = ford_fulkerson(graf_slownik, 0, 5)
print(f"Maksymalny przeplyw wynosi: {wynik}")
print(f"Maksymalny przeplyw (Graf 2) wynosi: {ford_fulkerson(graf_2, 0, 3)}")
print(f"Maksymalny przeplyw (Graf 3) wynosi: {ford_fulkerson(graf_3, 0, 3)}")