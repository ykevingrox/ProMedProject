from py_aho_corasick import py_aho_corasick
'''
# keywords only
A = py_aho_corasick.Automaton(['cash', 'shew', 'ew'])
text = "cashew"
for idx,k,v in A.get_keywords_found(text):
    assert text[idx:idx+len(k)] == k
'''
# keywords and values
kv = [('plague',1), ('shew',3), ('ew',3)]
kv.append(('foot',5))
print(kv)
A = py_aho_corasick.Automaton(kv)

text = "plague"
for idx,k,v in A.get_keywords_found(text):
    assert text[idx:idx+len(k)] == k
    assert v == dict(kv)[k]
    print(v)