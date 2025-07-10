#!/usr/bin/env python3
import os, sys, readline, importlib.util

PLUGIN_DIR = os.path.expanduser("~/.boomchainsh/plugins")
plugins = {}

def load_plugins():
    plugins.clear()
    if not os.path.isdir(PLUGIN_DIR):
        os.makedirs(PLUGIN_DIR)
    for filename in os.listdir(PLUGIN_DIR):
        if filename.endswith(".py"):
            name = filename[:-3]
            path = os.path.join(PLUGIN_DIR, filename)
            spec = importlib.util.spec_from_file_location(name, path)
            mod = importlib.util.module_from_spec(spec)
            try:
                spec.loader.exec_module(mod)
                plugins[name] = mod
            except Exception as e:
                print(f"[Plugin Error] {name}: {e}")

def completer(text, state):
    options = [c for c in list(plugins) + ["help", "exit", "clear", "plugin reload"] if c.startswith(text)]
    return options[state] if state < len(options) else None

def run_command(cmd):
    if cmd == "help":
        print("Core: help, exit, clear, plugin reload")
        print("Plugins:", ', '.join(plugins))
    elif cmd == "exit":
        print("Goodbye from BoomchainSH."); sys.exit(0)
    elif cmd == "clear":
        os.system("clear")
    elif cmd == "plugin reload":
        load_plugins()
        print("🔄 Reloaded")
    elif cmd in plugins:
        try: plugins[cmd].run()
        except Exception as e: print(f"[Error] {e}")
    else:
        print(f"❓ Unknown command: {cmd}")

def main():
    readline.parse_and_bind("tab: complete")
    readline.set_completer(completer)
    load_plugins()
    print("🔗 BoomchainSH v0.5 — Remote Plugin Install, Secrets, Autocomplete")
    print("Type 'help' or try: plugin reload")
    while True:
        try: run_command(input("🔗 boomchainsh> ").strip())
        except (KeyboardInterrupt, EOFError): break

if __name__ == "__main__":
    main()
