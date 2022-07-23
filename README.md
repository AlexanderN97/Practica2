Universidad Simón Bolívar

Alexander Nascimento

15-11002

Redes definidas por Software 

Práctica 2

Al ejecutarse el programa se ejecutaran las siguientes funciones
    - list=orgList() -> Obtiene la lista de la API_KEY
    - id=orgId(list) -> Obtiene el Id asociado al nombre de organización que se le pasa (DeLab)
    - devices=orgDev(id) -> Obtiene los dispositivos de DeLab
    - devicesStatuses=orgSta(id) -> Obtiene los status de los dispositivos de DeLab
    - devicesList=productType(devices) -> Simplificamos la lista para que nos de los devices que son tipo appliance y wireless
    - reorderList(devicesList,devicesStatuses) #Se reordena la lista de los dispositivos para que se muestre en el orden pedido y se eliminan los datos innecesarios
    - jsontocsv(devicesList) -> Generamos un archivo csv con la información necesaria de los dispositivos


En dado caso de que ocurra un error al obtener la información de la API saldrá un mensaje en la consola
