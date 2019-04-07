from Account.models import Account


class CurrentUserHelper():

    """
    isCurrent takes 0 arguments. It returns True is a there is a current Users and False is there is not.
    """
    def isCurrent(self):
        try:
            CurrentUser = Account.objects.get(currentUser=True)
            return True
        except Account.DoesNotExist:
            return False
    """
    getCurrentUsers takes 0 arguments. It returns the current User is there is one or None is there is not 
    a current User
    """
    def getCurrentUser(self):
        try:
            CurrentUser = Account.objects.get(currentUser=True)
            return CurrentUser
        except Account.DoesNotExist:
            return None
    """
    getCurrentUserTitel takes 0 arguments. It returns the Integer value of the Current users title. If there
    is not a Current User is returns 0.
    """
    def getCurrentUserTitle(self):
        try:
            CurrentUser = Account.objects.get(currentUser=True)
            return CurrentUser.title
        except Account.DoesNotExist:
            return 0
