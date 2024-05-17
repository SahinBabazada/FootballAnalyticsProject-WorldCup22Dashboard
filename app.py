# %% imports

import warnings
warnings.filterwarnings("ignore")

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from functions import new_line, id_match_dict, plot_percentage_bar, shot_map, pass_map, xg_plot, xg_per_min, threat_timeline

# %% data loading
df_statistics = pd.read_csv('datasets/match_statistics.csv')
df_match = pd.read_csv('datasets/df_match.csv')
df_shot = pd.read_csv('datasets/df_shot.csv')
df_result = pd.read_csv('datasets/df_results.csv')
df_info = pd.read_csv('datasets/df_info.csv')
df_goal = pd.read_csv('datasets/df_goal.csv')
df_penalty = pd.read_csv('datasets/df_penalty.csv')
df_pass = pd.read_csv('datasets/df_pass.csv')

# %% header set
st.set_page_config(layout = "wide", page_icon = 'logo.jpg', page_title='FIFA World Cup 2022')

st.markdown("<h1 style='text-align: center;'>Welcome to the World Cup 2022 Summary Application by Anar Abiyev!</h1>", unsafe_allow_html=True)
st.markdown("##### Click a match from group stage or playoffs and scroll down for comprehensive game summary and analysis!")


# %% group games
new_line(3)
st.markdown("<h1 style='text-align: center;'>Group Stage</h1>", unsafe_allow_html=True)
new_line(1)

id = None
st.image('grp3.png', use_column_width=True)

col1, col2, col3, col4 = st.columns(4)

st.markdown(
    """
<style>
button {
    height: 50px;
    weight: 1000px;
    padding-top: 10px !important;
    padding-bottom: 10px !important;
}
</style>
""",
    unsafe_allow_html=True,
)
with col1:
    col12, col11, col13 = col1.columns([0.4, 4, 1])
    col11.write('<div style="text-align: center;"><h4>Group A</h4></div>', unsafe_allow_html=True)
    if col11.button("Netherlands vs Qatar", use_container_width=True):
        id = 3857294
    if col11.button("Qatar vs Ecuador", use_container_width=True):
        id = 3857286
    if col11.button("Qatar vs Senegal", use_container_width=True):
        id = 3857301
    if col11.button("Ecuador vs Senegal", use_container_width=True):
        id = 3857267
    if col11.button('Netherlands vs Ecuador', use_container_width=True):
        id = 3857274
    if col11.button('Senegal vs Netherlands', use_container_width=True):
        id = 3857285

with col2:
    col12, col11, col13 = col2.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Group B</h4></div>', unsafe_allow_html=True)
    if col11.button("England vs United States", use_container_width=True):
        id = 3857272
    if col11.button("England vs Iran", use_container_width=True):
        id = 3857271
    if col11.button("Wales vs England", use_container_width=True):
        id = 3857261
    if col11.button("Iran vs United States", use_container_width=True):
        id = 3857278
    if col11.button("Wales vs Iran", use_container_width=True):
        id = 3857273
    if col11.button("United States vs Wales", use_container_width=True):
        id = 3857282

with col3:
    col12, col11, col13 = col3.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Group C</h4></div>', unsafe_allow_html=True)
    if col11.button("Poland vs Argentina", use_container_width=True):
        id = 3857264
    if col11.button("Argentina vs Mexico", use_container_width=True):
        id = 3857289
    if col11.button("Argentina vs Saudi Arabia", use_container_width=True):
        id = 3857300
    if col11.button("Saudi Arabia vs Mexico", use_container_width=True):
        id = 3857260
    if col11.button("Poland vs Saudi Arabia", use_container_width=True):
        id = 3857297
    if col11.button("Mexico vs Poland", use_container_width=True):
        id = 3857265

with col4:
    col12, col11, col13 = col4.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Group D</h4></div>', unsafe_allow_html=True)
    if col11.button("France vs Denmark", use_container_width=True):
        id = 3857266
    if col11.button("France vs Australia", use_container_width=True):
        id = 3857279
    if col11.button("Tunisia vs France", use_container_width=True):
        id = 3857275
    if col11.button("Australia vs Denmark", use_container_width=True):
        id = 3857257
    if col11.button("Denmark vs Tunisia", use_container_width=True):
        id = 3857254
    if col11.button("Tunisia vs Australia", use_container_width=True):
        id = 3857288

