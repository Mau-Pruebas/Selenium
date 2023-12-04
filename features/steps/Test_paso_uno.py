from behave import *
import time
import unittest
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.alert import Alert
from features.steps.Funciones import Funciones_Globales

@given(u'Abriendo navegador')
def step_impl(context):
    global driver, f

    context.driver = webdriver.Chrome()
    driver = context.driver
    driver.get("https://demo.seleniumeasy.com/basic-first-form-demo.html")
    f = Funciones_Globales(context.driver)


@when(u'Introducimos el valor "{user}" en los campos')
def step_impl(context, user):
    f.Texto_Multiple("xpath","//input[@id='user-message']",user,1)



@then(u'Enter the message and click Show Message')
def step_impl(context):
    f.Click_Multiple("xpath","//button[@type='button'][contains(.,'Show Message')]",1)



@then(u'Enter A "{x}" value')
def step_impl(context,x):
    f.Texto_Multiple("xpath","//input[contains(@id,'value1')]",x,1)


@then(u'Enter B "{y}" value')
def step_impl(context,y):
 f.Texto_Multiple("xpath","//input[contains(@id,'value2')]",y,1)


@then(u'Click Get Total button')
def step_impl(context):
 f.Click_Multiple("xpath","//button[@type='button'][contains(.,'Get Total')]",1)
 driver.close()