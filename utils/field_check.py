from utils.my_exception import ErrorEnum, MyException


def field_check(data, require_field):
    for key in require_field:
        val = data.get(key)
        if val is None or val == '':
            raise MyException(ErrorEnum.ARG_NULL, msg='`{}` is null'.format(key))

    return True
