# Motocykles Project.

The clue of this project was to download a instances of 14.000 motorcycles from [website](https://www.otomoto.pl/) try too find a great model with can predict prices

## Decription.

In scrapper I have created a tool with download a Data from website  
CSV contain cleaned csv file of motorcycles data  
encoder contains a One Hot Encoder uses to properly encode input data  
models contains models (NN, XGBoost, GradientBoost)  

## How to use.

You just need to run get_price.py and pass the features of motorcycle:
![obraz](https://user-images.githubusercontent.com/56366696/95180826-c5e37480-07c2-11eb-9de2-658d18b3bf56.png)

## Conclusion.

The XGBoost score is over 0.9 (0.9 R^2) at this step it's acceptable. Next iterations of model may have more data and better parameter tuning.
Overwall the task is to create web app and deploy it on heroku using XGBoost model.
