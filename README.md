# Plan :
I.	Présentation du projet et ses objectifs

II.	Outils et librairies utilisés :

1.	Outils utilises

2.	Libraries utilises

III.	Identification des sources de données

IV.	Démarche d'implémentation du projet

1.	Data visualisation du training dataset

1-1.	Introduction

1-2. Etude des variables

V.	Démarche d'implémentation du projet

VI.	L’entrainement du dataset:

   6-1-1. Le modèle choisi :

   6-1-2 : Bert : Comment ça marche ?

   6-1-3 : Les entrées du modèle :

   6-1-4 Les sorties du modèle :

   6-1-5 : Le modèle spécifique pour la classification :

  6-2 : Implémentation du code du modèle Bert :
  
   6-2-1-Importation du modèle :
   
   6-2-2-Data preprocessing :
   
 VII.	Web scraping :
 
 VIII.	Le stockage des données :
 
 IX.	Dashboard :
 
 X.	Création de l’application web :
 
 XI.	Conclusion


## I.	Présentation du projet et ses objectis :
On a travaillé sur un projet qui porte le nom de "Sentiment analysis sur les commentaires twitter et web scraping".
Il est dédié aux entreprises qui exploitent le réseau social Twitter pour se communiquer avec ses clients et présenter ses différents services afin de l’aider à savoir si ses clients aime ou déteste ses services.
 Le projet se comporte de deux phases principales. La première se comporte sur le sentiment analysis et la création d’un modèle de prédiction si un commentaire sur twitter est positif ou négatif.
La deuxième se comporte sur la création d’une application web qui permet de savoir si un post sur Twitter a des réactions positifs ou négatifs sur la plateforme en utilisant le web scraping pour la collecte des données et Django pour le développement de l’application.

## II.	Outils et librairies utilisés :

### 1-Outils :

#### Web scraping :
Les outils du web scraping sont des logiciels, c’est-à-dire des bots programmés pour examiner les bases de données et extraire des informations. Une grande variété de types de bots sont utilisés, dont beaucoup sont entièrement personnalisables pour :
•	Reconnaître les structures de sites HTML uniques.
•	Extraire et transformer du contenu.
•	Stockez les données.
•	Extraire les données des API.
#### Natural language processing (NLP) :
Le NLP (Natural Language Processing) est une branche de l’intelligence artificielle qui s’occupe particulièrement du traitement du langage écrit aussi appelé avec le nom français TALN (traitement automatique du langage naturel). En bref, c’est tout ce qui est lié au langage humain et au traitement de celui-ci par des outils informatiques.
Le NLP peut être divisé en 2 grandes parties, le NLU (Natural Language Understanding) et le NLG (Natural Language Generation).
•	Le premier est toute la partie « compréhension » du texte, prendre un texte en entrée et pouvoir en ressortir des données.
•	Le second, est générer du texte à partir de données, pouvoir construire des phrases cohérentes de manière automatique.

### 2-Librairies utilisés :

#### Selenium : 

Selenium est un outil d’automatisation de navigateur web. Il permet donc d’écrire, de manière plus ou moins assistée, des scripts dont l’exécution réalisera automatiquement des actions dans un navigateur web : visiter une page, cliquer sur un lien, remplir un formulaire, etc. et de récupérer les résultats de ces actions.
WebDriver est inclus dans Selenium. Nous allons l’utiliser dans la suite.
WebDriver est basé sur un modèle client-serveur. Un client de test envoie des "commandes" via des requêtes HTTP à un serveur WebDriver après initialisation d’une session. Ce dernier distribue les commandes auprès des drivers des navigateurs concernés. Ces drivers exécutent les commandes sur les navigateurs en question via des mécanismes d’automatisation internes, de l’OS ou du JS. C’est en réalité plus compliqué que cela, car ces drivers peuvent eux-mêmes être des serveurs WebDriver (Internet Explorer), communiquer via des web sockets (Safari), etc. Le driver n’est pas nécessairement un binaire, les drivers de Firefox et de Safari sont des extensions du navigateur par exemple.

#### Flask :

Flask est un micro framework open-source de développement web en Python. Il est classé comme microframework car il est très léger. Flask a pour objectif de garder un noyau simple mais extensible. Il n'intègre pas de système d'authentification, pas de couche d'abstraction de base de données, ni d'outil de validation de formulaires. Cependant, de nombreuses extensions permettent d'ajouter facilement des fonctionnalités. 

#### Tensorflow :

