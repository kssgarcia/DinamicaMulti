import CierreVec
import inspect
import Naturales
import CoorCuerpo
def filterStr(element):
    a = element.strip('(')
    a = a.strip(')')
    a = a.replace(", ", " ")
    return a.split(" ")

def return_dict(archivo):
    for _, obj in inspect.getmembers(archivo):
        if inspect.isclass(obj):
            holder = str(inspect.signature(getattr(archivo, obj.__name__)))
            holder_filter = filterStr(holder)
            ind = holder_filter.index('app') + 1
            return holder_filter[ind:]

