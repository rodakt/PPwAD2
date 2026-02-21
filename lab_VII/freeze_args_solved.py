def freeze_args(f, *args, **kwargs):
    args1 = args
    kwargs1 = kwargs

    def frozen(*args, **kwargs):
        args = args1 + args
        kwargs.update(kwargs1)
        return f(*args, **kwargs)

    return frozen
