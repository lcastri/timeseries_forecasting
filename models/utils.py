import os 
import logging
import tensorflow as tf
import absl.logging
from .words import *
from constants import ROOT_DIR
from enum import Enum

class Models(Enum):
    sIAED = "sIAED"
    mIAED = "mIAED"
    sT2V = "sT2V" 
    mT2V = "mT2V" 


MODELS = {
    Models.sIAED.value : "Single-output Input Attention Encoder Decoder",
    Models.mIAED.value : "Multi-output Input Attention Encoder Decoder",
    Models.sT2V.value : "Single-output Time2Vector LSTM",
    Models.mT2V.value : "Multi-output Time2Vector LSTM"
}


def init_config(config, folder, npast, nfuture, ndelay, nfeatures, features, use_att = False, use_cm = False, cm = None, cm_trainable = False, use_constraint = False):
    config[W_SETTINGS][W_FOLDER] = folder
    config[W_SETTINGS][W_NPAST] = npast
    config[W_SETTINGS][W_NFUTURE] = nfuture
    config[W_SETTINGS][W_NDELAY] = ndelay
    config[W_SETTINGS][W_NFEATURES] = nfeatures
    config[W_SETTINGS][W_FEATURES] = features
    config[W_SETTINGS][W_USEATT] = use_att
    config[W_INPUTATT][W_USECAUSAL] = use_cm
    config[W_INPUTATT][W_CMATRIX] = cm
    config[W_INPUTATT][W_CTRAINABLE] = cm_trainable
    config[W_INPUTATT][W_USECONSTRAINT] = use_constraint
    return config


def no_warning():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
    tf.get_logger().setLevel(logging.ERROR)
    absl.logging.set_verbosity(absl.logging.ERROR) 



def create_dir(folder):
    model_dir = ROOT_DIR + "/" + folder
    plot_dir = ROOT_DIR + "/" + folder + "/plots"
    pred_dir = ROOT_DIR + "/" + folder + "/predictions"
    if not os.path.exists(model_dir):
        os.makedirs(model_dir)
    if not os.path.exists(plot_dir):
        os.makedirs(plot_dir)
    if not os.path.exists(pred_dir):
        os.makedirs(pred_dir)
    return model_dir, plot_dir, pred_dir