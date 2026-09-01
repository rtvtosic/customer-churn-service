import mlflow


def load_model(experiment: str = "Telco Customer Churn",
               tracking_uri: str = "http://localhost:5000"):
    mlflow.set_experiment(experiment)
    mlflow.set_tracking_uri(tracking_uri)

    model = mlflow.sklearn.load_model("models:/telco-churn-RandomForest@champion")

    return model
