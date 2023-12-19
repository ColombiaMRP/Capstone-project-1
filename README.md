# How Should We Price Homes In Seattle?
Machine learning Zoomcamp Capstone Project to assist Seattle residents willing to sell their home with determining an optimal price

## Bussines description and analitical context
The provided dataset was retrieved from [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction) and includes sales prices of houses in the state of Washington (King county, where Seattle is located) between May 2014 and May 2015 among other explicative variables. The idea is to use those variables in order build a competent model to predict house sales prices. The primary tool used is regression model which, even with box-cox tranformed variables because of lack of normality, behaves poorly. Regularized regression model behaved even worst. Considering this, we studied two extra three base models on this data: Random forest and Xgboost. After finding that using original variables rather than box-cox tranformed resulted in better results with these models, we selected the best model to create a Web service which is latter isolated in a docker container and used in production, namely, to make the prediction of a house price in Seattle. Used variables are:

1. **id**: identification for a house
2. **date**: date house was sold
3. **price**: price house was sold at
4. **bedrooms**: number of bedrooms
5. **bathrooms**: number of bathrooms
6. **sqft_living**: square footage of the home
7. **sqft_lot**: square footage of the lot
8. **floors**: total floors (levels) in house
9. **waterfront**: whether or not the house has a view of a waterfront
10. **view**: an index from 0 to 4 of how good the view from the property is
11. **condition**: how good the condition of the house is
12. **grade**: overall grade given to the housing unit, based on King County grading system
13. **sqft_above**: square footage of the house apart from basement
14. **sqft_basement**: square footage of the basement
15. **yr_built**: year house was built
16. **yr_renovated**: year house was renovated
17. **zipcode**: zipcode of the house
18. **lat**: latitude coordinate of the house
19. **long**: longitude coordinate of the house


## How to use this repository

### Pre-requesits

```python
python
git
docker
```

### Cloning repository

First you should clone the repository to your local machine

```python
git https://github.com/ColombiaMRP/Capstone-project-1.git
```

### Virtual enviroment and Dependencies (Direct python running)

If you are going to directly run the jupyter notebook files or web service, you first have to set up the dedicated virtual enviroment and install dependencies. For doing so you should first go to the root of the project (the folder you have just cloned) and:

  1. Ensure that ```pipenv``` is installed. You can install it running:

      ```python
      pip install pipenv
      ```
     
  2. Set up the virtual enviroment and install dependencies. Including "-e ." makes the packages available within all the files in an editable mode:

      ```python
      pipenv install -e .
      ```
     You can see the list of installed packages using:

      ```python
      pipenv run pip freeze
      ```
     
  4. Now you can activate the VE and run python files for training the model and using it for predicting:

     ```python
      pipenv shell
      python train.py
      python predict.py
      ```
     Take into account that, for testing our model and making predictions, we use an example of a house with these chracteristics:

     ```python
     house ={'bedrooms':3,
             'bathrooms':4,
             'floors':3,
             'waterfront':0,
             'view':3,
             'condition':2,
             'grade':10,
             'yr_built':2004,
             'lat':47.6846,
             'long':-122.291,
             'sqft_living':1700,
             'sqft_lot':4100,
             'sqft_above':2000,
             'sqft_basement':800,
             'sqft_living15':3200,
             'sqft_lot15':6000}
             }
     ```
     
### Web Service Deployment

To host the service locally using the virtual environment, you need to start the flask aplication running:

```python
waitress-serve --listen=0.0.0.0:9696 WS_train:app
```
Now the Flask application is running, you can make HTTP requests to port 9696 running the file ```WS_predict.py``` where the house whose characteristics were defined above are passed in a json form and used for making a price prediction. Namely, you should run:

```python
pipenv WS_predict.py
```

### Docker Deployment

In Case you want to deploy the web service using and specific and dedicated docker container for that, the steps you might follow are:

  1. download the python image you need for containerizing the providing files using docker. You can do this running:

     ```python
      docker run python python:3.11-slim
      ```
  2. Build an image using the dockerfile provided in the repository:

     ```python
     docker build -t "image_name" .
      ```
  3. To list all the Docker images on your system and verify that the image is there, use:

     ```python
     docker images
      ```
  4. Now the image has been created, you can run a container from it using:

      docker run -it --rm -p 9696:9696 "image_name"

With the Flask application running inside Docker you can make HTTP requests to port 9696 running the file ```WS_predict.py``` where the house whose characteristics were defined above are passed in a json form and used for making a price prediction. Namely, you should run:

```python
pipenv WS_predict.py
```


### Final considerations

You can change the parameters to test out different scenarios by changing values or parameters in files ```predict.py``` (python direct running)  or ```WS_predict.py```(python web service/docker container running). Once you are happy with the ressults you can run again these files in either case for making predictions in a new console window inside the project folder. 

I would like to give a special "thank-you" to all my colleagues, as I recieved a warm collaboration from them all during the procces of building my project. I also thank for your future and sincere feedback to keep improving my habilities at this beatifull work.
