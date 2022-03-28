import typing, ctypes

@typing.overload
def test(o): pass

@ctypes.CFUNCTYPE(return_type, param_types)
def test(o):
	"""some implemented class for 'typedef return_type (*c_function_name)(param_types);' in python code..."""
	return 0

@ctypes.CFUNCTYPE(return_type, param_types)
def test(o):
  print(o)
	return 0
