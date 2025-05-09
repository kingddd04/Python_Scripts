import random

Selettore_di_Soggetto = random.randint(0, 100)
Selettore_di_Verbo = random.randint(0, 70)
Selettore_di_Complemento_oggetto = random.randint(0, 100)

Soggetto = {
0: "la casa",
1: "la vecchia",
2: "la noia",
3: "il piccione",
4: "la gatta",
5: "l'alieno", 
6: "la cometa",
7: "la matematica",
8: "la fiera",
9: "la maestra",
10: "l'ufficio",
11: "la tempesta",
12: "tua mamma",
13: "la matematica",
14: "il sole",
15: "il dinosauro",
16: "la banca",
17: "l'albero",
18: "la cantina",
19: "il capodanno",
20: "la gallina",
21: "l'aereo",
22: "il veleno",
23: "la mattina",
24: "la notte",
25: "la sera",
26: "la vicina",
27: "la fortuna",
28: "Davide",
29: "il mare",
30: "la montagna",
31: "la luna",
32: "l'orto",
33: "la guerra",
34: "Bianca",
35: "l'infinito",
36: "l'ananas",
37: "la ricchezza",
38: "la mela",
39: "la pasta",
40: "la palestra",
41: "il profumo",
42: "il negozio",
43: "la Russia",
44: "il porto",
45: "la pigrizia",
46: "il letto",
47: "il campo",
48: "la rispota",
49: "Paolo",
50: "la chitarra",
51: "la palestra",
52: "Valerio",
53: "Eleonora",
54: "la libreria",
55: "il vento",
56: "il futuro",
57: "la luce",
58: "la lanterna",
59: "la piscina",
60: "la festa",
61: "Il lavoro",
62: "La scuola",
63: "La cena",
64: "L'Italia",
65: "il soffitto",
66: "il passato",
67: "il borgo",
68: "Andrea",
69: "il risultato",
70: "il segreto",
71: "la sorella",
72: "la morte",
73: "Giulia",
74: "la neve",
75: "Il pappagallo",
76: "la città",
77: "la torre",
78: "la strada",
79: "la polvere",
80: "la pioggia",
81: "il serpente",
82: "il computer",
83: "il sale",
84: "la filosofia",
85: "la storia",
86: "il padre",
87: "l'antenato",
88: "il sosso",
89: "il sas",
90: "il film",
91: "il robot",
92: "la maschera",
93: "la nave",
94: "lo xilofono",
95: "Il razzo",
96: "il bosco",
97: "il pianoforte",
98: "il secchio",
99: "il pozzo",
100: "la televisione"
}

Verbo = {
0: "insultava",
1: "distruggeva",
2: "mescolava",
3: "vedeva",
4: "giocava",
5: "allontanava", 
6: "raggiungeva",
7: "provava",
8: "era",
9: "aveva",
10: "sembrava",
11: "costruiva",
12: "bruciava",
13: "Odiava",
14: "Amava",
15: "prendeva",
16: "rubava",
17: "salutava",
18: "zappava",
19: "colpiva",
20: "faceva sorridere",
21: "Faceva esplodere",
22: "Faceva Sorridere",
23: "rompeva",
24: "uccideva",
25: "illuminava",
26: "restituiva",
27: "Aiutava",
28: "aveva ricevuto",
29: "costruiva",
30: "Pregava",
31: "buttava",
32: "vinceva",
33: "raccontava",
34: "temeva",
35: "faceva",
36: "fermava",
37: "accelerava",
38: "irrigava",
39: "Faceva addormentare",
40: "sosteneva",
41: "invadeva",
42: "sognava",
43: "voleva ottenere",
44: "rivelava",
45: "spiegava",
46: "vendeva",
47: "traduceva",
48: "forniva",
49: "lanciava",
50: "faceva volare",
51: "abbatteva",
52: "bruciava",
53: "Imprigionava",
54: "otteneva",
55: "perdeva",
56: "completava",
57: "annientava",
58: "finiva",
59: "separava",
60: "riuniva",
61: "incontrava",
62: "riuniva",
63: "generava",
64: "voleva beme",
65: "demoliva",
66: "aspettava",
67: "suonava",
68: "sparava",
69: "caricava",
70: "magiava"
}

Complemento_Oggetto = {
0: "la casa",
1: "la vecchia",
2: "la noia",
3: "il piccione",
4: "la gatta",
5: "l'alieno", 
6: "la cometa",
7: "la matematica",
8: "la fiera",
9: "la maestra",
10: "l'ufficio",
11: "la tempesta",
12: "tua mamma",
13: "la matematica",
14: "il sole",
15: "il dinosauro",
16: "la banca",
17: "l'albero",
18: "la cantina",
19: "il capodanno",
20: "la gallina",
21: "l'aereo",
22: "il veleno",
23: "la mattina",
24: "la notte",
25: "la sera",
26: "la vicina",
27: "la fortuna",
28: "Davide",
29: "il mare",
30: "la montagna",
31: "la luna",
32: "l'orto",
33: "la guerra",
34: "Bianca",
35: "l'infinito",
36: "l'ananas",
37: "la ricchezza",
38: "la mela",
39: "la pasta",
40: "la palestra",
41: "il profumo",
42: "il negozio",
43: "la Russia",
44: "il porto",
45: "la pigrizia",
46: "il letto",
47: "il campo",
48: "la rispota",
49: "Paolo",
50: "la chitarra",
51: "la palestra",
52: "Valerio",
53: "Eleonora",
54: "la libreria",
55: "il vento",
56: "il futuro",
57: "la luce",
58: "la lanterna",
59: "la piscina",
60: "la festa",
61: "Il lavoro",
62: "La scuola",
63: "La cena",
64: "L'Italia",
65: "il soffitto",
66: "il passato",
67: "il borgo",
68: "Andrea",
69: "il risultato",
70: "il segreto",
71: "la sorella",
72: "la morte",
73: "Giulia",
74: "la neve",
75: "Il pappagallo",
76: "la città",
77: "la torre",
78: "la strada",
79: "la polvere",
80: "la pioggia",
81: "il serpente",
82: "il computer",
83: "il sale",
84: "la filosofia",
85: "la storia",
86: "il padre",
87: "l'antenato",
88: "il sosso",
89: "il sas",
90: "il film",
91: "il robot",
92: "la maschera",
93: "la nave",
94: "lo xilofono",
95: "Il razzo",
96: "il bosco",
97: "il pianoforte",
98: "il secchio",
99: "il pozzo",
100: "la televisione"
}



print(Soggetto[Selettore_di_Soggetto]+str(" ")+Verbo[Selettore_di_Verbo]+str(" ")+Complemento_Oggetto[Selettore_di_Complemento_oggetto])