TensorFlow est une bibliothèque open source de Machine Learning, créée par Google, permettant de développer et d’exécuter des applications de Machine Learning et de Deep Learning. Elle permet d’entraîner et d’exécuter des réseaux de neurones pour la classification de chiffres écrits à la main, la reconnaissance d’image, les plongements de mots, les réseaux de neurones récurrents, les modèles sequence-to-sequence pour la traduction automatique, ou encore le traitement naturel du langage.

#### Dash plotly :

Dash est une bibliothèque Python Open Source permettant de créer des applications Web réactives. Dash a commencé comme une preuve de concept publique sur GitHub il y a 2 ans. Cette bibliothèque va nous permettre de créer une dashboard inter-réactif dans notre application web avec les différentes graphiques possibles des résultats de notre étude.

#### Pandas :

Pandas est une librairie python qui permet de manipuler facilement des données à analyser :
•	Manipuler des tableaux de données avec des étiquettes de variables (colonnes) et d'individus (lignes).
•	Ces tableaux sont appelés DataFrames, similaires aux dataframes sous R.
•	On peut facilement lire et écrire ces dataframes à partir ou vers un fichier tabulé.
•	On peut faciler tracer des graphes à partir de ces DataFrames grâce à matplotlib.

#### Seaborn et matplotlib :

Ils sont des librairies de python qui permettent de visualisation des données. 



## III.	Identification des sources de données pour l'entrainement:

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

![Screenshot_1.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_1.png)

Voilà leurs types :

![Screenshot_2.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_2.png)

