#include <Python.h>
#include <string>

// c++ function to expose to python
const std::string greet()
{
   return std::string("hello, world");
}

// API function
static PyObject* greet(PyObject *self,PyObject *args)
{
	int n=0;
	if(!PyArg_ParseTuple(args,"i",&n)) return NULL;
	return Py_BuildValue("i",Prime(n));
}

// function list
static PyMethodDef extMethods[]={
	{ "greet",(PyCFunction)greet,METH_VARARGS},
		{NULL,NULL,0,NULL}
};

// initialize function
PyMODINIT_FUNC initext()
{
	Py_InitModule("ext",extMethods);
}