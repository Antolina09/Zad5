import math

def czytanie_z_pliku(plik_do_wczytania):
    tablica = []
    text_file = open(plik_do_wczytania, "r+")
    for line in text_file.readlines():
         tablica.extend(line.split())
    ilosc_zadan =  int(tablica[0])
    ilosc_maszyn = int(tablica[1])
    index = 2
    zadania_dla_maszyn = [[] for i in range(int(ilosc_maszyn))]
    while index < (ilosc_maszyn*ilosc_zadan +2):
        for k in range(ilosc_maszyn):
            zadania_dla_maszyn[k].append(int(tablica[index]))
            index+=1
    text_file.close()
    return zadania_dla_maszyn

def przepisanie_wart(tab):
    tab_temp = [[] for i in range(len(tab))]
    for i in range(len(tab)):
        for j in range(len(tab[0])):
            tab_temp[i].insert(j,tab[i][j])
    return tab_temp

def min_r(r):
    min = r[0]
    indeks = 0
    for i in range(len(r)):
        if r[i] < min:
            min =  r[i]
            indeks = i
    return min, indeks

def max_q(q):
    max = q[0]
    indeks = 0
    for i in range(len(q)):
        if q[i] > max:
            max =  q[i]
            indeks = i
    return max, indeks

def schrageeee(r,p,q):
    class problem_rpq:
        def __init__(self):
            self.r=[]
            self.p=[]
            self.q=[]
 
    class problem_rpq_ost:
        r=int(1e20)
        p=int(1e20)
        q=int(1e20)

    l_nn=problem_rpq()
    l_ng=problem_rpq()
    ost_kolejka=problem_rpq_ost()
 
    for x in range (len(r)):
        l_nn.r.append(r[x])
        l_nn.p.append(p[x])
        l_nn.q.append(q[x])

    akt_q=-1 #poczatkowo ekstremalnie male

    cmax=0
    indeks_zadania=-1
 
    t=min(l_nn.r)

    #wg pseudokodu, schrage z przerwaniami
    while l_nn.r.__len__() != 0 or l_ng.r.__len__() != 0: #koniec jezeli oba puste
        while l_nn.r.__len__() != 0 and min(l_nn.r) <= t: #bo ostatni przypadek rozstrzyga, ze l_nn.r == 0, wiec false
            indeks_zadania=l_nn.r.index(min(l_nn.r))
            l_ng.r.append(l_nn.r.pop(indeks_zadania))
            l_ng.p.append(l_nn.p.pop(indeks_zadania))
            l_ng.q.append(l_nn.q.pop(indeks_zadania))
 
            if l_ng.q[len(l_ng.q)-1] > ost_kolejka.q:
                ost_kolejka.p= t - l_ng.r[len(l_ng.q)-1]
                t = l_ng.r[len(l_ng.q)-1]
 
                if ost_kolejka.p >0:
                    l_ng.r.append(ost_kolejka.r)
                    l_ng.p.append(ost_kolejka.p)
                    l_ng.q.append(ost_kolejka.q)
 
        if l_ng.r.__len__() == 0:
            t=min(l_nn.r)
 
        else:
            akt_q = max(l_ng.q)
            indeks_zadania = l_ng.q.index(akt_q)
 
            ost_kolejka.r=l_ng.r.pop(indeks_zadania)
            ost_kolejka.p=l_ng.p.pop(indeks_zadania)
            ost_kolejka.q=l_ng.q.pop(indeks_zadania)
 
            t = t + ost_kolejka.p
            if cmax < t + ost_kolejka.q:
                cmax= t+ost_kolejka.q
    #print(cmax)
    return cmax

def Schrage(zadania):
    cmax = 0
    zadania_gotowe = [[],[],[]]
    zadania_niegotowe = zadania
    kolejnosc=[[],[],[]]
    t = min_r(zadania_niegotowe[0])[0]

    while zadania_gotowe != [[],[],[]] or zadania_niegotowe != [[],[],[]]:
        while zadania_niegotowe != [[],[],[]] and min_r(zadania_niegotowe[0])[0] <= t:
            indeks1 = min_r(zadania_niegotowe[0])[1]

            zadania_gotowe[0].append(zadania_niegotowe[0][indeks1])
            zadania_gotowe[1].append(zadania_niegotowe[1][indeks1])
            zadania_gotowe[2].append(zadania_niegotowe[2][indeks1])

            zadania_niegotowe[0].pop(indeks1)
            zadania_niegotowe[1].pop(indeks1)
            zadania_niegotowe[2].pop(indeks1)

        if zadania_gotowe == [[],[],[]]:
            t = min_r(zadania_niegotowe[0])[0] 
        else:
            max_czas, indeks2 = max_q(zadania_gotowe[2])

            t = t + zadania_gotowe[1][indeks2]
            kolejnosc[0].append(zadania_gotowe[0][indeks2])
            kolejnosc[1].append(zadania_gotowe[1][indeks2])
            kolejnosc[2].append(zadania_gotowe[2][indeks2])

            zadania_gotowe[0].pop(indeks2)
            zadania_gotowe[1].pop(indeks2)
            zadania_gotowe[2].pop(indeks2)
            cmax = max(cmax,t+max_czas)

    #print('cmax',cmax)
    #print('kol',kolejnosc)
    #print(max_czas)
    return cmax, kolejnosc 

