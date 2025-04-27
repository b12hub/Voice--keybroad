import speech_recognition as sr
import keyboard
from typing import Dict, List, Set

class VoiceCommandEngine:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.active = True
        self.command_history: List[str] = []

        self.key_mappings: Dict[str, str] = {

            'exit': '__exit__', 'stop': '__pause__', 'start': '__resume__',

            'escape': 'esc', 'enter': 'enter', 'space': 'space',
            'tab-space': 'tab', 'control': 'ctrl', 'shift': 'shift', 'alt': 'alt',
            'backspace': 'backspace', 'caps lock': 'caps lock', 'windows': 'win',
            'up': 'up', 'next': 'down', 'left': 'left', 'right': 'right',
            'delete': 'delete', 'insert': 'insert', 'home': 'home', 'end': 'end',

            'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4',
            'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9',
            'period': '.', 'comma': ',', 'question': '?', 'exclamation': '!',
            'colon': ':', 'semicolon': ';', 'slash': '/', 'backslash': '\\',
            'quote': "'", 'dollar': '$', 'percent': '%', 'ampersand': '&'
        }

        self.aliases: Dict[str, str] = {
            'close': 'alt+f4', 'save': 'ctrl+s', 'copy': 'ctrl+c',
            'paste': 'ctrl+v', 'undo': 'ctrl+z', 'redo': 'ctrl+y',
            'refresh': 'f5', 'menu': 'shift+f10', 'desktop': 'win+d',
            'task manager': 'ctrl+shift+esc','change language':'win+space'
        }

        self.allowed_commands: Set[str] = {
            'exit', 'stop', 'start', 'help', 'history'
        }

    def handle_special_commands(self, command: str) -> bool:
        command = command.lower()

        if command == '__exit__':
            print("Shutting down voice command engine...")
            exit(0)

        if command == '__pause__':
            self.active = False
            print("Paused - Say 'start' to resume")
            return True

        if command == '__resume__':
            self.active = True
            print("Resuming voice commands...")
            return True

        return False

    def process_command(self, command: str):
        self.command_history.append(command)
        print(f"\nCommand received: {command}")

        lower_command = command.lower()

        if lower_command in self.aliases:
            return self.press_keys(self.aliases[lower_command])

        if self.handle_special_commands(lower_command):
            return

        if not self.active:
            print("System paused. Say 'start' to activate.")
            return

        keys = self.convert_to_key_sequence(lower_command)
        if keys:
            self.press_keys("+".join(keys))
        else:
            print(f"Unrecognized command: {command}")

    def convert_to_key_sequence(self, command: str) -> List[str]:
        keys = []
        words = command.split()
        skip_next = False

        for i, word in enumerate(words):
            if skip_next:
                skip_next = False
                continue

            if word == 'f' and i < len(words) - 1:
                next_word = words[i + 1]
                number = self.key_mappings.get(next_word, next_word)
                if number.isdigit() and 1 <= int(number) <= 12:
                    keys.append(f'f{number}')
                    skip_next = True
                    continue

            if word in ['symbol', 'press'] and i < len(words) - 1:
                symbol = words[i + 1]
                keys.extend(self.handle_symbol(symbol))
                skip_next = True
                continue

            mapped = self.key_mappings.get(word, word)
            if len(mapped) == 1 and mapped.isalnum():
                keys.append(mapped)
            elif mapped in self.key_mappings.values():
                keys.append(mapped)

        return keys

    def handle_symbol(self, symbol: str) -> List[str]:
        symbol_map = {
            '!': ['shift', '1'], '@': ['shift', '2'],
            '#': ['shift', '3'], '$': ['shift', '4'],
            '%': ['shift', '5'], '^': ['shift', '6'],
            '&': ['shift', '7'], '*': ['shift', '8'],
            '(': ['shift', '9'], ')': ['shift', '0'],
            '_': ['shift', '-'], '+': ['shift', '='],
            '{': ['shift', '['], '}': ['shift', ']'],
            ':': ['shift', ';'], '"': ['shift', "'"],
            '<': ['shift', ','], '>': ['shift', '.'],
            '?': ['shift', '/'], '|': ['shift', '\\']
        }
        return symbol_map.get(symbol.lower(), [symbol])

    def press_keys(self, combination: str):
        try:
            keyboard.press_and_release(combination)
            print(f"Executed: {combination.replace('+', ' + ')}")
        except ValueError as e:
            print(f"Failed: {combination} - {str(e)}")

    def listen_and_process(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source, duration=1)
            print("Voice command engine ready. Say 'help' for options.")

        while True:
            try:
                with self.microphone as source:
                    print("\nListening...")
                    audio = self.recognizer.listen(
                        source,
                        timeout=5,
                        phrase_time_limit=3
                    )

                text = self.recognizer.recognize_google(audio).lower()
                self.process_command(text)

            except sr.WaitTimeoutError:
                print("No command detected")
            except sr.UnknownValueError:
                print("Couldn't understand speech")
            except sr.RequestError as e:
                print(f"Service Error: {e}")
            except Exception as e:
                print(f"System Error: {e}")


if __name__ == "__main__":
    engine = VoiceCommandEngine()
    engine.listen_and_process()