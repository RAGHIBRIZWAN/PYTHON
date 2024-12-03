import numpy as np

A = np.arange(1,6)
B = np.arange(6,11)

cosineSimilarity = round(np.dot(A,B)/(np.linalg.norm(A) * np.linalg.norm(B)),2)

print(cosineSimilarity)