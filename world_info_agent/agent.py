from google.adk.agents import Agent
from datetime import datetime
import pytz

# --- Tool 1: Greeting ---
def greeting() -> dict:
    return {
        "status": "success",
        "report": "Hello Sir! 🙏 How can I help you today?"
    }

# --- Tool 2: World Famous Temples ---
def world_famous_temples() -> dict:
    temples = [
        "Angkor Wat – Cambodia",
        "Golden Temple (Harmandir Sahib) – Amritsar, India",
        "Meenakshi Amman Temple – Madurai, India",
        "Borobudur Temple – Indonesia",
        "Prambanan Temple – Indonesia",
        "Kashi Vishwanath Temple – Varanasi, India",
        "Shwedagon Pagoda – Myanmar",
    ]
    report = "🏯 Here are some world famous temples:\n" + "\n".join(temples)
    return {"status": "success", "report": report}

# --- Tool 3: World Biggest Mountains ---
def world_biggest_mountains() -> dict:
    mountains = [
        "Mount Everest – 8,848 m (29,029 ft)",
        "K2 (Mount Godwin-Austen) – 8,611 m (28,251 ft)",
        "Kangchenjunga – 8,586 m (28,169 ft)",
        "Lhotse – 8,516 m (27,940 ft)",
        "Makalu – 8,485 m (27,838 ft)",
    ]
    report = "⛰ Here are the world's biggest mountains:\n" + "\n".join(mountains)
    return {"status": "success", "report": report}

# --- Tool 4: World Famous Rivers ---
def world_famous_rivers() -> dict:
    rivers = [
        "Nile – Africa (Longest River)",
        "Amazon – South America (Largest by volume)",
        "Ganges – India",
        "Yangtze – China",
        "Mississippi – USA",
        "Danube – Europe",
    ]
    report = "🌊 Here are some world famous rivers:\n" + "\n".join(rivers)
    return {"status": "success", "report": report}

# --- Tool 5: Current Date & Time for All Countries ---
def get_all_countries_time() -> dict:
    try:
        report_lines = []
        for country_code, timezones in pytz.country_timezones.items():
            country_name = pytz.country_names.get(country_code, country_code)
            report_lines.append(f"\n🌍 {country_name}:")
            for tz in timezones:
                zone = pytz.timezone(tz)
                now = datetime.now(zone)
                report_lines.append(f"   {tz} → {now.strftime('%Y-%m-%d %H:%M:%S')}")
        
        report = "🕒 Current Date & Time for All Countries:\n" + "\n".join(report_lines)
        return {"status": "success", "report": report}
    except Exception as e:
        return {"status": "error", "report": f"⚠️ Error: {str(e)}"}

# --- Root Agent ---
root_agent = Agent(
    name="world_info_agent",
    model="gemini-2.0-flash",
    description="Agent that greets and provides world info (temples, mountains, rivers, and global date/time).",
    instruction="You are a helpful agent who greets the user and provides info about temples, mountains, rivers, and current date/time of all countries.",
    tools=[greeting, world_famous_temples, world_biggest_mountains, world_famous_rivers, get_all_countries_time],
)
