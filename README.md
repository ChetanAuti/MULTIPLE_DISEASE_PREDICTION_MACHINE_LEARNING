# Multiple Disease Prediction System

A Streamlit-based dashboard for predicting Diabetes, Heart Disease, and Parkinson's Disease using pre-trained scikit-learn models. The app provides interactive, form-based inputs that match the models' training features and gives instant predictions.

**Project Structure**

- `app.py` - Main Streamlit application with UI and prediction forms.
- `Dataset/` - CSV datasets used for training: `diabetes.csv`, `heart.csv`, `parkinsons.csv`.
- `Notebook/` - Jupyter notebooks used for training and experimentation.
- `savedModels/` - Pre-trained and serialized models: `diabetes.sav`, `heart.sav`, `parkinsons.sav`.

**Requirements / Prerequisites**

- Python 3.8+ (tested with 3.10/3.11)
- pip

Recommended: create and activate a virtual environment:

```bash
python -m venv .venv
# Windows
.\.venv\Scripts\activate
# macOS / Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

If you don't have `requirements.txt`, install the core packages:

```bash
pip install streamlit scikit-learn pandas numpy streamlit-option-menu
```

**Running the App Locally**

1. Ensure the virtual environment is active and dependencies are installed.
2. From the project root, run:

```bash
streamlit run app.py
```

3. Open the browser at the address Streamlit prints (typically `http://localhost:8501`).

**Using the App**

- Use the left sidebar to pick one of the three prediction models: Diabetes, Heart Disease, or Parkinson's.
- Each model has a form with inputs that mirror the features the model was trained on. Fill the fields and click the form's submit button.
- The app returns a clear positive/negative message with a small result card.

Notes on controls:
- Encoded categorical fields are presented as discrete selectors to match the integer-encoded training values.
- Numeric inputs use `st.number_input` wrappers to ensure types match the model expectations.

**Model Details**

- Models are stored in `savedModels/` as pickle files. They were trained using scikit-learn and serialized with `pickle`.
- If you need to retrain a model, use the notebooks inside the `Notebook/` folder. The notebooks demonstrate data loading, preprocessing, model training, simple evaluation, and serialization.

**Rebuilding/Re-training Models**

A brief guideline to retrain models:

1. Open the corresponding notebook in `Notebook/` (e.g., `notebook/diabetes_prediction.ipynb`).
2. Verify paths to the dataset in `Dataset/` and adjust preprocessing if necessary.
3. Train and evaluate the model using scikit-learn.
4. Save the model with:

```python
import pickle
with open('savedModels/diabetes.sav', 'wb') as f:
    pickle.dump(model, f)
```

Make sure the trained model's `n_features_in_` matches the number of inputs the `app.py` form sends.

**Troubleshooting**

- Streamlit import errors: ensure you installed `streamlit` in the active environment.
- Format/string errors in inputs: helper functions `int_input()` and `float_input()` in `app.py` ensure correct argument order and types; avoid passing help text into the `format` parameter.
- Model shape errors: `ValueError: X has 8 features, but Model is expecting 22 features` indicates a mismatched model file. Rebuild or load the correct model matching the form inputs.

**Development Notes**

- UI helpers are implemented in `app.py` as `int_input()` and `float_input()` wrappers.
- The app uses `@st.cache_resource` to cache model loading for faster reloads.
- Styling is provided via inline CSS inside `app.py`.

**Contributing**

- Feel free to open issues or submit pull requests. Suggested improvements:
  - Add input presets for quick testing
  - Add SHAP/LIME explanations for predictions
  - Add logging and API endpoints for batch predictions

**License**

This project is provided as-is for educational purposes. Add your preferred license file (`LICENSE`) if you plan to publish or redistribute.

**Contact / Maintainer**

For questions, run instructions, or contribution discussion, open an issue in the repository or contact the maintainer.
