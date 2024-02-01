# Copyright © LFV


def Requirements(*requirements):
    def decorator(func):
        func.requirements = requirements
        return func

    return decorator


def SVCs(*svc_ids):
    def decorator(func):
        func.svc_ids = svc_ids
        return func

    return decorator
