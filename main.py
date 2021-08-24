#
# オブジェクトのシリアライズについて考える
#
import serializer
from someclass import SomeClass
import sys
from typing import List

def main(args: List[str]) -> int:

    someclass = SomeClass("class naaaaaame!", {'d1': 11.4})
    print(someclass)
    serialized = serializer.JSONSerializer().serialize(someclass)
    print(serialized)
    deserialized = serializer.JSONSerializer().deserialize(serialized)
    someclass_recovered = SomeClass.deserialized(deserialized)
    print(someclass_recovered)

    assert someclass.serialized() == someclass_recovered.serialized()

    
    return 0

if __name__ == "__main__":
    result = 0
    try:
        result = main(sys.argv) or 0
    except KeyboardInterrupt: 
        print("Ctrl+C")
        exit(result)
