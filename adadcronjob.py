import requests




api1 = "https://adad-api-1.onrender.com/"


try:
    headers = {
            "Content-Type": "application/json"
        }
    resp = requests.get(api1, headers=headers)
    
    
    print(resp.content)
    
    
except Exception as e:
    print("error while calling the api",e)