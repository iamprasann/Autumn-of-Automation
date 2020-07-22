import numpy as np

X=np.random.normal(5, 0.01, size=(20,20))
y=np.random.randint(0, 100, size=(20,1), dtype=np.int32)

theta=np.dot(np.dot(np.linalg.inv(np.dot(X.T, X)), X.T), y)
print(theta)
