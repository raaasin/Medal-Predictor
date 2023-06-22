# Olympic Medal Prediction Web Application

This repository contains code for a web application that predicts the number of medals a country is expected to achieve in the Olympics based on the number of athletes and previous medals won.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Introduction
The Olympic Medal Prediction Web Application is built using Python and Flask framework. It uses a linear regression model trained on historical data to predict the number of medals a country is expected to win in the Olympics.

The application loads data from a CSV file called `teams.csv`, which should contain information about different teams participating in the Olympics, including the team name, country, year, number of athletes, average age, previous medals won, and total medals won. The application pre-processes the data by selecting relevant columns and removing any rows with missing values.

A linear regression model is then trained using the selected predictors: the number of athletes and previous medals won. The trained model is saved to a file called `olympic.pkl` using pickle, a Python serialization library.

The web application utilizes the Flask framework to serve the predictive model. It provides a simple user interface where users can enter the number of athletes and previous medals of a country to obtain the predicted number of medals that country is expected to achieve. The prediction is performed by loading the trained model from the `olympic.pkl` file and making predictions using the provided features.

## Installation
To run the Olympic Medal Prediction Web Application locally, follow these steps:

1. Clone this repository to your local machine or download the code as a ZIP file.
2. Ensure you have Python 3 installed on your system.
3. Install the required dependencies by running the following command in your terminal:
   ```
   pip install -r requirements.txt
   ```

## Usage
1. Make sure you have completed the installation steps.
2. Place your data file named `teams.csv` in the same directory as the code files.
3. Run the following command in your terminal to start the web application:
   ```
   python app.py
   ```
4. Open a web browser and navigate to `http://localhost:5000` to access the web application.
5. Enter the number of athletes and previous medals for a country in the provided input fields.
6. Click the "Predict" button to see the predicted number of medals for that country.
7. The prediction will be displayed on the same page.

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). See the [LICENSE](./LICENSE) file for more details.

---

