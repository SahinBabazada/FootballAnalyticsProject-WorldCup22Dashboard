import matplotlib.pyplot as plt
import streamlit as st

import numpy as np
import pandas as pd
from matplotlib import colormaps
from matplotlib.colors import ListedColormap

from mplsoccer import (VerticalPitch, Pitch, create_transparent_cmap,
                       FontManager, arrowhead_marker, Sbopen)


def new_line(n=1, a = st):
    for _ in range(n):
        a.write("")


def id_match_dict(id):
    mapping = {3857256: 'Serbia vs Switzerland', 
               3869151: 'Argentina vs Australia', 
               3857257: 'Australia vs Denmark', 
               3857258: 'Brazil vs Serbia', 
               3857288: 'Tunisia vs Australia', 
               3857267: 'Ecuador vs Senegal', 
               3869321: 'Netherlands vs Argentina', 
               3857287: 'Uruguay vs South Korea', 
               3869486: 'Morocco vs Portugal', 
               3869685: 'Argentina vs France', 
               3857260: 'Saudi Arabia vs Mexico', 
               3857264: 'Poland vs Argentina', 
               3857266: 'France vs Denmark', 
               3857289: 'Argentina vs Mexico', 
               3857269: 'Brazil vs Switzerland', 
               3857294: 'Netherlands vs Qatar', 
               3869254: 'Portugal vs Switzerland', 
               3869118: 'England vs Senegal', 
               3869684: 'Croatia vs Morocco', 
               3869519: 'Argentina vs Croatia', 
               3869354: 'England vs France', 
               3869552: 'France vs Morocco', 
               3869420: 'Croatia vs Brazil', 
               3869220: 'Morocco vs Spain', 
               3869219: 'Japan vs Croatia', 
               3869253: 'Brazil vs South Korea', 
               3869152: 'France vs Poland', 
               3869117: 'Netherlands vs United States', 
               3857270: 'Portugal vs Uruguay', 
               3857263: 'Spain vs Germany', 
               3857259: 'Cameroon vs Serbia', 
               3857295: 'Japan vs Costa Rica', 
               3857283: 'Belgium vs Morocco', 
               3857284: 'Germany vs Japan', 
               3857282: 'United States vs Wales', 
               3857286: 'Qatar vs Ecuador', 
               3857301: 'Qatar vs Senegal', 
               3857300: 'Argentina vs Saudi Arabia', 
               3857299: 'South Korea vs Ghana', 
               3857298: 'Portugal vs Ghana', 
               3857297: 'Poland vs Saudi Arabia', 
               3857296: 'Croatia vs Belgium', 
               3857293: 'Ghana vs Uruguay', 
               3857292: 'Costa Rica vs Germany', 
               3857291: 'Spain vs Costa Rica', 
               3857290: 'Switzerland vs Cameroon', 
               3857285: 'Senegal vs Netherlands', 
               3857281: 'Croatia vs Canada', 
               3857280: 'Cameroon vs Brazil', 
               3857279: 'France vs Australia', 
               3857278: 'Iran vs United States', 
               3857277: 'Morocco vs Croatia', 
               3857276: 'Canada vs Morocco', 
               3857275: 'Tunisia vs France', 
               3857274: 'Netherlands vs Ecuador', 
               3857273: 'Wales vs Iran', 
               3857272: 'England vs United States', 
               3857271: 'England vs Iran', 
               3857268: 'Belgium vs Canada', 
               3857265: 'Mexico vs Poland', 
               3857262: 'South Korea vs Portugal', 
               3857261: 'Wales vs England', 
               3857255: 'Japan vs Spain', 
               3857254: 'Denmark vs Tunisia'}
    
    return mapping[id]

