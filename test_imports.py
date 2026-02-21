
try:
    import numpy as np
    print("numpy ok")
except ImportError:
    print("numpy missing")

try:
    import matplotlib.pyplot as plt
    print("matplotlib ok")
except ImportError:
    print("matplotlib missing")

try:
    import ipywidgets
    print("ipywidgets ok")
except ImportError:
    print("ipywidgets missing")

try:
    import ipympl
    print("ipympl ok")
except ImportError:
    print("ipympl missing")

try:
    import sklearn
    print("sklearn ok")
except ImportError:
    print("sklearn missing")
