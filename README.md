# HararaSpam
> A python script to spam the website http://asciibabes.appspot.com/ with ascii images.

Ascii images are just normal images recreated with ascii characters.  
http://www.glassgiant.com/ascii provides tools to create ascii images.  
This script uses all the images with .jpg extension in your pwd and post them one by one at glassgiant.com to get their equivalent ascii images and store those ascii images in a list. Once this is done, it uses an infinite while looop to post the stored ascii images to asciibabes.appspot.com!

## Python Libraries Used:
1. bs4 (BeautifulSoup4)
2. requests
3. glob 
