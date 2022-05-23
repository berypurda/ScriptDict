# Szkriptnyelvek 3. gyak feladat

- Írj egy **parkereso** függvényt, ami 2 listát vár paraméterül (egy fiú, és egy lány lista), és egy dictionary-t ad vissza.
- A feladat egy dictionary-t visszaadni, amiben minden fiúnak talál egy lány párt. Ha nem egyforma méretű listákat kap, térjen vissza **false**-al.
- 3 dolog alapján kell párosítani, első a legfontosabb, ha az nem lehetséges, akkor a második, ha az sem, akkor az utolsó kritériumot kell figyelembe venni:
- 1. Azonos kezdőbetű (ha több van, akkor az első találat)
- 2. Mindkét név i-re végződik (becenévként van megadva)
- 3. Közeli név hosszúság (a legrövidebb nevű fiút a legrövidebb nevű lánnyal, stb. Ha több van, akkor az első találat)

FONTOS: Fiúknak keressük a lány párokat, fordított sorrendben máshogy működne a feladat.

Példák:

`input: ["Barnabás", "István", "Dávid", "Dani", "Béla"], ["Bernadett", "Mónika", "Lili", "Lea", "Anikó"]`

`output: {"Barnabás" : "Bernadett", "Dani" : "Lili", "István" : "Mónika", "Dávid" : "Anikó", "Béla" : "Lea"}`

`input: ["Barnabás"], [] `

` output: False`

