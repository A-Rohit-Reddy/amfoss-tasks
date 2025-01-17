
from PySide6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton,QMessageBox,QVBoxLayout,QScrollArea
import requests
import os
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt

class SearchWindow(QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """
    def __init__(self):
        super().__init__()
        self.w = None   
        self.setFixedSize(850, 500)
        self.setWindowTitle("Pokemon Search")

        self.background_label = QLabel(self)
        self.background_label.setGeometry(self.rect())  # Cover the entire window

        # Load the image
        pixmap = QPixmap("/home/rohit-reddy/Poke-Search/assets/landing.png")
        if pixmap.isNull():
            print("Failed to load image.")
        else:
            # Scale the image to fit the window size
            scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio)
            self.background_label.setPixmap(scaled_pixmap)
            self.background_label.setScaledContents(True)
        
        def resizeEvent(self, event):
        # Whenever the window is resized, adjust the background image
            self.set_background_image()

        

        self.result_label=QLabel(self)
        self.result_label.setGeometry(450,150,300,400)
        self.result_label.setStyleSheet("color: white; font-size: 18px; font-weight: bold;")
        self.result_label.setText("")
        
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20) 
        self.textbox.setGeometry(50, 50, 280, 40)
        self.textbox.setStyleSheet("color: white; background-color: black; font-weight: bold;")

        # Inside __init__() of SearchWindow:

        self.image_label = QLabel(self)
        self.image_label.setGeometry(450, 5, 250, 200)  # Adjust the geometry as needed
        self.image_label.setScaledContents(True)


        label1 = QLabel("Enter the name", self)
        label1.setGeometry(50, 5, 600, 70)
        label1.setStyleSheet("color: white; font-weight: bold;")

        enter_button = QPushButton("Search", self)
        enter_button.setGeometry(50, 300, 160, 43)
        enter_button.clicked.connect(self.fetch_pokemon_data)
        
        capture_button = QPushButton("Capture", self)
        capture_button.setGeometry(50, 350, 160, 43)
        capture_button.clicked.connect(self.capture_pokemon_image)
        
        display_button = QPushButton("Display", self)
        display_button.setGeometry(50, 400, 160, 43)
        display_button.clicked.connect(self.display_captured_pokemon)
        

        self.current_image_url = None
        self.current_pokemon_name = None

        self.setStyleSheet("""
            QPushButton{
                background-color: light-grey;
                color: white;
                border: 1px solid #BA263E;
                font: bold 16px;
                text-align: center;
                border-radius: 10px;
                border-color: red;
            }
            QPushButton:hover {
                background-color: #BA263E;
                color: dark-grey;
            }
        """)

    ## TO-DO ##

    # 1 #
    # Fetch the data from from the API.
    # Display the name, official artwork (image), abilities, types and stats when queried with a Pokémon name.
    # Add the background provided in assets

    # 2 #
    # Capture the Pokémon i.e. download the image.

    # 3 #
    # Display all the Pokémon captured with their respective names using a new window.
    def fetch_pokemon_data(self):
        pokemon_name = self.textbox.text().strip().lower()
        if not pokemon_name:
            QMessageBox.warning(self, "Error", "Please enter a Pokémon name.")
            return

        try:
            response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}")
            print(response.status_code)
            data = response.json()

            # Extract Information
            self.current_pokemon_name = data["species"]["name"]
            self.current_image_url = data["sprites"]["other"]["official-artwork"]["front_default"]
            abilities = [ability["ability"]["name"] for ability in data["abilities"]]
            types = [t["type"]["name"] for t in data["types"]]
            stats = {stat["stat"]["name"]: stat["base_stat"] for stat in data["stats"]}


            # Display Data
            self.result_label.setText(
                f"Name: {self.current_pokemon_name.capitalize()}\n"
                f"Abilities: {', '.join(abilities)}\n"
                f"Types: {', '.join(types)}\n"
                f"Stats: \n {'\n'.join(f'{k}: {v}' for k, v in stats.items())}"
            )

            new_background_pixmap = QPixmap("/home/rohit-reddy/Poke-Search/assets/back.png")
            if not new_background_pixmap.isNull():
                self.background_label.setPixmap(new_background_pixmap)
                self.background_label.setScaledContents(True)
            else:
                print("Failed to load the new background image.")

            # Display Image
            pixmap = QPixmap()
            pixmap.loadFromData(requests.get(self.current_image_url).content)
            self.image_label.setPixmap(pixmap)

        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to fetch Pokémon data: {e}")

    def capture_pokemon_image(self):
        """
        Capture the Pokémon image by saving it locally.
        """
        if not self.current_image_url or not self.current_pokemon_name:
            QMessageBox.warning(self, "Error", "No Pokémon to capture. Search first.")
            return

        try:
            response = requests.get(self.current_image_url)
            response.raise_for_status()

            os.makedirs("captured_pokemon", exist_ok=True)
            file_path = os.path.join("captured_pokemon", f"{self.current_pokemon_name}.png")

            with open(file_path, "wb") as file:
                file.write(response.content)
            
            success_message = QMessageBox(self)
            success_message.setWindowTitle("Success")
            success_message.setText(f"Captured {self.current_pokemon_name.capitalize()}!")
            success_message.setStyleSheet("font-weight: bold; color: red;")
    
    # Load and scale the custom icon
            pixmap = QPixmap("/home/rohit-reddy/Poke-Search/assets/Poke_Ball_icon.png").scaled(64, 64, Qt.KeepAspectRatio, Qt.SmoothTransformation)
            success_message.setIconPixmap(pixmap)  # Set the scaled icon
            success_message.exec()
        
        except requests.exceptions.RequestException as e:
            QMessageBox.critical(self, "Error", f"Failed to download image: {e}")

    def display_captured_pokemon(self):
        captured_dir = "captured_pokemon"
        if not os.path.exists(captured_dir) or not os.listdir(captured_dir):
            QMessageBox.warning(self, "No Captured Pokémon", "No Pokémon have been captured yet.")
            return

    # Initialize a new window for displaying Pokémon
        self.captured_window = QWidget()
        self.captured_window.setWindowTitle("Captured Pokémon")
        self.captured_window.setFixedSize(400, 500)
        self.captured_window.setStyleSheet("color: white; font-weight: bold;")

        background_label = QLabel(self.captured_window)
        background_label.setGeometry(self.captured_window.rect())
        pixmap1 = QPixmap("/home/rohit-reddy/Poke-Search/assets/back.png")
        if pixmap1.isNull():
            print("Failed to load background image.")
        else:
        # Scale the image to cover the window
            scaled_pixmap1 = pixmap1.scaled(self.captured_window.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
            background_label.setPixmap(scaled_pixmap1)
            background_label.setScaledContents(True)

    # Set the background QLabel as the lowest layer
        background_label.lower()
    # Load Pokémon images and names
        self.captured_pokemon_files = [
            os.path.join(captured_dir, file) for file in os.listdir(captured_dir) if file.endswith(".png")
        ]
        self.current_pokemon_index = 0

    # Layout for navigation and display
        layout = QVBoxLayout()

        

    # Pokémon name label
        self.pokemon_name_label = QLabel(self.captured_window)
        self.pokemon_name_label.setStyleSheet("font-size: 20px; font-weight: bold; text-align: center;")
        self.pokemon_name_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.pokemon_name_label)

    # Pokémon image label
        self.pokemon_image_label = QLabel(self.captured_window)
        self.pokemon_image_label.setAlignment(Qt.AlignCenter)
        self.pokemon_image_label.setFixedSize(300, 300)
        layout.addWidget(self.pokemon_image_label)

    # Navigation buttons
        nav_layout = QVBoxLayout()
        self.back_button = QPushButton("Back", self.captured_window)
        self.back_button.clicked.connect(self.show_previous_pokemon)
        nav_layout.addWidget(self.back_button)
       

        self.next_button = QPushButton("Next", self.captured_window)
        self.next_button.clicked.connect(self.show_next_pokemon)
        nav_layout.addWidget(self.next_button)
        
        self.next_button.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                border: 1px solid white;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: red;
                color: black;
            }
        """)

        self.back_button.setStyleSheet("""
            QPushButton {
                background-color: black;
                color: white;
                border: 1px solid white;
                border-radius: 10px;
                font-weight: bold;
            }
            QPushButton:hover {
                background-color: red;
                color: black;
            }
        """)

        layout.addLayout(nav_layout)

        self.captured_window.setLayout(layout)
        self.update_pokemon_display()
        self.captured_window.show()

# Helper method to update the display based on the current index
    def update_pokemon_display(self):
        if not self.captured_pokemon_files:
            return

        current_file = self.captured_pokemon_files[self.current_pokemon_index]
        pokemon_name = os.path.splitext(os.path.basename(current_file))[0].capitalize()
        pixmap = QPixmap(current_file).scaled(300, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)

        self.pokemon_name_label.setText(pokemon_name)
        self.pokemon_image_label.setPixmap(pixmap)

    # Enable/Disable navigation buttons
        self.back_button.setEnabled(self.current_pokemon_index > 0)
        self.next_button.setEnabled(self.current_pokemon_index < len(self.captured_pokemon_files) - 1)

# Navigation methods
    def show_next_pokemon(self):
        if self.current_pokemon_index < len(self.captured_pokemon_files) - 1:
            self.current_pokemon_index += 1
            self.update_pokemon_display()

    def show_previous_pokemon(self):
        if self.current_pokemon_index > 0:
            self.current_pokemon_index -= 1
            self.update_pokemon_display()



if __name__ == "__main__":
    import sys
    from PySide6.QtWidgets import QApplication

    app = QApplication(sys.argv)
    window = SearchWindow()
    window.show()
    sys.exit(app.exec())
