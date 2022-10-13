
# coding: utf-8

# In[2]:

get_ipython().system('pip install  python-Levenshtein')


# In[28]:

import yake 
from rake_nltk import Rake
import nltk
from  textblob import Word
import textblob
import pandas as pd
import numpy as np 
import re
import string
from nltk.corpus import stopwords
import fuzzywuzzy
from fuzzywuzzy import fuzz
from fuzzywuzzy import process


# In[25]:

def yake_kw_extract(text,language='en',max_ngram_size=5,dedupplication_threshold=0.9,numOfKeywords=10):
    """keyword extraction using yake"""
    custom_extractor = yake.KeywordExtractor(lan=language,
                                         n=max_ngram_size,
                                         dedupLim = dedupplication_threshold,
                                        top=numOfKeywords,
                                        features=None)
    kws=custom_extractor.extract_keywords(c_text)
    return kws


# In[24]:

def rake_kw_extract(text,scope=10):
    """extraction of ranked phrases"""
    rake_nltk_var = Rake()
    rake_nltk_var.extract_keywords_from_text(text)
    kws = rake_nltk_var.get_ranked_phrases()[:scope]
    return kws


# In[ ]:

def rake_kw_extract_scores(text,scope=10):
    '''extraction of keyword with score values'''
    rake_nltk_var = Rake()
    rake_nltk_var.extract_keywords_from_text(text)
    kws = rake_nltk_var.get_ranked_phrases_with_scores()
    return kws


# In[ ]:

# Old  version that was using separeted cdata frames based on 3 filter basis, that were used to separated the data frames
#into 3 different ones. Since by abandoned that approach this approach is no longer valid this version of the fucntion is deprecated.
# please use the below one.

# def profanity_check(df):
#     """profanity check flagger for data frame, using on whole df,
#     created profanity lists won't be accesibile outside this function"""
#     profanity_file_customer = pd.read_excel("files/Keywords_List_Customer_Advisor.xlsx", sheet_name="Customer Keywords")
#     profanity_file_advisor = pd.read_excel("files/Keywords_List_Customer_Advisor.xlsx", sheet_name="Advisor Keywords")
#     customer_profanity=list(profanity_file_customer['Customer Speech Part'])
#     advisor_profanity=list(profanity_file_advisor['Advisor Speech Part'])
#     simultaneous_profanity = list(set(customer_profanity+advisor_profanity)) #casting as set and list to avoid dupes
#     df["clean_text_spell_checked"] = df.clean_text.apply(lambda txt:''.join(textblob.TextBlob(txt).correct()))
    
#     def customer_profanity_flag(column):
#         convo_words = nltk.word_tokenize(column)
#         for word in convo_words:
#             if word.lower() in customer_profanity:
#                 return "Customer Profanity"
#             else:
#                 return "No Profanity"
            
#     def advisor_profanity_flag(column):
#             adv_words = nltk.word_tokenize(column)
#             for word in adv_words:
#                 if word.lower() in advisor_profanity:
#                     return "Advisor Profanity"
#                 else:
#                     return "No Profanity"
    
#     def sim_profanity_flag(column):
#         sim_words = nltk.word_tokenize(column)
#         for word in sim_words:
#                 if word.lower() in simultaneous_profanity:
#                     return "Simultaneous Profanity"
#                 else:
#                     return "No Profanity"
        
        
        
                
    

#     customer = df[df['speaker'] == "Customer"]
#     advisor = df[df['speaker'] == "Agent"]
#     simultaneous = df[df['speaker'] == "simultaneous"]
    
#     customer["ProfanityFlag"] = customer['clean_text_spell_checked'].apply(customer_profanity_flag)
#     advisor["ProfanityFlag"] = advisor['clean_text_spell_checked'].apply(advisor_profanity_flag)
#     simultaneous["ProfanityFlag"] = simultaneous['clean_text_spell_checked'].apply(advisor_profanity_flag)
#     concatenated = pd.concat([customer,advisor,simultaneous])
    
