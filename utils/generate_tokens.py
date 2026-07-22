from livekit import api

token = (
    api.AccessToken(
        api_key="API9J9mzH8km7A8",
        api_secret="wkBMy9iZ77NreeHrMtn29PRnLiPi63k5xEHBiBSz9k0",
    )
    .with_identity("shubham")
    .with_name("Shubham")
    .with_grants(
        api.VideoGrants(
            room_join=True,
            room="demo-room",
        )
    )
)

print(token.to_jwt())