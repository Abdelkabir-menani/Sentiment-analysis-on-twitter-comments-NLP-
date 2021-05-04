#!/usr/bin/env python
# coding: utf-8

# ## Importing libraries
# 

# In[37]:


# DataFrame

import pandas as pd

# Utility

import numpy as np 
from string import punctuation 
import re
import warnings
warnings.filterwarnings('ignore')

# sklearn

from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.svm import LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import BernoulliNB
from sklearn.metrics import confusion_matrix, classification_report

# nltk

import nltk
from nltk.stem import WordNetLemmatizer
from nltk import sent_tokenize, word_tokenize
from nltk.corpus import stopwords

# plotting

from wordcloud import WordCloud
import seaborn as sns
import matplotlib.pyplot as plt


# ## Importing data

# In[2]:


train = pd.read_csv('sliceddata.csv', header=0,encoding='latin', names=['target','id','date','nq','username','txt'])
test= pd.read_csv('testdata.manual.2009.06.14.csv', header=None, names=['target','id','date','nq','username','txt'])


# In[3]:


train.head(10)


# In[4]:


test= pd.read_csv('testdata.manual.2009.06.14.csv', header=None, names=['target','id','date','nq','username','txt'])


# In[5]:


train2=train[['txt', 'target']]


# In[6]:


train2.head()


# ## data preprocessing

# In[7]:


def preprocessing(text):
    urlPattern = r"((http://)[^ ]*|(https://)[^ ]*|( www\.)[^ ]*)"
    userPattern = '@[^\s]+'
    stopwords_json = {"en":["a","a's","'s","shoulda","able","about","above","according","accordingly","across","actually","after","afterwards","again","against","ain't","all","allow","allows","almost","alone","along","already","also","although","always","am","among","amongst","an","and","another","any","anybody","anyhow","anyone","anything","anyway","anyways","anywhere","apart","appear","appreciate","appropriate","are","aren't","around","as","aside","ask","asking","associated","at","available","away","awfully","b","be","became","because","become","becomes","becoming","been","before","beforehand","behind","being","believe","below","beside","besides","best","better","between","beyond","both","brief","but","by","c","c'mon","c's","came","can","can't","cannot","cant","cause","causes","certain","certainly","changes","clearly","co","com","come","comes","concerning","consequently","consider","considering","contain","containing","contains","corresponding","could","couldn't","course","currently","d","definitely","described","despite","did","didn't","different","do","does","doesn't","doing","don't","done","down","downwards","during","e","each","edu","eg","eight","either","else","elsewhere","enough","entirely","especially","et","etc","even","ever","every","everybody","everyone","everything","everywhere","ex","exactly","example","except","f","far","few","fifth","first","five","followed","following","follows","for","former","formerly","forth","four","from","further","furthermore","g","get","gets","getting","given","gives","go","goes","going","gone","got","gotten","greetings","h","had","hadn't","happens","hardly","has","hasn't","have","haven't","having","he","he's","hello","help","hence","her","here","here's","hereafter","hereby","herein","hereupon","hers","herself","hi","him","himself","his","hither","hopefully","how","howbeit","however","i","i'd","i'll","i'm","i've","ie","if","ignored","immediate","in","inasmuch","inc","indeed","indicate","indicated","indicates","inner","insofar","instead","into","inward","is","isn't","it","it'd","it'll","it's","its","itself","j","just","k","keep","keeps","kept","know","known","knows","l","last","lately","later","latter","latterly","least","less","lest","let","let's","like","liked","likely","little","look","looking","looks","ltd","m","mainly","many","may","maybe","me","mean","meanwhile","merely","might","more","moreover","most","mostly","much","must","my","myself","n","name","namely","nd","near","nearly","necessary","need","needs","neither","never","nevertheless","new","next","nine","no","nobody","non","none","noone","nor","normally","not","nothing","novel","now","nowhere","o","obviously","of","off","often","oh","ok","okay","old","on","once","one","ones","only","onto","or","other","others","otherwise","ought","our","ours","ourselves","out","outside","over","overall","own","p","particular","particularly","per","perhaps","placed","please","plus","possible","presumably","probably","provides","q","que","quite","qv","r","rather","rd","re","really","reasonably","regarding","regardless","regards","relatively","respectively","right","s","said","same","saw","say","saying","says","second","secondly","see","seeing","seem","seemed","seeming","seems","seen","self","selves","sensible","sent","serious","seriously","seven","several","shall","she","should","shouldn't","since","six","so","some","somebody","somehow","someone","something","sometime","sometimes","somewhat","somewhere","soon","sorry","specified","specify","specifying","still","sub","such","sup","sure","t","t's","take","taken","tell","tends","th","than","thank","thanks","thanx","that","that's","thats","the","their","theirs","them","themselves","then","thence","there","there's","thereafter","thereby","therefore","therein","theres","thereupon","these","they","they'd","they'll","they're","they've","think","third","this","thorough","thoroughly","those","though","three","through","throughout","thru","thus","to","together","too","took","toward","towards","tried","tries","truly","try","trying","twice","two","u","un","under","unfortunately","unless","unlikely","until","unto","up","upon","us","use","used","useful","uses","using","usually","uucp","v","value","various","very","via","viz","vs","w","want","wants","was","wasn't","way","we","we'd","we'll","we're","we've","welcome","well","went","were","weren't","what","what's","whatever","when","whence","whenever","where","where's","whereafter","whereas","whereby","wherein","whereupon","wherever","whether","which","while","whither","who","who's","whoever","whole","whom","whose","why","will","willing","wish","with","within","without","won't","n't","wonder","would","wouldn't","x","y","yes","yet","you","you'd","'d","you'll","you're","'re","you've","your","yours","yourself","yourselves","z","zero"]}
    stopwords_json_en=set(stopwords_json['en'])
    stopwords_nltk_en = set(stopwords.words('english'))
    ponct=set(punctuation)
    
    
    text= text.lower()
    text = re.sub(urlPattern,'',text)
    text = re.sub(userPattern,'',text) 
    text_list=word_tokenize(text)    
    
    text_list=[word for word in text_list if word not in stopwords_nltk_en]
    text_list=[word for word in text_list if word not in stopwords_json_en]
    text_list=[word for word in text_list if word not in ponct]
    stemmer=nltk.stem.PorterStemmer()
    for i in range (len(text_list)):
        text_list[i]=stemmer.stem(text_list[i])
    return ' '.join(text_list)


