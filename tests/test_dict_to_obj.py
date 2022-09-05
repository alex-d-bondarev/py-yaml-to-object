from py_yaml_to_object.dict_to_obj import ObjectConverter


def test_simple_dict_to_obj():
    test_d = {'f1': 'v1', 'f2': 'v2'}
    d_to_obj = ObjectConverter().from_dict(test_d)
    assert test_d['f1'] == d_to_obj.f1


def test_multilevel_dict_to_obj():
    test_d = {
        'f1': {
            'sub_f1': {
                'sub_sub_f1': 'test'
            }
        }}
    d_to_obj = ObjectConverter().from_dict(test_d)
    assert test_d['f1']['sub_f1']['sub_sub_f1'] == d_to_obj.f1.sub_f1.sub_sub_f1


def test_list_in_dict():
    test_d = {'f1': ['v1', 'v2']}
    d_to_obj = ObjectConverter().from_dict(test_d)
    assert test_d['f1'][0] == d_to_obj.f1[0]


def test_multilevel_list_to_dict():
    test_d = {'f1': [
        'v1', {'f2': 'v2'}
    ]}
    d_to_obj = ObjectConverter().from_dict(test_d)
    assert test_d['f1'][1]['f2'] == d_to_obj.f1[1].f2
