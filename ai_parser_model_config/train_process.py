import rasa

model_directory = rasa.train(domain="D:/Projects/H12_Helper_3.0/ai_parser_model_config/domain.yml", config="D:/Projects/H12_Helper_3.0/ai_parser_model_config/config.yml",
                             training_files="D:/Projects/H12_Helper_3.0/ai_parser_model_config/train_data.yml", output="D:/Projects/H12_Helper_3.0/your_simple_helper/main/models")
