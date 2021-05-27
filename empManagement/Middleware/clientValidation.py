from rest_framework import response
from ..models import Client
from rest_framework import status
import requests
from requests.exceptions import HTTPError
import json
from ..ClientDataCapture import ClientDataTrackingModels,ClientDataTrackingSerializers
def ClientValidation(clientname):
        client=Client.objects.filter(client_name=clientname)
        print(client)
        if client :
            return True
        else :
           return False

def fnClientDataCapture(Capture_id,client_name,action='list',client_system_name='',session_id='',method_name=''
                        ,status_code='',response_message='',row_count=0,) :    
  
    data={"Capture_id":Capture_id,"client_name":client_name,"action":action,"client_system_name":client_system_name,
          "session_id":session_id, "method_name":method_name,"status_code":status_code,
          "response_message":response_message,
          "row_count":row_count}
    # data={"client_name":client_name}
    json_data = json.dumps(data)
    # Capture_id=json_data.get('Capture_id')
    headers = {'Content-type':'application/json', 'Accept':'application/json'}
    print(json_data)
    # serializer = ClientDataTrackingSerializers(data=data)
    try:
        if Capture_id==0:
         res=requests.post('http://127.0.0.1:8000/ClientDataCapture/', data = json_data,headers=headers)
        else:
         res=requests.put('http://127.0.0.1:8000/ClientDataCapture/{}/'.format(Capture_id), data = json_data,headers=headers)
        response_data_json=(res.json())        
        u_response_data_json={'raise_for_status':res.status_code}
        u_response_data_json.update(response_data_json)
        # print(u_response_data_json.get('Capture_id'))
        return(u_response_data_json)
        # res.raise_for_status()

    except HTTPError as http_err:
        print(f'HTTP error occurred: {http_err}')  # Python 3.6
    except Exception as err:
        print(f'Other error occurred: {err}')  # Python 3.6
    else:
            print('Success!')
    # if serializer.is_valid():            
    #         serializer.save()
    #         return response.Response({'msg': 'Data Created'}, status=status.HTTP_201_CREATED)
    # return response.Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    # requests.post
 