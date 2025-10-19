import inspect


def curry(func, argc):
    """
    This function turns the given function into a set of nested functions.

    func: is a function to be turned into curried function.
    argc: is a number of arguments that the given function takes.
    return: curried function.

    curry() raises ValueError if given argument count is not correct.
    """
    # If function has *arg- or **kwarg-like parameters
    is_variadic = (inspect.CO_VARARGS | inspect.CO_VARKEYWORDS) & func.__code__.co_flags
    # Take the signature of the function
    sig = inspect.signature(func)
    # The number of actual parameters
    arg_count = sum(
        1
        for arg in sig.parameters.values()
        if arg.kind not in (arg.VAR_POSITIONAL, arg.VAR_KEYWORD)
    )

    if (argc < arg_count) or (argc > arg_count and not is_variadic):
        raise ValueError("Invalid arguments count in 'curry()'.")

    def _inner(*args):
        if len(args) >= argc:
            return func(*args)

        def _partial(*more_args):
            return _inner(*(args + more_args))

        return _partial

    return _inner


def uncurry(func, argc):
    """
    This function turns curried function
    into normal function with given 'argc'
    arguments count. User must give correct number of arguments,
    otherwise function will return the
    curried function with reduced number of arguments.

    func: is a curried function to be turned into a normal function.
    argc: is a number of arguments of the function.
    return: normal function.

    uncurry() raises ValueError if 'argc' < 0.
    Returned function raises TypeError if invalid arguments were given in function call.
    """
    if argc < 0:
        raise ValueError("Invalid arguments count in 'uncurry()'.")

    def _uncurried(*args):
        if len(args) != argc:
            raise TypeError(
                f"Function takes {argc} arguments, but {len(args)} were given."
            )

        result = func
        for arg in args:
            result = result(arg)

        return result

    return _uncurried