col5, col6, col7, col8 = st.columns(4)

with col5:
    col12, col11, col13 = col5.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Group E</h4></div>', unsafe_allow_html=True)
    if col11.button("Spain vs Germany", use_container_width=True):
        id = 3857263
    if col11.button("Spain vs Costa Rica", use_container_width=True):
        id = 3857291
    if col11.button("Japan vs Spain", use_container_width=True):
        id = 3857255
    if col11.button("Japan vs Costa Rica", use_container_width=True):
        id = 3857295
    if col11.button("Germany vs Japan", use_container_width=True):
        id = 3857284
    if col11.button("Costa Rica vs Germany", use_container_width=True):
        id = 3857292

with col6:
    col12, col11, col13 = col6.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Group F</h4></div>', unsafe_allow_html=True)
    if col11.button("Belgium vs Morocco", use_container_width=True):
        id = 3857283
    if col11.button("Croatia vs Belgium", use_container_width=True):
        id = 3857296
    if col11.button("Belgium vs Canada", use_container_width=True):
        id = 3857268
    if col11.button("Croatia vs Canada", use_container_width=True):
        id = 3857281
    if col11.button("Canada vs Morocco", use_container_width=True):
        id = 3857276
    if col11.button("Morocco vs Croatia", use_container_width=True):
        id = 3857277

with col7:
    col12, col11, col13 = col7.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Group G</h4></div>', unsafe_allow_html=True)
    if col11.button("Brazil vs Serbia", use_container_width=True):
        id = 3857258
    if col11.button("Brazil vs Switzerland", use_container_width=True):
        id = 3857269
    if col11.button("Cameroon vs Brazil", use_container_width=True):
        id = 3857280
    if col11.button("Serbia vs Switzerland", use_container_width=True):
        id = 3857256
    if col11.button("Cameroon vs Serbia", use_container_width=True):
        id = 3857259
    if col11.button("Switzerland vs Cameroon", use_container_width=True):
        id = 3857290

with col8:
    col12, col11, col13 = col8.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Group H</h4></div>', unsafe_allow_html=True)
    if col11.button("Portugal vs Uruguay", use_container_width=True):
        id = 3857270
    if col11.button("Portugal vs Ghana", use_container_width=True):
        id = 3857298
    if col11.button("South Korea vs Portugal", use_container_width=True):
        id = 3857262
    if col11.button("South Korea vs Ghana", use_container_width=True):
        id = 3857299
    if col11.button("Ghana vs Uruguay", use_container_width=True):
        id = 3857293
    if col11.button("Uruguay vs South Korea", use_container_width=True):
        id = 3857287



# %% playoff games
st.markdown('---')
new_line(1)
#st.header("--------------------------------------------------Playoffs--------------------------------------------------")
st.markdown("<h1 style='text-align: center;'>Playoffs</h1>", unsafe_allow_html=True)
new_line(2)


col1, col2, col3, col4= st.columns(4)

with col1:
    col12, col11, col13 = col1.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Round of 16</h4></div>', unsafe_allow_html=True)
    new_line(2, col11)
    if col11.button('**Netherland** vs USA', use_container_width=True):
        id = 3869117
    if col11.button('**Argentina** vs Australia', use_container_width=True):
        id = 3869151
    new_line(2, col11)
    if col11.button('Japan vs **Croatia**', use_container_width=True):
        id = 3869219
    if col11.button('**Brasil** vs South Korea', use_container_width=True):
        id = 3869253
    new_line(2, col11)
    if col11.button('**England** vs Senegal', use_container_width=True):
        id = 3869118
    if col11.button('**France** vs Poland', use_container_width=True):
        id = 3869152
    new_line(2, col11)
    if col11.button('**Morocco** vs Spain', use_container_width=True):
        id = 3869220
    if col11.button('**Portugal** vs Switzerland', use_container_width=True):
        id = 3869254

