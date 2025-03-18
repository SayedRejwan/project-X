import sys
import random
from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QListWidget

class FakeAdminPanel(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()

        self.label = QLabel("Admin Panel - Demo")
        layout.addWidget(self.label)

        self.bookings_list = QListWidget()
        self.refresh_bookings()
        layout.addWidget(self.bookings_list)

        self.viewBookingsBtn = QPushButton("Refresh Bookings")
        self.viewBookingsBtn.clicked.connect(self.refresh_bookings)
        layout.addWidget(self.viewBookingsBtn)

        self.setLayout(layout)
        self.setWindowTitle("Salon Admin Panel - Fake Data")
        self.resize(400, 300)

    def refresh_bookings(self):
        self.bookings_list.clear()
        fake_bookings = [
            "Alice - Haircut - 20th March",
            "Bob - Massage - 22nd March",
            "Charlie - Facial - 25th March",
            "Diana - Haircut - 26th March"
        ]
        random.shuffle(fake_bookings)
        for booking in fake_bookings:
            self.bookings_list.addItem(booking)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    admin_panel = FakeAdminPanel()
    admin_panel.show()
    sys.exit(app.exec())
