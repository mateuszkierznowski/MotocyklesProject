import pandas as pd
import numpy as np
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
import joblib
from tensorflow.keras.layers import Dense, Input, Dropout, BatchNormalization
from sklearn.metrics import mean_absolute_error
import tensorflow as tf
from tensorflow.keras.models import Sequential

ohe = OneHotEncoder()
model = GradientBoostingRegressor()
df = pd.read_csv(r'CSV/motocykle_clean.csv', index_col=[0])
df = df.reset_index(drop=True)
categorical_cols = ['marka', 'model']
df['marka'] = df['marka'].str.lower()
df['model'] = df['model'].str.lower()
array = ohe.fit_transform(df[categorical_cols]).toarray()
array = pd.DataFrame(array)
numerical_cols = ['pojemnosc', 'przebieg', 'year']
new_df = pd.concat([df[numerical_cols], array], axis=1)

X = new_df
y = df['price']

model = GradientBoostingRegressor()
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model.fit(x_train, y_train)
model.score(x_test, y_test)
#joblib.dump(ohe, 'encoder/encoder.joblib')
#joblib.dump(model, 'GradientRModel.joblib')

random_regr = RandomForestRegressor()
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
random_regr.fit(x_train, y_train)
random_regr.score(x_test, y_test)

xgboost = XGBRegressor()
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
xgboost.fit(x_train, y_train)
xgboost.score(x_test, y_test)
#joblib.dump(xgboost, 'models/XGBoost.joblib')

#Categorical data is only Brand instead of Brand and Model
ohe = OneHotEncoder()
model = GradientBoostingRegressor()
df = pd.read_csv('motocykle_clean.csv', index_col=[0])
df = df.reset_index(drop=True)
categorical_cols = ['marka']
df['marka'] = df['marka'].str.lower()
df['model'] = df['model'].str.lower()
array = ohe.fit_transform(df[categorical_cols]).toarray()
array = pd.DataFrame(array)
numerical_cols = ['pojemnosc', 'przebieg', 'year']
new_df = pd.concat([df[numerical_cols], array], axis=1)

X = new_df
y = df['price']
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = tf.keras.models.Sequential()
NN_model = 1
NN_model = Sequential()
NN_model.add(Input(732,))
NN_model.add(Dense(256, kernel_initializer='normal', activation='relu'))
NN_model.add(Dropout(0.1))
NN_model.add(Dense(256, kernel_initializer='normal', activation='relu'))
NN_model.add(Dense(256, kernel_initializer='normal', activation='relu'))
NN_model.add(BatchNormalization())
NN_model.add(Dense(1, activation='linear'))

# Compile the network :
NN_model.compile(loss='mean_squared_error', optimizer='adam', metrics=['mean_absolute_error'])
NN_model.summary()
NN_model.fit(
    x=x_train,
    y=y_train,
    batch_size=12,
    epochs=20,
    validation_data=(x_test, y_test)
)
#joblib.dump(ohe,  'encoder/encoder_1_cat.joblib')
NN_model.save(r'models/NN_model.h5')