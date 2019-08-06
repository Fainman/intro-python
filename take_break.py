"""
Set an alarm to take a break by playing a youtube video
"""

import webbrowser
import time

def main():
    """
    Test function
    :return: non
    """
    video_address = "https://youtu.be/jfjfzKf85Ac"
    counter = 0
    while counter < 3:
        # Delay "sleep"
        time.sleep(3600) # 1 hour
        webbrowser.open(video_address)
        counter += 1


if __name__ == '__main__':
    main()
    exit(0)