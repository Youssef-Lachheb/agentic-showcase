import os
from dotenv import load_dotenv
load_dotenv()
from agent.classifier_agent import load_classifier_agent
from agent.solver_agent import load_solver_agent

def classify_query(agent, query):
    result = []
    agent.print_response(query, stream=False, capture=result)
    return result[0].strip().lower() if result else "arithmetic"

def main():
    print("📐 Math Tutor Duo (Agno Level 4 Agent)")
    print("Type a math question. Type 'exit' to quit.\n")

    classifier = load_classifier_agent()
    solver = load_solver_agent()

    while True:
        try:
            query = input("🧑 User: ").strip()
            if query.lower() in ("exit", "quit"):
                print("🫡 Exiting.")
                break

            topic = classify_query(classifier, query)
            print(f"🧠 Topic: {topic}")
            solver.print_response(query, stream=True)

        except KeyboardInterrupt:
            print("\n🛑 Interrupted.")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")

if __name__ == "__main__":
    main()
