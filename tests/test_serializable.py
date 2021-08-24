#
# serilalizable tests
#
import pytest, logging
from serializable.serializable import Serializable
from tests.someclass import SomeClass

def test_invalid_instantiation():
    """
    Serializableを直接インスタンス化することはできるが、
    serialized()は呼び出せない
    """
    serializable_class = Serializable()

    with pytest.raises(NotImplementedError):
        serializable_class.serialized()

    with pytest.raises(NotImplementedError):
        Serializable.deserialized({})

def test_valid_instantiation():
    """
    適当に作ったSerializableなクラスの生成とシリアライズ・デシリアライズ
    """
    some_class = SomeClass("testclasssssss", {'d1', 11.4})
    logging.debug(str(some_class))

    some_class_serialized = some_class.serialized()
    logging.debug(str(some_class_serialized))

    assert some_class_serialized['name'] == some_class.name
    assert some_class_serialized['datas'] == some_class.datas

    deserialized = SomeClass.deserialized(some_class_serialized)
    assert deserialized is not None
    assert some_class.serialized() == deserialized.serialized()
    logging.debug(deserialized)
