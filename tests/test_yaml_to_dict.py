from pathlib import Path

import yaml


def test_dict_from_yaml():
    yaml_path = Path(__file__).parent / 'test_files' / 'example.yaml'
    with open(yaml_path) as f:
        yaml_dict = yaml.safe_load(f)

        assert yaml_dict['root']['branch']['node'] == 'node value'
        assert yaml_dict['root']['branch']['list'][2] == 'value 3'
