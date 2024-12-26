import asyncio
import telethon
import glob
from pathlib import Path
from Zaid.utils import load_plugins
import logging
from Zaid import Zaid, client, ASSISTANT_ID
from Zaid.plugins.autoleave import leave_from_inactive_call

# Configure logging
logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.INFO)

# Load plugins dynamically
path = "Zaid/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name)

# Bot initialization
async def start_bot():
    print("[INFO]: LOADING ASSISTANT DETAILS")
    botme = await client.get_me()
    botid = botme.id  # Updated to avoid deprecated Telethon method
    print(f"[INFO]: ASSISTANT ID {botid}")
    await leave_from_inactive_call()  # Await the task directly
    print("[INFO]: SUCCESSFULLY STARTED BOT!")
    print("[INFO]: VISIT @TheUpdatesChannel")
    await Zaid.run_until_disconnected()  # Ensure the bot keeps running

# Main entry point
if __name__ == "__main__":
    asyncio.run(start_bot())  # Use asyncio.run for cleaner event loop handling
