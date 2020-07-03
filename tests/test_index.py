from util import consts, index


def test_simple():
    index.main(consts.TEST_PATH)
    with open(f'{consts.TEST_PATH}/test.md', 'r') as file:
        result = file.read()
    assert result == consts.TEST_DATA
