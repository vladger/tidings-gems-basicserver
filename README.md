# tidings-gems-basicserver
NOTE: this server uses actual OKRU user data, but the session had expired long ago.
A basic PHP server reverse engineering attempt and archival project for Gems social match-3 game known as "Твои Сокровища" by Dind Games, for the Flash client. One of the older social games.
# Findings
Unmodified SWF sends all requests to API backend encrypted, using its own encryption mechanism. By decompiling the Main SWF (or output113.js in HTML5 client), we can get the encryption key and the encrypt/decrypt functions (a JS-based decryption tool is ENCRYPTDECRYPT.html).
A level downloader script is now available. 

Dummy scripts: levelFinish_dummy.js (makes the game go back to levels on level finish), getVipScore.js, levelGetDecEnergy.js (makes the game reset the energy counter to 1 after selecting level), decBooster.js (deleted) (if decBooster.js empty exists, sets all booster count to 0)

# IMPORTANT NOTICE
This server is supposed to be used with the encryption turned OFF in the client Main.swf (by decompiling SWF and disabling Crypt), when it's off, the client sends POST requests with parameters in body.

# Setup guide
1) Install any webserver software with PHP support, set the public_html to make sure the server.php is on top
2) Use hosts or Fiddler, or other web proxy tool, to redirect requests from tidings.su to your server:
   crossdomain.xml, api.ok.ru/fb.do, gems_ok/www/api.php.
   If you want the background audio to work, redirect the folder /sounds to /www/sounds
   OR decompile the client Main.swf, replacing the tidings.su links to your IP with server running.
4) (Optional) Extract 1000 levels pack from zip, copy all .js files to /levels dir on server. You can download more levels from prod server using the leveldownloader.py script. After updating the levels, change the ml value in auth.js to your amount of downloaded levels count minus one.
5) Launch the client with index.html embed page in a browser that supports Flash OR open SWF in Flash Player Projector
# Progress
✅Request encryption mechanism (encryption/decryption tool)

✅Fake authorization (getting to the main menu)

✅Archived user state loading

✅Level loading (levels folder has 2 sample levels, "levels1-1000.zip" archive has the levels folder with 1000 levels archived. There are 199900 levels on main server.)

ℹ️ LEVEL ARCHIVAL PROGRESS: 0.5% (1000/199900)

ℹ️ PUZZLE ARCHIVAL WILL NOT BE DONE (thousands of same looping 450x450 animal pictures, btw levelfinish.js has fixed puzzle1)

✅Level finishing (real levelFinish.js (the star screen is now appearing with fixed dummy data, Main.swf caches stars until closed))

✅Puzzle photo loading (/puzzles folder)

❌Social friends

❌VK/OK/Mail API working right / replacement

❌Saving and loading data from database

❌HTML5 client support (untested, hard to download)
