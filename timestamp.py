from datetime import datetime

# Create a timestamped directory
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
model_dir = f'chatbot_model_{timestamp}'
os.makedirs(model_dir, exist_ok=True)

# Save everything with timestamp
encoder.save(os.path.join(model_dir, 'encoder_model'))
decoder.save(os.path.join(model_dir, 'decoder_model'))

# Save additional metadata
metadata = {
    'timestamp': timestamp,
    'max_length_inp': max_length_inp,
    'max_length_targ': max_length_targ,
    'units': units,
    'training_time': 'your_training_time',
    'performance_metrics': {
        'accuracy': 'your_accuracy',
        'loss': 'your_loss'
    }
}

with open(os.path.join(model_dir, 'metadata.pickle'), 'wb') as handle:
    pickle.dump(metadata, handle, protocol=pickle.HIGHEST_PROTOCOL)

print(f"Model saved with timestamp {timestamp}")
