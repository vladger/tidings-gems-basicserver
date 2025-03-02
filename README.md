# tidings-gems-basicserver
A basic PHP server reverse engineering attempt and archival project for Gems social match-3 game known as "Твои Сокровища" by Dind Games, for the Flash client. One of the older social games.
# Findings
Unmodified SWF sends all requests to API backend encrypted, using its own encryption mechanism. By decompiling the Main SWF (or output113.js in HTML5 client), we can get the encryption key and the encrypt/decrypt functions (a JS-based decryption tool is ENCRYPTDECRYPT.html).
This server is supposed to be used with the encryption turned off in the client (by decompiling SWF and disabling Crypt), when it's off, the client sends POST requests with parameters in body.
# Setup guide
1) Install any webserver software with PHP support, set the public_html to make sure the server.php is on top
2) Use hosts or Fiddler, or other web proxy tool, to redirect requests from tidings.su to your server:
   crossdomain.xml, api.ok.ru/fb.do, gems_ok/www/api.php
3) Launch the client with index.html embed page in a browser that supports Flash
# Progress
✅Request encryption mechanism (encryption/decryption tool)
✅Fake authorization (getting to the main menu)
✅Archived user state loading
✅Level loading (currently only level 1 and 2 saved, will be saving more levels, there are 19900 levels on servers)
❌Level finishing (currently hangs, needs adding handlers)
❌Social friends
❌VK/OK/Mail API working right / replacement
❌Saving and loading data from database
❌HTML5 client support (untested, hard to download)