#     return concatenated.sort_index()


# In[ ]:

def profanity_check(df):
    """profanity check flagger for data frame, using on whole df,
    created profanity lists won't be accesibile outside this function"""
    profanity_file_customer = pd.read_excel("files/Keywords_List_Customer_Advisor.xlsx", sheet_name="Customer Keywords")
    profanity_file_advisor = pd.read_excel("files/Keywords_List_Customer_Advisor.xlsx", sheet_name="Advisor Keywords")
    customer_profanity=list(profanity_file_customer['Customer Speech Part'])
    advisor_profanity=list(profanity_file_advisor['Advisor Speech Part'])
    simultaneous_profanity = lisdef profanity_check(df):
#     """profanity check flagger for data frame, using on whole df,
#     created profanity lists won't be accesibile outside this function"""
#     profanity_file_customer = pd.read_excel("files/Keywords_List_Customer_Advisor.xlsx", sheet_name="Customer Keywords")
#     profanity_file_advisor = pd.read_excel("files/Keywords_List_Customer_Advisor.xlsx", sheet_name="Advisor Keywords")
#     customer_profanity=list(profanity_file_customer['Customer Speech Part'])
#     advisor_profanity=list(profanity_file_advisor['Advisor Speech Part'])
#     simultaneous_profanity = list(set(customer_profanity+advisor_profanity)) #casting as set and list to avoid dupes
#     df["clean_text_spell_checked"] = df.clean_text.apply(lambda txt:''.join(textblob.TextBlob(txt).correct()))
    
#     def customer_profanity_flag(column):
#         convo_words = nltk.word_tokenize(column)
#         for word in convo_words:
#             if word.lower() in customer_profanity:
#                 return "Customer Profanity"
#             else:
#                 return "No Profanity"
            
#     def advisor_profanity_flag(column):
#             adv_words = nltk.word_tokenize(column)
#             for word in adv_words:
#                 if word.lower() in advisor_profanity:
#                     return "Advisor Profanity"
#                 else:
#                     return "No Profanity"
    
#     def sim_profanity_flag(column):
#         sim_words = nltk.word_tokenize(column)
#         for word in sim_words:
#                 if word.lower() in simultaneous_profanity:
#                     return "Simultaneous Profanity"
#                 else:
#                     return "No Profanity"
        
        
        
                
    

#     customer = df[df['speaker'] == "Customer"]
#     advisor = df[df['speaker'] == "Agent"]
#     simultaneous = df[df['speaker'] == "simultaneous"]
    
#     customer["ProfanityFlag"] = customer['clean_text_spell_checked'].apply(customer_profanity_flag)
#     advisor["ProfanityFlag"] = advisor['clean_text_spell_checked'].apply(advisor_profanity_flag)
#     simultaneous["ProfanityFlag"] = simultaneous['clean_text_spell_checked'].apply(advisor_profanity_flag)
#     concatenated = pd.concat([customer,advisor,simultaneous])
    
#     return concatenated.sort_index()t(set(customer_profanity+advisor_profanity)) #casting as set and list to avoid dupes
    
    def customer_profanity_flag(column):
        convo_words = nltk.word_tokenize(column)
        for word in convo_words:
            if word.lower() in customer_profanity:
                return "Customer Profanity"
            else:
                return "No Profanity"
            
    def advisor_profanity_flag(column):
            adv_words = nltk.word_tokenize(column)
            for word in adv_words:
                if word.lower() in advisor_profanity:
                    return "Advisor Profanity"
                else:
                    return "No Profanity"
    
    def sim_profanity_flag(column):
        sim_words = nltk.word_tokenize(column)
        for word in sim_words:
                if word.lower() in simultaneous_profanity:
                    return "Simultaneous Profanity"
                else:
                    return "No Profanity"
        
        
    df["ProfanityFlag"] = df['clean_text'].apply(sim_profanity_flag)
    
    return df


