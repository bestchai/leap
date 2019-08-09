import pdb
import json
import inspect
import numpy as np

""" Returns differentially private result through the laplace mechanism
Adds noise from laplace distribution to result such that result is epsilon, delta dp
"""
def laplace(result, epsilon, delta, sensitivity):
    if delta == 0:
        noise = np.random.laplace(loc = 0, scale = sensitivity/float(epsilon), size = (1,1))
    else:    
        sigma = (sensitivity/(epsilon))*np.sqrt(2*np.log(1.25/delta))
        noise = np.random.normal(0.0, sigma, 1)

    return result + noise

""" Returns differentially private result through the exponential mechanism
http://dimacs.rutgers.edu/~graham/pubs/slides/privdb-tutorial.pdf
https://www.cis.upenn.edu/~aaroth/courses/slides/Lecture3.pdf

epsilon, delta: sampled output is epsilon delta differentially private
D: Dataset
out_range: candidate output values to sample from
score_fn(Dataset, output): returns how good output is for Dataset
sensitivity:    sensitivity of the score function for dataset D
"""
def exponential(epsilon, delta, D, out_range, score_fn, sensitivity=None):
    sample_pr = np.zeros(len(out_range))
    # Expensive computation of the sensitivity
    if sensitivity is None:
        sensitivity = -1
        for i,y in enumerate(D):
            D_prime = D[:i] + D[i+1:]
            for y in out_range:
                q_d = score_fn(D, y)
                q_d_prime = score_fn(D_prime, y)
                candidate_sensitvity = abs(q_d - q_d_prime)
                if candidate_sensitvity > sensitivity: 
                    sensitivity = candidate_sensitvity

    for i,y in enumerate(out_range):
        sample_pr[i] = np.exp(epsilon*score_fn(D, y / (2*sensitivity)))
    sample_pr = sample_pr / sample_pr.sum()
    
    sample = np.random.choice(out_range, 1, p=sample_pr).item()
    return sample