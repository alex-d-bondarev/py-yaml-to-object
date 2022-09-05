from pathlib import Path

from src.dict_to_obj import ObjectConverter


def test_dict_from_yaml():
    yaml_path = Path(__file__).parent / 'test_files' / 'example.yaml'
    y_to_obj = ObjectConverter().from_yaml(yaml_path)
    assert y_to_obj.root.branch.node == 'node value'
    assert y_to_obj.root.branch.list[2] == 'value 3'
