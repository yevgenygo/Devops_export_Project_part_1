import requests
user_id=None
user_name=None
def post_user_rest(user_id,user_name):
    res = requests.post('http://127.0.0.1:5000/users/' + str(user_id), json={"user_name":user_name})
    res_data = res.json()
    return(res_data,res.status_code)

def get_user_rest(user_id):
    res = requests.get('http://127.0.0.1:5000/users/' + str(user_id))
    res_data = res.json()
    return (res_data['user_name'],res.status_code)