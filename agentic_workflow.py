
# Simple Agentic Workflow (Raw Python)
# Design patterns used:
# 1. Planning
# 2. Tool Use
# 3. Reflection
# 4. Multi-agent style task separation

def planner(task):
    return ["Understand task", "Generate answer", "Review answer"]

def tool_use(text):
    # Example tool function
    return text.upper()

def worker(task):
    processed = tool_use(task)
    return f"Processed Result: {processed}"

def reflection(output):
    if len(output) < 10:
        return output + " [Reviewed]"
    return output

def run_agent(task):
    plan = planner(task)
    print("Plan:", plan)
    result = worker(task)
    final = reflection(result)
    return final

if __name__ == "__main__":
    task = input("Enter task: ")
    print(run_agent(task))
