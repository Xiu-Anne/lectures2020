import numpy as np
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import matplotlib.pyplot as plt


X, y = load_digits(return_X_y=True)


plt.imshow(X[0].reshape(8, 8))
plt.savefig('images/digit.png', dpi=200)
plt.close('all')



X_ = TSNE(n_components=2).fit_transform(X)
# X_ = tsne.transform(X)

f, ax = plt.subplots(figsize=(4, 2.5))
for i, lab in enumerate(np.unique(y)):
    plt.scatter(X_[y == lab, 0], X_[y == lab, 1], label=i)
# plt.legend()

plt.savefig('tsne.png', dpi=200)

X_ = pca = PCA(n_components=2).fit_transform(X)
f, ax = plt.subplots(figsize=(4, 2.5))
for i, lab in enumerate(np.unique(y)):
    plt.scatter(X_[y == lab, 0], X_[y == lab, 1], label=i)
# plt.legend()

plt.savefig('pca.png', dpi=200)
# plt.show()