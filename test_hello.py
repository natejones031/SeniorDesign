import hello_ext
assert 'greet' in dir(hello_ext)
assert callable(hello_ext.greet)
print hello_ext.greet()
