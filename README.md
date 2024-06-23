# Overview of Adult Income Classifier

This Streamlit web application predicts whether a person's income exceeds $50K/year based on various demographic features. The app uses a Random Forest classifier trained on the [Adult Income dataset](https://archive.ics.uci.edu/ml/datasets/adult) from the UCI Machine Learning Repository.

This model can be useful depending on scenarios:

- **Healthcare**: This could enable healthcare institutions to study the data of older population and develop targeted health plans for them.
- **Risk Management**: Insurance companies can use this model to look out for people with more risk, which could influence premium rate or loan terms.

# Data Description

The dataset was extracted from the 1994 Census bureau database. I have handled the '?' in the dataset with 'NA'. This will prevent potential inconsistencies during model training. The prediction task is to determine whether a person makes over $50K a year.

### Features

| Variable Name  | Type        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| -------------- | ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| age            | Integer     | age of the person                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| workclass      | Categorical | Describes socioeconomic group of the person - Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked                                                                                                                                                                                                                                                                                                        |
| fnlwgt         | Categorical | Describes weight assigned by the US census bureau to each row                                                                                                                                                                                                                                                                                                                                                                                              |
| education      | Categorical | Highest education of the person - Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool                                                                                                                                                                                                                                                                    |
| education-num  | Integer     | Number of years spent in education. Ex. 1 denotes Preschool and 16 signifies Doctorate                                                                                                                                                                                                                                                                                                                                                                     |
| marital-status | Categorical | Marital status of the person - Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse                                                                                                                                                                                                                                                                                                                   |
| occupation     | Categorical | Professional of the person - Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces                                                                                                                                                                                                      |
| relationship   | Categorical | Describes relationship, if any to other person in the dataset. Example, Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried                                                                                                                                                                                                                                                                                                                 |
| race           | Categorical | Describes human categorization - White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black                                                                                                                                                                                                                                                                                                                                                               |
| sex            | Binary      | Biological attributes - Female, Male                                                                                                                                                                                                                                                                                                                                                                                                                       |
| capital-gain   | Continuous  | Amount the person represented by this record has gained                                                                                                                                                                                                                                                                                                                                                                                                    |
| capital-loss   | Continuous  | Amount the person represented by this record has lost                                                                                                                                                                                                                                                                                                                                                                                                      |
| hours-per-week | Continuous  | Hours per week a person has worked                                                                                                                                                                                                                                                                                                                                                                                                                         |
| native-country | Categorical | Native Country of Person - United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands. |
| income         | Integer     | Income of the person >50K,<=50K                                                                                                                                                                                                                                                                                                                                                                                                                            |



### Target Variable

- **income**: <=50K, >50K.

### About fnlwgt (final weight)

The `fnlwgt` represents the final weight of the survey sample and is used to ensure that the sample reflects the actual population distribution. It's controlled to independent estimates of the civilian noninstitutional population of the US, prepared monthly by the Census Bureau.

For more details about the dataset, you can visit the [dataset page](https://archive.ics.uci.edu/ml/datasets/adult).

# Algorithm Description

- **Random Forest Setup**: Constructed a Random Forest classifier, which is consisting of multiple decision trees.
- **Hyperparameter Tuning**: Fine-tuned hyperparameters such as the number of trees (n_estimators), maximum depth of each tree (max_depth), minimum samples required to split a node (min_samples_split), etc., using techniques like grid search or random search.
- **Training Process**: Fit the Random Forest model to the training data, where each decision tree is trained on a bootstrap sample of the data (randomly sampled with replacement).
- **Prediction**: Use the trained Random Forest model to predict whether an individual's salary is likely to be greater than 50k based on their feature inputs.

# Tools Used

- **Streamlit app**: Streamlit is a popular framework for building interactive web applications with Python.

## Access the App

You can access the deployed Random Forest model-based app [here](https://adultincomeclassifier-o9u0pczpe9.streamlit.app/).

# Ethical Concerns

- **Data Bias**: The dataset used for training the model might reflect historical biases or inequalities (e.g. gender or racial biases in salaries). This can lead to biased predictions.
- **Mitigation**: We can conduct thorough bias assessments on the dataset. Also, by ensuring diverse representation in the dataset and considering using techniques that do not bias, during model training.

