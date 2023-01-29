from pathlib import Path

from parameter_decorators.common import create_decorator


def validator(param, signature_item):
    return signature_item.annotation == Path and isinstance(param, str)


def converter(param, signature_item):
    return Path(param)


def reannotator(signature_item):
    return str


def reannotation_validator(signature_item):
    return signature_item.annotation == Path


def str_to_path(*params, reannotate: bool = True):
    """
    Decorator for converting string parameters to path.
    :param params: List of parameters names to convert, omit to convert all.
    :param reannotate: Whether to change the function annotation.
    """
    reannotator_ = reannotator if reannotate else None
    reannotation_validator_ = reannotation_validator if reannotate else None
    return create_decorator(params, validator=validator, converter=converter, reannotator=reannotator_,
                            reannotation_validator=reannotation_validator_)