with col2:
    col12, col11, col13 = col2.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Quarter Finals</h4></div>', unsafe_allow_html=True)
    new_line(4, col11)
    if col11.button('Netherland vs **Argentina**', use_container_width=True):
        id = 3869321
    new_line(6, col11)
    if col11.button('**Croatia** vs Brasil', use_container_width=True):
        id = 3869420
    new_line(6, col11)
    if col11.button('England vs **France**', use_container_width=True):
        id = 3869354
    new_line(6, col11)
    if col11.button('**Morocco** vs Portugal', use_container_width=True):
        id = 3869486

with col3:
    col12, col11, col13 = col3.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Semi Finals</h4></div>', unsafe_allow_html=True)
    new_line(9, col11)
    if col11.button('**Argentina** vs Croatia', use_container_width=True):
        id = 3869519
    new_line(16, col11)
    if col11.button('**France** vs Morocco', use_container_width=True):
        id = 3869552

with col4:
    col12, col11, col13 = col4.columns([0.4, 4, 1])

    col11.write('<div style="text-align: center;"><h4>Final / 3rd Place</h4></div>', unsafe_allow_html=True)
    new_line(15, col11)
    if col11.button('**Argentina** vs France', use_container_width=True):
        id = 3869685

    if col11.button('**Croatia** vs Morocco', use_container_width=True):
        id = 3869684

 
