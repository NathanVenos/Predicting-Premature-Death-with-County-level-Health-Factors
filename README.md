# Where The Healthy People Are
Project Rationale: Health insurance companies could only use Adjusted Community Rating for pricing all health plans sold on the individual and small group insurance markets. One of the criteria for ACR is geographic area and many US states and territories set administrative counties as the boundary insurers can use for risk adjustment. We analyze county-level health data to see how well we can predict population health based on observable factors. 

Methodology: We use data from the RWJF County Health Rankings & Roadmap project to perform a Least Angel Regression in a Lasso Regression model for our feature selection in predicting premature death as measured by Years of Potential Life Lost in a county in 2018. We applied a cross-validation approach to our model as well as examine each feature, its quatratic, and interaction effects to arrive at our final model. After settling on a model we apply it to our test data and find that our estimates perform almost exactly as under training data.  
  
Presentation Link: https://docs.google.com/presentation/d/1vHJyUb5ubBKMJhIvFHG3cZ5jyBuqF6pLcCf4nZIZbqo/edit?usp=sharing
