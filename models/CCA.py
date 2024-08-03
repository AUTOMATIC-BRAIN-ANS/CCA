import numpy as np
from scipy.linalg import eigh, svd


class MyCCA():
    def __init__(self, dim):
        self.dim = dim
        self.weights_x = None
        self.weights_y = None
        self.corr_values = None

    def center_cols(self, M, N):
        m = np.mean(M, axis=0)
        M = M - np.tile(m, (N, 1))
        return M

    def fit(self, X, Y, r1=0, r2=0, tol=1e-12):
        N = X.shape[0]
        dim_x = X.shape[1]
        dim_y = Y.shape[1]

        X = self.center_cols(X, N)
        Y = self.center_cols(Y, N)

        cov_matrix_xx = (X.T @ X) / (N - 1) + r1 * np.eye(dim_x)
        cov_matrix_yy = (Y.T @ Y) / (N - 1) + r2 * np.eye(dim_y)
        cov_matrix_xy = (X.T @ Y) / (N - 1)

        [eigenval_xx, eigenvect_xx] = eigh(cov_matrix_xx)
        idx_x = np.where(eigenval_xx > tol)[0]
        eigenval_xx = eigenval_xx[idx_x]
        eigenvect_xx = eigenvect_xx[:, idx_x]

        [eigenval_yy, eigenvect_yy] = eigh(cov_matrix_yy)
        idx_y = np.where(eigenval_yy > tol)[0]
        eigenval_yy = eigenval_yy[idx_y]
        eigenvect_yy = eigenvect_yy[:, idx_y]

        whitening_x = eigenvect_xx @ np.diag(1 / np.sqrt(eigenval_xx)) @ eigenvect_xx.T
        whitening_y = eigenvect_yy @ np.diag(1 / np.sqrt(eigenval_yy)) @ eigenvect_yy.T

        T = whitening_x @ cov_matrix_xy @ whitening_y

        [U, D, V] = svd(T)
        min_val = min(self.dim, len(D))
        self.weights_x = whitening_x @ U[:, :min_val]
        self.weights_y = whitening_y @ V.T[:, :min_val]
        self.corr_values = np.diag(D)[:min_val, :min_val]

    def transform(self, X, Y):
        X = self.center_cols(X, X.shape[0])
        Y = self.center_cols(Y, X.shape[0])
        canonical_variables_x = X @ self.weights_x
        canonical_variables_y = Y @ self.weights_y
        return canonical_variables_x, canonical_variables_y
