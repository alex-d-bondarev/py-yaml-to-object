import yaml


def test_dict_from_yaml():
    with open('test_files/example.yaml') as f:
        yaml_dict = yaml.safe_load(f)

        assert yaml_dict['root']['branch']['node'] == 'node value'
        assert yaml_dict['root']['branch']['list'][2] == 'value 3'
