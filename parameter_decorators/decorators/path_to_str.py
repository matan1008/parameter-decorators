import os
from functools import partial
from pathlib import Path

from parameter_decorators.common import create_decorator


def validator(param, signature_item):
    return signature_item.annotation == str and isinstance(param, Path)


def converter(param, signature_item, expanduser):
    if expanduser:
        param = Path(param).expanduser()
    return str(param)


def reannotator(signature_item):
    return os.PathLike


def reannotation_validator(signature_item):
    return signature_item.annotation == str


def path_to_str(*params, expanduser: bool = False, reannotate: bool = True):
    """
    Decorator for converting path parameters to string.
    :param params: List of parameters names to convert, omit to convert all.
    :param expanduser: Whether to expand decorated paths.
    :param reannotate: Whether to change the function annotation.
    """
    reannotator_ = reannotator if reannotate else None
    reannotation_validator_ = reannotation_validator if reannotate else None
    return create_decorator(params, validator=validator, converter=partial(converter, expanduser=expanduser),
                            reannotator=reannotator_, reannotation_validator=reannotation_validator_)
