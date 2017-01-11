#-*-coding: utf-8 -*-
import logging
import numpy as np
from gensim.models import word2vec
from gensim.models.word2vec import LineSentence

import os.path
import sys
import multiprocessing
 
from gensim.corpora import WikiCorpus
from gensim.models import Word2Vec


class myTry(object):
	"""docstring for myTry"""
	def __init__(self):
		#super(myTry, self).__init__()
		file_dir = 'w2c_log.txt'
		logging.basicConfig(format='%(asctime)s:%(levelname)s: %(message)s', level=logging.INFO, filename = file_dir)

		self.filePath = '..\jieba_result\sina_default_mode.txt'

	def generateModel(self):
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

	def useGoogleVetor(self):
		#memory error
		model = word2vec.Word2Vec.load_word2vec_format('GoogleNews-vectors-negative300.bin.gz',binary=True)
		print model.most_similar(positive=['woman','king'], negative=['man'], topn=5)
	#generateModel(filePath)
	#useGoogleVetor()
"""
class wikiData(object):
	
	def __init__(self, arg):
		#super(wikiData, self).__init__()
		self.arg = arg"""

#if __name__=='__main__':
def trainWikiData():
	program = os.path.basename(sys.argv[0])
	logger = logging.getLogger(program)

	logging.basicConfig(format='%(asctime)s: %(levelname)s: %(message)s')
	logging.root.setLevel(level=logging.INFO)
	logger.info("running %s" % ' '.join(sys.argv))

	# check and process input arguments
	if len(sys.argv) < 4:
		print globals()['__doc__'] % locals()
		sys.exit(1)
	inp, outp1, outp2 = sys.argv[1:4]

	model = Word2Vec(LineSentence(inp), size=400, window=5, min_count=5,
			workers=multiprocessing.cpu_count())

	# trim unneeded model memory = use(much) less RAM
	#model.init_sims(replace=True)
	model.save(outp1)
	model.save_word2vec_format(outp2, binary=False)

	'''
	#train:
	python train_word2vec.py wiki.zh.text.jian.seg wiki.zh.text.model wiki.zh.text.vector
	'''
def useWikiModel():
	model = word2vec.Word2Vec.load("wiki.zh.text.model")
	
	result = model.most_similar(u"公安局")
	for e in result:
		print e[0], e[1]
	print model.similarity(u"计算机", u"自动化")
	print model.doesnt_match(u"早餐 晚餐 午餐 中心".split())
useWikiModel()