def plot_percentage_bar(value1, value2):

  if (value1 > 0) and (value2 > 0):
    total = value1 + value2
    percentage1 = (value1 / total) * 100
    percentage2 = (value2 / total) * 100

    fig, ax = plt.subplots(figsize=(3, 0.3))
    
    if percentage1 > percentage2:   
      ax.barh(0, percentage1, color='#2bc22d')
      ax.barh(0, percentage2, left=percentage1, color='#c2372b')
    elif percentage1 == percentage2:
      ax.barh(0, percentage1, color='#9497a1')
      ax.barh(0, percentage2, left=percentage1, color='#9497a1')
    else:
      ax.barh(0, percentage1, color='#c2372b')
      ax.barh(0, percentage2, left=percentage1, color='#2bc22d')

    ax.text(percentage1 / 2, 0, f'{value1}', ha='center', va='center', color='white')
    ax.text(percentage1 + percentage2 / 2, 0, f'{value2}', ha='center', va='center', color='white')

    ax.set_xlim(0, 100)
    ax.set_yticks([])
    ax.set_xticks([])  
    ax.set_xlabel('')
    
  elif (value1 + value2) == 0:
    value1 = 1; value2 = 1
    total = value1 + value2
    percentage1 = (value1 / total) * 100
    percentage2 = (value2 / total) * 100

    fig, ax = plt.subplots(figsize=(3, 0.3))
    if percentage1 > percentage2:   
      ax.barh(0, percentage1, color='#2bc22d')
      ax.barh(0, percentage2, left=percentage1, color='#c2372b')
    elif percentage1 == percentage2:
      ax.barh(0, percentage1, color='#9497a1')
      ax.barh(0, percentage2, left=percentage1, color='#9497a1')
    else:
      ax.barh(0, percentage1, color='#c2372b')
      ax.barh(0, percentage2, left=percentage1, color='#2bc22d')

    ax.text(percentage1 / 2, 0, f'{value1-1}', ha='center', va='center', color='white')
    ax.text(percentage1 + percentage2 / 2, 0, f'{value2-1}', ha='center', va='center', color='white')

    ax.set_xlim(0, 100)
    ax.set_yticks([])
    ax.set_xticks([])  
    ax.set_xlabel('')  

  else:
    if (value1 > value2):
      total = value1 + value2
      percentage1 = (value1 / total) * 100
      percentage2 = (value2 / total) * 100
        
      fig, ax = plt.subplots(figsize=(3, 0.3))
      if percentage1 > percentage2:   
        ax.barh(0, percentage1, color='#2bc22d')
        ax.barh(0, percentage2, left=percentage1, color='#c2372b')
      elif percentage1 == percentage2:
        ax.barh(0, percentage1, color='#9497a1')
        ax.barh(0, percentage2, left=percentage1, color='#9497a1')
      else:
        ax.barh(0, percentage1, color='#c2372b')
        ax.barh(0, percentage2, left=percentage1, color='#2bc22d')

      ax.text(percentage1 / 2, 0, f'{value1}', ha='center', va='center', color='white')
        #ax.text(percentage1 + percentage2 / 2, 0, f'{value2-1}', ha='center', va='center', color='white')

      ax.set_xlim(0, 100)
      ax.set_yticks([])
      ax.set_xticks([])  
      ax.set_xlabel('')  

    else:
      total = value1 + value2
      percentage1 = (value1 / total) * 100
      percentage2 = (value2 / total) * 100

      fig, ax = plt.subplots(figsize=(3, 0.3))

      if percentage1 > percentage2:   
        ax.barh(0, percentage1, color='green')
        ax.barh(0, percentage2, left=percentage1, color='red')
      elif percentage1 == percentage2:
        ax.barh(0, percentage1, color='gray')
        ax.barh(0, percentage2, left=percentage1, color='gray')
      else:
        ax.barh(0, percentage1, color='red')
        ax.barh(0, percentage2, left=percentage1, color='green')
      
      ax.text(percentage1 + percentage2 / 2, 0, f'{value2}', ha='center', va='center', color='white')
      ax.set_xlim(0, 100)
      ax.set_yticks([])
      ax.set_xticks([])  
      ax.set_xlabel('')  

  return fig


