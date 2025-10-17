def curry(func, argc=None):
    if argc is None:
        argc = func.__code__.co_argcount

    def _inner(*args):
        if len(args) >= argc:
            return func(*args)

        def _partial(*more_args):
            return _inner(*(args + more_args))

        return _partial

    return _inner