if id:

    st.markdown("---")
    new_line(2)
    st.markdown("<h1 style='text-align: center;'>Match Analysis:</h1>", unsafe_allow_html=True)
    new_line(2)


    # %% score board

    xt_flag = df_result[df_result['match_id'] == id]['et_flag'].iloc[0]
    ps_flag = df_result[df_result['match_id'] == id]['ps_flag'].iloc[0]

    home_team = df_result[df_result['match_id'] == id]['home_team_name'].iloc[0]
    away_team = df_result[df_result['match_id'] == id]['away_team_name'].iloc[0]
    home_team_ft = df_result[df_result['match_id'] == id]['home_FT_score'].iloc[0]
    away_team_ft = df_result[df_result['match_id'] == id]['away_FT_score'].iloc[0]
        
    if xt_flag:

        home_team_xt = df_result[df_result['match_id'] == id]['home_ET_score'].iloc[0]
        away_team_xt = df_result[df_result['match_id'] == id]['away_ET_score'].iloc[0]

        html_string = "<h2 style='text-align: center;'>FT: {} - {}</h2>".format(home_team_ft,
                                                                                away_team_ft)
        st.markdown(html_string, unsafe_allow_html=True)
        
        html_string = "<h1 style='text-align: center;'>AET: {} {} - {} {}</h1>".format(home_team,home_team_xt,
                                                                                       away_team_xt, away_team)
        st.markdown(html_string, unsafe_allow_html=True)
    else:
        html_string = "<h1 style='text-align: center;'>FT: {} {} - {} {}</h1>".format(home_team, home_team_ft,
                                                                                      away_team_ft, away_team)
        st.markdown(html_string, unsafe_allow_html=True)

    # goals
    df_goal_match = df_goal[df_goal['match_id'] == id]

    if df_goal_match.shape[0] == 0:
        pass
    else:
        col1, col2 = st.columns(2)
        for index, goal in df_goal_match.iterrows():
            if goal['team_name'] == home_team:
                if goal['autogoal'] == False:
                    col1.markdown("<div style='text-align: right; font-size: 16pt; line-height: 1;'>{} {}' </div>".format(goal['player_name'], goal['minute_print']), unsafe_allow_html=True)
                    col2.write('')
                    col2.write('')
                else:
                    col1.markdown("<div style='text-align: right; font-size: 16pt; line-height: 1;'>{} {} (OG)'</div>".format(goal['player_name'], goal['minute_print']), unsafe_allow_html=True)
                    col2.write('')
                    col2.write('')
            else:
                if goal['autogoal'] == False:
                    col2.markdown("<div style='text-align: left; font-size: 16pt; line-height: 1;'> {}' {}</div>".format(goal['minute_print'], goal['player_name']), unsafe_allow_html=True)
                    col1.write('')
                    col1.write('')
                else:
                    col2.markdown("<div style='text-align: left; font-size: 16pt; line-height: 1;'> (OG){}' {}</div>".format(goal['minute_print'], goal['player_name']), unsafe_allow_html=True)
                    col1.write('')
                    col1.write('')

    

    if ps_flag:
        home_team_ps = df_result[df_result['match_id'] == id]['home_PenSh_score'].iloc[0]
        away_team_ps = df_result[df_result['match_id'] == id]['away_PenSh_score'].iloc[0]     
        html_string = "<h2 style='text-align: center;'>PS: {} - {}</h2>".format(home_team_ps,
                                                                                away_team_ps)
        st.markdown(html_string, unsafe_allow_html=True)

        df_penalty_match = df_penalty[df_penalty['match_id'] == id]
        col1, col2 = st.columns(2)
        for index, goal in df_penalty_match.iterrows():
            if goal['team_name'] == home_team:
                if goal['outcome_name'] == 'ps_goal':
                    col1.markdown("<div style='text-align: right; font-size: 16pt; line-height: 1;'>{} 🟢 </div>".format(goal['player_name']), unsafe_allow_html=True)
                    col1.write('')
                else:
                    col1.markdown("<div style='text-align: right; font-size: 16pt; line-height: 1;'>{} 🔴 </div>".format(goal['player_name']), unsafe_allow_html=True)
                    col1.write('')
           
            else:
                if goal['outcome_name'] == 'ps_goal':
                    col2.markdown("<div style='text-align: left; font-size: 16pt; line-height: 1;'>🟢 {} </div>".format(goal['player_name']), unsafe_allow_html=True)
                    col2.write('')

                else:
                    col2.markdown("<div style='text-align: left; font-size: 16pt; line-height: 1;'>🔴 {} </div>".format(goal['player_name']), unsafe_allow_html=True)
                    col2.write('')


    new_line(1)
    st.markdown('---')
    new_line(1)

    # %% match info
    
    row = df_info[df_info['match_id'] == id]

    
    st.markdown("<h3 style='text-align: center;'>Match Info</h3>", unsafe_allow_html=True)
    st.write('')
    
    col1, col2 = st.columns(2)

    col1.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Date:</div>", unsafe_allow_html=True)
    col2.markdown("<div style='text-align: left; font-size: 18pt; line-height: 1;'>{}</div>".format(row['match_date'].iloc[0]), unsafe_allow_html=True)
    col1.write('')
    col2.write('')
    

    col1.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Competition Stage:</div>", unsafe_allow_html=True)
    col2.markdown("<div style='text-align: left; font-size: 18pt; line-height: 1;'>{}</div>".format(row['competition_stage_name'].iloc[0]), unsafe_allow_html=True)
    col1.write('')
    col2.write('')

    col1.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Stadium:</div>", unsafe_allow_html=True)
    col2.markdown("<div style='text-align: left; font-size: 18pt; line-height: 1;'>{}</div>".format(row['stadium_name'].iloc[0]), unsafe_allow_html=True)
    col1.write('')
    col2.write('')
    
    col1.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Attendance:</div>", unsafe_allow_html=True)
    col2.markdown("<div style='text-align: left; font-size: 18pt; line-height: 1;'>{}</div>".format(row['attendance'].iloc[0]), unsafe_allow_html=True)
    col1.write('')
    col2.write('')    

    col1.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Referee:</div>", unsafe_allow_html=True)
    col2.markdown("<div style='text-align: left; font-size: 18pt; line-height: 1;'>{}</div>".format(row['referee_name'].iloc[0]), unsafe_allow_html=True)
    col1.write('')
    col2.write('')
    
    col1.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Referee Country:</div>", unsafe_allow_html=True)
    col2.markdown("<div style='text-align: left; font-size: 18pt; line-height: 1;'>{}</div>".format(row['referee_country_name'].iloc[0]), unsafe_allow_html=True)
    

    new_line(1)
    st.markdown('---')
    new_line(1)

    # %% statistics
    st.markdown("<h3 style='text-align: center;'>Statistics: {} - {}</h3>".format(home_team, away_team), unsafe_allow_html=True)
    st.write('')

    row_stats = df_statistics[df_statistics['match_id'] == id]

    col1, col2 = st.columns(2)

    col11, col12 = col1.columns(2)
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Possession:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(row_stats['home_possession'].iloc[0], row_stats['away_possession'].iloc[0]))

    col11.write("")
    col11.write("")
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Attempted Passes:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(row_stats['home_attempted_pases'].iloc[0], row_stats['away_attempted_pases'].iloc[0]))


    col11.write("")
    col11.write("")
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Pass Completion Percentage:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(round(row_stats['home_completed_passes'].iloc[0] / row_stats['home_attempted_pases'].iloc[0], 2) * 100, 
                                     round(row_stats['away_completed_passes'].iloc[0] / row_stats['away_attempted_pases'].iloc[0], 2) * 100))

    col11.write("")
    col11.write("")
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Total Shots:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(df_shot[(df_shot['match_id'] == id) & (df_shot['team_name'] == home_team) & (df_shot['ps'] == False)].shape[0],
                                     df_shot[(df_shot['match_id'] == id) & (df_shot['team_name'] == away_team) & (df_shot['ps'] == False)].shape[0]))


    col11.write("")
    col11.write("")
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Shots on Target:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(row_stats['home_sot'].iloc[0], row_stats['away_sot'].iloc[0]))


    col11.write("")
    col11.write("")
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Saves:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(row_stats['home_saves'].iloc[0], row_stats['away_saves'].iloc[0]))

    col11, col12 = col2.columns(2)

    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Fouls:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(row_stats['home_fouls'].iloc[0], row_stats['away_fouls'].iloc[0]))

    col11.write("")
    col11.write("")
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Corners:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(row_stats['home_corners'].iloc[0], row_stats['away_corners'].iloc[0]))


    col11.write("")
    col11.write("")
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Offsides:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(row_stats['home_offsides'].iloc[0], row_stats['away_offsides'].iloc[0]))

    col11.write("")
    col11.write("")
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Tackles:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(row_stats['home_tackles'].iloc[0], row_stats['away_tackles'].iloc[0]))

    col11.write("")
    col11.write("")
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Duals Won:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(row_stats['home_aerials_won'].iloc[0], row_stats['away_aerials_won'].iloc[0]))

    col11.write("")
    col11.write("")
    col11.write("")
    col11.markdown("<div style='text-align: right; font-size: 18pt; line-height: 1;'>Long Balls:</div>", unsafe_allow_html=True)
    col12.pyplot(plot_percentage_bar(row_stats['home_long_balls'].iloc[0], row_stats['away_long_balls'].iloc[0]))


    # %% shot maps
    
    st.markdown('---')
    st.markdown("<h2 style='text-align: center;'>Shot Maps</h2>", unsafe_allow_html=True)
    col1, col2 = st.columns(2)
    col1.pyplot(shot_map(id, df_shot, df_result, 1))
    col2.pyplot(shot_map(id, df_shot, df_result, 2))

    # %% xg plots
    st.markdown('---')
    st.markdown("<h2 style='text-align: center;'>xG Plots</h2>", unsafe_allow_html=True)
    st.write('')
    col1, col2 = st.columns(2)
    col1.pyplot(xg_plot(id, df_shot, df_result, 1))
    col2.pyplot(xg_plot(id, df_shot, df_result, 2))

    # %% xg threat timeline
    st.markdown('---')
    st.markdown("<h2 style='text-align: center;'>xG Threat Timeline</h2>", unsafe_allow_html=True)
    st.write('')
    a = xg_per_min(id, df_shot, df_result)
    st.pyplot(threat_timeline(a[0], a[1], a[2], a[3]))

    # %% pass maps
    st.markdown('---')
    st.markdown("<h2 style='text-align: center;'>Top 9 Players with the most passes</h2>", unsafe_allow_html=True)
    st.write('')
    col1, col2 = st.columns(2)
    col1.pyplot(pass_map(id, df_pass, df_result, 1))
    col2.pyplot(pass_map(id, df_pass, df_result, 2))
    

        
