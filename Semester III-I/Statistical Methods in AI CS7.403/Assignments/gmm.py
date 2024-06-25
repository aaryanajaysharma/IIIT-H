import numpy as np
class GMM:
    def __init__(self, n_components, max_iterations=1000, tol=1e-4):
        self.n_components = n_components
        self.max_iterations = max_iterations
        self.tol = tol
        self.log_likelihoods = []

    def initialize_parameters(self, X):
        n_samples, n_features = X.shape
        np.random.seed(0)
        random_indices = np.random.choice(n_samples, size=self.n_components, replace=False)
        # print("random indices")
        # print(random_indices)
        
        self.means = X[random_indices]
        # print("means")
        # print(self.means)
        # shape = no. of gaussians, no. of features

        self.covariances = [np.eye(n_features) for _ in range(self.n_components)]
        # print("covariances")
        # print(self.covariances)
        # shape = no. of gaussians, no. of features, no. of features

        self.mixing_coefficients = np.ones(self.n_components) / self.n_components
        # print("mixing coefficients")
        # print(self.mixing_coefficients)
        # shape = no. of gaussians

    # routine to get parameters and mixing coefficients
    def get_parameters(self):
        return self.means, self.covariances, self.mixing_coefficients

    def gaussian_pdf(self, x, mean, cov):

        D = len(mean)
        det  = np.linalg.det(cov)
        inv = np.linalg.inv(cov)
        norm = 1.0 / ((2 * np.pi) ** (D / 2) * det ** 0.5)
        exponent = -0.5 * np.dot(np.dot((x - mean).T, inv), (x - mean))
        # np.exp gives e^(exponent)
        return norm * np.exp(exponent)

    def expectation_step(self, X):
        n_samples = X.shape[0]
        self.responsibilities = np.zeros((n_samples, self.n_components))

        for i in range(n_samples):
            for j in range(self.n_components):
                # calculate the posterior probability of each sample for each gaussian
                self.responsibilities[i, j] = self.mixing_coefficients[j] * self.gaussian_pdf(X[i], self.means[j], self.covariances[j])

            self.responsibilities[i] /= np.sum(self.responsibilities[i])

    def maximization_step(self, X):
        n_samples = X.shape[0]
        n_features = X.shape[1]

        for j in range(self.n_components):
            Nj = np.sum(self.responsibilities[:, j])
                                        # to make it a column vector for broadcasting
            self.means[j] = np.sum(X * self.responsibilities[:, j][:, np.newaxis], axis=0) / Nj
            # Inside the maximization_step method, before updating covariances
            # we add a regularization term to the covariance matrix to avoid numerical instability
            # REGULARIZATION_TERM = 1e-6
            # self.covariances[j] += np.eye(n_features) * REGULARIZATION_TERM
            diff = X - self.means[j]
            self.covariances[j] = np.dot(diff.T, diff * self.responsibilities[:, j][:, np.newaxis]) / Nj
            self.covariances[j] += np.eye(n_features) * 1e-4
            
            
        self.mixing_coefficients = np.mean(self.responsibilities, axis=0)
        
        self.log_likelihoods.append(self.log_likelihood(X))
    #  routine to fit data
    def fit(self, X):
        self.initialize_parameters(X)
        self.X = X

        for iteration in range(self.max_iterations):
            prev_means = np.copy(self.means)

            self.expectation_step(X)
            self.maximization_step(X)

            # Check for convergence
            if np.all(np.abs(self.means - prev_means) < self.tol):
                break
    # routing to predict the cluster
    def predict(self):
        self.expectation_step(self.X)
        return np.argmax(self.responsibilities, axis=1)
    
    def log_likelihood(self, X):
        n_samples = X.shape[0]
        log_likelihood = 0.0
        # summation of log likelihoods of all samples
        for i in range(n_samples):
            likelihood = 0.0
            # summation of likelihoods of all gaussians
            for j in range(self.n_components):
                likelihood += self.mixing_coefficients[j] * self.gaussian_pdf(X[i], self.means[j], self.covariances[j])
            log_likelihood += np.log(likelihood)

        return log_likelihood

    def aic(self, X):
        log_likelihood = self.log_likelihood(X)
        n_features = X.shape[1]
                     # 3 GAUSSIANS        # FOR MEAN   # FOR COVARIANCE                       # FOR MIXING COEFFICIENTS
        num_params = (self.n_components * (n_features + n_features * (n_features + 1) / 2)) + (self.n_components - 1)
        aic = -2 * log_likelihood + 2 * num_params
        return aic

    def bic(self, X):
        log_likelihood = self.log_likelihood(X)
        n_samples, n_features = X.shape
        
        num_params =  self.n_components * (n_features + n_features * (n_features + 1) / 2) + (self.n_components - 1)
        bic = -2 * log_likelihood + np.log(n_samples) * num_params
        return bic