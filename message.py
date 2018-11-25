import steganography
from pip._vendor.distlib.compat import raw_input
from steganography.steganography import Steganography

def send_message():

    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = "C:\Users\shubham\Desktop\secret\output.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice]['chats'].append(new_chat)

    print("Your secret message image is ready!")
