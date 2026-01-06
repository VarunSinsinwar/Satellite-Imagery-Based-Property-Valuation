# Satellite-Imagery-Based-Property-Valuation
This project focuses on building a multimodal machine learning pipeline to predict residential property prices by integrating tabular housing attributes with satellite imagery. Traditional valuation models rely heavily on structured features such as size, location, and age of a property. This work extends that paradigm by incorporating visual neighborhood context extracted from satellite images.
The following sections explain each file in this repository.
## Data Fetcher Python script
This file contains the code which is used to fetch all the satellite images of a particular zoom and resolution using MapBox API. We first have to save the API token MAPBOX_TOKEN variable, which I have not shared in the script. All files will be saved to the assigned the folder.
## Preprocessing Python Notebook
This file contains the exploratory data analysis of the tabular data. It gives the idea of the data, and what feature engineering and preprocessing we can perform before model training.
## Model Training Python Notebook
This notebook contains the data reading, preprocessing (scaling, normalization and transformation), model making and training, and predictions on test dataset using the trained model. The model is a residual network. First, an only tabular (TabularFCNet) network is trained, then predictions are saved. After this, the fusion network (FusionRegressor) predicts the residuals. Then, finally both of them are added to get final predictions. Keeping models on evaluation mode, predictions are made and saved into test_predictions.csv file.
## Model TabularFCNet notebook
This contains the only tabular dta trained network. This is just for comparison to fusion architecture.
## Report
This is a pdf which contains the Report of the project, which has info about dataset, EDA, model architecture, Training strategy and conclusion.
