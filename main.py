import sys
import os
from llama_cpp import Llama
from colorama import init, Fore, Style

# --- 1. SETUP UI & PATHS ---
init(autoreset=True) 

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_logo():
    logo = f"""{Fore.GREEN}
      ________                                             
     /  _____/___________    _____   _____   ___________   
    /   \  __\_  __ \__  \  /     \ /     \_/ __ \_  __ \  
    \    \_\  \  | \// __ \|  Y Y  \  Y Y  \  ___/|  | \/  
     \______  /__|  (____  /__|_|  /__|_|  /\___  >__|     
            \/           \/      \/      \/     \/         
    {Fore.CYAN}      >>> CHAOS MODE | ANTI-DETECTOR V2 <<<
    {Style.RESET_ALL}"""
    print(logo)

# --- 2. LOAD QWEN MODEL ---
clear_screen()
print_logo()
print(f"{Fore.YELLOW}[SYSTEM] Loading Qwen-2.5-3B (High Variance Mode)...{Style.RESET_ALL}")

model_name = "models/qwen2.5-3b-instruct-q4_k_m.gguf"
model_path = resource_path(model_name)

if not os.path.exists(model_path):
    print(f"{Fore.RED}[ERROR] Model not found at: {model_path}{Style.RESET_ALL}")
    input("Press Enter to exit...")
    sys.exit()

# Qwen 3B fits easily on RTX 2050 (4GB VRAM)
llm = Llama(
    model_path=model_path,
    n_ctx=4096,      
    n_gpu_layers=-1, 
    verbose=False
)

# --- 3. PROCESSING FUNCTIONS ---

def get_multiline_input():
    print(f"\n{Fore.CYAN}" + "="*60)
    print(" PASTE TEXT BELOW (Type 'END' on new line to finish)")
    print("="*60 + f"{Style.RESET_ALL}")
    
    lines = []
    print(f"{Fore.GREEN}[USER] > {Style.RESET_ALL}", end="")
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == "END":
            break
        lines.append(line)
    return "\n".join(lines)

def humanize_chunk(text_chunk):
    # --- THE "CHAOS" PROMPT ---
    # We explicitly tell it to AVOID standard AI patterns.
    system_instruction = (
        "You are a ghostwriter for a senior researcher. Rewrite this text to bypass AI detection. "
        "Strict Guidelines:\n"
        "1. DO NOT use these words: 'delve', 'crucial', 'underscore', 'landscape', 'transformative', 'harness', 'leverage'.\n"
        "2. BREAK THE RHYTHM: Do not start sentences with 'Moreover', 'Furthermore', or 'In conclusion'.\n"
        "3. VOICE CHANGE: Switch unpredictably between active and passive voice.\n"
        "4. IMPERFECTION: Use conversational transitions like 'Basically,' or 'In simple terms,' to sound human.\n"
        "5. Keep the technical meaning accurate, but change the grammar structure entirely."
    )
    
    output = llm.create_chat_completion(
        messages=[
            {"role": "system", "content": system_instruction},
            {"role": "user", "content": f"Rewrite this to sound human:\n{text_chunk}"}
        ],
        # --- THE "HUMAN" SETTINGS ---
        temperature=1.0,      # MAX Randomness (Safe limit)
        top_k=40,             # Filters out the most "obvious" robotic words
        top_p=0.95,           # Nucleus sampling for variety
        repeat_penalty=1.15,  # Forces it to never repeat a phrase
        max_tokens=2000
    )
    return output['choices'][0]['message']['content']

def process_full_text(full_text):
    paragraphs = full_text.split('\n\n')
    cleaned_paragraphs = [p for p in paragraphs if p.strip()]
    full_result = []
    
    print(f"\n{Fore.YELLOW}[AI] Injecting variance into {len(cleaned_paragraphs)} blocks...{Style.RESET_ALL}")

    for i, p in enumerate(cleaned_paragraphs):
        print(f"{Fore.YELLOW}  >> Rewriting block {i+1}...{Style.RESET_ALL}")
        rewritten = humanize_chunk(p)
        full_result.append(rewritten)

    return "\n\n".join(full_result)

# --- 4. MAIN LOOP ---
if __name__ == "__main__":
    clear_screen()
    print_logo()
    
    while True:
        user_text = get_multiline_input()
        
        if not user_text.strip():
            continue
        if user_text.strip().upper() == "EXIT":
            break

        final_output = process_full_text(user_text)
        
        print(f"\n{Fore.MAGENTA}" + "#"*60)
        print(" HUMANIZED RESULT:")
        print("#"*60 + f"{Style.RESET_ALL}\n")
        print(final_output)
        print(f"\n{Fore.MAGENTA}" + "#"*60 + f"{Style.RESET_ALL}")
        
        choice = input(f"\n{Fore.CYAN}[SYSTEM] Press Enter to continue or type 'exit': {Style.RESET_ALL}")
        if choice.lower() == 'exit':
            break