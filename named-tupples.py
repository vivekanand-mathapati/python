from collections import namedtuple

Color = namedtuple('color',['red','green','blue'])
color = Color(55,155,255)

print(color.red)