def shot_map(id, df_shot, df_results, team_flag):
  
  home_team = df_results[df_results['match_id'] == id]['home_team_name'].iloc[0]
  away_team = df_results[df_results['match_id'] == id]['away_team_name'].iloc[0]

  home_score = df_results[df_results['match_id'] == id]['home_ET_score'].iloc[0]
  away_score = df_results[df_results['match_id'] == id]['away_ET_score'].iloc[0]

  team = home_team if team_flag == 1 else away_team

  df_match = df_shot[df_shot['match_id'] == id]
  df_shot_team = df_match[df_match['team_name'] == team]
  df_goal = df_shot_team[df_shot_team['outcome_name'] == 'goal']
  df_notgoal = df_shot_team[df_shot_team['outcome_name'] == 'notgoal']

  pitch = VerticalPitch(pad_bottom=0.5, half=True, goal_type='box', goal_alpha=0.6)  
  fig, ax = pitch.draw(figsize=(12, 10))

  sc = pitch.scatter(df_notgoal.x, df_notgoal.y,
                    # size varies between 100 and 1000 (points squared)
                    s=(df_notgoal.shot_statsbomb_xg * 900) + 100,
                    c='#b94b75',
                    edgecolors='#383838',  # give the markers a charcoal border
                    # for other markers types see: https://matplotlib.org/api/markers_api.html
                    marker='h',
                    ax=ax)


  sc = pitch.scatter(df_goal.x, df_goal.y,
                    s=(df_goal.shot_statsbomb_xg * 900) + 100,
                    c='#009900',  
                    edgecolors='#383838',  
                    marker='h',
                    ax=ax)



  if team_flag == 1:
    txt = ax.text(x=40, y=80, s='{}\nTotal Shots: {} Goals: {}, xG: {}'.format(team.upper(),
                                                                               df_shot_team[df_shot_team['ps'] == False].shape[0],
                                                                               df_results[df_results['match_id'] == id]['home_ET_score'].iloc[0],
                                                                               round(df_shot_team[df_shot_team['ps'] == False]['shot_statsbomb_xg'].sum(), 2)), 
                  size=30,
                  color='#4d544f', va='center', ha='center')
  elif team_flag == 2:

    txt = ax.text(x=40, y=80, s='{}\nTotal Shots: {} Goals: {}, xG: {}'.format(team.upper(),
                                                                               df_shot_team[df_shot_team['ps'] == False].shape[0],
                                                                               df_results[df_results['match_id'] == id]['away_ET_score'].iloc[0],
                                                                               round(df_shot_team[df_shot_team['ps'] == False]['shot_statsbomb_xg'].sum(), 2)), 
                  size=30,
                  color='#4d544f', va='center', ha='center')
    

    #plt.gca().invert_yaxis()
    
  return fig


def pass_map(id, df_pass, df_results, team_flag):
  
  home_team = df_results[df_results['match_id'] == id]['home_team_name'].iloc[0]
  away_team = df_results[df_results['match_id'] == id]['away_team_name'].iloc[0]

  if team_flag == 1:
    team = home_team
    color = '#3556b8'
  else:
    team = away_team
    color= '#c24138'
  
  
  a = df_pass[(df_pass['match_id'] == id) & (df_pass['team_name'] == team)]
  
  passes = a[['x', 'y', 'end_x', 'end_y', 'player_name']]

  player_pass_counts = passes['player_name'].value_counts()
  sorted_player_pass_counts = player_pass_counts.sort_values(ascending=False)
  names = sorted_player_pass_counts.head(9).reset_index()['player_name'].tolist()

  #draw 4x4 pitches
  pitch = Pitch(line_color='black', pad_top=20)
  fig, axs = pitch.grid(ncols = 3, nrows = 3, grid_height=0.85, title_height=0.06, axis=False,
                      endnote_height=0.04, title_space=0.04, endnote_space=0.01)

  #for each player
  for name, ax in zip(names, axs['pitch'].flat[:len(names)]):
      #put player name over the plot
      ax.text(60, -10, name,
              ha='center', va='center', fontsize=14)
      #take only passes by this player
      player_df = passes.loc[passes["player_name"] == name]
      #scatter
      pitch.scatter(player_df.x, player_df.y, alpha = 0.2, s = 50, color = color, ax=ax)
      #plot arrow
      pitch.arrows(player_df.x, player_df.y,
              player_df.end_x, player_df.end_y, color = color, ax=ax, width=1)

  #We have more than enough pitches - remove them
  for ax in axs['pitch'][-1, 16 - len(names):]:
      ax.remove()

  #Another way to set title using mplsoccer
  axs['title'].text(0.5, 0.5, '{}'.format(team), ha='center', va='center', fontsize=25)
  #plt.show()

  return fig



import matplotlib.pyplot as plt

