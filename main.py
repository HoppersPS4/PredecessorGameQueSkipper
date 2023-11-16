import requests
import random
import time

user_agents = [
    "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.1 Mobile/15E148 Safari/604.1",
    "Mozilla/5.0 (PlayStation 5 8.20) AppleWebKit/601.2 (KHTML, like Gecko)",
    "Mozilla/5.0 (PlayStation 4 11.00) AppleWebKit/601.2 (KHTML, like Gecko)",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/119.0",
    "Mozilla/5.0 (Linux; Android 14; SM-A205U) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.6045.134 Mobile Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 Edg/119.0.2151.58"
]

def random_line(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        return random.choice(lines).strip()

def generate_random_email(first_name, last_name):
    domains = ["pornhub.com", "gmail.com", "yahoo.com", "youporn.com", "gaypornhd.com", "gmx.de", "gmx.net"]
    domain = random.choice(domains)
    random_number = random.randint(1000, 9999)
    email = f"{first_name.lower()}.{last_name.lower()}{random_number}@{domain}"
    return email

def RegisterFakeRefUsers():
    url = "https://www.predecessorgame.com/api/ps-beta-signup"

    proxies = [ 
        'http://172.67.238.67:80',
        'http://172.67.186.143:80',
        'http://172.67.181.8:80',
        'http://172.67.83.151:80',
        'http://172.64.207.96:80',
        'http://172.67.110.33:80',
        'http://66.235.200.119:80',
        'http://159.112.235.134:80',
        'http://159.112.235.232:80',
    ]

    num_iterations = 5
    hours_to_sleep = 1  # Set the number of hours to sleep
    total_iterations = 0

    while True:  # Run indefinitely
        for _ in range(num_iterations):
            for attempt in range(5):  # Retry 5 times if request fails
                random_first_name = random_line("FirstName.txt")
                random_last_name = random_line("LastName.txt")

                random_email = generate_random_email(random_first_name, random_last_name)

                proxy = proxies[attempt % len(proxies)]

                user_agent = random.choice(user_agents)

                headers = {
                    "Host": "www.predecessorgame.com",
                    "Cookie": "_ga=GA1.1.1934670820.1699898414; _fbp=fb.1.1699920678399.575969818; _csrf=hvDY_0oLHn0g8_5otiKfoy7s; _gcl_au=1.1.2108489854.1699898440.144178858.1699922231.1699922230; _ga_TCC8E8VM94=GS1.1.1699920339.2.1.1699922554.0.0.0",
                    "Content-Length": "532",
                    "Sec-Ch-Ua": '"Chromium";v="119", "Not?A_Brand";v="24"',
                    "Content-Type": "application/json",
                    "Csrf-Token": "47XyhwVN-UbgbZM-aFG6ZzBwJFWIhGHDaG-Q",
                    "Sec-Ch-Ua-Mobile": "?0",
                    "User-Agent": user_agent,  # Use the selected user agent
                    "Sec-Ch-Ua-Platform": '"Windows"',
                    "Accept": "*/*",
                    "Origin": "https://www.predecessorgame.com",
                    "Sec-Fetch-Site": "same-origin",
                    "Sec-Fetch-Mode": "cors",
                    "Sec-Fetch-Dest": "empty",
                    "Referer": "https://www.predecessorgame.com/play/playstation-beta-access?ref_id=Z5W9HWW0Y",
                    "Accept-Encoding": "gzip, deflate, br",
                    "Accept-Language": "de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7",
                    "Priority": "u=1, i"
                }

                data = {
                    "email": random_email,
                    "firstName": f"New{random_first_name}",
                    "lastName": f"New{random_last_name}",
                    "answers": [
                        {"question_value": "Which platform would you like to participate on?", "answer_value": " PlayStation 5"},
                        {"question_value": "Which region will you participate from?", "answer_value": " Europe"},
                        {"question_value": "Would you like to receive news, special offers, feedback surveys and playtest invitations from Omeda Studios?", "answer_value": "Yes"}
                    ],
                    "referral": "https://www.predecessorgame.com/play/playstation-beta-access?ref_id=Z5W9HWW0Y"
                }

                try:
                    response = requests.post(url, json=data, headers=headers, proxies={'http': proxy}, timeout=10)
                    response.raise_for_status() 
                    print("Generated Email:", random_email)
                    print(f"Used proxy: {proxy}")
                    print("Referral:", data["referral"])
                    print("User Agent:", user_agent)
                    print("Response status code:", response.status_code)
                    print("Response text:", response.text, "\n")
                    break  # Break the inner loop if the request is successful
                except requests.exceptions.RequestException as e:
                    print(f"Error making request: {e}. Retrying...\n")
                    time.sleep(1)  # Sleep for 1 second before retrying

            #time.sleep(hours_to_sleep * 3600)  # Sleep for the specified number of hours
            total_iterations += 1

            if total_iterations % 5 == 0:
                print(f"Total iterations: {total_iterations}. Sleeping for an hour...")
                time.sleep(hours_to_sleep * 3600)  # Sleep for an hour before resetting num_iterations to 0

# Call the function
RegisterFakeRefUsers()
