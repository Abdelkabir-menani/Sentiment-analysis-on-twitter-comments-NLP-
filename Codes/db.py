our_list=[]
        for x in collec.find():
            our_list.append(x)    
        df=pd.DataFrame(our_list)

        new_model=tf.keras.models.load_model (r'.\codes\static\twitter_bert')

        tokenizerSaved = bert.tokenization.FullTokenizer(
            vocab_file=os.path.join(r'.\codes\static\twitter_bert', r'assets\vocab.txt'),
            do_lower_case=False)

        
        l=[]
        for x in range(len(df.txt.values)):
            inputs = bert_encode(string_list=list(df.txt.values[x]), 
                                tokenizer=tokenizerSaved, 
                                max_seq_length=240)
            m=4
            prediction= new_model.predict(inputs)
            if np.argmax(prediction)>0.5:
                pass
            else:
                m=0
            print(df.txt.values[x],' is: ', m)
            l.append(m)
        df['target']=l
        replies_cnt=len(df)
        total_likes=''
        for i in range (len(a[0][2])):
            if a[0][2][i].isnumeric():
                total_likes+=a[0][2][i]
        Quote_Tweets=''
        for i in range (len(a[0][4])):
            if a[0][4][i].isnumeric():
                Quote_Tweets+=a[0][4][i]
        retweet_cnt=a[0][3]
        prop=[total_likes,Quote_Tweets,replies_cnt,retweet_cnt]
        print(df.head(9))
        print(total_likes,' ',Quote_Tweets,' ',replies_cnt,' ' ,retweet_cnt )














        replies_cnt=len(df)
    total_likes=''
    for i in range (len(a[0][2])):
        if a[0][2][i].isnumeric():
            total_likes+=a[0][2][i]
    Quote_Tweets=''
    for i in range (len(a[0][4])):
        if a[0][4][i].isnumeric():
            Quote_Tweets+=a[0][4][i]
    retweet_cnt=a[0][3]
    prop=[total_likes,Quote_Tweets,replies_cnt,retweet_cnt]
    print(df.head(9))
    print(total_likes,' ',Quote_Tweets,' ',replies_cnt,' ' ,retweet_cnt )