# Customer Churn Prediction.

Customer attrition, also known as customer churn, customer turnover, or customer defection, is the loss of clients or customers.

Telephone service companies, Internet service providers, pay TV companies, insurance firms, and alarm monitoring services, often use customer attrition analysis and customer attrition rates as one of their key business metrics because the cost of retaining an existing customer is far less than acquiring a new one. Companies from these sectors often have customer service branches which attempt to win back defecting clients, because recovered long-term customers can be worth much more to a company than newly recruited clients.

Predictive analytics use churn prediction models that predict customer churn by assessing their propensity of risk to churn. Since these models generate a small prioritized list of potential defectors, they are effective at focusing customer retention marketing programs on the subset of the customer base who are most vulnerable to churn.

In this project I aim to build a model which can predict customer churn. I also aim to build an app which can be used to understand why a specific customer would stop the service and to know his/her expected lifetime value.  

## Final Customer Churn Prediction App
<img src=https://raw.githubusercontent.com/Ayush100304/Customer-Survival-Analysis-and-Churn-Prediction/main/app-pic.png>

## Project Organization
```
.
├── Images/                             : contains images
├── static/                             : plots to show gauge chart, hazard and survival curve, shap values in Flask App 
│   └── images/
│       ├── hazard.png
│       ├── surv.png
│       └── new_plot.png
├── templates/                          : contains html template for flask app
│   └── index.html
├── Exploratory Data Analysis.ipynb     : Data Analysis to understand customer data
├── Churn Prediction Model.ipynb        : Random Forest model to predict customer churn
├── app.py                              : Flask App
├── app-pic.png                         : Final App image  
├── requirements.txt                    : requirements to run this model
├── Procfile                            : procfile for app deployment
└── README.md                           : Report
```

## Customer Churn Prediction
I aim to implement a machine learning model to accurately predict if the customer will churn or not.

### Analysis

**Churn and Tenure Relationship:**

<p align="center">
<img src="https://raw.githubusercontent.com/Ayush100304/Customer-Survival-Analysis-and-Churn-Prediction/main/Images/tenure-churn.png" width="600" height="300"/>
</p>

- As we can see the higher the tenure, the lesser the churn rate. This tells us that the customer becomes loyal with the tenure.

<br />

**Tenure Distrbution by Various Services:**

<p align="center">
<img src="https://raw.githubusercontent.com/Ayush100304/Customer-Survival-Analysis-and-Churn-Prediction/main/Images/tenure-dist.png" width="340" height="250"/>
</p>

- When the customers are new they do not opt for various services and their churning rate is very high. This can be seen in above plot for Streaming Movies and this holds true for all various services.

<br />

**Internet Service By Contract Type:**

<p align="center">
<img src="https://raw.githubusercontent.com/Ayush100304/Customer-Survival-Analysis-and-Churn-Prediction/main/Images/internetservice-contract.png" width="360" height="250"/>
</p>

- Many of the people of who opt for month-to-month Contract choose Fiber optic as Internet service and this is the reason for higher churn rate for fiber optic Internet service type.

<br />

**Payment method By Contract Type:**

<p align="center">
<img src="https://raw.githubusercontent.com/Ayush100304/Customer-Survival-Analysis-and-Churn-Prediction/main/Images/payment-contract.png" width="500" height="250"/>
</p>

- People having month-to-month contract prefer paying by Electronic Check mostly or mailed check. The reason might be short subscription cancellation process compared to automatic payment.

<br />

**Monthly Charges:**

<p align="center">
<img src="https://raw.githubusercontent.com/Ayush100304/Customer-Survival-Analysis-and-Churn-Prediction/main/Images/monthlycharges.png" width="300" height="220"/>
</p>

- As we can see the customers paying high monthly fees churn more.

<br />

### Modelling

For the modelling, I will use tress based Ensemble method as we do not have linearity in this classification problem. Also, we have a class imbalance of 1:3 and to combat it I will assign class weightage of 1:3 which means false negatives are 3 times costlier than false positives. I built a model on 80% of data and validated model on remaining 20% of data keeping in mind that I do not have data leakage. The random forest model has many hyperparameters and I tuned them using Grid Search Cross Validation while making sure that I do not overfit.

The final model resulted in 0.62 F1 score and 0.85 ROC-AUC. The resulting plots can be seen below.

<p align="center">
<img src="https://raw.githubusercontent.com/Ayush100304/Customer-Survival-Analysis-and-Churn-Prediction/main/Images/model_1.png" width="600" height="300"/>
<img src="https://raw.githubusercontent.com/Ayush100304/Customer-Survival-Analysis-and-Churn-Prediction/main/Images/model_feat_imp.png" width="600" height="400"/>

</p>






