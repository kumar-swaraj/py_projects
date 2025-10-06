import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from model import Prediction
from sklearn.linear_model import LinearRegression  # type: ignore
from sklearn.metrics import mean_absolute_error, r2_score  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore


def make_prediction(
    inputs: list[float], outputs: list[float], input_value: float, plot: bool = False
) -> Prediction:
    if len(inputs) != len(outputs):
        raise Exception("Length of 'inputs' and 'outputs' must match")

    # Create a dataframe for our data
    df = pd.DataFrame(dict(inputs=inputs, outputs=outputs))

    # Reshape the data using Numpy (X: Inputs, Y: Outputs)
    X = np.array(df["inputs"]).reshape(-1, 1)
    Y = np.array(df["outputs"]).reshape(-1, 1)

    # Split the data into training data to test our model
    train_X, test_X, train_Y, test_Y = train_test_split(
        X, Y, random_state=0, test_size=0.20
    )

    # Initialize the model and test it
    model = LinearRegression()
    model.fit(train_X, train_Y)

    # Prediction
    y_prediction = model.predict([[input_value]])  # type: ignore
    y_line = model.predict(X)

    # Testing for accuracy
    y_test_prediction = model.predict(test_X)

    # Plot the data
    if plot:
        display_plot(inputs=X, outputs=Y, y_line=y_line)  # type: ignore

    # Return the data
    return Prediction(
        value=y_prediction[0][0],
        r2_score=r2_score(test_Y, y_test_prediction),
        slope=model.coef_[0][0],
        intercept=model.intercept_[0],  # type: ignore
        mean_absolute_error=mean_absolute_error(test_Y, y_test_prediction),
    )


def display_plot(inputs: list[float], outputs: list[float], y_line):
    plt.scatter(inputs, outputs, s=12)
    plt.xlabel("Input")
    plt.ylabel("Outputs")
    plt.plot(inputs, y_line, color="r")
    plt.show()


def main() -> None:
    years: list[float] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    earnings: list[float] = [1000, 800, 2000, 1500, 3400, 3700, 4000, 3800, 5000, 4800]
    my_input: int = 25

    prediction: Prediction = make_prediction(
        inputs=years,
        outputs=earnings,
        input_value=my_input,
        plot=False,
    )
    print("Input:", my_input)
    print(prediction)


if __name__ == "__main__":
    main()
