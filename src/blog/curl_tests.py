"""

http://127.0.0.1:8000/api/posts/testing/edit/

danielmendoza
curl -X POST -d "username=danielmendoza&password=danielmendoza" http://127.0.0.1:8000/api/auth/token/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImRhbmllbG1lbmRvemEiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6IiIsImV4cCI6MTQ2NzI1ODUzOH0.xntB_Y79lFIggI94vjozwb1qVXv8A_VOaC3xixvb4Sw

curl -X POST -H "Content-Type: application/json" -d '{"content":"new comment"}' -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImRhbmllbG1lbmRvemEiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6IiIsImV4cCI6MTQ2NzI1ODUzOH0.xntB_Y79lFIggI94vjozwb1qVXv8A_VOaC3xixvb4Sw" 'http://127.0.0.1:8000/api/comments/create/?type=post&slug=testing'


testinguser

curl -X POST -d "username=testinguser&password=testinguser" http://127.0.0.1:8000/api/auth/token/

eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3Rpbmd1c2VyIiwidXNlcl9pZCI6OCwiZW1haWwiOiJ0ZXN0aW5ndXNlckBnbWFpbC5jb20iLCJleHAiOjE0NjcyNTg3MDl9.VYMi2LLTRTobxfxqBkzQIHUIsZZ7U3BRwGggF8prw1o

curl -X POST -H "Content-Type: application/json" -d '{"content":"new comment reply"}' -H "Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6InRlc3Rpbmd1c2VyIiwidXNlcl9pZCI6OCwiZW1haWwiOiJ0ZXN0aW5ndXNlckBnbWFpbC5jb20iLCJleHAiOjE0NjcyNTg3MDl9.VYMi2LLTRTobxfxqBkzQIHUIsZZ7U3BRwGggF8prw1o" 'http://127.0.0.1:8000/api/comments/create/?type=post&slug=testing&parent_id=45'






eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VybmFtZSI6ImRhbmllbG1lbmRvemEiLCJ1c2VyX2lkIjoxLCJlbWFpbCI6IiIsImV4cCI6MTQ2NzI2NjU2NX0.mGbX8X0Osl3oOzcq12eb5YbvW7G_gcjkppk9d1k2rf0
"""