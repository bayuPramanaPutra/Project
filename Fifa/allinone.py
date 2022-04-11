import streamlit as st
import pickle
import pandas as pd

with open('final_pipe.pkl', 'rb') as model_best:
    model = pickle.load(model_best)

cols = ['overall', 'potential', 'wage_eur', 'age', 'height_cm', 'weight_kg',
       'league_level', 'club_contract_valid_until', 'weak_foot', 'skill_moves',
       'international_reputation', 'release_clause_eur', 'pace', 'shooting',
       'passing', 'dribbling', 'defending', 'physic', 'attacking_crossing',
       'attacking_finishing', 'attacking_heading_accuracy',
       'attacking_short_passing', 'attacking_volleys', 'skill_dribbling',
       'skill_curve', 'skill_fk_accuracy', 'skill_long_passing',
       'skill_ball_control', 'movement_acceleration', 'movement_sprint_speed',
       'movement_agility', 'movement_reactions', 'movement_balance',
       'power_shot_power', 'power_jumping', 'power_stamina', 'power_strength',
       'power_long_shots', 'mentality_aggression', 'mentality_interceptions',
       'mentality_positioning', 'mentality_vision', 'mentality_penalties',
       'mentality_composure', 'defending_marking_awareness',
       'defending_standing_tackle', 'defending_sliding_tackle',
       'goalkeeping_diving', 'goalkeeping_handling', 'goalkeeping_kicking',
       'goalkeeping_positioning', 'goalkeeping_reflexes', 'position_sum',
       'tags_sum', 'traits_sum', 'league_name', 'club_position',
       'nation_position', 'preferred_foot', 'work_rate', 'body_type']

st.title('Football Player Market Value Predictor')

overall = st.number_input('overall', min_value=1, max_value=99)
potential = st.number_input('potential', min_value=1, max_value=99)
wage_eur = st.number_input('wage_eur', min_value=0, max_value=500000)
age = st.number_input('age', min_value=15, max_value=45)
height_cm = st.number_input('height_cm', min_value=150, max_value=210)
weight_kg = st.number_input('weight_kg', min_value=40, max_value=100)
league_level = st.number_input('league_level', min_value=1, max_value=6)
club_contract_valid_until = st.number_input('club_contract_valid_until', min_value=2020, max_value=2031)
weak_foot = st.number_input('weak_foot', min_value=1, max_value=5)
skill_moves = st.number_input('skill_moves', min_value=1, max_value=5)
international_reputation = st.number_input('international_reputation', min_value=1, max_value=5)
release_clause_eur = st.number_input('release_clause_eur', min_value=0, max_value=500000000)
pace = st.number_input('pace', min_value=1, max_value=99)
shooting = st.number_input('shooting', min_value=1, max_value=99)
passing = st.number_input('passing', min_value=1, max_value=99)
dribbling = st.number_input('dribbling', min_value=1, max_value=99)
defending = st.number_input('defending', min_value=1, max_value=99)
physic = st.number_input('physic', min_value=1, max_value=99)
attacking_crossing = st.number_input('attacking_crossing', min_value=1, max_value=99)
attacking_finishing = st.number_input('attacking_finishing', min_value=1, max_value=99)
attacking_heading_accuracy = st.number_input('attacking_heading_accuracy', min_value=1, max_value=99)
attacking_short_passing = st.number_input('attacking_short_passing', min_value=1, max_value=99)
attacking_volleys = st.number_input('attacking_volleys', min_value=1, max_value=99)
skill_dribbling = st.number_input('skill_dribbling', min_value=1, max_value=99)
skill_curve = st.number_input('skill_curve', min_value=1, max_value=99)
skill_fk_accuracy = st.number_input('skill_fk_accuracy', min_value=1, max_value=99)
skill_long_passing = st.number_input('skill_long_passing', min_value=1, max_value=99)
skill_ball_control = st.number_input('skill_ball_control', min_value=1, max_value=99)
movement_acceleration = st.number_input('movement_acceleration', min_value=1, max_value=99)
movement_sprint_speed = st.number_input('movement_sprint_speed', min_value=1, max_value=99)
movement_agility = st.number_input('movement_agility', min_value=1, max_value=99)
movement_reactions = st.number_input('movement_reactions', min_value=1, max_value=99)
movement_balance = st.number_input('movement_balance', min_value=1, max_value=99)
power_shot_power = st.number_input('power_shot_power', min_value=1, max_value=99)
power_jumping = st.number_input('power_jumping', min_value=1, max_value=99)
power_stamina = st.number_input('power_stamina', min_value=1, max_value=99)
power_strength = st.number_input('power_strength', min_value=1, max_value=99)
power_long_shots = st.number_input('power_long_shots', min_value=1, max_value=99)
mentality_aggression = st.number_input('mentality_aggression', min_value=1, max_value=99)
mentality_interceptions = st.number_input('mentality_interceptions', min_value=1, max_value=99)
mentality_positioning = st.number_input('mentality_positioning', min_value=1, max_value=99)
mentality_vision = st.number_input('mentality_vision', min_value=1, max_value=99)
mentality_penalties = st.number_input('mentality_penalties', min_value=1, max_value=99)
mentality_composure = st.number_input('mentality_composure', min_value=1, max_value=99)
defending_marking_awareness = st.number_input('defending_marking_awareness', min_value=1, max_value=99)
defending_standing_tackle = st.number_input('defending_standing_tackle', min_value=1, max_value=99)
defending_sliding_tackle = st.number_input('defending_sliding_tackle', min_value=1, max_value=99)
goalkeeping_diving = st.number_input('goalkeeping_diving', min_value=1, max_value=99)
goalkeeping_handling = st.number_input('goalkeeping_handling', min_value=1, max_value=99)
goalkeeping_kicking = st.number_input('goalkeeping_kicking', min_value=1, max_value=99)
goalkeeping_positioning = st.number_input('goalkeeping_positioning', min_value=1, max_value=99)
goalkeeping_reflexes = st.number_input('goalkeeping_reflexes', min_value=1, max_value=99)
position_sum = st.number_input('position_sum', min_value=1, max_value=5)
tags_sum = st.number_input('tags_sum', min_value=1, max_value=5)
traits_sum = st.number_input('traits_sum', min_value=1, max_value=5)