def SchragePMTN(zadania):
    kol = przepisanie_wart(zadania)
    cmax = 0
    zadania_gotowe = [[],[],[]]
    zadania_niegotowe = zadania
    t, l = 0, 0 
    #q0 = 1e300*1e300

    while zadania_gotowe != [[],[],[]] or zadania_niegotowe != [[],[],[]]:
        while zadania_niegotowe != [[],[],[]] and min_r(zadania_niegotowe[0])[0] <= t:
            indeks1 = min_r(zadania_niegotowe[0])[1]
            zadania_gotowe[0].append(zadania_niegotowe[0][indeks1])
            zadania_gotowe[1].append(zadania_niegotowe[1][indeks1])
            zadania_gotowe[2].append(zadania_niegotowe[2][indeks1])

            zadania_niegotowe[0].pop(indeks1)
            zadania_niegotowe[1].pop(indeks1)
            zadania_niegotowe[2].pop(indeks1)
            
            if zadania_gotowe[2][-1] > zadania_gotowe[2][l]:
                zadania_gotowe[1][l] = t - zadania_gotowe[0][-1]
                t = zadania_gotowe[0][-1]
                if zadania_gotowe[1][l] > 0:
                    zadania_gotowe[0].append(zadania_gotowe[0][l])
                    zadania_gotowe[1].append(zadania_gotowe[1][l])
                    zadania_gotowe[2].append(zadania_gotowe[2][l])
            
        if zadania_gotowe == [[],[],[]]: 
            t = min_r(zadania_niegotowe[0])[0] 
        else:
            max_czas, indeks2 = max_q(zadania_gotowe[2])

            l = indeks2
            t = t + zadania_gotowe[1][indeks2]
            zadania_gotowe[0].pop(indeks2)
            zadania_gotowe[1].pop(indeks2)
            zadania_gotowe[2].pop(indeks2)
            cmax = max(cmax,t+max_czas)
    #print(cmax)
    return cmax, kol

def licz_abc(zadania):
    cmax,kol = Schrage(zadania)
    cb = kol[0][0] + kol[1][0]

    for i in range(1,len(kol[0])):
        if kol[0][i] > cb:
            cb += kol[0][i] - cb + kol[1][i]
        else:
            cb += kol[1][i]
        if cb + kol[2][i] == cmax:
            b = i

    cb = kol[0][0] + kol[1][0]
    a = 0
    for i in range(1,b+1):
        if kol[0][i] > cb:
            a = i
            cb += kol[0][i] - cb + kol[1][i]
        else:
            cb += kol[1][i]

    cos, kont = 0, 0
    for i in range(b-1,a-1,-1):
        if kol[2][i] < kol[2][b]:
            c = i
        else:
            cos += i
        kont += i
    if cos == kont:
        c = 'nieint'
    return b, c, kol, cmax

def Carlier(zadania,ub):
    UB = ub
    b, c, kol, U = licz_abc(zadania)
    tab = przepisanie_wart(kol)
    tab[0].insert(0,UB)
    kolejnosc = []

    pprim = 0
    
    if U < UB:
        UB = U
        kolejnosc = przepisanie_wart(kol)
    
    if type(c) != int:
        if kolejnosc != []:
            kolejnosc[0].insert(0,UB)
            return kolejnosc
        else:
            kol[0].insert(0,UB)
            return kol

    rprim = min(kol[0][c+1:b+1])
    qprim = min(kol[2][c+1:b+1])
    
    for i in range(c+1,b+1):
        pprim = pprim + kol[1][i]
    
    rpic = kol[0][c]
    kol[0][c] = max(kol[0][c], rprim + pprim)

    r = kol[0]
    p = kol[1]
    q = kol[2]
    LB = schrageeee(r,p,q)

    if LB < UB:
        tab2 = Carlier(kol,LB)
        UB = tab2[0][0]
        tab2[0].pop(0)
        kol = przepisanie_wart(tab2)


    kol[0][c] = rpic
    
    qpic = kol[2][c]
    kol[2][c] = max(kol[2][c], qprim + pprim)

    r = kol[0]
    p = kol[1]
    q = kol[2]
    LB = schrageeee(r,p,q)


    tab = przepisanie_wart(kol)
    tab.insert(0,UB)

    if LB < UB:
        tab3 = Carlier(kol,LB)
        UB = tab3[0][0]
        tab3[0].pop(0)
        kol = przepisanie_wart(tab3)
    
    kol[2][c] = qpic

    tab = przepisanie_wart(kol)
    tab[0].insert(0,LB)
    print('cmax ost',LB)
    return tab

zadania = czytanie_z_pliku("intest.txt")
ub = math.inf
Carlier(zadania,ub)
