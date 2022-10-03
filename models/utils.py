import os 
import logging
import tensorflow as tf
import absl.logging
from .words import *
from constants import ROOT_DIR, RESULT_DIR
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


def init_config(config, folder, npast, nfuture, ndelay, nfeatures, features,
                use_att = False, use_cm = False, cm = None, cm_trainable = False, use_constraint = False, constraint = None):
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
    config[W_INPUTATT][W_TRAINTHRESH] = constraint
    return config


def no_warning():
    os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' 
    tf.get_logger().setLevel(logging.ERROR)
    absl.logging.set_verbosity(absl.logging.ERROR) 


def cmd_attention_map(att, catt_f, catt_t, catt_tc):
    use_att = att or catt_f or catt_t or (catt_tc[0] == 'True')
    use_cm = catt_f or catt_t or (catt_tc[0] == 'True')
    cm_trainable = catt_t or (catt_tc[0] == 'True')
    use_constraint = (catt_tc[0] == 'True')
    constraint = float(catt_tc[1]) if catt_tc[1] is not None else None

    return use_att, use_cm, cm_trainable, use_constraint, constraint
