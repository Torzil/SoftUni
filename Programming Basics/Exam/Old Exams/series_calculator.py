from math import floor

series_name = input()
number_of_seasons = int(input())
number_of_episodes_per_season = int(input())
episode_duration_without_ads = float(input())

total_episode_duration = (episode_duration_without_ads
                          + episode_duration_without_ads * 0.2)
total_season_duration = number_of_episodes_per_season * total_episode_duration + 10
total_series_duration = floor(total_season_duration * number_of_seasons)

print(f"Total time needed to watch the {series_name} series is {total_series_duration} minutes.")
