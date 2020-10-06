import joblib
import numpy as np
def get_price_of_mbike(enc_path, model_path):
    # Program need low letters because onehotencoder categories also are lower letters.
    brand = str(input("Select brand?: ")).lower()
    b_model = str(input("Select model?: ")).lower()
    capacity = int(input("What's the capacity of the model?: "))
    kilometers = int(input("How many kilometers motorcycle has driven?: "))
    year = int(input("What's the year of motorcycle?: "))

    model = joblib.load(model_path)
    enc = joblib.load(enc_path)
    # len(enc.categories_) is equal to 2, that's why I use list comprehension
    # to extreact data from list
    enc_cat_lst = [enc for model in enc.categories_ for enc in model]
    while True:
        if brand in enc_cat_lst:
            if b_model in enc_cat_lst:
                sample = np.array([brand, b_model, capacity, kilometers, year])
                cat = sample[:2]
                cat = cat.reshape(1, 2)
                sample_encoded = enc.transform(cat).toarray()
                sample_numerical = sample[2:].reshape(1, 3)
                full_sample = np.concatenate((sample_numerical, sample_encoded), axis=1)
                m_price = model.predict(full_sample)
                return "Price of your motorbike is equal to {} PLN".format(int(m_price[0]))
            else:
                return 'Unidentified model of motorbike please check spelling!'
        else:
            return 'Unidentified brand of a motorbike, please check spelling!'


if __name__ == "__main__":
    price = get_price_of_mbike(r'encoder\encoder.joblib', r'models\GradientRModel.joblib')
    print(price)
