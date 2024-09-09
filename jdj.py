def f(x, y=[]):
2.     y.append(x)
3.     return id(y), y
4. print(f(23))
5. print(f(42))

   
   
