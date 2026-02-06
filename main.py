from PIL import Image
import numpy as np

img = Image.open("cookie.png")
print("rgb(123, 102, 0) pate")
print("rgb(52, 43, 0) chocolat")
print("rgb(255, 0, 0) rouge")
print()
arr = np.array(img)

lg, H = img.size
MASSE_PATE = 30
MASSE_CHOCOLAT = 10


liste_donnee = [list(arr[i][j][:-1]) for j in range(lg) for i in range(H)]
liste_pate = [(j, i) for j in range(lg) for i in range(H) 
              if list(arr[i][j][:-1]) == [123, 102, 0]]
liste_chocolat = [(j, i) for j in range(lg) for i in range(H) 
              if list(arr[i][j][:-1]) == [52, 43, 0]]

centre_masse_pate = (sum([i[0] for i in liste_pate])/len(liste_pate), 
                       sum([i[1] for i in liste_pate])/len(liste_pate))

centre_masse_chocolat = (sum([i[0] for i in liste_chocolat])/len(liste_chocolat), 
                            sum([i[1] for i in liste_chocolat])/len(liste_chocolat))



print(f"Coordonnées centre d'interie chocolat :{centre_masse_chocolat}")
print(f"Coordonnées centre d'interie pate :{centre_masse_pate}")

centre_masse_cookie = ((centre_masse_chocolat[0] * MASSE_CHOCOLAT + centre_masse_pate[0] * MASSE_PATE)/(MASSE_PATE + MASSE_CHOCOLAT),
                       (centre_masse_chocolat[1] * MASSE_CHOCOLAT + centre_masse_pate[1] * MASSE_PATE)/(MASSE_PATE + MASSE_CHOCOLAT))

print(f"Coordonnées centre d'interie cookie :{centre_masse_cookie}")

coordonnee_rouge = liste_donnee = [(j, i) for j in range(lg) for i in range(H) 
                                   if list(arr[i][j][:-1]) == [255, 0, 0]][0]

#Distance centre d' masse et croix rouge

distance_croix_rouge = np.sqrt((coordonnee_rouge[0]* 0.25 - centre_masse_cookie[0]* 0.25)**2 
                               + 
                               (coordonnee_rouge[1]* 0.25 - centre_masse_cookie[1]* 0.25)**2 ) 

print(f"Distance centre demasse et croix rouge :{distance_croix_rouge}")


"""Travail 4"""

masse_elementaire_pate = MASSE_PATE / len(liste_pate)
masse_elementaire_chocolat = MASSE_CHOCOLAT / len(liste_chocolat)

print(f"Masse élémentaire du chocolat :{masse_elementaire_chocolat} g/pixels\n"
      +
      f"Masse élémentaire du pate :{masse_elementaire_pate} g/pixels")

#moment_inertie_chocolat = moment 
