class Struct(object):
    def __init__(self, data):
        for name, value in data.items():
            setattr(self, name, self._wrap(value))

    def _wrap(self, value):
        if isinstance(value, (tuple, list, set, frozenset)):
            return type(value)([self._wrap(v) for v in value])
        else:
            return Struct(value) if isinstance(value, dict) else value


class ObjectConverter:
    """
    Credit to https://stackoverflow.com/a/6993694
    """

    def from_dict(self, a_dict):
        return Struct(a_dict)
