import pickle
from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

# Function to train the model and save it as a pickle file
def train_model():
    iris = load_iris()
    X, y = iris.data, iris.target
    clf = RandomForestClassifier()
    clf.fit(X, y)
    # Save the trained model
    with open("app/model.pkl", "wb") as f:
        pickle.dump(clf, f)

if __name__ == "__main__":
    train_model()