league_name = st.selectbox('league_name',
                            ('USA Major League Soccer',
                            'Argentina Primera División',
                            'English League Championship',
                            'English Premier League',
                            'Spain Primera Division',
                            'English League One',
                            'Spanish Segunda División',
                            'English League Two',
                            'Italian Serie A',
                            'French Ligue 1',
                            'Japanese J. League Division 1',
                            'German 3. Bundesliga',
                            'German 1. Bundesliga',
                            'French Ligue 2',
                            'Turkish Süper Lig',
                            'Portuguese Liga ZON SAGRES',
                            'Belgian Jupiler Pro League',
                            'German 2. Bundesliga',
                            'Mexican Liga MX',
                            'Holland Eredivisie',
                            'Polish T-Mobile Ekstraklasa',
                            'Saudi Abdul L. Jameel League',
                            'Chinese Super League',
                            'Romanian Liga I',
                            'Swedish Allsvenskan',
                            'Norwegian Eliteserien',
                            'Campeonato Brasileiro Série A',
                            'Korean K League 1',
                            'Danish Superliga',
                            'Austrian Football Bundesliga',
                            'Scottish Premiership',
                            'Indian Super League',
                            'Australian Hyundai A-League',
                            'Swiss Super League',
                            'Rep. Ireland Airtricity League',
                            'Liga de Fútbol Profesional Boliviano',
                            'Colombian Liga Postobón',
                            'Paraguayan Primera División',
                            'Ecuadorian Serie A',
                            'Chilian Campeonato Nacional',
                            'Venezuelan Primera División',
                            'Peruvian Primera División',
                            'Uruguayan Primera División',
                            'Greek Super League',
                            'Italian Serie B',
                            'Russian Premier League',
                            'Czech Republic Gambrinus Liga',
                            'None',
                            'South African Premier Division',
                            'Ukrainian Premier League',
                            'Croatian Prva HNL',
                            'Hungarian Nemzeti Bajnokság I',
                            'Finnish Veikkausliiga',
                            'Cypriot First Division',
                            'UAE Arabian Gulf League',
                            'English National League'
                            ))

club_position = st.selectbox('club_position',
                            ('SUB',
                            'RES',
                            'RCB',
                            'LCB',
                            'RB',
                            'LB',
                            'ST',
                            'LCM',
                            'RCM',
                            'RM',
                            'LM',
                            'CAM',
                            'LDM',
                            'RS',
                            'LS',
                            'RDM',
                            'RW',
                            'LW',
                            'CB',
                            'CDM',
                            'RWB',
                            'LWB',
                            'CM',
                            'None',
                            'LF',
                            'RF',
                            'LAM',
                            'RAM',
                            'CF'
                            ))

nation_position = st.selectbox('nation_position',
                                ('None', 'Start', 'SUB')
                                )

preferred_foot = st.selectbox('preferred_foot',
                                ('Right', 'Left')
                                )

work_rate = st.selectbox('work_rate',
                        ('Medium/Medium',
                        'High/Medium',
                        'Medium/High',
                        'High/High',
                        'High/Low',
                        'Medium/Low',
                        'Low/Medium',
                        'Low/High',
                        'Low/Low'
                        ))

body_type = st.selectbox('body_type',
                        ('Normal (170-185)',
                        'Lean (170-185)',
                        'Normal (185+)',
                        'Lean (185+)',
                        'Normal (170-)',
                        'Stocky (170-185)',
                        'Lean (170-)',
                        'Stocky (185+)',
                        'Unique',
                        'Stocky (170-)'
                        ))


# inference
new_data = [
        overall, potential, wage_eur, age, height_cm, weight_kg,
        league_level, club_contract_valid_until, weak_foot, skill_moves,
        international_reputation, release_clause_eur, pace, shooting,
        passing, dribbling, defending, physic, attacking_crossing,
        attacking_finishing, attacking_heading_accuracy,
        attacking_short_passing, attacking_volleys, skill_dribbling,
        skill_curve, skill_fk_accuracy, skill_long_passing,
        skill_ball_control, movement_acceleration, movement_sprint_speed,
        movement_agility, movement_reactions, movement_balance,
        power_shot_power, power_jumping, power_stamina, power_strength,
        power_long_shots, mentality_aggression, mentality_interceptions,
        mentality_positioning, mentality_vision, mentality_penalties,
        mentality_composure, defending_marking_awareness,
        defending_standing_tackle, defending_sliding_tackle,
        goalkeeping_diving, goalkeeping_handling, goalkeeping_kicking,
        goalkeeping_positioning, goalkeeping_reflexes, position_sum,
        tags_sum, traits_sum, league_name, club_position,
        nation_position, preferred_foot, work_rate, body_type
    ]

new_data = pd.DataFrame([new_data], columns=cols)

hasil = model.predict(new_data)

st.header(hasil[0])
st.header('Euro')