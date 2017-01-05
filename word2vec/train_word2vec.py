#-*-coding: utf-8 -*-
import logging
import numpy as np
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence

file_dir = 'w2c_log.txt'
logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO, filename = file_dir)

filePath = '..\jieba_result\sina_default_mode.txt'

def generateModel(filePath):
	#sentences = LineSentence(filePath)
	sentences = word2vec.Text8Corpus(filePath)
	model = word2vec.Word2Vec(sentences, size=200)
	fname = 'vector.txt'
	model.save(fname)  # binary format
	print model
	# print model[u"暴恐"]
	y2 = model.most_similar(u"暴恐", topn=20)
	for item in y2:
		print item[0], item[1]


generateModel(filePath)

