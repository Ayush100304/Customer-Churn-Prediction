import numpy as np
import pickle
from flask import Flask, request, render_template

app = Flask(__name__)

model = pickle.load(open("model.pkl", "rb"))


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    gender = int(request.form["gender"])

    SeniorCitizen = 1 if "SeniorCitizen" in request.form else 0
    Partner = 1 if "Partner" in request.form else 0
    Dependents = 1 if "Dependents" in request.form else 0
    PaperlessBilling = 1 if "PaperlessBilling" in request.form else 0

    MonthlyCharges = int(request.form["MonthlyCharges"])
    Tenure = int(request.form["Tenure"])
    TotalCharges = MonthlyCharges * Tenure

    PhoneService = 1 if "PhoneService" in request.form else 0

    MultipleLines = 0
    if PhoneService and "MultipleLines" in request.form:
        MultipleLines = 1

    InternetService_Fiberoptic = 0
    InternetService_No = 0

    if request.form["InternetService"] == "0":
        InternetService_No = 1
    elif request.form["InternetService"] == "2":
        InternetService_Fiberoptic = 1

    OnlineSecurity = (
        1 if ("OnlineSecurity" in request.form and InternetService_No == 0) else 0
    )

    OnlineBackup = (
        1 if ("OnlineBackup" in request.form and InternetService_No == 0) else 0
    )

    DeviceProtection = (
        1 if ("DeviceProtection" in request.form and InternetService_No == 0) else 0
    )

    TechSupport = (
        1 if ("TechSupport" in request.form and InternetService_No == 0) else 0
    )

    StreamingTV = (
        1 if ("StreamingTV" in request.form and InternetService_No == 0) else 0
    )

    StreamingMovies = (
        1 if ("StreamingMovies" in request.form and InternetService_No == 0) else 0
    )

    Contract_Oneyear = 0
    Contract_Twoyear = 0

    if request.form["Contract"] == "1":
        Contract_Oneyear = 1
    elif request.form["Contract"] == "2":
        Contract_Twoyear = 1

    PaymentMethod_CreditCard = 0
    PaymentMethod_ElectronicCheck = 0
    PaymentMethod_MailedCheck = 0

    if request.form["PaymentMethod"] == "1":
        PaymentMethod_CreditCard = 1
    elif request.form["PaymentMethod"] == "2":
        PaymentMethod_ElectronicCheck = 1
    elif request.form["PaymentMethod"] == "3":
        PaymentMethod_MailedCheck = 1

    features = [[
        gender,
        SeniorCitizen,
        Partner,
        Dependents,
        Tenure,
        PhoneService,
        MultipleLines,
        OnlineSecurity,
        OnlineBackup,
        DeviceProtection,
        TechSupport,
        StreamingTV,
        StreamingMovies,
        PaperlessBilling,
        MonthlyCharges,
        TotalCharges,
        InternetService_Fiberoptic,
        InternetService_No,
        Contract_Oneyear,
        Contract_Twoyear,
        PaymentMethod_CreditCard,
        PaymentMethod_ElectronicCheck,
        PaymentMethod_MailedCheck
    ]]

    prediction = model.predict(features)[0]
    probability = model.predict_proba(features)[0][1]

    result = "Customer is likely to Churn" if prediction == 1 else "Customer is not likely to Churn"

    return render_template(
        "index.html",
        prediction_text=result,
        probability=f"{probability*100:.2f}%"
    )


if __name__ == "__main__":
    app.run(debug=True)
