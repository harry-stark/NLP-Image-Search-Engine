import tensorflow as tf
from tensorflow import keras
import tensorflow_addons as tfa
import tensorflow_hub as hub
import tensorflow_text

def text_enc():
   
   return keras.models.load_model("engine/models/text_encoder")


def img_encoder():
    return keras.models.load_model("engine/models/image_encoder")
