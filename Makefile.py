CC = g++
PYLIBPATH = $(shell python-config --exec-prefix)/lib
LIB = -L$(PYLIBPATH) $(shell python-config --libs) -lboost_python
OPTS = $(shell python-config --include) -O2

default: hello_ext.so
	@python ./test_hello.py

hello_ext.so: hello_ext.o
	$(CC) $(LIB) -Wl,-rpath,$(PYLIBPATH) -shared $< -o $@

hello_ext.o: hello_ext.cpp Makefile
	$(CC) $(OPTS) -c $< -o $@

clean:
	rm -rf *.so *.o

.PHONY: default clean