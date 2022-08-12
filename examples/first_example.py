from whats_api import Client, User

client = Client(user_dir="C:\\Users\\neluc\\AppData\\Local\\Google\\Chrome\\User Data\\Default")
user = User(client)

name = user.get_name()
status = user.get_status()

message = f"Hello, this is {name}.\n" \
          f"Have you seen my status - ({status})?"

client.message_send(phone_number="+79266715859", message=message)
