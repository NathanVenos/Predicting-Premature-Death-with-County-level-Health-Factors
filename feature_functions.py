import pandas as pd
from statsmodels.stats.outliers_influence import variance_inflation_factor
from sklearn.linear_model import LassoLarsIC
from itertools import combinations

def variance_inflation_factor_printout(feature_list, DataFrame):
    """
    Passes the inputs into statsmodel's variance_inflation_factor function.
    Returns a DataFrame with each feature and its variance inflation factor.
    """
    feature_df = DataFrame[feature_list]
    vif = [variance_inflation_factor(feature_df.values, i)
           for i in range(feature_df.shape[1])]
    data = list(zip(feature_list, vif))
    data_df = pd.DataFrame(data, columns=['Feature','VIF'])
    return data_df

def LassoLarsIC_df(X, y, criterion):
    """
    Passes the inputs into sklearn's LassoLarsIC model selection function.
    Returns the rss, intercept and all coefficients as a DataFrame 
    as well as a list containing the features with non-zero coefficients.
    """
    model = LassoLarsIC(criterion=criterion)
    model.fit(X, y.iloc[:, 0])

    model_rss = model.score(X, y.iloc[:, 0])
    results = ([model_rss]
               + [model.intercept_]
               + list(model.coef_))

    results_cols = ['rss', 'intercept']+list(X.columns)
    results_dict = {'results': results}
    results_df = pd.DataFrame.from_dict(results_dict,
                                        orient="index",
                                        columns=results_cols)
    remaining_features = list(
        results_df.iloc[0][results_df.iloc[0] != 0].index[2:])
    
    return results_df, remaining_features

def add_interactions_and_squares(DataFrame):
    """
    Takes a Dataframe of features and adds columns with
    an interaction for every cobination of features as well as
    the square of each feature.
    Returns the resulting DataFrame.
    """
    df = DataFrame.copy()
    for combo in combinations(df.columns,2):
        df[str(combo[0])
               +'_INTERACTION_'
               +str(combo[1])] = df[combo[0]] * df[combo[1]]

    for col in df.columns:
        df[col+'_2'] = df[col]**2
    
    return df