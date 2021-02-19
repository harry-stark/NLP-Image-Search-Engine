from .pipeline import pipeline
from .models import img_encoder,text_enc

import tensorflow as tf
import numpy as np
def generator(way:str):
 image_encoder=img_encoder()
 imgfil,prep_img=pipeline(way)
 vis_embedding=tf.math.l2_normalize(image_encoder(np.array(prep_img)),axis=1)
 return vis_embedding,imgfil

def querygen(query:list):
    text_enco=text_enc()
    quem=tf.math.l2_normalize(text_enco(tf.convert_to_tensor(query)),axis=1)
    return quem


def find_match(imgem,queryem,k:int):
    
    #dot_similarity =tf.matmul(queryem,imgem,transpose_b=True)
    dot_similarity =np.matmul(np.array(queryem),np.array(imgem).T)
    results = tf.math.top_k(dot_similarity,k).indices.numpy()
    return results[0]
