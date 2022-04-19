import numpy as np
z = [1, 1, 0, 1]
z1 = np.array(z)

H = np.array([[1, 1, 0, 1, 1, 0, 0],
              [1, 0, 1, 0, 0, 1, 0],
              [0, 1, 1, 1, 0, 0, 1]])

B = H[:, :4]
G = np.concatenate(np.eye(H.shape[1]), B.transpose())
