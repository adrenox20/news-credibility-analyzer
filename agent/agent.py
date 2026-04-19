from langgraph.graph import StateGraph

from model.predict import predict_news
from agent.risk_analyzer import analyze_risk
from rag.retriever import retrieve
from agent.llm import generate_report

def node_ml(state):
    state["ml"] = predict_news(state["text"])
    return state

def node_risk(state):
    state["risks"] = analyze_risk(state["text"])
    return state

def node_retrieve(state):
    state["facts"] = retrieve(state["text"])
    return state

def node_llm(state):
    state["report"] = generate_report(
        state["text"],
        state["risks"],
        state["facts"],
        state["ml"]
    )
    return state

graph = StateGraph(dict)

graph.add_node("ml", node_ml)
graph.add_node("risk", node_risk)
graph.add_node("retrieve", node_retrieve)
graph.add_node("llm", node_llm)

graph.set_entry_point("ml")

graph.add_edge("ml", "risk")
graph.add_edge("risk", "retrieve")
graph.add_edge("retrieve", "llm")

app = graph.compile()