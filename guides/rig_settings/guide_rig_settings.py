from os.path import dirname, join
from .. rig_settings.guide_rig_settings_actions import *

images_dir = join(dirname(__file__), 'images')

GUIDE_STEPS_SETTINGS = (
    #Shoulder Automatic Movement
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': SETTINGS_Shoulder_Movement
    },
    #Torso Rotation
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': SETTINGS_Torso_Rotation
    },
    #Neck Rotation
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': SETTINGS_Neck_Rotation
    },
    #Torso Inverted Rotation
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': SETTINGS_Torso_Inv_Rotation
    },
    #Torso Stretching Curve
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': SETTINGS_Torso_Stretching
    },
    #Torso Pelvis Compensation
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': SETTINGS_Pelvis_Compensation
    },
    #Torso Pelvis Compensation
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': SETTINGS_Foot_Roll
    },
    #Volume Variation
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': SETTINGS_Volume_Variation
    },
    #Feet Floor
    {
        'imagen': 'DT_Finish_A.jpg',
        'titulo': {
            'EN': 'Define Character Body Objects',
            'ES': 'Paso 1'
            },
        'texto': {
            'EN': "Select all the objects that conform the character's body and press the Set Body Objects button",
            'ES': 'Si el personaje es simétrico, activa la opción X-Mirror'
            },
        'accion': SETTINGS_Feet_Floor
    },
)



