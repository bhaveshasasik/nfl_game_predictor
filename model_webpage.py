import streamlit as st
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, classification_report
from sklearn.model_selection import train_test_split


def preprocess_all_files(file_paths):
    all_data = []
    for file_path in file_paths:
        data = pd.read_csv(file_path)
        data = data[data['Unnamed: 0'] != 'Week']
        data.rename(columns={
            'Score': 'Team_Points',
            'Score.1': 'Opponent_Points',
            'Offense': 'Team_TotalYards',
            'Offense.1': 'Team_PassYards',
            'Offense.2': 'Team_RushYards',
            'Offense.3': 'Team_Turnovers',
            'Defense': 'Opponent_TotalYards',
            'Defense.1': 'Opponent_PassYards',
            'Defense.2': 'Opponent_RushYards',
            'Defense.3': 'Opponent_Turnovers'
        }, inplace=True)
        numeric_cols = [
            'Team_Points', 'Opponent_Points', 'Team_TotalYards', 'Team_PassYards',
            'Team_RushYards', 'Team_Turnovers', 'Opponent_TotalYards',
            'Opponent_PassYards', 'Opponent_RushYards', 'Opponent_Turnovers'
        ]
        for col in numeric_cols:
            data[col] = pd.to_numeric(data[col], errors='coerce')
        data = data.dropna(subset=numeric_cols)
        data['Team'] = file_path.split('/')[-1].split('_')[0]
        data['Home_Field'] = (data['Unnamed: 0'] == 'Home').astype(int)  # Add home-field advantage as binary
        all_data.append(data)
    combined_data = pd.concat(all_data, ignore_index=True)
    return combined_data

def train_and_evaluate_model(combined_data):
    features = ['Team_TotalYards', 'Team_PassYards', 'Team_RushYards', 'Team_Turnovers',
                'Opponent_TotalYards', 'Opponent_PassYards', 'Opponent_RushYards', 'Opponent_Turnovers', 'Home_Field']
    combined_data['Outcome'] = (combined_data['Team_Points'] > combined_data['Opponent_Points']).astype(int)
    X = combined_data[features]
    y = combined_data['Outcome']

    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, stratify=y)

    # Normalize features
    scaler = StandardScaler()
    X_train = scaler.fit_transform(X_train)
    X_test = scaler.transform(X_test)

    # Train model
    model = RandomForestClassifier(random_state=42)
    model.fit(X_train, y_train)


    return model, combined_data, scaler

def predict_matchup(model, combined_data, scaler, team_a, team_b, home_team):
    team_a_stats = combined_data[combined_data['Team'] == team_a].iloc[0][
        ['Team_TotalYards', 'Team_PassYards', 'Team_RushYards', 'Team_Turnovers']
    ].tolist()
    team_b_stats = combined_data[combined_data['Team'] == team_b].iloc[0][
        ['Team_TotalYards', 'Team_PassYards', 'Team_RushYards', 'Team_Turnovers']
    ].tolist()
    home_field = 1 if home_team == team_a else 0

    matchup_stats = pd.DataFrame([team_a_stats + team_b_stats + [home_field]], columns=[
        'Team_TotalYards', 'Team_PassYards', 'Team_RushYards', 'Team_Turnovers',
        'Opponent_TotalYards', 'Opponent_PassYards', 'Opponent_RushYards', 'Opponent_Turnovers', 'Home_Field'
    ])
    matchup_stats = scaler.transform(matchup_stats)
    prediction = model.predict(matchup_stats)
    probability = model.predict_proba(matchup_stats)[0][1]
    outcome = team_a if prediction[0] == 1 else team_b
    return outcome, probability

file_paths = [
    'bears_data.csv',
    'bengals_data.csv',
    'bills_data.csv',
    'broncos_data.csv',
    'browns_data.csv',
    'buccaneers_data.csv',
    'cardinals_data.csv',
    'chargers_data.csv',
    'chiefs_data.csv',
    'colts_data.csv',
    'commanders_data.csv',
    'cowboys_data.csv',
    'dolphins_data.csv',
    'eagles_data.csv',
    'falcons_data.csv',
    'giants_data.csv',
    'jaguars_data.csv',
    'jets_data.csv',
    'lions_data.csv',
    'packers_data.csv',
    'panthers_data.csv',
    'patriots_data.csv',
    'raiders_data.csv',
    'rams_data.csv',
    'ravens_data.csv',
    'saints_data.csv',
    'seahawks_data.csv',
    'steelers_data.csv',
    'texans_data.csv',
    'titans_data.csv',
    'vikings_data.csv',
    '49ers_data.csv'
]

# Preprocess all files and train model
combined_data = preprocess_all_files(file_paths)
model, combined_data, scaler = train_and_evaluate_model(combined_data)


st.write("""
         # NFL Victor Predictor
         """)

team_list = ['Select Team',
    'Bears',
    'Bengals',
    'Bills',
    'Broncos',
    'Browns',
    'Buccaneers',
    'Cardinals',
    'Chargers',
    'Chiefs',
    'Colts',
    'Commanders',
    'Cowboys',
    'Dolphins',
    'Eagles',
    'Falcons',
    'Giants',
    'Jaguars',
    'Jets',
    'Lions',
    'Packers',
    'Panthers',
    'Patriots',
    'Raiders',
    'Rams',
    'Ravens',
    'Saints',
    'Seahawks',
    'Steelers',
    'Texans',
    'Titans',
    'Vikings',
    '49ers']

home_team = st.selectbox("Home Team", team_list)
away_team = st.selectbox("Away Team", team_list)

if st.button("Predict", type="primary"):
    
    if (home_team == 'Select Team') or (away_team == 'Select Team'):
        st.text("Please select two different teams to compete")
    elif home_team == away_team:
        st.text("A team can't play against itself")
    else:
        output,confidence = predict_matchup(model, combined_data, scaler, home_team.lower(), away_team.lower(), home_team.lower())
        st.success("Predicted Winner: "+str(output))
        st.success("Confidence: "+str(confidence))
    

