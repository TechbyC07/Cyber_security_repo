from stegano import lsb

#secret = lsb.hide("Meme.jpg", "SOS, I need your help, call emergency services")
#secret.save("Stegano_img.png")

secret_message = lsb.reveal("Stegano_img.png")
print(secret_message)