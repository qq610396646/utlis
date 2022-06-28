# -*- coding: utf-8 -*-
import os

def new_python_package(path):
	filepath=os.path.join(path,"__init__.py")
	with open(filepath,"w",encoding="utf-8") as f:
		pass

def new_python_file(path,name):
	filepath=os.path.join(path,name)
	with open(filepath,"w",encoding="utf-8") as f:
		pass

def new_dirtory(path,name):
	"""
	是否包含数据库

	"""
	path=os.path.join(path,name)
	os.mkdir(path)

def main():
	filestructs=["bin","conf","docs","lib","log","src","tests","utils","data"]
	if NEWDB:
		filestructs+["db"]

	packagesstucts=["bin","lib","utils","tests"]
	original_files=["requirement.txt","README.md","main.py","setup.py"]
	path=os.getcwd()

	for file in filestructs:
		new_dirtory(path,file)
	for packages in filestructs:
		new_python_package(packages)
	for orgfile in original_files:
		new_python_file(path,orgfile)


if __name__ == '__main__':
	NEWDB=False
	main()
	