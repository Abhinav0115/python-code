# Check that tuple is immutable or not
tpl = (1, "abhi", 3, 4, 5)

tpl[0] = 2
print(tpl) # TypeError: 'tuple' object does not support item assignment


