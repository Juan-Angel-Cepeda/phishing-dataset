import joblib

def preditct(data,model):
    if model == "Support Vector Machine":
        model = joblib.load(f'models/svm_clasifier.pkl')
    elif model == "Random Forest Classifier":
        model = joblib.load(f'models/random_forest_clasifier.pkl')
    elif model == "Extra Trees Classifier":
        model = joblib.load(f'models/extra_trees_clasifier.pkl')
    
    return model.predict(data)