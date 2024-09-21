# Computer-Vision-Fish

Voici le resumee de mon travail Pour ce projet :
# Objectif : 
Développement des techniques d’intelligence artificielle
pour la reconnaissance et la classification des poissons à
partir d’images

# Donnees originales : 
Videos

# Principales etapes suivi pour arriver a l'objectif :
## Analyse des donnees
Pour une meilleur suivi de qualite, nous avons analysees les videos. Cliquez sur [Analyse_Exploratoire.ipynb](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Analyse_Exploratoire.ipynb) , l'analyse faite.
## Extractions des images a partir des videos :
Avec un nombre des donnees videos recus, nous devons passer a l'extraction des images pour l'apprentissage automatique. cliquez sur [Video_Images_Extraction.py](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Video_Images_Extraction.py) pour extraire les images. et cliquer sur [Extract_Quality_Images.py](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Extract_Quality_Images.py)

## Pretraitement des images :
Les images enregistree dans un fichier csv ont besoins de pretraitement  pour qu'il soit compatible avec l'usage de d'apprentissage. cliquer sur [Preparations_donnees.ipynb](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Preparations_donnees.ipynb), pour le detail.

![Texte alternatif](https://miro.medium.com/v2/resize:fit:828/format:webp/1*U-fN4t-mq8EDqfgafjM_zw.png))


## Apprentissage automatique pour la detection :
### Methode 1 : YOLO
Cliquer sur [Yolov5_training.ipynb](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Yolov5_training.ipynb), pour entrainer nos images avec YOLO version 5. Cliquer sur [Yolov8_training.ipynb](https://github.com/Mikael1226/Computer-Vision-Fish/blob/main/Yolov8_training.ipynb), pour entrainer avec YOLO version 8.
### Methode 2 : Detectron2
