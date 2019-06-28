!pip install pyTelegramBotAPI
!pip install python-telegram-bot


#print(TOKEN) #

import model.py 					# to import the neural network model
import telegram_bot_config.py 		# to import the Token for the bot
import telebot
import requests
import urllib.request
from PIL import Image
from google.colab.patches import cv2_imshow
import urllib
import cv2
import numpy as np
from io import BytesIO

base_dl_url = "https://api.telegram.org/file/bot{}/{}"

uploding_img = False
uploding_style = False

def download_photo(url):
    url_response = urllib.request.urlopen(url)
    img_array = np.array(bytearray(url_response.read()), dtype=np.uint8)
    img = cv2.imdecode(img_array, -1)
    return(img)
  
  
style_img_url = "https://raw.githubusercontent.com/jcjohnson/neural-style/master/examples/inputs/starry_night_google.jpg"
style_img = image_loader_url(style_img_url)

content_img_url = "https://ichef.bbci.co.uk/news/800/cpsprodpb/10CB5/production/_104398786_b8f788b8-5293-46c2-87db-91d9b7b0530c.jpg"
content_img = image_loader_url(content_img_url)

st1_url = "https://raw.githubusercontent.com/jcjohnson/neural-style/master/examples/inputs/starry_night_google.jpg"
st2_url = 'https://i.redd.it/71p6ffhdcj531.jpg'
st3_url = 'https://i.stack.imgur.com/UYbLT.png'

def show_img(img):
    cv2_imshow(img)
    

def change_to_byte_stream(image):    
    image = image.cpu().clone()   
    image = image.squeeze(0)   
    image = unloader(image)
    image=Image.fromarray(np.array(image)[:,:,[2,1,0]])
    output_stream = BytesIO()
    image.save(output_stream, format='PNG')
    output_stream.seek(0)
    return output_stream
    
    
def apply_style_transfer(content_img, style_img):
  
  input_img = content_img.clone()
  output = run_style_transfer(cnn, cnn_normalization_mean, cnn_normalization_std,content_img, style_img, input_img)

  output_stream = change_to_byte_stream(output)
  return output_stream
  #print(output_stream)
  #image=bytearray(image)
  

'''


'''

def send_message(bot,chat_id, text):
    bot.send_message(chat_id, text)


    
    
    
    
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(func=lambda message:(message.content_type=='text' and (message.text.lower()=='hi' or message.text.lower()=='hello')))
def echo_all(message):
    chat_id = message.chat.id
    bot.reply_to(message, message.text+" "+message.from_user.first_name+" "+message.from_user.last_name+'!'\
                "\nUse the commands /start or /help to get more info about me:).")


@bot.message_handler(commands=['start'])
def send_welcome(message):
    global uploding_style, uploding_img
    uploding_style = False
    uploding_img = False
    chat_id = message.chat.id
    bot.send_message(chat_id, "This Bot applies a style transfer algorithm using neural network."\
                 "\n\nYou can use the following commands:"\
                 "\n\n1-/help: shows the help docs."\
                 "\n2-/sendphoto: to send the photo that you want to apply style changing to. \ndefault:https://ichef.bbci.co.uk/news/800/cpsprodpb/10CB5/production/_104398786_b8f788b8-5293-46c2-87db-91d9b7b0530c.jpg"\
                 "\n\n3-/sendstyle: to upload your own style photo. \ndefault:https://raw.githubusercontent.com/jcjohnson/neural-style/master/examples/inputs/starry_night_google.jpg"\
                 "\n\n4-/applystyletrans: to start the style transfer process."\
                 "\n\n5-/showstyles: to show different available styles."\
                 "\n\n6-/style1: to choose the first style."\
                 "\n\n6-/style2: to choose the second style."\
                 "\n\n6-/style3: to choose the third style.")

    
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "This Bot applies a style transfer algorithm using neural network."\
                 "\n\nYou can use the following commands:"\
                 "\n\n1-/help: shows the help docs."\
                 "\n2-/sendphoto: to send the photo that you want to apply style changing to. \n'default:https://ichef.bbci.co.uk/news/800/cpsprodpb/10CB5/production/_104398786_b8f788b8-5293-46c2-87db-91d9b7b0530c.jpg'"\
                 "\n\n3-/sendstyle:to upload your own style photo. \n'default:https://raw.githubusercontent.com/jcjohnson/neural-style/master/examples/inputs/starry_night_google.jpg'"\
                 "\n\n4-/applystyletrans: to start the style transfer process."\
                 "\n\n5-/showstyles: to show different available styles."\
                 "\n\n6-/style1: to choose the first style."\
                 "\n\n6-/style2: to choose the second style."\
                 "\n\n6-/style3: to choose the third style."\
                 "\n\n by default there is already a style image and content image.. if you call the command "\
                 "/applystyletrans without uploading photos the algorithm will be applied on the default photos."\
                 "\n\nIf you want to chage the content photo use the /sendphoto command."\
                 "\nIf you want to change the style photo use the /sendstyle command."\
                 "\nWhen you are ready use /applystyletrans to apply the algorithm on the last uploaded photos.")
        
    
    
