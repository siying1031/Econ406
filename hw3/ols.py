"""
Siying homework3 Q1
"""
import pandas as pd
import numpy as np

df = pd.read_csv('campus.csv')

def extract_variable_means(dataset_filename):
    '''Calculates the mean values of the number of total campus crimes, 
    employedpolice officers, and total college enrollment.
    
    Parameters
    ----------
    dataset_filename​ : String
        The name of the dataset.

    Returns
    -------
    Int
        Mean of the number of total campus crimes, employedpolice officers, 
        and total college enrollment .

    '''
    df = pd.read_csv(dataset_filename)
    df = df.dropna()
    df_mean = df[['crime','police','enroll']].mean()
    return df_mean.tolist()

def extract_estimator_and_covariance(dataset_filename):
    '''Calculates the ols estimator vector
    
    Parameters
    ----------
    dataset_filename : Sting
       Name of the dataset.

    Returns
    -------
    Int
        The value of Beta Hat, the estimator.

    '''
    df = pd.read_csv(dataset_filename)
    df = df.dropna()    
    #Only Keep the data of lcrime and lenroll
    b1 = df.iloc[:,4:6]
    # Transform b1 to array
    b1 = np.array(b1).astype('float')
    nrow = b1.shape[0]

    intercept = np.ones((nrow,1))
    #Add a column of 1’s in the dataset.
    b2 = b1[:,1].reshape(-1,1)
    
    # X independent variable: lenroll
    X = np.concatenate((intercept,b2),axis=1)
    # Y dependent variable:lcrime
    Y = b1[:,0].T

    bh = np.dot(np.linalg.inv(np.dot(X.T,X)),np.dot(X.T,Y))
    return bh
