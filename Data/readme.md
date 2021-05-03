# Identification des sources de données :

On a choisi une base de données connu dans la littérature sous le nom Sentiment140. 
Cette source de données se comporte de deux fichiers csv l’un d’apprentissage et l’autre du test.
Ils se component de 6 columns :

0 – target: la polarite du tweet (0 = negative, 4 = positive)

1 – id : L’id du tweet 

2 – date : La date du tweet 

3 – query : the query 

4 – username : L’utilisateur de celui qui a posté le tweet

5 – txt : Le texte du tweet 

Voici un extrait de notre data qui compose de 10 lignes et 6 colonnes (target, id, date, query, username, txt) :
![Picture1.png](https://github.com/Abdelkabir-menani/Test_project/blob/main/Images/Picture1.png)

Voilà leurs types :

![Picture2.png](https://github.com/Abdelkabir-menani/Test_project/blob/main/Images/Picture2.png)

Cette base de données a été automatiquement extraite par opposition à ce que les humains annotent chaque tweet avec sa polarité. Dans leur approche, on supposait que tout tweet avec des émoticônes positives, comme :), était positif, et les tweets avec des émoticônes négatives comme :(, étaient négatifs. Et on a utilisé l'API Twitter Search pour collecter ces tweets en utilisant la recherche par mot-clé.
