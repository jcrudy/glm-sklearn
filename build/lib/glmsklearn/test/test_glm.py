from nose.tools import assert_equal, assert_not_equal, assert_true, assert_false, \
    assert_almost_equal, assert_list_equal
import numpy as np
from glmsklearn import BinomialRegression, GammaRegression, GaussianRegression, \
    InverseGaussianRegression, NegativeBinomialRegression, PoissonRegression
from statsmodels.genmod.families.family import Binomial, Gamma, Gaussian,\
    InverseGaussian, NegativeBinomial, Poisson
from sklearn.pipeline import Pipeline
from sklearn.decomposition.pca import PCA



class TestGlm():
    def __init__(self):
        #Generate some data
        np.random.seed(1)
        self.X = np.random.normal(size=(100,10))**2
        self.beta = np.random.normal(size=10)**2
        self.eta = np.dot(self.X, self.beta) + .1*np.random.normal(size=100)
        
    def test_binomial(self):
        model = BinomialRegression()
        y = Binomial().fitted(self.eta)
        model.fit(self.X, y)
        y_hat = model.predict(self.X)
        diff = y_hat - y
        rsq = 1 - np.mean(diff**2) / np.mean((y-np.mean(y))**2)
        assert_true(rsq > .99)
    
    def test_gamma(self):
        model = GammaRegression()
        y = Gamma().fitted(self.eta)
        model.fit(self.X, y)
        y_hat = model.predict(self.X)
        diff = y_hat - y
        rsq = 1 - np.mean(diff**2) / np.mean((y-np.mean(y))**2)
        assert_true(rsq > .99)
    
    def test_gaussian(self):
        model = GaussianRegression()
        y = Gaussian().fitted(self.eta)
        model.fit(self.X, y)
        y_hat = model.predict(self.X)
        diff = y_hat - y
        rsq = 1 - np.mean(diff**2) / np.mean((y-np.mean(y))**2)
        assert_true(rsq > .99)
        
    def test_inverse_gaussian(self):
        model = InverseGaussianRegression()
        y = InverseGaussian().fitted(self.eta)
        model.fit(self.X, y)
        y_hat = model.predict(self.X)
        diff = y_hat - y
        rsq = 1 - np.mean(diff**2) / np.mean((y-np.mean(y))**2)
        assert_true(rsq > .99)
        
    def test_negative_binomial(self):
        model = NegativeBinomialRegression()
        y = NegativeBinomial().fitted(self.eta)
        model.fit(self.X, y)
        y_hat = model.predict(self.X)
        diff = y_hat - y
        rsq = 1 - np.mean(diff**2) / np.mean((y-np.mean(y))**2)
        assert_true(rsq > .99)
        
    def test_poisson(self):
        model = PoissonRegression()
        y = Poisson().fitted(self.eta)
        model.fit(self.X, y)
        y_hat = model.predict(self.X)
        diff = y_hat - y
        rsq = 1 - np.mean(diff**2) / np.mean((y-np.mean(y))**2)
        assert_true(rsq > .99)
    
    def test_with_pipeline(self):
        model = Pipeline([('PCA',PCA()), ('Poisson',PoissonRegression())])
        y = Poisson().fitted(self.eta)
        model.fit(self.X, y)
        y_hat = model.predict(self.X)
        diff = y_hat - y
        rsq = 1 - np.mean(diff**2) / np.mean((y-np.mean(y))**2)
        assert_true(rsq > .99)
        
if __name__ == '__main__':
    import nose
    nose.run(argv=[__file__, '-s', '-v'])
    
    