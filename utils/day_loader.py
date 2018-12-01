

def my_import(module, className):
    """
    dynamically loads a python module
    :param module: the module the class is in
    :param clazz:
    :return:
    """
    mod = __import__(module, fromlist=[className])
    return getattr(mod, className)


class DayLoader:

    def __init__(self, day):
        self.day = day

    def load_day(self, input_stream, output_stream):
        return my_import('days.day%d' % self.day, 'Day%d' % self.day)(input_stream, output_stream)


