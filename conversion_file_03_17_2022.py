x="""## typedef PyObject* (*getattrfunc) (PyObject*, char*);
## typedef PyObject* (*getattrofunc) (PyObject*, PyObject*);
## typedef int (*setattrfunc) (PyObject*, char*, PyObject*);
## typedef int (*setattrofunc) (PyObject*, PyObject*, PyObject*);
## typedef PyObject* (*reprfunc) (PyObject*);
## typedef Py_hash_t (*hashfunc) (PyObject*);
## typedef PyObject* (*richcmpfunc) (PyObject*, PyObject*, int);
## typedef PyObject* (*getiterfunc) (PyObject*);
## typedef PyObject* (*iternextfunc) (PyObject*);
## typedef PyObject* (*descrgetfunc) (PyObject*, PyObject*, PyObject*);
## typedef int (*descrsetfunc) (PyObject*, PyObject*, PyObject*);
## typedef int (*initproc) (PyObject*, PyObject*, PyObject*);
## typedef PyObject* (*newfunc) (PyTypeObject*, PyObject*, PyObject*);
## typedef PyObject* (*allocfunc) (PyTypeObject*, Py_ssize_t);
## typedef PyObject* (*ternaryfunc) (PyObject*, PyObject*, PyObject*);
## typedef Py_ssize_t (*lenfunc) (PyObject*);
## typedef PyObject* (*vectorcallfunc) (PyObject* callable, PyObject* const *args, size_t nargssf, PyObject* kwnames);
## typedef PyObject* (*PyCFunction) (PyObject*, PyObject*);
""".replace('## ', '').split(';\n')

vectorcallfunc=CFUNCTYPE(POINTER(PyObject), POINTER(POINTER(PyObject)), c_size_t, POINTER(PyObject))

def f_split_str(a):
	return a.split()

def f_get_func_anotation_name(a):
	return a[2].replace('*','').strip('()')


def f_get_func_restype_and_argtypes(a):
	return a[1].strip('()'), a[3:]

#print(list(map(f_get_func_anotation_name, list(map(f_split_str, x))[:-1:]))) ## function names

def f_lazy_redefinition(a0):
	c_func_name=f_get_func_anotation_name(a0)
	restype, argtypes = list(f_get_func_restype_and_argtypes(a0))[:]
	restype, argtypes = restype.replace('PyObject*','POINTER(PyObject)'), (' '.join(argtypes)).replace('PyObject*','POINTER(PyObject)')
	restype, argtypes = restype.replace('int','c_int'), (''.join(argtypes)).replace('int','c_int')
	restype, argtypes = restype.replace('PyTypeObject*','POINTER(PyTypeObject)'), (''.join(argtypes)).replace('PyTypeObject*','POINTER(PyTypeObject)')
	restype, argtypes = restype.replace('ssize_t' ,'c_ssize_t'), (''.join(argtypes)).replace('ssize_t' ,'c_ssize_t')
	restype, argtypes = restype.replace('Py_c_ssize_t' ,'Py_ssize_t'), (''.join(argtypes)).replace('Py_c_ssize_t' ,'Py_ssize_t')
	restype, argtypes = restype.replace('char*' ,'c_char_p'), (''.join(argtypes)).replace('char*' ,'c_char_p')
	
	return str(c_func_name+" = CFUNCTYPE("+restype+", "+argtypes[1:])


for a0 in list(map(f_split_str, x))[:-1:]:
	print(f_lazy_redefinition(a0))
	
#for d in list(map(f_get_func_restype_and_argtypes, list(map(f_split_str, x))[:-1:])):
#	print(d)
