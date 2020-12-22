# Author: Jens Putzeys
# Date: 22-12-2020 (DD-MM-YYYY)
# I wrote this small program in a quarter of an hour to try to win one of the 100 iPhone12's from UnboxTherapy, but failed after two accounts
# got banned from Twitter after sending too many messages :(
# Update: wrote some documentation

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import random

###
# Define functions
###

def open_driver(url):
    """
    Open the webpage from the given url.
    :param url: link to webpage
    :return: driver object
    """

    # Defining firefox webdriver
    driver = webdriver.Firefox(executable_path='/lib/geckodriver-v0.27.0-linux64/geckodriver')

    driver.get(url)

    return driver


def check_login(dr, lbxp):
    """
    Waits for login page to load.
    :param dr: selenium webdriver
    :param lbxp: xpath of login button
    :return: void
    """

    # Wait until the login button has appeared
    while (len(dr.find_elements_by_xpath(lbxp)) == 0):
        print('waiting login...')


def login(dr, idxp, pwxp, id, pswd):
    """
    Logs the user in with the given id and password.
    :param dr: selenium webdriver
    :param idxp: xpath of the id field
    :param pwxp: xpath of the password field
    :param id: username, email or phone number
    :param pswd: password
    :return: void
    """

    # Fill in id
    d.find_element_by_xpath(idxp).send_keys(id)

    # Fill in password
    d.find_element_by_xpath(pwxp).send_keys(pswd)

    # Hit enter
    d.find_element_by_xpath(pwxp).send_keys(Keys.ENTER)


def tweet(dr, wtxp, tbxp, msg):
    """
    Tweets the given message.
    :param dr: selenium webdriver
    :param wtxp: xpath of the input box to write the message
    :param tbxp: xpath of the tweet button to send the tweet
    :param msg: the actual message that needs to be sent
    :return: void
    """
    # Send a variable number of tweets
    for i in range(0, 100):
        # Click on the message field to start typing
        dr.find_element_by_xpath(wtxp).click()

        # Start typing
        actions = ActionChains(dr)
        actions.send_keys(msg)
        actions.perform()

        # Click the send button
        d.find_element_by_xpath(tbxp).click()
        

        msg += '?' # Extend message because posts have to be unique
        n = 1
        n += random.randint(0, 1) # Random to prevent activating spam on Twitter
        time.sleep(n)


###
# Call functions
###

d = open_driver('https://twitter.com/home')

login_button_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[3]/div/div/span/span'
check_login(d, login_button_xpath)

id_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[1]/label/div/div[2]/div/input'
password_xpath = '/html/body/div/div/div/div[2]/main/div/div/div[1]/form/div/div[2]/label/div/div[2]/div/input'
login_id = input('Email or username or phone number: ')
login_password = input('Password: ')
login(d, id_xpath, password_xpath, login_id, login_password)

time.sleep(5) # Wait for main page to load (could be optimized like check_login())

write_tweet_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div'
tweet_button_xpath = '/html/body/div/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span'
message = '#100FREEiPhone12 @LewLater can I win an iPhone?'
tweet(d, write_tweet_xpath, tweet_button_xpath, message)
