class other:
    pass
    
class person:
    pass
class employee(other,person):
    pass
import inspect
print(inspect.getmro(employee))


