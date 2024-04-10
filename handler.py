from pathlib import Path
import boto3
from nba_api.live.nba.endpoints import scoreboard

# TODO bucket name as an environment variable
# TODO date should be the name of the file. then snowpipe should insert the file name into the "date" column
# TODO docstrings
# TODO it would be more convenient if we had boto3 installed locally - is it possible to exclude it from requirements?
# TODO downloading from nba_api and processing should be in a separate function
# TODO create a git repository for this project


def first_function(event, context):
  result = process_raw_games()
  
  save_file_to_s3(text="\n".join(result), bucket_name="nba-games-daily-scores", file_path="hello.txt")
  return {
    'statusCode': 200,
    'body': str(result),
  }


def save_file_to_s3(text: str, bucket_name: str, file_path: Path):
  encoded_text = text.encode("utf-8")
  s3_path = "" + file_path

  s3 = boto3.resource("s3")
  s3.Bucket(bucket_name).put_object(Key=s3_path, Body=encoded_text)

def process_raw_games() -> list[str]:

  games_raw = scoreboard.ScoreBoard().get_dict()

  games = games_raw["scoreboard"]["games"]

  header = "date,home_team,home_score,away_team,away_score"
  lines = []
  lines.append(header)
  for game in games:
    row = [
      game["gameEt"].split("T")[0],
      game["homeTeam"]["teamName"],
      game["homeTeam"]["score"],
      game["awayTeam"]["teamName"],
      game["awayTeam"]["score"],
    ]
    row = ",".join([str(r) for r in row])
    lines.append(row)
  return lines