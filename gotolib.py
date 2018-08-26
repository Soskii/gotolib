import inspect
import warnings


def goto(loc):
    warnings.warn("We're very sorry", FutureWarning)
    file = inspect.currentframe().f_back
    while file.f_globals["__name__"] != "__main__":
        file = file.f_back
    exec(open(file.f_globals["__file__"]).read().split("# " + str(loc))[1])
    quit()
