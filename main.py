from ui.app import App
from logic.calculator import Calculator
from event_connector import EventConnector


def main():
    app = App()
    calculator = Calculator()
    event_connector = EventConnector(app, calculator)
    event_connector.connect_events()
    app.run()


if __name__ == '__main__':
    main()
