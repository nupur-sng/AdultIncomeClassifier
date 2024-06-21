# Adult Income Classifier

This Streamlit web application predicts whether a person's income exceeds $50K/year based on various demographic features. The app uses a Random Forest classifier trained on the [Adult Income dataset](https://archive.ics.uci.edu/ml/datasets/adult) from the UCI Machine Learning Repository.

## Dataset Information

The dataset was extracted from the 1994 Census bureau database by Ronny Kohavi and Barry Becker. It contains a set of reasonably clean records selected using the conditions: ((AAGE>16) && (AGI>100) && (AFNLWGT>1) && (HRSWK>0)). The prediction task is to determine whether a person makes over $50K a year.

### Features

- **age**: continuous.
- **workclass**: Private, Self-emp-not-inc, Self-emp-inc, Federal-gov, Local-gov, State-gov, Without-pay, Never-worked.
- **fnlwgt**: continuous.
- **education**: Bachelors, Some-college, 11th, HS-grad, Prof-school, Assoc-acdm, Assoc-voc, 9th, 7th-8th, 12th, Masters, 1st-4th, 10th, Doctorate, 5th-6th, Preschool.
- **education_num**: continuous.
- **marital_status**: Married-civ-spouse, Divorced, Never-married, Separated, Widowed, Married-spouse-absent, Married-AF-spouse.
- **occupation**: Tech-support, Craft-repair, Other-service, Sales, Exec-managerial, Prof-specialty, Handlers-cleaners, Machine-op-inspct, Adm-clerical, Farming-fishing, Transport-moving, Priv-house-serv, Protective-serv, Armed-Forces.
- **relationship**: Wife, Own-child, Husband, Not-in-family, Other-relative, Unmarried.
- **race**: White, Asian-Pac-Islander, Amer-Indian-Eskimo, Other, Black.
- **sex**: Female, Male.
- **capital_gain**: continuous.
- **capital_loss**: continuous.
- **hours_per_week**: continuous.
- **native_country**: United-States, Cambodia, England, Puerto-Rico, Canada, Germany, Outlying-US(Guam-USVI-etc), India, Japan, Greece, South, China, Cuba, Iran, Honduras, Philippines, Italy, Poland, Jamaica, Vietnam, Mexico, Portugal, Ireland, France, Dominican-Republic, Laos, Ecuador, Taiwan, Haiti, Columbia, Hungary, Guatemala, Nicaragua, Scotland, Thailand, Yugoslavia, El-Salvador, Trinadad&Tobago, Peru, Hong, Holand-Netherlands.

### Target Variable

- **income**: <=50K, >50K.

## About fnlwgt (final weight)

The `fnlwgt` represents the final weight of the survey sample and is used to ensure that the sample reflects the actual population distribution. It's controlled to independent estimates of the civilian noninstitutional population of the US, prepared monthly by the Census Bureau.

For more details about the dataset, you can visit the [dataset page](https://archive.ics.uci.edu/ml/datasets/adult).

## Access the App

You can access the deployed Random Forest model-based app [here](https://adultincomeclassifier-o9u0pczpe9.streamlit.app/).

---

This README provides an overview of the Adult Income Classifier app, the dataset used, and additional information about the `fnlwgt` feature. For more detailed documentation, feel free to explore the app itself and the dataset sources.
