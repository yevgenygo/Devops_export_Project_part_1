import requests
import db_client
user_id = 40
user_name="yyy"
def post_user_rest():
    res = requests.post('http://127.0.0.1:5000/users/' + str(user_id), json={"user_name":user_name})
    res_data = res.json()
    return(res_data,res.status_code)

def get_user_rest():
    res = requests.get('http://127.0.0.1:5000/users/' + str(user_id))
    res_data = res.json()
    return (res_data['user_name'],res.status_code)

post_json, post_status= post_user_rest()
if (post_status == 200):
    user_name_from_get, get_status = get_user_rest()
    if user_name_from_get == user_name:
        print("Test passed successfully - GET REST method showed the same user name that was sent by POST REST METHOD")
        print("Status of get rest request" + str(get_status))
        print("Direct query for user name from DB: " + str(db_client.get_user_rest(user_id)))
    else:
        print("status of get rest request" + str(get_status))
else:
    print("status of get request:" +str(post_json))


