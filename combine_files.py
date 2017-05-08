#################
### This function is used to combine all files in one dictionary into one file.
#################
import sys, os

file_dir = 'I:/data/sina_news_article/'
#file_dir = 'D:\\New folder\\test'
def join(path, out_filename):
	out_file = open(out_filename, 'w+')
	err_files = []
	if os.path.isdir(path):
		for fpath,path,fnames in os.walk(path):
			for fname in fnames:
				try:
					fname_path = os.path.join(fpath,fname)
					fo = open(fname_path, 'r')
					out_file.write(fo.read())
					out_file.write('\n\n')
					fo.close()
					print fname_path
				except IOError:
					print 'error joining', fname 
					err_files.append(fname)
					
if __name__ == '__main__':
		out_filename = file_dir + '/combined/sina_news_article.txt'
		join(file_dir, out_filename)