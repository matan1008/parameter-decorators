import inspect
from functools import wraps


def create_decorator(params, validator, converter, reannotator=None, reannotation_validator=None):
    def decorate_func(f):
        signature = inspect.signature(f)

        @wraps(f)
        def new_f(*args, **kwargs):
            try:
                ba = signature.bind(*args, **kwargs)
            except TypeError:
                # Binding failed, let the original function traceback rise.
                try:
                    f(*args, **kwargs)
                except TypeError as e:
                    e.__context__ = None
                    raise e

            for param_name in ba.arguments:
                param = ba.arguments[param_name]
                signature_item = signature.parameters[param_name]
                if (not params and validator(param, signature_item)) or param_name in params:
                    ba.arguments[param_name] = converter(param, signature_item)
            return f(*ba.args, **ba.kwargs)

        if reannotator is not None:
            new_params = {k: v for k, v in signature.parameters.items()}
            for param_name in new_params:
                signature_item = new_params[param_name]
                if (not params and reannotation_validator(signature_item)) or param_name in params:
                    new_params[param_name] = new_params[param_name].replace(annotation=reannotator(signature_item))
            new_f.__signature__ = signature.replace(parameters=list(new_params.values()))

        return new_f

    return decorate_func