@bot.message_handler(commands=['showstyles'])
def show_styles(message):
    
    chat_id = message.chat.id
    bot.send_message(chat_id, "you can use one of the following styles")
    
    #st4_url = 'https://juliacomputing.com/assets/img/style/lily.jpg'
    bot.send_message(chat_id, "you can use this style by using /style1")
    img = image_loader_url(st1_url)
    img = change_to_byte_stream(img)
    bot.send_photo(chat_id, img)
    
    bot.send_message(chat_id, "you can use this style by using /style2")
    img = image_loader_url(st2_url)
    img = change_to_byte_stream(img)
    bot.send_photo(chat_id, img)
    
    bot.send_message(chat_id, "you can use this style by using /style3")
    img = image_loader_url(st3_url)
    img = change_to_byte_stream(img)
    bot.send_photo(chat_id, img)
    
    '''
    bot.send_message(chat_id, "you can use this style by using style4")
    img = image_loader_url(st4_url)
    img = change_to_byte_stream(img)
    bot.send_photo(chat_id, img)
    '''
    

@bot.message_handler(commands=['style1'])
def select_style1(message):  
    global style_img
    chat_id = message.chat.id
    style_img = image_loader_url(st1_url)
    out = change_to_byte_stream(style_img)
    bot.send_message(chat_id, "The style image is selected.")
    bot.send_photo(chat_id, out)
    
    
@bot.message_handler(commands=['style2'])
def select_style1(message):
    global style_img
    chat_id = message.chat.id
    style_img = image_loader_url(st2_url)
    out = change_to_byte_stream(style_img)
    bot.send_message(chat_id, "The style image is selected.")
    bot.send_photo(chat_id, out)
    
    
@bot.message_handler(commands=['style3'])
def select_style1(message):    
    global style_img
    chat_id = message.chat.id
    style_img = image_loader_url(st3_url)
    out = change_to_byte_stream(style_img)
    bot.send_message(chat_id, "The style image is selected.")
    bot.send_photo(chat_id, out)
    
    
    
@bot.message_handler(commands=['sendphoto'])
def send_img(message):
    global uploding_style, uploding_img
    chat_id = message.chat.id
    uploding_style = False
    uploding_img = True
    bot.send_message(chat_id, "waiting for the content image:)")

@bot.message_handler(commands=['sendstyle'])
def send_style(message):
    global uploding_style, uploding_img
    chat_id = message.chat.id
    uploding_style = True
    uploding_img = False
    bot.send_message(chat_id, "waiting for the style image:)")

    
@bot.message_handler(commands=['applystyletrans'])
def apply_style_trans(message):
    global content_img, style_img
    chat_id = message.chat.id
    send_message(bot, chat_id, "the style transfer will start.. \nthis may takes about 15 seconds.")
    img = apply_style_transfer(content_img, style_img)
    bot.send_photo(chat_id, img)
    

  

@bot.message_handler(content_types=['photo'])
def handle_style(message):
    global content_img, style_img, uploding_style, uploding_img
    if (uploding_style):
      file_id = message.photo[-1].file_id
      chat_id = message.chat.id
      file_info= bot.get_file(file_id)

      file = requests.get(base_dl_url.format(TOKEN, file_info.file_path))
      #print(file_info)
      file_path=file_info.file_path

      photo_url = 'https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_path)
      #print(photo_url)
      
      style_img = image_loader_url(photo_url)

      send_message(bot, chat_id, "the style photo is uploaded.")
      uploding_style = False
    if(uploding_img):
      uploding_img = False
  
      #print("got photo from chat_id:{}, User:{}".format(message.chat.id,message.chat.username))
      file_id = message.photo[-1].file_id
      chat_id = message.chat.id
      file_info= bot.get_file(file_id)

      file = requests.get('https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN, file_info.file_path))
      #print(file_info)
      file_path=file_info.file_path
      photo_url = 'https://api.telegram.org/file/bot{0}/{1}'.format(TOKEN,file_path)
      #print(photo_url)
      
      content_img = image_loader_url(photo_url)
      send_message(bot, chat_id, "the content photo is uploaded.")
      
  


bot.polling()

