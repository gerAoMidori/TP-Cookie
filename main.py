"""   (123, 102, 0) -----> pate
      (52, 43, 0)   -----> chocolat
      (255, 0, 0)   -----> croix rouge

      size : A 2-tuple, containing (width, height) in pixels. (Source -----> https://pillow.readthedocs.io/en/stable/reference/Image.html#PIL.Image.new)

"""
from calc import distance_x_y
from PIL import Image
import numpy as np

img = Image.open("cookie.png")
arr = np.array(img)

lg, H = img.size
MASSE_PATE = 30
MASSE_CHOCOLAT = 10


liste_donnee = [list(arr[i][j][:-1]) for j in range(lg) for i in range(H)]

liste_pate = [(j, i) for j in range(lg) for i in range(H) 
              if list(arr[i][j][:-1]) == [123, 102, 0]]

liste_chocolat = [(j, i) for j in range(lg) for i in range(H) 
              if list(arr[i][j][:-1]) == [52, 43, 0]]

NOMBRE_CHOCOLAT = len(liste_chocolat)
NOMBRE_PATE = len(liste_pate)

centre_masse_pate = (sum([i[0] for i in liste_pate])/NOMBRE_PATE, 
                       sum([i[1] for i in liste_pate])/NOMBRE_PATE)

centre_masse_chocolat = (sum([i[0] for i in liste_chocolat])/NOMBRE_CHOCOLAT, 
                            sum([i[1] for i in liste_chocolat])/NOMBRE_CHOCOLAT)

print(f"Coordonnées centre d'interie chocolat :{centre_masse_chocolat}")
print(f"Coordonnées centre d'interie pate :{centre_masse_pate}")

centre_masse_cookie = ((centre_masse_chocolat[0] * MASSE_CHOCOLAT + centre_masse_pate[0] * MASSE_PATE)/(MASSE_PATE + MASSE_CHOCOLAT),
                       (centre_masse_chocolat[1] * MASSE_CHOCOLAT + centre_masse_pate[1] * MASSE_PATE)/(MASSE_PATE + MASSE_CHOCOLAT))

print(f"Coordonnées centre d'interie cookie :{centre_masse_cookie}")

coordonnee_rouge = liste_donnee = [(j, i) for j in range(lg) for i in range(H) 
                                   if list(arr[i][j][:-1]) == [255, 0, 0]][0]

#Distance centre de masse et croix rouge

distance_croix_rouge = np.sqrt(distance_x_y(coordonnee_rouge, centre_masse_cookie)) 

print(f"Distance centre demasse et croix rouge :{distance_croix_rouge}")


"""Travail 4"""

masse_elementaire_pate = MASSE_PATE / NOMBRE_PATE
masse_elementaire_chocolat = MASSE_CHOCOLAT / NOMBRE_CHOCOLAT

print(f"Masse élémentaire du chocolat :{masse_elementaire_chocolat} g/pixels")
print(f"Masse élémentaire du pate :{masse_elementaire_pate} g/pixels")


moment_inertie_chocolat = (sum([distance_x_y(i, coordonnee_rouge) * masse_elementaire_chocolat for i in liste_chocolat]))
moment_inertie_pate = (sum([distance_x_y(i, coordonnee_rouge) * masse_elementaire_pate for i in liste_pate]))
moment_inertie_cookie= moment_inertie_chocolat + moment_inertie_pate

print(f"Moment d'inertie du chocolat :{moment_inertie_chocolat} kg.mm2")
print(f"Moment d'inertie de la pate :{moment_inertie_pate} kg.mm2")
print(f"Moment d'inertie du cookie :{moment_inertie_cookie} kg.mm2")


"""Travail 5"""

