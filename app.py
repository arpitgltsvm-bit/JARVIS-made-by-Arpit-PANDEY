
from config import APP_NAME, VERSION
from Brain.Brain import think
from memory import remember, recall, forget
from Voice import listen

print("=" * 40)
print(f"Welcome to {APP_NAME}")
print(f"Version: {VERSION}")
print("=" * 40)

print("JARVIS: System started. I am listening.")

while True:

    try:
        user = listen()

        if not user:
            print("JARVIS: I didn't hear anything.")
            continue

        user = user.strip()
        command = user.lower()

        print("You:", user)

        # Exit command
        if command in ["exit", "exit jarvis", "stop jarvis"]:
            print("JARVIS: Goodbye!")
            break

        # Remember name
        elif command.startswith("my name is"):
            name = user[11:].strip()

            if name:
                remember("name", name)
                print(f"JARVIS: Nice to meet you, {name}!")
            else:
                print("JARVIS: Please tell me your name.")

        # Recall name
        elif command == "what is my name":
            name = recall("name")

            if name:
                print(f"JARVIS: Your name is {name}.")
            else:
                print("JARVIS: I don't know your name yet.")

        # Forget name
        elif command == "forget my name":
            if forget("name"):
                print("JARVIS: I have forgotten your name.")
            else:
                print("JARVIS: I don't have your name stored.")

        # AI response
        else:
            response = think(user)
            print("JARVIS:", response)

    except KeyboardInterrupt:
        print("\nJARVIS: Shutting down. Goodbye!")
        break

    except Exception as e:
        print("JARVIS Error:", e)
