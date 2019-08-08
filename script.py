# Python script to find Ultimate Guitar tabs, and save them in playlist.
# Read Readme.md for more information...

from selenium import webdriver
import time

username = <UG Username>
password = <UG Password>
UG_URL = 'https://www.ultimate-guitar.com/'

songs = []
# Example: 'Oceans Hillsong United'

# Arrays to push completed songs to.
done = []
unable = []


# Function that finds urls of tabs that have the best rating
def scrapper(song):
    #Set up driver for your engine
    driver = webdriver.Chrome()
    driver.get(UG_URL)

    time.sleep(2)

    cookie = driver.find_element_by_xpath("//button[contains(text(),'Got it, thanks!')]")
    cookie.click()

    search_field = driver.find_element_by_xpath("//input[@name='value']")
    search_field.send_keys(song)

    time.sleep(1)

    search_button = driver.find_element_by_xpath(
        "//button[span='Search']")
    search_button.click()

    time.sleep(2)

    # Find highest rated tab
    highest = driver.find_element_by_xpath("//a[contains(text(),'High rated')]")
    highest.click()

    time.sleep(2)
    
    # Generally, if webcrawling were to fail, it would be here...
    try:
        tabURL = driver.find_element_by_xpath("//div[div[4]='chords']/div[2]/header/span/span/a")
        tabURL.click()
        time.sleep(2)
        button_push(driver)
    except:
        print(song + " Was unable to be loaded")

# Function that signs into UG on tab page and places tab in playlist
def button_push(driver):
    # Sign into account
    sign_in = driver.find_element_by_xpath("//button[span[contains(text(),'Sign in')]]")
    sign_in.click()

    time.sleep(2)

    user_field = driver.find_element_by_xpath("//input[@name='username']")
    user_field.send_keys(username)

    password_field = driver.find_element_by_xpath("//input[@name='password']")
    password_field.send_keys(password)

    signed_in = driver.find_element_by_xpath("//footer/button")
    signed_in.click()

    time.sleep(2)

    # click 'Add to Playlist'
    playlist_button = driver.find_element_by_xpath(
        "//button[span='Add to playlist']")
    playlist_button.click()

    time.sleep(1)

    # Click on playlist
    add_button = driver.find_element_by_xpath("/html/body/div[6]/article/section/div[2]/article/div/div/div/div[2]/div[4]/div/span/button")
    add_button.click()

    # Click on Done button
    done_button = driver.find_element_by_xpath(
        "//button[span='Done']")
    done_button.click()

    # Quit driver and engine window
    driver.quit()

for song in songs:
    scrapper(song)
