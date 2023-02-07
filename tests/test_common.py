import pytest

from parameter_decorators import path_to_str


def test_parameters_binding_failure():
    @path_to_str()
    def function(a: str):
        assert isinstance(a, str)

    with pytest.raises(TypeError):
        function(c='/path')
