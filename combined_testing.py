import db_client
from Rest_Methods import get_user_rest, post_user_rest
from frontend_testing import frontend_test
user_id = 84
user_name="yyy"

post_json, post_status= post_user_rest(user_id,user_name)
if (post_status == 200):
    user_name_from_get, get_status = get_user_rest(user_id)
    if user_name_from_get == user_name:
        print("Test passed successfully - GET REST method showed the same user name that was sent by POST REST METHOD")
        print("Status of get rest request" + str(get_status))
        print("Direct query for user name from DB: " + str(db_client.get_user(user_id)))
        user_name_sel = frontend_test(str(user_id))
        print(user_name_sel)
    else:
        print("status of get rest request" + str(get_status))
else:
    print("status of post rest request:" +str(post_json))

