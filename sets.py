st = set()
print(type(st))

st = {1,2,3,4,5,5,5}
print(st)
st.add(6)
print(st)
st.remove(5)
print(st)

st1 = {1,2,3,4}
st2 = {3,4,5,6}
print(st1.intersection(st2))
print(st2.union(st1))
print(st1.difference(st2))

st2 = {1,2}
print(st1.issuperset(st2))
print(st2.issubset(st1))

st2.clear()
print(st2)
