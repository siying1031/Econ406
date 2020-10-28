"""
Siying homework3 Q1
"""
import pandas as pd
import numpy as np

#df = pd.read_csv('campus.csv')

def extract_variable_means(dataset_filename):
    '''Calculates the mean values of the number of total campus crimes,
    employedpolice officers, and total college enrollment.

    Parameters
    ----------
    dataset_filename​ : String
        The name of the dataset.

    Returns
    -------
    List
        Mean of the number of total campus crimes, employedpolice officers,
        and total college enrollment .

    '''
    data_frame = pd.read_csv(dataset_filename)
    data_frame = data_frame.dropna()
    df_mean = data_frame[['crime','police','enroll']].mean()
    return df_mean.tolist()

def extract_estimator_and_covariance(dataset_filename):
    '''Calculates the ols estimator vector

    Parameters
    ----------
    dataset_filename : Sting
       Name of the dataset.

    Returns
    -------
    Array
        The value of Beta Hat, the estimator.

    '''
    data_frame = pd.read_csv(dataset_filename)
    data_frame = data_frame.dropna()
    #Only Keep the data of lcrime and lenroll
    beta_1 = data_frame.iloc[:,4:6]
    # Transform b1 to array
    beta_1 = np.array(beta_1).astype('float')
    nrow = beta_1.shape[0]

    intercept = np.ones((nrow,1))
    # add a column of 1’s in the dataset.
    beta_2 = beta_1[:,1].reshape(-1,1)

    # X independent variable: lenroll
    x_lenroll = np.concatenate((intercept,beta_2),axis=1)
    # Y dependent variable: lcrime
    y_lcrime= beta_1[:,0].T

    b_hat = np.dot(np.linalg.inv(np.dot(x_lenroll.T,x_lenroll)),np.dot(x_lenroll.T,y_lcrime))
    return b_hat
