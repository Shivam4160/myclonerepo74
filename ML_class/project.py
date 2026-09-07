import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestRegressor

def predict_bgmi_score():
    print("Which tournament's data do you want to predict?")
    print("1. BGMS Final")
    print("2. PMWC Final")
    tourney_choice = int(input("Enter choice (1 or 2): "))
    
    if tourney_choice == 1:
        df = pd.read_csv("BGMS_FINAL.csv")
    elif tourney_choice == 2:
        df = pd.read_csv("PMWC_FINAL.csv")
    else:
        print("Invalid choice.")
        return

    team_encoder = LabelEncoder()
    map_encoder = LabelEncoder()
    
    df['Team_Encoded'] = team_encoder.fit_transform(df['Team'])
    df['Map_Encoded'] = map_encoder.fit_transform(df['Map'])
    
    X = df[['Team_Encoded', 'Map_Encoded']]
    y = df[['Elims', 'Placement', 'Placement Points', 'Total Points']]
    
    model = RandomForestRegressor(random_state=1)
    model.fit(X, y)
    
    print("\nAvailable Teams:")
    teams = team_encoder.classes_
    for i in range(len(teams)):
        print(str(i + 1) + ". " + teams[i])
    team_choice = int(input("Select Team (number): ")) - 1
    
    print("\nAvailable Maps:")
    maps = map_encoder.classes_
    for i in range(len(maps)):
        print(str(i + 1) + ". " + maps[i])
    map_choice = int(input("Select Map (number): ")) - 1
    
    input_data = pd.DataFrame({'Team_Encoded': [team_choice], 'Map_Encoded': [map_choice]})
    
    prediction = model.predict(input_data)[0]

    print("\n=== NEXT MATCH PREDICTION ===")
    print("Team:", teams[team_choice])
    print("Map:", maps[map_choice])
    print("Team Kills:", round(prediction[0]))
    print("Team Placement:", round(prediction[1]))
    print("Placement Points:", round(prediction[2]))
    print("Total Score:", round(prediction[3]))


predict_bgmi_score()