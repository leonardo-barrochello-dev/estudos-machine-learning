
import numpy as np
import sys
import os

# Set working directory to the classification lab folder
os.chdir(r'c:\Estudos\ML\Nivel 2 - Machine Learning\Classification')
sys.path.append('.')

from plt_overfit import overfit_example

try:
    # Initialize the overfit example
    ofit = overfit_example(False)
    
    # Let's test linear regression first as it's a common failure point with 'normalize'
    ofit.logistic = False
    ofit.degree = 2
    ofit.xlim = (0, 30)
    ofit.X = np.arange(0, 30, 1)
    ofit.y = ofit.X**2 + np.random.randn(30)
    
    print("Testing Linear Regression (Ridge)...")
    ofit.linear_regression()
    print("Linear Regression ok")

except Exception as e:
    print(f"Linear Regression failed: {e}")
    import traceback
    traceback.print_exc()

try:
    print("\nTesting Logistic Regression...")
    ofit.logistic = True
    ofit.degree = 2
    ofit.X = np.random.randn(50, 2)
    # create a quadratic boundary
    ofit.y = (ofit.X[:,1] + 0.5 > ofit.X[:,0]**2).astype(int)
    ofit.logistic_regression()
    print("Logistic Regression ok")
except Exception as e:
    print(f"Logistic Regression failed: {e}")
    import traceback
    traceback.print_exc()
