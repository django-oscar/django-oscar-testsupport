import mock
from django.utils.functional import curry


def dataProvider(fn_data_provider):
    """
    Data provider decorator, allows another callable to provide the data for
    the test.  This is a nice feature from PHPUnit which is very useful.  Am
    sticking with the JUnit style naming as unittest does this already.

    Implementation based on:
    http://melp.nl/2011/02/phpunit-style-dataprovider-in-python-unit-test/#more-525
    """
    def test_decorator(test_method):
        def execute_test_method_with_each_data_set(self):
            for data in fn_data_provider():
                if (len(data) == 2 and isinstance(data[0], tuple) and
                    isinstance(data[1], dict)):
                    # Both args and kwargs being provided
                    args, kwargs = data[:]
                else:
                    args, kwargs = data, {}
                try:
                    test_method(self, *args, **kwargs)
                except AssertionError, e:
                    self.fail("%s (Provided data: %s, %s)" % (e, args, kwargs))
        return execute_test_method_with_each_data_set
    return test_decorator


# This will be in Oscar 0.6 - it should be functools though!
def compose(*functions):
    """
    Compose functions

    This is useful for combining decorators.
    """
    def _composed(*args):
        for fn in functions:
            try:
                args = fn(*args)
            except TypeError:
                # args must be scalar so we don't try to expand it
                args = fn(args)
        return args
    return _composed


no_database = mock.patch(
    'django.db.backends.util.CursorWrapper', mock.Mock(
        side_effect=RuntimeError("Using the database is not permitted!")))


no_filesystem = mock.patch('__builtin__.open', mock.Mock(
    side_effect=RuntimeError("Using the filesystem is not permitted!")))


no_sockets = mock.patch('socket.getaddrinfo', mock.Mock(
    side_effect=RuntimeError("Using sockets is not permitted!")))


no_externals = no_diggity = compose(
    no_database, no_filesystem, no_sockets)  # = no doubt
