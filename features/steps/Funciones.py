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

class Funciones_Globales():
    def __init__(self,driver):
        self.driver = driver

    def Tiempo(self,tie):
        t = time.sleep(tie)
        return t

    def Navegar(self,Url,tie):
        self.driver.maximize_window()
        self.driver.get(Url)
        print("Pagina abierta "+str(Url))
        t = time.sleep(tie)
        return t

    def Texto_Multiple(self,tipo,selector,texto,tiempo):
        if(tipo == "xpath"):
          try:
            valor = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.XPATH,selector)
            valor.clear()
            valor.send_keys(texto)
            print("Escribiendo en el campo {} el texto {}".format(selector,texto))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
             print(ex.msg)
             print("No se encontro el elemento: "+ selector)

        elif(tipo =="id"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.ID, selector)
                valor.clear()
                valor.send_keys(texto)
                print("Escribiendo en el campo {} el texto {}".format(selector, texto))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)
    def Click_Multiple(self,tipo,selector,tiempo):
        if(tipo == "xpath"):
          try:
            valor = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.XPATH,selector)
            valor.click()
            print("Haciendo click en el campo {} ".format(selector))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: "+ selector)

        elif(tipo == "id"):
            try:
                valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
                valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
                valor = self.driver.find_element(By.ID, selector)
                valor.click()
                print("Haciendo click en el campo {} ".format(selector))
                t = time.sleep(tiempo)
                return t
            except TimeoutException as ex:
                print(ex.msg)
                print("No se encontro el elemento: " + selector)



    def Select_XPath(self,xpath,tipo,dato,tiempo):
        try:
            valor = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.XPATH,xpath)
            valor = Select(valor)

            if(tipo == "texto"):
                valor.select_by_visible_text(dato)
                print("El campo Seleccionado es: {} ".format(dato))
            elif(tipo == "value"):
                valor.select_by_value(dato)
                print("El campo Seleccionado es: {} ".format(dato))
            elif(tipo == "index"):
                valor.select_by_index(dato)
                print("El campo Seleccionado es: {} ".format(dato))

            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: "+ xpath)

    def Select_ID(self,ID,tipo,dato,tiempo):
        try:
            valor = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,ID)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.ID,ID)
            valor = Select(valor)

            if(tipo == "texto"):
                valor.select_by_visible_text(dato)
                print("El campo Seleccionado es: {} ".format(dato))
            elif(tipo == "value"):
                valor.select_by_value(dato)
                print("El campo Seleccionado es: {} ".format(dato))
            elif(tipo == "index"):
                valor.select_by_index(dato)
                print("El campo Seleccionado es: {} ".format(dato))

            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: "+ ID)


    def Upload_XPath(self,xpath,path,tiempo):
        try:
            valor = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.XPATH,xpath)
            valor.send_keys(path)
            print("La imagen que se sube es: {} ".format(path))

            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: "+ xpath)

    def Upload_ID(self,ID,path,tiempo):
        try:
            valor = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.ID,ID)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.ID,ID)
            valor.send_keys(path)
            print("La imagen que se sube es: {} ".format(path))

            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: "+ ID)

    #Funcion con Xpath para hacer check en radio and check buttons
    def Check_XPath(self,xpath,tiempo):
        try:
            valor = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,xpath)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();",valor)
            valor = self.driver.find_element(By.XPATH,xpath)
            valor.click()
            print("Haciendo click en el elemento: {} ".format(xpath))

            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: "+ xpath)

    # Funcion Con ID para hacer check en radio and check buttons
    def Check_ID(self, ID, tiempo):
        try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, ID)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.ID, ID)
            valor.click()
            print("Haciendo click en el elemento: {} ".format(ID))
            t = time.sleep(tiempo)
            return t
        except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + ID)

    #Función para multiples checks
    def Check_Multiples_XPath(self,tiempo,*args):
        for num in args:
         try:
             valor = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located((By.XPATH,num)))
             valor = self.driver.execute_script("arguments[0].scrollIntoView();",valor)
             valor = self.driver.find_element(By.XPATH,num)
             valor.click()
             print("Haciendo click en el elemento: {} ".format(num))

             t = time.sleep(tiempo)
             return t
         except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: "+ num)


    def Double_Click(self,tipo,selector,tiempo):
        if(tipo == "xpath"):
          try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, selector)
            act = ActionChains(self.driver)
            act.double_click(valor).perform()
            print("Double click en {}".format(selector))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + selector)

        elif (tipo == "id"):
          try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.ID, selector)
            act = ActionChains(self.driver)
            act.double_click(valor).perform()
            print("Double click en {}".format(selector))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
              print(ex.msg)
              print("No se encontro el elemento: " + selector)

    def Derecho_Click(self,tipo,selector,tiempo):
        if(tipo == "xpath"):
          try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, selector)
            act = ActionChains(self.driver)
            act.context_click(valor).perform()
            print("Click Derecho en {}".format(selector))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + selector)

        elif (tipo == "id"):
          try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.ID, selector)
            act = ActionChains(self.driver)
            act.context_click(valor).perform()
            print("Click Derecho en {}".format(selector))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
              print(ex.msg)
              print("No se encontro el elemento: " + selector)

    #Funcion Drag and Drop
    def DragDrop_Click(self,tipo,selector,destino,tiempo):
        if(tipo == "xpath"):
          try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, selector)

            valor2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, destino)))
            valor2 = self.driver.execute_script("arguments[0].scrollIntoView();", valor2)
            valor2 = self.driver.find_element(By.XPATH, destino)

            act = ActionChains(self.driver)
            act.drag_and_drop(valor,valor2).perform()
            print("Arrastrando objetvo {} en {}".format(selector,destino))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + selector)

        elif (tipo == "id"):
          try:
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.ID, selector)

            valor2 = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, destino)))
            valor2 = self.driver.execute_script("arguments[0].scrollIntoView();", valor2)
            valor2 = self.driver.find_element(By.XPATH, destino)

            act = ActionChains(self.driver)
            act.drag_and_drop(valor, valor2).perform()
            print("Arrastrando objetvo {} en {}".format(selector, destino))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
              print(ex.msg)
              print("No se encontro el elemento: " + selector)

    #Dragon Drop coordenate
    def DragDrop_Click_Coordenates(self,tipo,selector,x,y,tiempo):
        if(tipo == "xpath"):
          try:
            self.driver.switch_to.frame(0)
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, selector)


            act = ActionChains(self.driver)
            act.drag_and_drop_by_offset(valor,x,y).perform()
            print("Arrastrando objetvo {} en x:{} y:{}".format(selector,x,y))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + selector)

        elif (tipo == "id"):
          try:
            self.driver.switch_to.frame(0)
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.ID, selector)

            act = ActionChains(self.driver)
            act.drag_and_drop_by_offset(valor, x,y).perform()
            print("Arrastrando objetvo {} en x:{} y:{}".format(selector, x,y))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
              print(ex.msg)
              print("No se encontro el elemento: " + selector)

    def Click_Coordenates(self,tipo,selector,x,y,tiempo):
        if(tipo == "xpath"):
          try:
            #self.driver.switch_to.frame(0)
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.XPATH, selector)


            act = ActionChains(self.driver)
            act.move_to_element_with_offset(valor,x,y).click().perform()
            print("Hacienco click en el elemento {} en x:{} y:{}".format(selector,x,y))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
            print(ex.msg)
            print("No se encontro el elemento: " + selector)

        elif (tipo == "id"):
          try:
            #self.driver.switch_to.frame(0)
            valor = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.ID, selector)))
            valor = self.driver.execute_script("arguments[0].scrollIntoView();", valor)
            valor = self.driver.find_element(By.ID, selector)



            act = ActionChains(self.driver)
            act.move_to_element_with_offset(valor,x,y).click().perform()
            print("Haciendo click en el elemento {} en x:{} y:{}".format(selector, x,y))
            t = time.sleep(tiempo)
            return t
          except TimeoutException as ex:
              print(ex.msg)
              print("No se encontro el elemento: " + selector)