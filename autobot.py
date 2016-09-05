def main():
	import shelve
	allrows = shelve.open('drows')

	try:
		allrows['0'] = {1:'foo', 2:'bar', 3:'Lumberjack'}
		allrows['Hello'] = {'foo':'Hello', 'bar':'World', 'Lumberjack':'?'}
		allrows['Spam'] = {'foo':'Spam', 'bar':'Eggs', 'Lumberjack':'?'}
	except Exception as e:
		print(e)
		exit()
	finally:
		allrows.close()

	allrows = shelve.open('drows.db')
	
	fargs = {}
	for item in allrows['0']:
		fname = allrows['0'][item]
		if fname in globals():
			fargs[fname] = {}
			from inspect import signature, _empty
			sig = signature(eval(fname))
			print("%s is a function with arguments %s" % (fname, sig))
			for param in sig.parameters.values():
				print(param)
				pname = param.name
				pdefault = param.default
				if pdefault is _empty:
					fargs[fname][pname] = None
					print('Required parameter : %s %s' % (fname, pname))
				else:
					#print("%s %s %s" % (fname, pname, pdefault))
					fargs[fname][pname] = pdefault
					print("I ve default values for : %s %s %s" % (fname, pname, pdefault))
					print(fargs)
		else:
			print("%s is not a function" % fname)	

	for item in allrows:
		if item != '0':
			print("%s: %s" % (item, allrows[item]))

def delrow(allrows, rowkey):
	print("Going to delete the row with rowkey = %s" % rowkey)
	try:
		del allrows[rowkey]
		print("Deleted the row")
	except Exception as e:
		print(e)
		pass

def Lumberjack(job, play='', status='Okay'):
	return 'I m Okay'
	 

if __name__ == "__main__" : 
	main() 
