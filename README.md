# python-serializable

## Overview

Object serialization utility.

## Installation

To install:

```
pip install git+https://github.com/Enchan1207/python-serializable
```

To uninstall:

```
pip uninstall serializable
```

## Usage

First, suppose you have a class like this:

```python
class SomeClass():

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
```

To "serialize" this object, inherit `serializable.Serializable` to SomeClass.

```
import serializable

 - class SomeClass():
 + class SomeClass(serializable.Serializable):
```

And implement two methods shown below:

 - `serialized(self) -> Dict[str, Any]` : return informations that you need to generate same instance with it.
 - `static deserialized(serialized: Dict[str, Any]) -> Optional[Serializable]` : create instance of this class from "serialized" object.

Yeah it's time to magic:

```
some_class = SomeClass("user", 19)
some_class_serialized = some_class.serialized()

assert some_class_serialized['name'] == some_class.name
assert some_class_serialized['datas'] == some_class.datas

some_class_deserialized = SomeClass.deserialized(some_class_serialized)

assert some_class.serialized() == deserialized.serialized()
```
## License

All files in this repository is published under MIT License.
In details, see [LICENSE](LICENSE).

