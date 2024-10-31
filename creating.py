import os

# Create a directory for the model
model_dir = 'chatbot_model'
os.makedirs(model_dir, exist_ok=True)

# Save everything in the model directory
encoder.save(os.path.join(model_dir, 'encoder_model'))
decoder.save(os.path.join(model_dir, 'decoder_model'))

with open(os.path.join(model_dir, 'inp_lang.pickle'), 'wb') as handle:
    pickle.dump(inp_lang, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(os.path.join(model_dir, 'targ_lang.pickle'), 'wb') as handle:
    pickle.dump(targ_lang, handle, protocol=pickle.HIGHEST_PROTOCOL)

with open(os.path.join(model_dir, 'model_config.pickle'), 'wb') as handle:
    pickle.dump(model_config, handle, protocol=pickle.HIGHEST_PROTOCOL)

print(f"Model and configurations saved in '{model_dir}' directory!")