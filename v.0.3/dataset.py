from nba_api.stats.endpoints import leaguegamelog
import pandas as pd

season1213 = leaguegamelog.LeagueGameLog(season='2012-13').get_data_frames()[0].drop(columns=['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'WL',
                                                                                              'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'VIDEO_AVAILABLE'])
season1314 = leaguegamelog.LeagueGameLog(season='2013-14').get_data_frames()[0].drop(columns=['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'WL',
                                                                                              'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'VIDEO_AVAILABLE'])
season1415 = leaguegamelog.LeagueGameLog(season='2014-15').get_data_frames()[0].drop(columns=['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'WL',
                                                                                              'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'VIDEO_AVAILABLE'])
season1516 = leaguegamelog.LeagueGameLog(season='2015-16').get_data_frames()[0].drop(columns=['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'WL',
                                                                                              'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'VIDEO_AVAILABLE'])
season1617 = leaguegamelog.LeagueGameLog(season='2016-17').get_data_frames()[0].drop(columns=['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'WL',
                                                                                              'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'VIDEO_AVAILABLE'])
season1718 = leaguegamelog.LeagueGameLog(season='2017-18').get_data_frames()[0].drop(columns=['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'WL',
                                                                                              'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'VIDEO_AVAILABLE'])

season1819 = leaguegamelog.LeagueGameLog(season='2018-19').get_data_frames()[0].drop(columns=['TEAM_ID', 'TEAM_ABBREVIATION', 'TEAM_NAME', 'GAME_ID', 'GAME_DATE', 'WL',
                                                                                              'MIN', 'FGM', 'FGA', 'FG_PCT', 'FG3M', 'FG3A', 'FG3_PCT', 'FTM', 'FTA', 'FT_PCT', 'OREB', 'DREB', 'REB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS', 'VIDEO_AVAILABLE'])

frames = [season1213, season1314, season1415,
          season1516, season1617, season1718]
result = pd.concat(frames)


result.to_csv(r'C:include your path',
              index=False, header=True)
season1819.to_csv(
    r'C:\include your path', index=False, header=True)

print('done')
