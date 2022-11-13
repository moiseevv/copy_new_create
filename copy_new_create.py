#! /usr/bin/env python3

import os,re,datetime
from pathlib import Path
path_1 = '/home/bitrix/cp_2022_06/sec'
path_2 = '/home/bitrix/cp_2022_06/uf'
last_create = datetime.datetime.strptime('07.10.2022 19:50', '%d.%m.%Y %H:%M')

def record_f(p,d,l):
	'''
		Will used after deleted comment in function wall. Used show listening files.
	'''
	with open('Listening_files.txt', 'a') as file:
		print('etap_1 p',file=file)
		print(p, file=file)
		print('etap_2 d',file=file)
		print(d, file=file)
		print('etap_3 l',file=file)
		print(l, file=file)

def copy_new(p):
	if os.path.isdir(p):
			
		new_dir_mk = (str(p.replace(path_1,path_2)))
		mk_dir(new_dir_mk)
		if os.path.isdir(new_dir_mk):
			print(f'	Seccess dir -  {new_dir_mk}')
def log_create(x):
	with open('log_create_dir.txt','a') as file:
		print(f'Create directory - {x}',file = file)
		print(f'Time create of directory {datetime.datetime.now()}', file=file)
def record_da(a):
	with open('log_create_file.txt','a') as file:
		print(f'Created faile  - {a}', file=file)
		print(f'Time create file {datetime.datetime.now()}', file=file)
def mk_dir(create_dir):
	if not os.path.isdir(create_dir):
		os.mkdir(create_dir)
		os.chmod(create_dir,0o777)
		log_create(create_dir)

def copy_file_l(path_x,path_y):
	if not os.path.exists(path_y):
		if test_time_create(path_x):
			comand = f'cp {path_x} {path_y}'
			os.popen(comand)
			print(comand)
			comand_2 = f'chmod 777 {path_y}'
			os.popen(comand_2)
			record_da(path_y)

def test_time_create(path_x):
		global last_time
		time_create_isch = os.path.getmtime(path_x)
		time_create = datetime.datetime.fromtimestamp(time_create_isch)
		if time_create > last_create:
			return True
		else:
			return False

		
def walk(path):
	for p,d,l in os.walk(path):
		#record_f(p,d,l)
		if not os.path.islink(p):
			if test_time_create(p):
				copy_new(p)
		for file_test in l:
			path_ft = os.path.join(p,file_test)
			if not os.path.islink(path_ft):
				new_path = path_ft.replace(path_1,path_2)
				copy_file_l(path_ft,new_path)
	
walk(path_1)


