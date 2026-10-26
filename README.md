# Iris Flower Classification

College data mining mini-project with a short Python script and an editable Word report.

## Project files

- `main.py` — complete runnable Python program.
- `Iris_Flower_Classification_Report.docx` — college-style project report, including results and setup steps.

## Run in VS Code on Windows

1. Install Python 3 and Visual Studio Code. Add the Microsoft **Python** extension to VS Code.
2. Extract the downloaded project ZIP to a normal folder.
3. In VS Code, click **File > Open Folder**, then select the extracted folder.
4. Click **Terminal > New Terminal**.
5. Run `py -m pip install scikit-learn` to install the only extra package.
6. Run `py main.py`.
7. Read the species names, accuracy, confusion matrix, classification report, and sample prediction in the terminal.

If the `py` command is unavailable, try `python -m pip install scikit-learn` and `python main.py` instead. Use **Python: Select Interpreter** in VS Code if the correct Python environment is not selected.

## Method

The program loads scikit-learn's built-in Iris dataset, containing 150 flowers across 3 species and 4 flower measurements. It divides the records into 80% training and 20% testing, fits a maximum-depth-3 Decision Tree, and evaluates the held-out test set.

The final sample `[5.1, 3.5, 1.4, 0.2]` contains measurements in this order:

1. Sepal length (centimetres)
2. Sepal width (centimetres)
3. Petal length (centimetres)
4. Petal width (centimetres)

Replace these four numbers to test another hypothetical flower measurement. This is an educational classifier trained on a small, classic dataset, so a high test accuracy is not a guarantee of performance on photographs or other plant species.

## Dataset and documentation

- scikit-learn built-in Iris dataset: https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html
- scikit-learn DecisionTreeClassifier: https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html
