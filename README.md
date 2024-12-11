# NFL Game Predictor

Welcome to the **NFL Game Predictor** repository! This project uses a **Random Forest Classifier** to predict the outcomes of NFL games based on team statistics. The predictions include confidence scores and take into account home-field advantage. This repository contains the backend machine learning model and all necessary datasets. Our front-end is hosted on **Streamlit** at [NFL Game Predictor App](https://nflgamepredictor-5hckdtkzbdzot6ynmrtpky.streamlit.app).

---

## Repository Structure

### Files and Directories

- **`Random_forest_FINAL.ipynb`**: The main Jupyter Notebook containing the machine learning pipeline, from data preprocessing to model training and evaluation.
- **Datasets**:
  - Individual team data files (e.g., `49ers_data.csv`, `bears_data.csv`): Contain team-specific stats used to train and test the model.
  - `total_schedule.csv`: Consolidated schedule of games.
  - `football_stats.csv`: Includes aggregated and additional metrics for analysis.
- **Model Files**:
  - `random_forest_model.joblib`: Trained Random Forest model.
  - `scaler.pkl`: Scaler used for feature normalization.
- **`model_webpage.py`**: The Python script for deploying the model via Streamlit.
- **`requirements.txt`**: Contains all the Python dependencies required to run the project.
- **`README.md`**: This readme file.

---

## Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/nfl-game-predictor.git
   cd nfl-game-predictor
   ```

2. **Install Dependencies**:
   Use the `requirements.txt` file to install all necessary libraries:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit App**:
   Start the Streamlit front end to visualize predictions:
   ```bash
   streamlit run model_webpage.py
   ```

4. **Data and Model Files**:
   Ensure all dataset files and model files (`random_forest_model.joblib` and `scaler.pkl`) are in the correct directory.

---

## Features

- **Game Prediction**:
  Predict the winner of a matchup with a confidence score. Includes home-field advantage as a feature.
  
- **Data Visualization**:
  Includes exploratory data analysis (EDA) visualizations, such as feature distributions, correlation matrices, and boxplots.

- **Streamlit Integration**:
  A user-friendly interface for entering team matchups and viewing predictions.

---

## How It Works

1. **Data Preprocessing**:
   - Team-specific data is preprocessed, with features like `TotalYards`, `PassYards`, `RushYards`, and `Turnovers` used for training.
   - Home-field advantage is included as a binary feature.

2. **Model Training**:
   - A Random Forest Classifier is trained using these features, and hyperparameters are optimized for better accuracy.

3. **Prediction**:
   - Users input two teams and specify the home team.
   - The model predicts the winner and provides a confidence score for the prediction.

---

## Example

To illustrate the model’s performance, we predicted the matchup between the **Lions** and **Commanders**. The model correctly predicted the Lions to win with a confidence score of **69%**, aligning with the Lions’ strong performance this season and the Commanders’ recent struggles.

---

## Future Work

- Incorporating player-level data and recent performance metrics.
- Expanding model features to include weather conditions, injuries, and advanced analytics.
- Enhancing the user interface for a more interactive experience.

---

## Authors

- Akhil Sharma
- Bhavesha Sasikumar
- Jackson Cmelak
- Denil Neil 
