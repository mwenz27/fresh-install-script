"""
Create a script to install items without needing to search for the links ever again.

run the code for windows 'python main.py windows'
built on 18-01-2023
"""
import argparse
import subprocess
import os
import toml
import webbrowser

current_directory = os.getcwd()

parser = argparse.ArgumentParser()
parser.add_argument("os", help="specify windows, mac, linux or chrome")
args = parser.parse_args()


def freshinstall():
    """Windows - Opens Browser and opens tabs
    Mac - Opens Browser and opens tabs
    Linux - Runs Linux commands
    """
    file_name = f"{args.os}.toml"
    file_path = os.path.join(current_directory, file_name)
    try:
        # Read the TOML file
        with open(file_path, 'r') as f:
            data = toml.load(f)

        if args.os == "windows":
            # Open each URL in a new browser tab
            for url_list in data['url_list']:
                webbrowser.open_new_tab(url_list['url'])
                print(url_list['name'])
                if url_list["url"] == "https://ninite.com/":
                    print(""" Select Items
                                Zoom, a popular video conferencing software
                                Discord, a popular communication and chat platform for gamers
                                VLC, a media player
                                Spotify, a music streaming service
                                Krita, a digital painting and illustration software
                                Greenshot, a screenshot software
                                Google Earth, a virtual globe and map software
                                Steam, a digital distribution platform for video games
                                7-zip, a file archiving software
                                Anaconda, a distribution of the Python and R programming languages
                    """)
        elif args.os == "mac":
            for url_list in data['url_list']:
                webbrowser.open_new_tab(url_list['url'])
                print(url_list['name'])
        elif args.os == "linux":
            for app in data["apps"]:
                subprocess.run(["sudo", "apt-get", "install", "-y", app], shell=False)
                print(data["name"])
        elif args.os == "chrome":
            for url_list in data["extensions"]:
                print(url_list["name"])
                webbrowser.open_new_tab(url_list["url"])
    except FileNotFoundError:
        print(f"{file_name} not found in {current_directory}.")
    except:
        print("An error occurred.")


if __name__ == '__main__':
    freshinstall()
