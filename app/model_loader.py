import pickle


def load_model(model_dir: str = "final_model"):
    with open(f"{model_dir}/model.pkl", 'rb') as f:
        model = pickle.load(f)

    return model


if __name__ == "__main__":
    model = load_model()
    print(model)