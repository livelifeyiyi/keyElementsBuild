# -*- coding: utf-8 -*-
import pandas as pd

dict_path = 'D:\data\dict.txt'
words = pd.read_table(dict_path, sep='\s+', names=['word', 'frequency', 'pos'])

sorted_words = words.sort(['frequency'], ascending=False)
sorted_words.to_csv('D:\data\dict_sorted_de.txt', index=False, sep=' ')