def xg_plot(id, df_shot, df_results, team_flag):
  
    home_team = df_results[df_results['match_id'] == id]['home_team_name'].iloc[0]
    away_team = df_results[df_results['match_id'] == id]['away_team_name'].iloc[0]
    et_flag = df_results[df_results['match_id'] == id]['et_flag'].iloc[0]

    if team_flag == 1:
        team = home_team
        color = '#3556b8'
    else:
        team = away_team
        color= '#c24138'

    df_xg = df_shot[(df_shot['match_id'] == id)&(df_shot['ps'] == False)&(df_shot['team_name'] == team)]

    df_xg = df_xg[['team_name', 'match_id', 'outcome_name', 'ps', 'shot_statsbomb_xg', 'minute']]
    df_xg = df_xg.sort_values('minute')
    df_goal = df_xg[df_xg['outcome_name'] == 'goal']

    mins = [15, 30, 45, 60, 75, 90]
    mins_et = mins + [105, 120]

    xg_sums = [0]
    shot_mins = df_xg.minute.tolist()
    for min in shot_mins:
        s = df_xg[df_xg['minute'] <= min].shot_statsbomb_xg.sum()
        xg_sums.append(round(s, 3))

    if et_flag == 0:
        x = mins
    else:
        x = mins_et

    fig, ax = plt.subplots()
    ax.step([0]+shot_mins, xg_sums, color=color)
    ax.set_title('{}'.format(team))
    ax.set_xlabel('Minute')
    ax.set_ylabel('xG sum')
    
    if et_flag == 0:
      ax.set_xlim(0, 95)
      ax.set_ylim(0, 3)
    else:
      ax.set_xlim(0, 125)
      ax.set_ylim(0, 3)
    if df_goal.shape[0] > 0:
        mins = df_goal.minute.tolist()
        for min in mins:
            s = df_xg[df_xg['minute'] <= min].shot_statsbomb_xg.sum()
            ax.scatter(min, s, color='black', s=100)

    return fig


def xg_per_min(id, df_shot, df_results):
  
  home_team = df_results[df_results['match_id'] == id]['home_team_name'].iloc[0]
  away_team = df_results[df_results['match_id'] == id]['away_team_name'].iloc[0]
  et_flag = df_results[df_results['match_id'] == id]['et_flag'].iloc[0]

  df1 = df_shot[(df_shot['match_id'] == id) & (df_shot['team_name'] == home_team) & (df_shot['ps'] == False)]
  df2 = df_shot[(df_shot['match_id'] == id) & (df_shot['team_name'] == away_team) & (df_shot['ps'] == False)]

  df1 = df1[['minute', 'team_name', 'shot_statsbomb_xg', 'outcome_name', 'match_id']]
  df2 = df2[['minute', 'team_name', 'shot_statsbomb_xg', 'outcome_name', 'match_id']]

  mins = list(range(5, 96, 5))
  mins_et = list(range(5, 126, 5))

  xg1 = [df1[df1['minute'] < 5].shot_statsbomb_xg.sum()]
  xg2 = [df2[df2['minute'] < 5].shot_statsbomb_xg.sum()]
  
  if et_flag == 0:
    for i in range(1, len(mins)):
      s = df1[(df1['minute'] < mins[i]) & (df1['minute'] > mins[i-1])].shot_statsbomb_xg.sum()
      xg1.append(s)
      s = df2[(df2['minute'] < mins[i]) & (df2['minute'] > mins[i-1])].shot_statsbomb_xg.sum()
      xg2.append(s)

    return xg1, xg2, mins, [home_team, away_team]
  else:
    for i in range(1, len(mins_et)):
      s = df1[(df1['minute'] < mins_et[i]) & (df1['minute'] > mins_et[i-1])].shot_statsbomb_xg.sum()
      xg1.append(s)
      s = df2[(df2['minute'] < mins_et[i]) & (df2['minute'] > mins_et[i-1])].shot_statsbomb_xg.sum()
      xg2.append(s)

    return xg1, xg2, mins_et, [home_team, away_team]
  
def threat_timeline(xg1, xg2, mins, teams):
  
  xg2 = [-x for x in xg2]


  positive_color = '#3556b8'
  negative_color = '#c24138'

  fig, ax = plt.subplots(figsize=(20, 6))

  x = np.arange(len(mins))

  bars = ax.bar(x, xg1, align='center', color=[positive_color if val >= 0 else negative_color for val in xg1])
  bars = ax.bar(x, xg2, align='center', color=[positive_color if val >= 0 else negative_color for val in xg2])

  ax.set_xticks(x)
  ax.set_xticklabels(mins)

  # Add a legend for the colors
  ax.legend(handles=[plt.Rectangle((0,0),1,1,color=positive_color), plt.Rectangle((0,0),1,1,color=negative_color)],
            labels=teams)

  # Display the plot
  #plt.gca().set_yticklabels([])
  ax.axis('off')

  return fig
