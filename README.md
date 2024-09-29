# Computer-Vision-Fish

Résumé de mon travail pour ce projet :

# Objectif : 
Développement de techniques d'intelligence artificielle pour la reconnaissance et la classification des poissons à partir d'images.

# Données originales :
Vidéos.

# Principales étapes suivies pour atteindre l'objectif :
## Analyse des données 
Pour assurer une meilleure qualité du traitement, nous avons effectué une analyse des vidéos. Cliquez sur [Analyse_Exploratoire.ipynb](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Analyse_Exploratoire.ipynb), pour accéder aux détails de l'analyse.
## Extraction des images à partir des vidéos 
À partir des données vidéos reçues, nous avons procédé à l'extraction d'images pour l'apprentissage automatique. Cliquez sur [Video_Images_Extraction.py](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Video_Images_Extraction.py) pour extraire les images, et sur [Extract_Quality_Images.py](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Extract_Quality_Images.py), pour trier les images de bonnes et mauvaises qualités.

## Prétraitement des images 
Les images, enregistrées dans un fichier CSV, nécessitent un prétraitement pour être compatibles avec les algorithmes d'apprentissage. Cliquez sur [Preparations_donnees.ipynb](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Preparations_donnees.ipynb), pour plus de détails.

Structure des données après la préparation :

![Texte alternatif](https://miro.medium.com/v2/resize:fit:828/format:webp/1*U-fN4t-mq8EDqfgafjM_zw.png))


## Apprentissage automatique pour la détection des poissons :
### Methode : YOLO
Cliquer sur [Yolov5_training.ipynb](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Yolov5_training.ipynb), pour entraîner nos images avec YOLO version 5. Cliquer sur [Yolov8_training.ipynb](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Yolov8_training.ipynb), pour entraîner avec YOLO version 8 de taille m et xl.

## Apprentissage automatique pour la classification des poissons :
Données deja entrainées sur une applications developpée au sein de mon laboratoire.