# In[8]:


train['processed_tweets'] = train['txt'].apply(lambda x: preprocessing(x))
print('Text Preprocessing complete.')


# In[9]:


train.head(10)


# word cloud for negative and positive tweets 

# In[10]:


plt.figure(figsize = (15,15)) 
wc = WordCloud(max_words = 2000 , width = 1600 , height = 800).generate(" ".join(train[train.target == 0].processed_tweets))
plt.imshow(wc , interpolation = 'bilinear')


# In[11]:


plt.figure(figsize = (15,15)) 
wc = WordCloud(max_words = 2000 , width = 1600 , height = 800).generate(" ".join(train[train.target == 4].processed_tweets))
plt.imshow(wc , interpolation = 'bilinear')


# ## Splitting Data

# In[12]:


X = train['processed_tweets'].values
y = train['target'].values


# ## Vectorization

# In[13]:


vector = TfidfVectorizer(sublinear_tf=True)
X = vector.fit_transform(X)
print(f'Vector fitted.')
print('No. of feature_words: ', len(vector.get_feature_names()))


# In[17]:


print(X.shape)
print(y.shape)


# ## Splittind data into one for training and other for validation

# In[18]:


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.20, random_state=101)


# In[19]:


print("X_train", X_train.shape)
print("y_train", y_train.shape)
print()
print("X_test", X_test.shape)
print("y_test", y_test.shape)


# ## Model Building

# ### Model evaluating function

# In[21]:


def model_Evaluate(model):
    #accuracy of model on training data
    acc_train=model.score(X_train, y_train)
    #accuracy of model on test data
    acc_test=model.score(X_test, y_test)
    
    print('Accuracy of model on training data : {}'.format(acc_train*100))
    print('Accuracy of model on testing data : {} \n'.format(acc_test*100))

    # Predict values for Test dataset
    y_pred = model.predict(X_test)

    # Print the evaluation metrics for the dataset.
    print(classification_report(y_test, y_pred))
    
    # Compute and plot the Confusion matrix
    cf_matrix = confusion_matrix(y_test, y_pred)

    categories  = ['Negative','Positive']
    group_names = ['True Neg','False Pos', 'False Neg','True Pos']
    group_percentages = ['{0:.2%}'.format(value) for value in cf_matrix.flatten() / np.sum(cf_matrix)]

    labels = [f'{v1}\n{v2}' for v1, v2 in zip(group_names,group_percentages)]
    labels = np.asarray(labels).reshape(2,2)

    sns.heatmap(cf_matrix, annot = labels, cmap = 'Reds',fmt = '',
                xticklabels = categories, yticklabels = categories)

    plt.xlabel("Predicted values", fontdict = {'size':14}, labelpad = 10)
    plt.ylabel("Actual values"   , fontdict = {'size':14}, labelpad = 10)
    plt.title ("Confusion Matrix", fontdict = {'size':18}, pad = 20)


# ### Logistic Regression

# In[31]:


lg = LogisticRegression()
history=lg.fit(X_train, y_train)
model_Evaluate(lg)


# ### Linear SVM

# In[35]:


svm = LinearSVC()
svm.fit(X_train, y_train)
model_Evaluate(svm)


# ### Random Forest

# In[38]:


rf = RandomForestClassifier(n_estimators = 20, criterion = 'entropy', max_depth=50)
rf.fit(X_train, y_train)
model_Evaluate(rf)


# ### Naive Bayes 

# In[39]:


nb = BernoulliNB()
nb.fit(X_train, y_train)
model_Evaluate(nb)


# In[ ]:




