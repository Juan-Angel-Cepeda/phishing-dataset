import joblib

def preditct(data,model):
    if model == "Support Vector Machine":
        model = joblib.load('models/svm_clasifier.pkl')
        pipeline = joblib.load('pipelines/pipeline_svm.pkl')
    elif model == "Random Forest Classifier":
        model = joblib.load('models/random_forest_clasifier.pkl')
        pipeline = joblib.load('pipelines/pipeline_trees.pkl')
    elif model == "Extra Trees Classifier":
        model = joblib.load('models/extra_trees_clasifier.pkl')
        pipeline = joblib.load('pipelines/pipeline_extra_trees.pkl')
    
    data = pipeline.transform(data)
    return model.predict(data)