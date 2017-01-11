import langid
#引入langid模块
def translate(inputFile, outputFile):
	fin = open(inputFile, 'r')
	#以读的方式打开输入文件
	fout = open(outputFile, 'w')
	#以写的方式打开输出文件
	for eachLine in fin:
		#依次读入每一行
		line = eachLine.strip().decode('utf-8', 'ignore')
		#去除每行的首位空格等，并统一转化成Unicode
		lineTuple = langid.classify(line)
		#调用langid来对该行进行语言检测,返回二元组,格式('zh', -36.78374981880188)
		if lineTuple[0] == "zh":
		#如果该行语言大部分为中文，则不进行任何处理
		continue
	outstr = line
	#如果该行语言为非中文，则准备输出
	fout.write(outstr.strip().encode('utf-8') + '\n')
	#输出非中文的行，从Unicode转化成utf-8输出
	fin.close()
	fout.close()
if __name__ == '__main__':
	#相当于main函数
	translate("myInputFile.txt", "myOutputFile.txt")