from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from expenses.models import Person

@login_required
def loggedInView(request):
    """
    after log in, if no person, create
    """
    user = request.user
    if user.person_set.count() < 1:
        Person(user=user, name = 'Anonymous').save()
    return redirect('/profiles/%s' % user.username)