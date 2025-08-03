from agents.ingest_agent import IngestAgent
from agents.insights_agent import InsightsAgent
from agents.followup_agent import FollowUpAgent
from core.memory import SharedMemory

def main():
    memory = SharedMemory()

    ingest = IngestAgent()
    df = ingest.run("data/sample.csv")
    memory.set("df", df)

    insights = InsightsAgent()
    md_report = insights.run(df)
    memory.set("report", md_report)

    print("\n📊 Data Insights Report:\n")
    print(md_report)

    followup = FollowUpAgent()
    followup.run(df)

if __name__ == "__main__":
    main()
