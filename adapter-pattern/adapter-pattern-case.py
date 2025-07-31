class Adapter:
    pass

class ArrayAdapter(Adapter):
    _data = []

    def __init__(self, data):
        self._data = data   

    def createUi(self):
        return self._data
    
class BaseAdapter(Adapter):
    _data = []

    def __init__(self, data):
        self._data = data

    def createUi(self):
        length = len(self._data)
        for i in range(0, length):
            self._data[i] = self._data[i].upper()
        return self._data
            
class ListView:
    _adapter = None

    def set_adapter(self, adapter):
        self._adapter = adapter

    def show(self):
        data = self._adapter.createUi()
        for item in data:
            print(item)
            
data = ["Easy learning C",
        "Easy learning Java",
        "Easy learning Python",
        "Easy learning C++",
        "Easy learning C#"
        ]

listView = ListView()
listView.set_adapter(ArrayAdapter(data))
listView.show() 

listView.set_adapter(BaseAdapter(data))
listView.show()