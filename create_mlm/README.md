# Creating the machine learning model
Since the problem was a classification problem, the model had to be a supervised classification model.
## Choosing the right model
I built a pipeline that allowed me to train two classification models in parallel and compare the results directly. 
The models were Random Forest and Logistic Regression. In the end, the Random Forest Model was chosen.
## Hyperparamter Tuning with GridSearch
To fine tune the model I used GridSearch. Since I had a data set with nearly 60.000 data points, I trained GridSearch with a GPU to speed up the process.
## Results
After the Hyperparamter Tuning the results were. 

Train accuracy:   82%

Test  accuracy:   74%

Cross-Validation: 75%

## Features
I used a total of 9 technical features to build the machine learning model. 
4 of the features were relations features, which I created myself to show the relation of price to certain factors.









## License
[MIT](https://choosealicense.com/licenses/mit/)