# In[ ]:

class TextCleaner:
    def __init__(self,name, text):
        self.name = name
        self.text = text
        profanity_file_customer = pd.read_excel("files/Keywords_List_Customer_Advisor.xlsx", sheet_name="Customer Keywords")
        profanity_file_advisor = pd.read_excel("files/Keywords_List_Customer_Advisor.xlsx", sheet_name="Advisor Keywords")
        
        
    def myname(self):
        return self.name
    
    def return_sentence(self):
        return self.text
    
    def lower_case(self):
        return str((self.text)).lower()
   
    def remove_noise(self):
        text = re.sub('\[.*?\]', ' ', self.text)
        text = re.sub('\w*\d\w*', ' ',  self.text)
        text = re.sub('https?://\S+|www\.\S+', ' ',  self.text)
        text = re.sub('[%s]' % re.escape(string.punctuation), ' ',  self.text)
        text = re.sub('\S*@\S*\s?',' ',  self.text)
        text = re.sub('[^A-Za-z0-9]+', '',  self.text)
        text = re.sub(r'[A-Za-z0-9]*@[A-Za-z]*\.?[A-Za-z0-9]*',' ',  self.text)
        
        return text
    
    def tokenize_words(self):
        return nltk.word_tokenize(self.text)
    
    def tokenize_sentence(self):
        return nltk.sent_tokenize(self.text)


# In[ ]:

def fuzzy_matching_of_keywords(df):
    customer_keywords = pd.read_excel("files/Customer_Keyw.xlsx")
    keywords_list = keywords_list = list(customer_keywords['Customer Speech Part'])
    
    
    def fuzzy_match_ratio(column):
        return process.extract(column, keywords_list, scorer=fuzz.token_set_ratio)
    
    def fuzzy_match_highest_ratio(column):
        return process.extractOne(column, keywords_list, scorer=fuzz.token_set_ratio)
    
    def fuzzy_match_highest_ratio_score(column):
        score = process.extractOne(column, keywords_list, scorer=fuzz.token_set_ratio)
        return score[1]
    
    def fuzzy_match_highest_ratio_string(column):
        score = process.extractOne(column, keywords_list, scorer=fuzz.token_set_ratio)
        return score[0]
    
    df['fuzzy_match_ratio'] = df['clean_text'].apply(fuzzy_match_ratio)
    df['fuzzy_best_match_ratio'] = df['clean_text'].apply(fuzzy_match_highest_ratio)
    df['highest_match_string'] = df['clean_text'].apply(fuzzy_match_highest_ratio_string)
    df['highest_match_ratio'] = df['clean_text'].apply(fuzzy_match_highest_ratio_score)
    
    
    return df 


# In[1]:

def keyword_flag(df):
    customer_keywords = pd.read_excel("files/Keywords_List_Customer_Advisor.xlsx", sheet_name="Customer Keywords")
    keywords_list = keywords_list = list(customer_keywords['Customer Speech Part'])
    
    def word_on_list_check(column):
        if column in keywords_list:
            return  "In"
        else:
            return "Not In"
    
    def threshold(column):
        if column == 100:
            return "Match"
        elif column >= 85:
            return "Possible Match"
        else:
            return "No match"
    
    df['match_threshold'] = df['highest_match_ratio'].apply(threshold)
    df['in_keyword_list'] = df['highest_match_string'].apply(word_on_list_check)
    
    return df
    
    
    
    
def keyword_list_flag(df):
    condition1 = df["match_threshold"] == "Match"
    condition2 = df["in_keyword_list"] == "In"
    final_condition = (condition1 & condition2)
    df["keyword_match"] = df["keyword_match"]=1
    df["keyword_match"] = df.where(final_condition, other=0)
    return df


# In[ ]:

def words_matched_100(column):
    """Returns all of the words that scored 100 on a fuzzy 
    match and adds it to a single columns"""
    return [x[0] for x in column if x[1]==100]

