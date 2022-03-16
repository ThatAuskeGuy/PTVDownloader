# PTVDownloader
A Python tool to download the current day's Pathway To Victory podcast

#### Why Did I Make This?
Pathway To Victory is a production of First Baptist Church of Dallas' pastor Dr. Robert Jeffress. They have it in a podcast version, but they only keep the previous two week's podcasts. I wanted an easy way to keep all of them, but it it really kind of hard to figure out how to download them. I'm sure somewhere there is an archive of old podcasts, but if I knew about it, I wouldn't have had the opportunity to play around with and learn Beautiful Soup. I'm planning on setting it up as a cronjob. Hopefully you find it as useful as I do.

#### What Does it Do?
PTVDownloader will check the website to see if there is a new podcast based on the current day's date. If there is, it will work its way to where the audio file is located, and then create an .mp3 file of the podcast as well as a text file of it's description in a folder named after the series the podcast is in. These files, as written in the python file, will be saved in the same directory as the program.
