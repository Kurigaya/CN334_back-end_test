from dotenv import load_dotenv
import requests
import os

class Connection:
    # Your Firebase Realtime Database URL
    def __init__(self) -> None:
        load_dotenv()
        self.firebase_url = os.environ.get("FIREBASE_KEY")
    # GET    
    def get_data(self, path):
        response = requests.get(self.firebase_url + path)
        if response.status_code == 200:
            data = response.json()
            return data
        else:
            print("Error:", response.text)
    # POST
    def store_data(self, path, json):
        response = requests.post(self.firebase_url + path, json=json)
        if response.status_code == 200:
            print("Data successfully sent to Firebase!")
        else:
            print("Error:", response.text)
    # PATCH
    def update_data(self, path, new_data):
        response = requests.patch(self.firebase_url + path, json=new_data)
        if response.status_code == 200:
            print("Data updated successfully!")
        else:
            print("Error:", response.text)
        return response.json()
    # Delete
    def delete_data(self, path):
        response = requests.delete(self.firebase_url + path)
        if response.status_code == 200:
            print("The Item Deleted Successfully!")
            return {"msg": "The Item Deleted Successfully!",
                    "response": response.json()}
        else:
            print("Error deleting old key:", response.text)

firebase = Connection()

# Example
# name = 'gege'
# data = {
#     'name': name,
#     'played_time': 0,
#     'tel': '0877777777',
#     'score': 0
# }
# path = f'users_score/{name}.json' # user_ref
# user_number = 1
# firebase.store_data(path, data)
# firebase.get_data(path)
# firebase.update_data(path, data)
# firebase.update_played(path)