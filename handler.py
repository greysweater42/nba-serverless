from pathlib import Path
import boto3
from nba_api.live.nba.endpoints import scoreboard


def save_nba_game_scores(event, context):
    games = download_nba_scores()
    result = process_raw_games(games=games)

    save_file_to_s3(
        text="\n".join(result),
        # TODO bucket name as an environment variable
        bucket_name="nba-games-daily-scores",
        file_path="nba-daily.csv",
    )
    return {
        "statusCode": 200,
        "body": str(result),
    }


def download_nba_scores() -> list[dict]:
    games_raw = scoreboard.ScoreBoard().get_dict()
    games = games_raw["scoreboard"]["games"]
    return games


def process_raw_games(games: list[dict]) -> list[str]:
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


def save_file_to_s3(text: str, bucket_name: str, file_path: Path) -> None:
    encoded_text = text.encode("utf-8")
    s3 = boto3.resource("s3")
    s3.Bucket(bucket_name).put_object(Key=file_path, Body=encoded_text)
