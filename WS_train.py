from flask import Flask
from flask import request
from flask import jsonify
import pickle
import xgboost as xgb
import re
import numpy as np



model_file='m_xgb_rg.bin'

with open(model_file,'rb') as f_in:
    dv,model=pickle.load(f_in)

app = Flask('app')


@app.route('/WS_train', methods=['POST'])
def predict():
    house = request.get_json()

    features = dv.get_feature_names_out()
    features = [re.sub(r'[\[\]<>]', '', feature) for feature in features]

    x = dv.transform([house])
    dval = xgb.DMatrix(x, feature_names=features)

    y_pred = model.predict(dval)

    result = {
        'Estimated price': np.exp(float(y_pred)),
    }

    return jsonify(result)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=9696)

