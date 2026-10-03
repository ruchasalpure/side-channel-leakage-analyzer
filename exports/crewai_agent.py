from crewai import Agent

side_channel_leakage_analyzer = Agent(
    role="Side Channel Leakage Analyzer",
    goal="Deliver high-precision autonomous Side Channel Leakage Analyzer operations",
    backstory="Engineered under OpenGAP governance standards.",
    verbose=True,
    allow_delegation=False
)
