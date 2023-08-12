import configparser

# Define the path to the config.conf file
config_file = "config.conf"

# Create a ConfigParser instance and read the config file
config = configparser.ConfigParser()
config.read(config_file)

# Access the parameters
param_1 = config.get("parameters", "FOLDER_PATH")

# Print the parameters
print("PARAMETER_1:", param_1)
