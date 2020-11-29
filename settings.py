from pydantic import BaseSettings


class AWSSettings(BaseSettings):
    video_bucket: str
    aws_access_key_id: str
    aws_secret_access_key: str

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"
