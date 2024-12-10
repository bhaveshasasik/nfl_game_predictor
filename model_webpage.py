import streamlit as st

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
        output = "This is a placeholder"
        st.success(output)
    


    