Cette base de données a été automatiquement extraite par opposition à ce que les humains annotent chaque tweet avec sa polarité. Dans leur approche, on supposait que tout tweet avec des émoticônes positives, comme :), était positif, et les tweets avec des émoticônes négatives comme :(, étaient négatifs. Et on a utilisé l'API Twitter Search pour collecter ces tweets en utilisant la recherche par mot-clé.

## IV.	Démarche d'implémentation du projet

### 1.	Data visualisation du training dataset:

#### 1-1. Introduction :

De nos jours, les entreprises ont pris conscience de la véritable valeur de la donnée. En l'exploitant, elles peuvent, désormais, améliorer leur compréhension des motivations des consommateurs, des conditions de leur marché, mais, également, mieux contrôler leur réputation sur le marché. Mais les résultats sont encore plus pertinents avec une solution « Data Viz ». Cette dernière étant définit comme une façon de représenter l'information sous forme graphique, en mettant en évidence les modèles et les tendances des données afin d’aider des collaborateurs et des décideurs à se faire rapidement une idée. Passons à l’utilisation de cet outil adapté au contexte d’actualité. En cas de besoin d’éclairage ou de plus de détails sur certaines parties, vous êtes invité à consulter le fichier code, joint à ce rapport.

#### 1-1. Etude des variables :

##### Variable target :

Variable target est une variable qualitative nominal qui est la variable cible dans notre étude. Elle est composée de deux modalités : 0 pour un tweet négatif et 4 pour un tweet positif.

![Screenshot_3.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_3.png)

Ce diagramme ci-dessus représente les pourcentages respectifs des tweets positives et les tweets négatives dans notre data. On a choisi de collecter nos données de façon que les nombres des tweets positives et des tweets négatives sont égaux, cela pour avoir une équivalence dans la sélection de notre modèle.

##### Variable txt :

La variable txt est une variable qualitative nominal qui porte le contenu des tweets sous forme de texte, puisque cette variable est de type texte, c’est plus compliqué de faire la visualisation de ses données. C’est pour cela on a créé une variable quantitative appelle ‘lenght’ qui représente la longueur de texte des tweets. 

![Screenshot_4.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_4.png)

A gauche, on observe les différentes valeurs de statistique descriptive de la variable lenght pour les tweets positives, on remarque qu’on a 800000 tweets positives, et que le minimum de la longueur de texte d’un tweet positive est un caractère et pour le max c’est 64 caractères. Ce graphe ci-dessus représente la distribution de la longueur du texte des tweets positives.

![Screenshot_5.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_5.png)

A gauche, on observe les différentes valeurs de statistique descriptive de la variable lenght pour les tweets negative, on remarque qu’on a 800000 tweets negative, et que le minimum de la longueur de texte d’un tweet negative est un caractère et pour le max c’est 57 caractères. Ce graphe ci-dessus représente la distribution de la longueur du texte des tweets positives.

##### Variable usernames:

Variable usernames est une variable qualitative nominal qui représente l’utilisateur qui a publie le tweet soit positive soit négative.
On voulait savoir la liste des utilisateurs qui ont publié le plus des tweets positives et négatives dans notre dataset :

![Screenshot_6.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_6.png)

Dans le graphique ci-dessus, on remarque que what_bugs_u est l’utilisateur qui a publié le plus des tweets positives avec un nombre de tweet égal 246. Ainsi la liste du top 10 utilisateurs qui publient des tweets positives.

![Screenshot_7.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_7.png)

Dans le graphique ci-dessus, on remarque que lost_dog est l’utilisateur qui a publié le plus des tweets negatives avec un nombre de tweet égal 550. Ainsi la liste du top 10 utilisateurs qui publient des tweets negatives.

## V.	Environnement de travail :

En voyant le sujet, nous pensions à utiliser le langage de programmation : Python. Nous étions libres de choisir le langage que nous désirions, mais nos tuteurs nous ont confirmé que l’utilisation de Python serait sûrement plus judicieuse grâce à la multitude de bibliothèques présentes pour le data science. Nous avons décidé d’utiliser la version 3.7 et nous avons choisi VsCode comme IDE et Jupyter notebook.

![Screenshot_8.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_8.png)

## VI.	L’entrainement du dataset:

#### 6-1-1 : Le modèle choisi :

Après l’étude de plusieurs algorithme de machine learning et du deep learning, depuis la régression linéaire, Naive bayes, Randomforest .. passant par les modèle des réseaux de neurones : les CNN puis les RNN et finalement les transformers, et à partir de l’étude de tout ces modèles, on a choisi de travailler sur le modèle BERT(Bidirectional Encoder Representations from Transformers) qui est un transformer développé par google qui se compose d’une pile d’encoders de Transformers entraînés conditionné à la fois par le contexte gauche et droit ce qui le permet d’être parfait pour ce genre de tâches qui sont en relation avec le langage puisque ce genre d’entrainement le permet de bien comprendre le contexte des phrases ce qui nous donne de bon résultats.

#### 6-1-2 : Bert : Comment ça marche ?

Il existe deux tailles de modèles pour BERT :
BERT BASE de taille comparable à celle de l’OpenAI Transformer (1) afin de comparer les performances.
BERT LARGE, un modèle beaucoup plus grand qui a atteint l’état de l’art des résultats rapportés dans l’article du BERT (2).

![Screenshot_9.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_9.png)

Les deux modèles BERT ont un grand nombre de couches d’encodeurs (appellées Transformer Block dans l’article d’origine) : douze pour la version de base, et vingt-quatre pour la version large. Ils ont également des réseaux feedforward plus grands (768 et 1024 unités cachées respectivement) et plus de têtes d’attention (12 et 16 respectivement) que la configuration par défaut dans l’implémentation initial du Transformer de Vaswani et al. (6 couches de codeurs, 512 unités cachées, et 8 têtes d’attention).

Depuis d’autres tailles de modèles ont été créé pour BERT, allant de 4.4 millions de paramètres pour le BERT-Tiny (utilisable sur un CPU), à 1270M pour le XLarge. Un tableau récapitulatif des modèles plus petits que le BERT Base :

![Screenshot_10.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_10.png)

Tableau issu de la publication de Iulia Turc et al(3).

#### 6-1-3 : Les entrées du modèle :

![Screenshot_11.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_11.png)

Le premier token d’entrée est un jeton spécial [CLS] pour des raisons qui apparaîtront plus tard. CLS est ici l’abréviation de classification.
Tout comme l’encodeur du Transformer, BERT prend une séquence de mots en entrée qui remonte dans la pile. Chaque couche applique l’auto-attention et transmet ses résultats à un réseau feed-forward, puis les transmet à l’encodeur suivant comme la figure ci-dessous :

![Screenshot_12.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_12.png)

L’architecture est identique au Transformer jusqu’à présent (à part la taille, qui sont juste des configurations que nous pouvons définir).
L’entrainement de Bert se fait dans deux étapes principales à savoir le pré-entrainement et le fine tuning.
On explique premièrement comment le pré-entrainement se passe.
Trouver la bonne manière d’entraîner une pile d’encodeurs est un obstacle complexe que BERT résout en adoptant un concept de « modèle de langage masqué » (Masked LM en anglais) tiré de la littérature antérieure (il s’agit d’une Cloze task). Cette procédure consiste à prendre aléatoirement 15% des tokens en entrée puis à masquer 80% d’entre eux, en remplacer 10% par un autre token complètement aléatoire (un autre mot) et de ne rien faire dans le cas des 10% restant. L’objectif est que le modèle prédise correctement le token original modifié (via la perte d’entropie croisée). Le modèle est donc obligé de conserver une représentation contextuelle distributionnelle de chaque jeton d’entrée.

![Screenshot_13.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_13.png)

Afin d’améliorer BERT dans la gestion des relations existant entre plusieurs phrases, le processus de pré-entraînement comprend une tâche supplémentaire : étant donné deux phrases (A et B), B est-il susceptible d’être la phrase qui suit A, ou non ? cette phase est nommée next sentence prediction.

![Screenshot_14.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_14.png)

La deuxième tâche sur laquelle BERT est pré-entraîné est une tâche de classification. La tokenisation est simplifiée à l’extrême dans ce graphique car BERT utilise en fait WordPieces comme tokens plutôt que des mots. Ainsi certains mots sont décomposés en plus petits morceaux.
En gros le pré-entrainement du modèle permet de BERT à comprendre le langage humain et de saisir le contexte des phrases. Sa représentation est la suivante :

![Screenshot_15.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_15.png)

#### 6-1-4 : Les sorties du modèle :

Chaque position fournit un vecteur de taille hidden_size (768 dans BERT Base). Pour l’exemple de classification des phrases que nous avons examiné ci-dessus, nous nous concentrons uniquement sur la sortie de la première position (à laquelle nous avons passé le jeton spécial [CLS]).

![Screenshot_16.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_16.png)

Ce vecteur peut maintenant être utilisé comme entrée pour un classifieur de notre choix. L’article obtient d’excellents résultats en utilisant simplement un réseau neuronal à une seule couche comme classifieur.

![Screenshot_17.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_17.png)

Alors après la phase du pré-entrainement on passe à la phase du fine-tuning qui n’est autre que personnaliser notre modèle pour faire une tâche spécifique.

#### 6-1-5 : Le modèle spécifique pour la classification :

E représente l’embedding d’entrée, Ti rereprésente la représentation contextuelle du token, [CLS] est le symbole spécial pour la sortie de la classification, et [SEP] est le symbole spécial pour séparer les séquences de tokens non consécutives.

![Screenshot_18.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_18.png)

Et c’est exactement ce modèle qu’on a implémenter en python en utilisant la bibliothèque tensorflow.

### 6-2 : Implémentation du code du modèle Bert :

#### 6-2-1 : Importation du modèle :

Après l’importation de tous les bibliothèques qu’on va utilisé on importe notre dataset et prend juste 0.05 de la taille totale du dataset pour l’entrainement afin de ne pas tomber dans un problème du temps, puis on précise notre X la variable explicative (txt dans notre cas) et Y la variable cible (target dans notre cas) et puis on les décompose en groupe d’entrainement et groupe de test et finalement on définit les encoder.

![Screenshot_19.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_19.png)

Importation du modèle BERT-cased pré-entrainé :

![Screenshot_20.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_20.png)

#### 6-2-2 : Data preprocessing :

Premièrement, on importe les outils qu’on va utiliser pour le prétraitement.

fulltokenizer : pour transformer les phrases en tokens.

vocab_file : le corpus utlisée dans le pré-entrainement de Bert de la langue anglaise

do_lower_case : Pour omettre la casse. 

![Screenshot_21.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_21.png)

Le modèle s'attend à ce que ses deux phrases d'entrée soient concaténées. Cette entrée doit commencer par un token [CLS] « Ceci est un problème de classification » et chaque phrase doit se terminer par un jeton [SEP] « Séparateur » :

![Screenshot_22.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_22.png)

On prend la première phrase de notre dataset comme exemple :

![Screenshot_23.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_23.png)

On ajoute les trois inputs du modèle à savoir input_word_ids, input_mask et input_type et on forme la fonction bert_encode :

![Screenshot_24.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_24.png)

Après l’ajout de quelques hyperparamètres, on compile notre modèle et on entraine ses hyperparamètres, le résultat nous donne un modèle avec +89% de précision :

![Screenshot_25.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_25.png)

Après on l’enregistre pour qu’on puisse l’utiliser dans la prédiction dans l’application web :

![Screenshot_26.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_26.png)

## VII.	Web scraping :

Il y’a beaucoup d’outils qui existent pour faire le web scraping comme scrapy, beautiful_soup et beaucoup d’autres outils, mais pour faire le web scraping pour une page html dynamique (il faut scroller au-dessous pour que les commentaires d’un post se télécharge), on a choisi Selenium qui permet de Controller le navigateur en utilisant le driver chromdriver pour effectuer des commandes automatiques comme le scroll etc..

![Screenshot_27.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_27.png)
![Screenshot_28.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_28.png)

Ces deux fonctions permettent de collecter toutes les commentaires d’un tweet donné et d’autres informations (comme le nom d’utilisateur, la date..) tout en saisissant le lien du post comme input.

## VIII.	Le stockage des données :

Après la collecte des données, c’est nécessaire de stocker notre base de données pour toute utilisation ultérieure. On a achevé cela avec MongoDb qui stocke les données dans des collections.

![Screenshot_29.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_29.png)

Notre base de données enregistre la data collectée comme suit :

![Screenshot_30.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_30.png)

## IX.	Dashboard :

On réalise notre dashboard à l’aide de la bibliothèque dash plotly.

![Screenshot_31.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_31.png)

La page principale est ci-dessous, elle est composée de 5 tabs principaux.
La première donne un échantillon des données collectés avec leur prédictions (soit positive :4 ou négative :0).

![Screenshot_32.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_32.png)

La deuxième montre le word cloud des tweets positives et négatives selon le choix de l’utilisateur :

![Screenshot_33.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_33.png)

![Screenshot_34.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_34.png)

Le troisième concerne le distplot de la longueur des tweets positives et négatives selon la densité :

![Screenshot_35.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_35.png)

Le quatrième nous donne une pie chart de la distribution des tweets positives et négatives. Ce graphique nous permet de savoir si l’utilisateur aime ou déprécie le post donné en input.

![Screenshot_36.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_36.png)

Ici par exemple 89.5% des personnes ont commenter avec un tweet positif et juste 10.5% ont commenter avec un tweet négatif. Donc, on peut déduire que ce post à un sentiment positif sur les gens.

Le cinquième graphique est l’histogramme qui définit la longueur des tweets positives et négatives selon la fréquence :

![Screenshot_37.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_37.png)

X.	Création de l’application web :
Maintenant nous avons tout ce qu’est est requis pour créer une application web dont on peut présenter les résultats de l’apprentissage automatique et de l’analyse des sentiments.

Nous avons décidé d’utiliser Flask durant ce processus. Flask est un petit framework Web Python qui fournit des outils et des fonctionnalités utiles qui facilitent la création d'applications Web en Python. Il offre de la flexibilité aux développeurs et constitue un cadre plus accessible pour les nouveaux développeurs, car vous pouvez créer rapidement une application Web en utilisant un seul fichier Python. Flask est également extensible et ne force pas une structure de répertoire particulière ou ne nécessite pas de code compliqué avant de commencer.

Après avoir installé Flask on commence avec les étapes de création de l’application et de faire la connexion avec toutes les autres composantes qu’on a déjà fait.
Premièrement, on construit une application de base flask dans le main.py

![Screenshot_38.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_38.png)

Puis on ajoute tous les bluprints des pages qu’on va utiliser dans l’application web sur init.py, on a juste 2 blueprints dans notre cas : home et pagee

![Screenshot_39.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_39.png)

Puis, on effectue une commande post dans la fonction Home pour extraire le lien que l’utilisateur saisit et on le donne comme input pour la fonction qui fait du web scraping, après on stocke les données restituées dans notre collection dans Mongodb puis on load notre modèle bert pour la prédiction des sentiments des commentaires du post et finalement on retourne la page html page1.

![Screenshot_40.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_40.png)
![Screenshot_41.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_41.png)

La page principale de l’application web Flask est comme suit, on saisit le lien du post, s’il est valable, on fait automatiquement toutes les instructions expliqués précédemment.

![Screenshot_42.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_42.png)

Et quand toutes les instructions sont terminées avec succès, l’application retourne la page 2.

![Screenshot_43.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_43.png)

Quand on clique sur Dashboard en haut, le dashboard qu’on a détaillé auparavant s’affiche.

![Screenshot_44.png](https://github.com/Abdelkabir-menani/Sentiment-analysis-on-twitter-comments/blob/main/Images/Screenshot_44.png)

## XI.	Conclusion :

De nos jours, l'analyse des sentiments ou l'exploration d'opinions est un sujet brûlant en apprentissage automatique. Nous sommes encore loin de détecter très précisément les sentiments d'un corpus de textes en raison de la complexité dans la langue anglaise et encore plus si l'on considère d'autres langues telles que Chinois.
Dans ce projet, on a essayé de faciliter aux entreprises la connaissance des sentiments de leurs clients utilisateurs de twitter envers un post donné dans la platforme en utilisant le modèle BERT tout en l’intégrant dans une application web et finalement une dashboard qui facilite la compréhension des résultats. 
