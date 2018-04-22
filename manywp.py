manywords = lambda stringy, d : (stringy in d) or (len([1 for i in range(1,len(stringy)) if (stringy[:i] in d and manywords(stringy[i:],d)) ])>0)
