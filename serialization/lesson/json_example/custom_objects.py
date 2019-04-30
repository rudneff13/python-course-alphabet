from __future__ import annotations

import json


class Programmer:

    def __init__(self, name, language="Python", position="Junior") -> None:
        self.name = name
        self.language = language
        self.position = position
        self.enough_coffee = False

    def __str__(self):
        return f"Programmer. Name: {self.name}." \
            f"Lang :{self.language}; Postion: {self.position} developer"

    @classmethod
    def from_json(cls, data):
        name = data['name']
        language = data['language']
        position = data['position']
        pr = Programmer(name=name, language=language, position=position)
        pr.enough_coffee = data.get('enough_coffee', False)
        return pr

    @staticmethod
    def to_json(obj: Programmer):
        data = {"name": obj.name, "language": obj.language, "position": obj.position}
        return data


if __name__ == "__main__":
    programmer = Programmer("Flash")

    print(programmer)
    ser_pr = ''
    # Should raise TypeError. Json does not know how to work with custom objects
    try:
        ser_pr = json.dumps(programmer)
        print(ser_pr)
    except TypeError as e:
        print(e)

    # Should work fine. Use custom json decoder
    try:
        ser_pr = json.dumps(programmer, default=Programmer.to_json)
        print(type(ser_pr), ser_pr)
    except TypeError as e:
        print(e)

    # Should not fault. But we will get dict instead of object
    try:
        load_pr = json.loads(ser_pr)
        print(type(load_pr), load_pr)
    except TypeError as e:
        print(e)

    # Should works fine. Use custom hook
    try:
        load_pr = json.loads(ser_pr, object_hook=Programmer.from_json)
        print(type(load_pr), load_pr)
    except TypeError as e:
        print(e)
