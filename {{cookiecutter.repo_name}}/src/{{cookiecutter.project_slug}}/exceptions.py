""" Exceptions module """


class {{ cookiecutter.project_name.title().replace(' ', '').replace('-', '').replace('_','') }}Error(Exception):
    """ Base Exception for AWS Pricing """

    fmt = "{}"

    def __init__(self, *args, **kwargs):
        msg = self.fmt.format(*args, **kwargs)
        super().__init__(self, msg)
