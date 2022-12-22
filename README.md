# random_wallpaper

## About
Use this package to randomly choose a frame from your favorite video or movie and set it as your wallpaper. Included is a Windows batch file to automate this process using Windows Task Scheduler

Note: This package is currently only supported on Windows

## Getting Started
1. Clone the repo
   ```sh
   git clone https://github.com/hpvok13/random_wallpaper.git 
   ```
2. Add a video directory
   ```sh
   cd random_wallpaper
   mkdir videos
   ```
3. Add mp4 videos to videos/ directory
4. Run the script
   ```sh
   python random_wallpaper.py
   ```

You're done! Enjoy a simple random selection from any frame of any number of videos whenever you want. If you want to schedule this to recur periodically, you'll need to create a batch file and add a task to the Windows Task scheduler. Included in this package is a script to create a batch file for you.
1. Create batch file
   ```sh
   python create_batch.py
   ```
2. Schedule your wallpaper refresh using Windows Task Scheduler. Follow the instructions [here](https://datatofish.com/python-script-windows-scheduler/#:~:text=Double%2Dclick%20on%20the%20Task,Python%20script%20daily%20at%206am.), starting at step 4. Schedule the task for a given frequency, on startup, login, or any other trigger.

Now you're really done! Enjoy a random, fresh wallpaper as often as you want from your favorite movies and videos.
