from django.contrib.auth.decorators import login_required, user_passes_test
from django.shortcuts import get_object_or_404
from expenses.models import Household, Person

__author__ = 'jackdreilly'


def simple_decorator(decorator):
    """This decorator can be used to turn simple functions
    into well-behaved decorators, so long as the decorators
    are fairly simple. If a decorator expects a function and
    returns a function (no descriptors), and if it doesn't
    modify function attributes or docstring, then it is
    eligible to use this. Simply apply @simple_decorator to
    your decorator and it will automatically preserve the
    docstring and function attributes of functions to which
    it is applied."""
    def new_decorator(f):
        g = decorator(f)
        g.__name__ = f.__name__
        g.__doc__ = f.__doc__
        g.__dict__.update(f.__dict__)
        return g
    # Now a few lines needed to make simple_decorator itself
    # be a well-behaved decorator.
    new_decorator.__name__ = decorator.__name__
    new_decorator.__doc__ = decorator.__doc__
    new_decorator.__dict__.update(decorator.__dict__)
    return new_decorator

def person_from_user(user):
    return user.person_set.all()[0]

@simple_decorator
def user_in_household(f):

    """
    this is a decorated decorator that takes in a
    function that returns a function that executes
    a function that is decorated once, then again
    with a decorator generator that is generated
    from an anonymous function that takes as input
    an argument from the original function and from
    the decorated function, then finally executes
    the original function inside
	fuck you jack, that paragraph means nothing
    """

    def check_func(*args,**kwargs):
        @user_passes_test(lambda user: get_object_or_404(Household,pk=kwargs['pk']) in person_from_user(user).household_set.all())
        @login_required
        def new_f(*a, **k):
            return f(*a, **k)
        return new_f(*args, **kwargs)
    return check_func

@simple_decorator
def user_is_person(f):
    def check_func(*args,**kwargs):
        @user_passes_test(lambda user: get_object_or_404(Person,pk=kwargs['pk']) == person_from_user(user))
        @login_required
        def new_f(*a, **k):
            return f(*a, **k)
        return new_f(*args, **kwargs)
    return check_func



  
