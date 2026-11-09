# evadetheordinary

# 🌌 evadetheordinary (EvaSievePortal) 🌌

A custom, lightweight Python backend architecture designed to operate entirely on local Android hardware via Termux. The system acts as an automated token gateway and optimization node—taking simple user inputs and dynamically expanding them into granular, multi-layered, cinematic prompt scripts via locally hosted LLMs.

## 🕵️‍♂️ The Backstory: A Mysterious Discovery

To be completely honest, **I have absolutely no active memory of generating, writing, creating or using this script. Doubt that i was hacked so someone else could give credit to me for their work, especially because it took me over 3 hours just to login to Github yesterday to publish my other repo (forgot that I had a new s23ultra and had set up this account using a passkey on my old phone. And they said to just toss out my old device because i replaced it with a undamaged model. Look at me now, 🤑 fresh repo who dis?)**

*   **The Discovery:** While auditing my GitHub account, I stumbled upon this repository completely out of nowhere. 
*   **The Authenticity Check:** Confused about where it came from, I ran a deep code audit across public code repositories and open web forums. The results came back **100% authentic**. There are zero copies, stolen templates, or duplicate blocks anywhere on the internet. This is completely original work written directly on my device.
*   **The Hobby Reality Check:** i am struggling to believe I am capable of engineering a structured Python class that interfaces with low-level Android hardware APIs— don't recall a single minute of it—is the ultimate proof that taking up coding as a hobby to help stay away from the pub is working as well as a doorbell on a submarine. Anyway, welcome to my journey of self taught coding and software development, hope you enjoy the ride 😉

## ⚙️ Core Mechanics & Architecture

The script handles local prompt processing using a modular `EvaSievePortal` architecture:

1.  **Local Inference Hook:** Connects directly via a terminal subprocess to a local `llama3.2:3b` model hosted through an offline Ollama hardware grid.
2.  **Cinematic Prompt Expansion:** Intercepts short concepts and wraps them in specialized system prompt directives, forcing the model to generate hyper-descriptive, multi-layered rendering tokens optimized for visual AI generators.
3.  **Local Credit/Gate Guard:** Simulates an internal runtime database (`user_database`) tracking user accounts, monitoring credit balances, and handling runtime execution locks for suspended accounts. Includes a hardcoded developer access bypass key (`free_user_7`).
4.  **Hardware API Triggers (Termux-API):** Upon a successful inference cycle, the script reaches out of the terminal environment and interfaces with the physical phone hardware, executing native Android vibration hooks (`termux-vibrate`) and pushing custom audio status banners (`termux-notification`).

## 🛠️ Required External Applications & Setup

To execute this script successfully on Android hardware, the local environment requires the following applications to be running and configured alongside Termux:

1. **Ollama Server:** The host machine must have the local `ollama` service installed, active, and the model downloaded via:
   ```bash
   ollama pull llama3.2:3b
   ```
2. **Termux:API Android App:** The standalone [Termux:API application](https://github.com) must be installed on the device to expose native hardware hooks.
3. **Termux:API Package:** The command-line wrappers must be installed inside the terminal environment:
   ```bash
   pkg install termux-api
   ```

---
*Built entirely inside Termux on a s23ultra mobile. Alleged and wild claims of Maintained by [HerrSchlitz](https://github.com).*

***
💡 *Note: The documentation structure, layout optimization, and codebase authenticity verification tests for this repository were co-authored and executed with AI assistance. I genuinely have no recollection of creating this, why and what i used it for. TBH, I wouldn't be surprised if AI wrote the code as well as the README.me. Why does bourbon have to be so good 😅*

***
⚠️ \* *Warning: The current shell interpolation implementation inside `os.system` for `termux-notification` passes the raw prompt directly into the command string. If a user inputs a prompt containing double quotes (`"`), it will break the string escaping bounds and likely cause a script crash or execution failure. A future patch utilizing `subprocess.run()` array arguments will be added to sanitise the inputs once i have time and access to set up the extra steps, added note as warning and so you can clone and edit yourself if wanted 😘 .*

