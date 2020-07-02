import index
from util import consts


def test_simple():
    assert len(index.create_data(consts.TEST_PATH)) == consts.TEST_NUM
    assert len(index.create_data(consts.TEST_PATH_1)) == consts.TEST_NUM_1
    assert index.create_data(consts.TEST_PATH)[0]['count'] == consts.TEST_NUM_2
    assert index.create_data(consts.TEST_PATH_1)[0]['str'] == consts.TEST_STR
