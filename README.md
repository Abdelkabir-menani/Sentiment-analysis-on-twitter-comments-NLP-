# Test_project


# Plan :
I.	Présentation du projet et ses objectifs
II.	Outils et librairies utilisés :
1.	Outils utilises
2.	Libraries utilises
III.	Identification des sources de données
IV.	Démarche d'implémentation du projet
1.	Data Viz
2.	Data prep
3.	Conception et Modélisation 
4.	Implémentation des scrapers et API de collection


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

#### BeautifulSoup : 

Beautiful Soup est une bibliothèque Python d'analyse syntaxique de documents HTML et XML créée par Leonard Richardson. Elle produit un arbre syntaxique qui peut être utilisé pour chercher des éléments ou les modifier. Lorsque le document HTML ou XML est mal formé (par exemple s'il manque des balises fermantes), Beautiful Soup propose une approche à base d'heuristiques afin de reconstituer l'arbre syntaxique sans générer d'erreurs. Cette approche est aussi utilisée par les navigateurs web modernes. Elle est disponible pour Python 2.7 et Python 3.

#### Django :
Django est une infrastructure d'application (aussi appelé Framework) côté serveur extrêmement populaire et dotée de beaucoup de fonctionnalités, écrite en Python. 
Django vous aide à écrire une application qui est :

##### Complète

Django suit la philosophie "Piles incluses" et fournit presque tout ce que les développeurs pourraient vouloir faire. Comme tout ce dont vous avez besoin est une partie de ce "produit", tout fonctionne parfaitement ensemble, suivant des principes de conception cohérents, il possède également une documentation complète et à jour.

##### Polyvalent

Django peut être (et a été) utilisé pour créer presque tous les genres de sites — du gestionnaire de données aux wikis, jusqu'aux réseaux sociaux et aux sites d'actualités. Il peut fonctionner avec n'importe quelle infrastructure côté client, et peut renvoyer des données dans quasiment n'importe quel format (notamment HTML, RSS, JSON, XML, etc). Le site sur lequel vous lisez en ce moment est basé sur Django !

Tandis qu'il fournit presque toutes les fonctionnalités dont vous pourriez avoir besoin (comme des bases de données populaires, des moteurs de modélisation, etc.), il peut tout de même être étendu pour utiliser d'autres composants si besoin.

##### Sécurisé

Django aide les développeurs à éviter les erreurs de sécurité classique en fournissant une infrastructure conçue pour "faire ce qu'il faut" pour protéger les sites internet automatiquement. Par exemple, Django fournit un moyen sécurisé pour gérer les comptes des utilisateurs ainsi que leurs mots de passe, évitant les erreurs classiques comme mettre des informations sur la session dans des cookies, où elles sont vulnérables (à la place les cookies contiennent seulement une clé, et les données sont stockées dans la base de données), ou directement stocker des mots de passe, au lieu de mot de passe hachés.

Un mot de passé haché est une valeur dont la longueur est fixée, créée en envoyant le mot de passe à travers une fonction de hachage cryptographique. Django peut vérifier si un mot de passe entré est correct en l'envoyant dans la fonction de hachage et en comparant le retour avec la valeur stockée dans la base de données. De ce fait, la nature unidirectionnelle de la fonction rend difficile pour un attaquant de retrouver le mot de passe d'origine, même si la valeur hachée est compromise.

Django active par défaut la protection contre beaucoup de vulnérabilités, comme les injections SQL, le cross-site scripting, le cross-site request forgery et le clickjacking (voir Website security pour plus de détails sur ce genre d'attaques).

##### Scalable

Django utilise une architecture composite "shared-nothing" (chaque composant de l'architecture est indépendant des autres, et peut ainsi être remplacé ou changé si besoin). En ayant des séparations nettes entres les différentes parties, Django peut se scaler lors d'une hausse de trafic en ajoutant du hardware à tous les niveaux : serveurs cache, serveurs de base de données, serveurs d'application. Certains des sites les plus fréquentés ont réussi à scaler Django pour répondre à leur demande (par exemple, Instagram et Disqus pour ne nommer qu'eux deux).

##### Maintenable

Les principes de design du code Django encouragent la création d'un code simple à maintenir et réutilisable. Il fait notamment appel à la philosophie du Ne Vous Répétez Pas (DRY pour Don't Repeat Yourself en anglais), afin d'éviter toute duplication superflue, réduisant la taille de votre code. Django promeut aussi le regroupement de fonctionnalités reliées entre elles en "applications" réutilisables et, à un plus bas niveau, regroupe des lignes de code dépendantes entre elles en modules (suivant les lignes du motif d'architecture Modèle-vue-contrôleur (MVC)).

##### Portable

Django est écrit en Python, qui fonctionne sous diverses plateformes. Cela veut dire que vous ne serez plus contraint par une plateforme en particulier, et vous pourrez faire fonctionner vos applications sous autant de versions de Linux, Windows et Mac OS X que vous le souhaitez. De plus, Django est très bien supporté par plusieurs fournisseurs d'hébergement web, qui offrent souvent des infrastructures et de la documentation spécifiques pour héberger des sites Django.

#### Natural Language Toolkit (NLTK) :
NLTK est une bibliothèque de fonctions dédiées au traitement automatique du langage naturel au sens large, le but étant de couvrir toutes les manipulations informatiques sur les langues naturelles : calcul de fréquences de mots sur des corpus, apprentissage, construction de représentations syntaxiques et sémantiques. La suite fournit des modules et des corpus (corpus libres ou parties libres de certains corpus). Cette suite se base sur le langage de programmation Python. 

#### Pandas :
Pandas est une librairie python qui permet de manipuler facilement des données à analyser :
•	Manipuler des tableaux de données avec des étiquettes de variables (colonnes) et d'individus (lignes).
•	Ces tableaux sont appelés DataFrames, similaires aux dataframes sous R.
•	On peut facilement lire et écrire ces dataframes à partir ou vers un fichier tabulé.
•	On peut faciler tracer des graphes à partir de ces DataFrames grâce à matplotlib.

#### Seaborn et matplotlib :
Ils sont des librairies de python qui permettent de visualisation des données. 

#### Sklearn :
Est une Librairie de python qui permet la manipulation des modèles de machine Learning.

## III.	Identification des sources de données :
see folder /Data.

## IV.	Démarche d'implémentation du projet

### 1.	Data Viz:

see folder /Data_viz.

### 2.	Data prep

see folder /Data_prep.

