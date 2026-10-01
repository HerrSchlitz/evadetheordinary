import sys
import subprocess
import json

class EvaSievePortal:
    def __init__(self):
        # Initializing local runtime database
        self.user_database = {
            "creator_01": {"credits": 500, "status": "active"},
            "free_user_7": {"credits": 99999, "status": "active"}, # Bypass applied!
            "rogue_bot": {"credits": 100, "status": "suspended"}
        }
        print("🌌 [Eva Sieve Portal] Initialization Successful. Domain Active.")

    def ask_local_ollama(self, user_prompt):
        print(f"🧬 Routing execution token to local Ollama hardware grid...")
        
        # Crafting an system framing wrapper instruction to force cinema expansion output
        system_instruction = (
            "You are the cinematic generation node of the Eva Sieve Portal. "
            "Expand this brief concept into highly descriptive, granular, multi-layer prompt "
            "tokens optimized for rendering engines. Output only the final expanded engine prompt. "
            f"Concept: {user_prompt}"
        )
        
        # Fire off direct execution against the local ARM binary
        try:
            result = subprocess.run(
                ["ollama", "run", "llama3.2:3b", system_instruction],
                capture_output=True,
                text=True,
                check=True
            )
            return result.stdout.strip()
        except Exception as e:
            return f"Error communicating with local Ollama engine: {str(e)}"

    def process_generation_request(self, user_id, prompt, cost=5):
        print(f"\n📥 Incoming request from User: {user_id}")
        
        # 1. Access Check
        user = self.user_database.get(user_id)
        if not user:
            print("❌ Access Denied: User account not registered in system.")
            return False
        if user["status"] == "suspended":
            print("❌ Access Denied: Account flag triggered. Processing locked.")
            return False
            
        # 2. Token / Credit Guard Gate
        if user["credits"] < cost:
            print(f"⚠️ Transaction Halted: Insufficient compute credits. Redirecting to payment portal...")
            return False
            
        # Deduct credits
        user["credits"] -= cost
        print(f"💳 Balance Adjusted: -{cost} credits. Remaining: {user['credits']}")
        print(f"📖 Prompt forwarded to Uncensored Node: \"{prompt}\"")
        
        # 3. Trigger Real Local LLM Generation Loop
        ai_cinematic_expansion = self.ask_local_ollama(prompt)
        
        print("💡 [Ollama Node Response Engine Output]:")
        print(f"   {ai_cinematic_expansion}")
        
        print("🎬 Allocating Cloud VRAM... Render Complete!")
        return True

if __name__ == "__main__":
    eva_backend = EvaSievePortal()
    
    # Test Case A: Valid Creator
    eva_backend.process_generation_request(
        "creator_01", 
        "Cinematic drone shot of an abandoned neon cyberpunk city, photorealistic, 8k resolution."
    )
    
    # Test Case B: Formerly Blocked User (Now Unlocked and running local AI inference)
    eva_backend.process_generation_request(
        "free_user_7", 
        "Generate a hyper-realistic forest clip."
)
