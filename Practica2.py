#Imports

import pprint
from pprint import pp
import json
from urllib import response
import requests
import csv
import time

#Urls
urlorg = "https://api.meraki.com/api/v1/organizations"
urldev= "https://api.meraki.com/api/v1/organizations/organizationId/devices"
urlsta= "https://api.meraki.com/api/v0/organizations/organizationId/deviceStatuses"

#Header
payload = None
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}

#Functions 

def orgList():                                              # Obtiene la lista de la API_KEY
    response = requests.request('GET', urlorg, headers=headers, data = payload)
    orgList= json.loads(response.text)
    if response.raise_for_status()!=None:
        print("Se jodió la vaina jefecit@")
    return orgList

def  orgId(orgList):                                        #Obtiene el Id asociado al nombre de organización que se le pasa
    DeLab=[]
    for i in range(len(orgList)):
        if(orgList[i]["name"]=="DeLab"):    	    
            DeLab.append(orgList[i])
        DeLab.append(0)
    return DeLab[0]['id']

def orgDev(Id):                                             #Obtiene los devices de DeLab
    urldev1="https://api.meraki.com/api/v1/organizations/organizationId/devices".replace('organizationId', Id)
    response= requests.request('GET', urldev1, headers=headers, data = payload)
    orgDev= json.loads(response.text)
    if response.raise_for_status()!=None:
        print("Se jodió la vaina jefecit@")
    return orgDev

def orgSta(Id):                                             #Obtiene los status de los devices de DeLab
    urlsta1="https://api.meraki.com/api/v0/organizations/organizationId/deviceStatuses".replace('organizationId', Id)
    response= requests.request('GET', urlsta1, headers=headers, data = payload)
    orgStatus=response.json()
    if response.raise_for_status()!=None:
        print("Se jodió la vaina jefecit@")
    return orgStatus


def productType(orgDev):                                    # Simplificamos la lista para que nos de los devices que son tipo appliance y wireless
    simplifiedList=[]
    for i in range(len(orgDev)):
        if(orgDev[i]["productType"]== "appliance"):
            simplifiedList.append(orgDev[i])
        if(orgDev[i]["productType"]== "wireless"):
            simplifiedList.append(orgDev[i])
    return simplifiedList

def reorderList(x,y):                                       # Arreglamos las listas y les damos el orden establecido en la actividad y borramos los datos innecesarios
    for i in range(len(x)):
        xcopy = x[i].copy()
        x[i].clear()
        
        if xcopy["productType"]=="wireless":
            x[i]["productType"] = xcopy["productType"]
            x[i]["model"] = xcopy["model"]
            x[i]["name"] = xcopy["name"]
            x[i]["mac"] = xcopy["mac"]
            for k in range (len(y)):
                if x[i]["mac"] == y[k]["mac"]:
                    x[i]["publicIp"] = y[k]["publicIp"]
            x[i]["lanIp"] = xcopy["lanIp"]
            x[i]["serial"] = xcopy["serial"]
            for j in range (len(y)):
                if x[i]["serial"] == y[j]["serial"]:
                    x[i]["status"] = y[j]["status"]
            
                           
        else:
            x[i]["productType"] = xcopy["productType"]
            x[i]["model"] = xcopy["model"]
            x[i]["name"] = xcopy["name"]
            x[i]["mac"] = xcopy["mac"]
            for k in range (len(y)):
                if x[i]["mac"] == y[k]["mac"]:
                    x[i]["publicIp"] = y[k]["publicIp"]
            x[i]["wan1Ip"] = xcopy["wan1Ip"]
            x[i]["serial"] = xcopy["serial"]
            for j in range (len(y)):
                if x[i]["serial"] == y[j]["serial"]:
                    x[i]["status"] = y[j]["status"]

def jsontocsv(x):                                           # Pasamos de json a csv
    blank=[]
    header=x[0].keys()
    with open('DevicesList.csv','w') as inventory:
        inventory_writer= csv.writer(inventory,delimiter=',')
        inventory_writer.writerow(header)
        for i in range(len(x)):
            if(x[0]['productType']==x[i]['productType']):
                inventory_writer.writerow(x[i].values())
        i=0
        while(x[0]['productType']==x[i]['productType']):
            i=1+i
        header=x[i].keys()
        inventory_writer.writerow(blank)
        inventory_writer.writerow(header)
        for i in range(len(x)):
            if(x[0]['productType']!=x[i]['productType']):
                inventory_writer.writerow(x[i].values())

def cincomin():                                             # Espera 5 minutos
    time.sleep(300)

# Llamada a las funciones

list=orgList()  
id=orgId(list)
#id='681155'

while(True):

    devices=orgDev(id)
    devicesStatuses=orgSta(id)
    devicesList=productType(devices)
    reorderList(devicesList,devicesStatuses) #Se reordena devicesList
    jsontocsv(devicesList)
    cincomin()
