import netmiko
from netmiko import ConnectHandler
from datetime import datetime
import os

# Configuration du périphérique (exemple Cisco)
device = {
    'device_type': 'cisco_ios',  # Peut être changé selon l'équipement (juniper, arista, etc.)
    'host': '192.168.1.1',  # Adresse IP du routeur/switch
    'username': 'admin',
    'password': 'password123',
    'secret': 'enable_password',  # Mot de passe enable si nécessaire
}

# Se connecter au périphérique
try:
    connection = ConnectHandler(**device)
    connection.enable()
    
    # Exécuter la commande pour obtenir la configuration
    config_output = connection.send_command('show running-config')
    
    # Fermer la connexion
    connection.disconnect()
    
    # Sauvegarder la configuration dans un fichier
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"backup_config_{device['host']}_{timestamp}.txt"
    
    with open(filename, "w") as file:
        file.write(config_output)
    
    print(f"Configuration sauvegardée dans {filename}")

except Exception as e:
    print(f"Erreur : {e}")
