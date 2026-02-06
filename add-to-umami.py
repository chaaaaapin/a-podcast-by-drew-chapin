import requests
import json

BASE_URL = "https://data.discoverability.co"
USERNAME = "claude"
PASSWORD = "noMgan-kipher-wawna4***"

# 1. Authenticate
print("Authenticating...")
r = requests.post(f"{BASE_URL}/api/auth/login", json={"username": USERNAME, "password": PASSWORD})
data = r.json()
token = data["token"]
headers = {"Authorization": f"Bearer {token}"}
teams = data["user"]["teams"]

print(f"Authenticated. Found {len(teams)} teams.")

# Find TDC Internal team
tdc_team = None
for team in teams:
    print(f"Team: {team['name']} (ID: {team['id']})")
    if team['name'] == 'TDC Internal':
        tdc_team = team
        break

if not tdc_team:
    print("ERROR: TDC Internal team not found")
    exit(1)

team_id = tdc_team['id']
print(f"Using TDC Internal team: {team_id}")

# 2. Create website
print("\nCreating website...")
website_data = {
    "name": "apodcastbydrewchapin.com",
    "domain": "apodcastbydrewchapin.com",
    "teamId": team_id
}

r = requests.post(
    f"{BASE_URL}/api/websites",
    headers=headers,
    json=website_data
)

if r.status_code == 200:
    result = r.json()
    print("Website created successfully!")
    print(json.dumps(result, indent=2))
    print(f"\nWebsite ID: {result['id']}")
else:
    print(f"ERROR: {r.status_code}")
    print(r.text)
