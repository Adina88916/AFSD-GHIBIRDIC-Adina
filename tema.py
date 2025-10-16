articol = """La preluarea celui de-al doilea mandat, în prima săptămână credeam că vom continua reformele angajate în primul mandat
şi că voi putea implementa aspectele din raportul «QX», dar în câteva zile, toată logica s-a schimbat când Guvernul a intrat
într-o linie de austeritate accentuată, chiar măsuri de criză bugetar-fiscală. 
Aceste măsuri de criză fiscal-bugetară au adus o serie de schimbări care ne-au ajutat financiar să avem salarii şi burse
până la sfârşitul anului şi au provocat paradigmele vechi pe care le aveam în sistem. 
Acum, după ce ne-am stabilizat, reformele de abia de acum încep, până acum am luat măsuri de criză fiscal-bugetară. 
Între aceste reforme, învăţământul dual este fundamental pentru că noi, în educaţie, spunem că vrem să formăm competenţe, 
pentru că mai multe competenţe ne duc spre mai multe profesii şi ocupaţii, legaţi de societate şi de piaţa muncii. 
Liceele tehnologice trebuie să se transforme în timp în şcoli duale, până în anul 2029”, a afirmat Daniel David."""

mijloc = len(articol) // 2
prima_parte = articol[:mijloc]
a_doua_parte = articol[mijloc:]

prima_parte = prima_parte.upper().strip()

a_doua_parte = a_doua_parte[::-1]
punctuatie = ".,!?«»”"
for char in punctuatie:
    a_doua_parte = a_doua_parte.replace(char, "")
a_doua_parte = a_doua_parte.capitalize()

rezultat = prima_parte + a_doua_parte
print(rezultat)
