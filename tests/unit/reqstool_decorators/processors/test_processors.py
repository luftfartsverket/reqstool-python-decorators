import pytest
from src.reqstool_python_decorators.processors.decorator_processor import ProcessDecorator
from ruamel.yaml import YAML


@pytest.fixture
def process_decorator_instance():
    return ProcessDecorator()


def test_find_python_files(process_decorator_instance: ProcessDecorator, tmpdir):
    tmpdir.join("pythonfile.py").write("content")
    result = process_decorator_instance.find_python_files(tmpdir)
    assert result == [str(tmpdir.join("pythonfile.py"))]


def test_get_functions_and_classes(process_decorator_instance: ProcessDecorator, tmpdir):
    file_path = str(tmpdir.join("test_file.py"))
    tmpdir.join("test_file.py").write('@SVCs("SVC_001")\nclass Test:\n  pass')
    process_decorator_instance.get_functions_and_classes(file_path, ["SVCs"])
    assert process_decorator_instance.req_svc_results[0]["name"] == "Test"
    assert process_decorator_instance.req_svc_results[0]["decorators"][0]["args"][0] == "SVC_001"
    assert process_decorator_instance.req_svc_results[0]["decorators"][0]["name"] == "SVCs"
    assert process_decorator_instance.req_svc_results[0]["elementKind"] == "CLASS"


def test_map_type_known_type(process_decorator_instance: ProcessDecorator):
    result = process_decorator_instance.map_type("FUNCTION")
    assert result == "METHOD"


def test_map_type_unknown_type(process_decorator_instance: ProcessDecorator):
    result = process_decorator_instance.map_type("CLASS")
    assert result == "CLASS"


def test_write_to_yaml(process_decorator_instance: ProcessDecorator, tmp_path):
    yaml_language_server = (
        "# yaml-language-server: $schema=https://schemas.se/requirements-tool/v1/annotations.schema.json"
    )

    test_output_file = tmp_path / "test_output.yml"
    sample_formatted_data = """
                            requirement_annotations:
                                implementations:
                                    REQ_101:
                                        - elementKind: "CLASS"
                                            fullyQualifiedName: "com.example.RequirementsExample"
                                    """
    process_decorator_instance.write_to_yaml(output_file=test_output_file, formatted_data=sample_formatted_data)

    assert test_output_file.exists()

    with open(test_output_file, "r") as test_file:
        assert yaml_language_server in test_file.read()
        test_file.seek(0)
        yaml = YAML()
        loaded_data = yaml.load(test_file)
        assert sample_formatted_data == loaded_data


@pytest.mark.skip(reason="Test manually and check structure of the annotations.yml file generated in dist folder")
def test_process_decorated_data(process_decorator_instance: ProcessDecorator):
    paths = ["tests"]
    process_decorator_instance.process_decorated_data(path_to_python_files=paths)
