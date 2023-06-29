import json
"""
JSON Examples from https://www.javatpoint.com/json-example
"""


class DictWrapper:
    """
    This class wraps a json object and allow access the members as object attributes.

    Example 1:

    Json format: json_obj1["employee"]["name"]

    Wrap format: json_obj2.employee.name

    Example 2:

    Json format: json_obj1["menu"]["popup"]["menuitem"][1]["onclick"]

    Wrap format: json_obj2.menu.popup.menuitem[1].onclick
    """

    def __init__(self, json_obj=None):
        if json_obj:
            self.static_load(self, json_obj)

    @staticmethod
    def set_attribute(instance, name, value):
        """
        Add a new attribute to an instance, if the attribute name does not already exists.
        :param instance: Object where to add the attribute
        :param name: New attribute name
        :param value: Attribute value
        :return: None
        """
        if not hasattr(instance, name):
            setattr(instance, name, value)

    @staticmethod
    def static_load(instance, json_obj):
        """
        Iterate a json members and add attributes to the instance.
        :param instance: Object where to add the attributes from json_obj
        :param json_obj: json object (python dictionary)
        :return: None
        """
        if isinstance(json_obj, dict):
            for el in json_obj.items():
                n = el[0]
                v = el[1]
                if isinstance(v, dict):
                    nv = DictWrapper(v)
                    DictWrapper.set_attribute(instance, n, nv)
                elif isinstance(v, list):
                    li = []
                    for ele in v:
                        nv = DictWrapper(ele)
                        li.append(nv)
                    DictWrapper.set_attribute(instance, n, li)
                else:
                    DictWrapper.set_attribute(instance, n, v)
        if isinstance(json_obj, list):
            li = []
            for el in json_obj:
                nv = DictWrapper(el)
                li.append(nv)
            DictWrapper.set_attribute(instance, 'list', li)

    def __repr__(self):
        """
        Return the content as json string.
        :return: String
        """
        res = "{"
        for e in self.__dict__.items():
            if len(res) > 1:
                res += ', '
            val = e[1]
            if isinstance(e[1], str):
                val = f'"{e[1]}"'
            res += f'"{e[0]}": {val}'
        res += "}"
        return res


json_txt = """
    {  
        "employee": {  
            "name":       "Mario",   
            "salary":      56000,   
            "married":    true  
        }  
    }  
"""

json_obj1 = json.loads(json_txt)
json_formatted_str = json.dumps(json_obj1, indent=2)
print(json_formatted_str)
print('json_obj1["employee"] :', json_obj1["employee"])
print('json_obj1["employee"]["name"] :', json_obj1["employee"]["name"])

json_obj2 = DictWrapper(json_obj1)
print('json_obj2.employee :', json_obj2.employee)
print('json_obj2.employee.name : ', json_obj2.employee.name)
print('json_obj2 :', json_obj2)


json_txt = """
    {"menu": {  
      "id": "file",  
      "value": "File",  
      "popup": {  
        "menuitem": [  
          {"value": "New", "onclick": "CreateDoc()"},  
          {"value": "Open", "onclick": "OpenDoc()"},  
          {"value": "Save", "onclick": "SaveDoc()"}  
        ]  
      }  
    }}  
"""

json_obj1 = json.loads(json_txt)
json_formatted_str = json.dumps(json_obj1, indent=2)
print(json_formatted_str)
print('json_obj1["menu"]["id"] :', json_obj1["menu"]["id"])
print('json_obj1["menu"]["popup"]["menuitem"][1] :', json_obj1["menu"]["popup"]["menuitem"][1])
print('json_obj1["menu"]["popup"]["menuitem"][1]["onclick"] :', json_obj1["menu"]["popup"]["menuitem"][1]["onclick"])

json_obj2 = DictWrapper(json_obj1)
print('json_obj2.menu.id:', json_obj2.menu.id)
print('json_obj2.menu.popup.menuitem[1] :', json_obj2.menu.popup.menuitem[1])
print('json_obj2.menu.popup.menuitem[1].onclick :', json_obj2.menu.popup.menuitem[1].onclick)
print('json_obj2 :', json_obj2)

json_txt = """
    [  
        {"name":"Ram", "email":"Ram@gmail.com"},  
        {"name":"Bob", "email":"bob32@gmail.com"}  
    ]   
"""

json_obj1 = json.loads(json_txt)
json_formatted_str = json.dumps(json_obj1, indent=2)
print(json_formatted_str)
print('json_obj1 :', json_obj1)
print('json_obj1[1]["email"] :', json_obj1[1]["email"])

json_obj2 = DictWrapper(json_obj1)
print('json_obj2 :', json_obj2)
print('json_obj2.list[1].email :', json_obj2.list[1].email)

