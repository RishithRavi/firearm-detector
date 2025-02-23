import tensorflow_hub as hub
import tensorflow as tf

# Load model from TensorFlow Hub
yamnet_model = hub.load("https://tfhub.dev/google/yamnet/1")

# Save it locally
yamnet_model_path = "yamnet_saved"
tf.saved_model.save(yamnet_model, yamnet_model_path)

print(f"✅ YAMNet model saved at: {yamnet_model_path}")
