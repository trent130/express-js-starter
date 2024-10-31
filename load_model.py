# Load the models
from tensorflow import keras
loaded_encoder = keras.models.load_model('encoder_model')
loaded_decoder = keras.models.load_model('decoder_model')

# Load the tokenizers
with open('inp_lang.pickle', 'rb') as handle:
    loaded_inp_lang = pickle.load(handle)

with open('targ_lang.pickle', 'rb') as handle:
    loaded_targ_lang = pickle.load(handle)

# Load the configuration
with open('model_config.pickle', 'rb') as handle:
    loaded_config = pickle.load(handle)

# Extract the configurations
max_length_inp = loaded_config['max_length_inp']
max_length_targ = loaded_config['max_length_targ']
units = loaded_config['units']

print("Model and configurations loaded successfully!")