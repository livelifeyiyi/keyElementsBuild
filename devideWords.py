# -*- coding: utf-8 -*-

import sys  
import re  
import codecs  
import os  
import shutil  
import jieba  
import jieba.analyse  
  
#导入自定义词典  
jieba.load_userdict("dict_all.txt")  
  
#Read file and cut  
def read_file_cut():      
    #create path  
    pathBaidu = "BaiduSpiderCountry\\"  
    resName = "Result_Country.txt"  
    if os.path.exists(resName):  
        os.remove(resName)  
    result = codecs.open(resName, 'w', 'utf-8')  
  
    num = 1  
    while num<=100:  #5A 200 其它100  
        name = "%04d" % num   
        fileName = pathBaidu + str(name) + ".txt"  
        source = open(fileName, 'r')  
        line = source.readline()  
          
        while line!="":  
            line = line.rstrip('\n')  
            #line = unicode(line, "utf-8")  
            seglist = jieba.cut(line,cut_all=False)  #精确模式  
            output = ' '.join(list(seglist))         #空格拼接  
            #print output  
            result.write(output + ' ')               #空格取代换行'\r\n'  
            line = source.readline()  
        else:  
            print 'End file: ' + str(num)  
            result.write('\r\n')    
            source.close()  
        num = num + 1  
    else:  
        print 'End Baidu'  
        result.close()  
  
#Run function  
if __name__ == '__main__':  
    read_file_cut()  