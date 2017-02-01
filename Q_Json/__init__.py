import objectpath
import json

def get_json_items(json_str, path):
    """
    Returns list of items from the provided json according to the provided ObjectPath (http://objectpath.org/tutorial.html)
    
    *Args:*\n
    _json_str_ - json-string;\n
    _path_ - ObjectPath expression;
        
    *Return:*\n
    List of items according to the ObjectPath query
        
        *Example:*\n
        | *Settings* | *Value* |
        | Library    | Q_Json |
        | *Variables* | *Value* |
        | ${test_str} | {"user":{"actions":{"name":"reading","description":"blablabla"},"name": "John"}} |
        | ${query}    | $.user[@.name is 'John'].actions[@.name is 'reading'].description |
        | *Test Cases* | *Action* | *Argument* | *Argument* |
        | Find description | ${answer}=      | Get Json Items | ${test_str} | ${query} |
        |                  | Should be Equal | ${answer[0]}   | blablabla   |
    """
    json_struct = json.loads(json_str)    
    tree = objectpath.Tree(json_struct)
    entries = tree.execute(path)
    res = []
    for entry in entries:
        res.append(entry)

    return res