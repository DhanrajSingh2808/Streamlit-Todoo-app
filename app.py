import streamlit as st
import json
import os
# Define default_data dictionary

TASKS_FILE = "tasks.json"
COMMENTS_FILE = "comments.json"

default_data = {
    "Case-in-Advance (CIA) Models": {
        "Certainty Case": [
            "Model setup and solution",
            "Consumption velocity",
            "Steady-state analysis: Superneutrality of inflation",
            "Modifications to the basic model:",
            "Uncertainty",
            "CIA applying to a subset of goods",
            "Consumption-leisure trade-off",
            "Utility as a function of inflation",
            "Cash and credit goods",
            "CIA and investment goods"
        ],
        "Stochastic CIA Model": [
            "Basic model setup",
            "Productivity shocks and their dynamics"
        ]
    },
    "Search-Theoretic Models of Money": {
        "Motivation and Frictions": [
            "Defining money and its societal use",
            "Contrasting search theory with DSGE and OLG models",
            "Identifying frictions that make money essential:",
            "Double-coincidence of wants problem",
            "Lack of long-run commitment enforcement",
            "Agent anonymity"
        ],
        "Kiyotaki and Wright (1993)": [
            "Model setup: Fixed money and goods",
            "Trading strategies and equilibrium types:",
            "Non-monetary equilibrium",
            "Monetary equilibrium",
            "Mixed-monetary equilibrium",
            "Welfare analysis:",
            "Welfare as average utility",
            "Impact of money supply on welfare",
            "Comparison with alternative arrangements (e.g., credit)"
        ],
        "Trejos and Wright (1995): Endogenous Prices": [
            "Relaxing the fixed-price assumption",
            "Utility and cost functions",
            "Bargaining and value functions",
            "Equilibrium analysis and efficiency"
        ],
        "Third-Generation Models: Endogenous Prices and Goods": [
            "Relaxing the fixed money holdings assumption",
            "Computational and theoretical approaches",
            "Lagos and Wright (2005): Two-market model",
            "Environment with day and night markets",
            "Utility function and assumptions",
            "Money holdings and distribution",
            "Value functions for decentralized and centralized markets",
            "Terms of trade:",
            "Double coincidence",
            "Single coincidence"
        ]
    },
    "Money and Public Finance": {
        "Government Budget Constraint": [
            "Sources of government revenue: Taxes, bonds, money creation",
            "Real vs. nominal budget constraint",
            "Ex-post vs. ex-ante real rate of return",
            "Seigniorage:",
            "Definition and measurement",
            "Relationship to inflation and tax base",
            "Friedman Rule"
        ],
        "Intertemporal Budget Balance": [
            "Restrictions on government borrowing and seigniorage",
            "Present discounted value of tax and seigniorage revenue",
            "No-Ponzi condition",
            "Primary deficit and implications for government surplus"
        ],
        "Money and Fiscal Policy Frameworks": [
            "Two ways to vary money stock:",
            "Shifting from tax-financed to seigniorage-financed expenditure",
            "Open market operations",
            "Relationship between monetary and fiscal policies",
            "Different policy regimes:",
            "Active monetary, passive fiscal",
            "Active fiscal, passive monetary (fiscal dominance)",
            "Ricardian regime"
        ],
        "Deficits and Inflation": [
            "Fiscal dominance and its implications for seigniorage",
            "Unpleasant monetarist arithmetic: Implications of reduced fiscal surplus",
            "Ricardian vs. non-Ricardian fiscal policy:",
            "Impact of lump-sum taxes and transfers vs. open market operations",
            "Role of debt backing and its impact on price level",
            "Steady-state price level and the role of government liabilities",
            "Government budget constraint and nominal interest rate",
            "Fiscal solvency and price level determination"
        ],
        "Financing Fiscal Deficits with Money Creation": [
            "Feasibility of raising a deficit in steady-state",
            "Equilibrium inflation rate and seigniorage",
            "Cagan model of inflation:",
            "Relationship between money supply growth and inflation",
            "Money demand function and seigniorage maximization"
        ]
    },
    "Optimal Taxation and Seigniorage": {
        "Minimizing Distortionary Costs": [
            "Optimal tax package should include seigniorage",
            "Equalizing marginal distortionary cost across taxes",
            "Intertemporal optimality and tax smoothing"
        ],
        "Optimal Seigniorage and Temporary Shocks": [
            "Tax smoothing and permanent vs. temporary expenditures",
            "Allocative distortions and anticipated inflation",
            "Flexible response to unexpected disturbances"
        ]
    },
    "Inflation and Government Financing": {
        "Integrating Inflation with Public Finance": [
            "Optimal inflation tax and its relationship to tax structure",
            "Conditions for taxing money"
        ],
        "Basic Ramsey Problem": [
            "Maximizing utility subject to government revenue requirement"
        ],
        "Approaches to Solving the Problem": [
            "Dual approach: Indirect utility function and tax rates",
            "Primal approach: Quantities as government controls"
        ]
    },
    "Time Inconsistency in Monetary Policy": {
        "Reasons for Time Inconsistency": [
            "Incentives of central banks",
            "Designing effective policymaking institutions"
        ],
        "Inflation under Discretionary Policy": [
            "Trade-off between output and inflation volatility"
        ],
        "Precommitment to a Policy Rule": [
            "Optimal linear rule and comparison with discretion"
        ],
        "Reasons for Inflation Bias": [],
        "Solutions to Time Inconsistency": [
            "Reputation and repeated games",
            "Preferences for a central bank",
            "Restricted flexibility",
            "Targeting rules:",
            "Inflation targeting",
            "Exchange rate systems"
        ]
    },
    "Targeting Rules: Central Bank Policies": {
        "Flexible vs. Strict Targeting": [
            "Trade-offs between meeting targets and other objectives"
        ],
        "Nominal Income Targeting": [
            "Benefits and drawbacks"
        ]
    },
    "Nominal Price and Wage Rigidities": {
        "Wage Rigidity and Monetary Policy Effects": [
            "One-period wage rigidity",
            "Staggered, multi-period wage contracts (Taylor model)"
        ],
        "Wage Rigidity in an MIU Model": [
            "Assumptions and equations",
            "Impact of money growth disturbance",
            "Nominal wage setting"
        ],
        "Taylor's Model: Staggered Nominal Adjustment": [
            "Price setting and inertia"
        ],
        "Imperfect Competition and Nominal Rigidities": [
            "Menu costs and their macroeconomic implications",
            "Limitations of menu cost models"
        ],
        "A Basic Model of Monopolistic Competition": [
            "Final and intermediate good production",
            "Profit maximization and price setting"
        ],
        "Time-Dependent Pricing (TDP) Models": [
            "Taylor model revisited: Staggered price adjustments",
            "Calvo model: Random price adjustments",
            "Comparison of Taylor and Calvo models"
        ]
    },
    "New Keynesian Monetary Economics": {
        "DSGE Models and New Keynesian (NK) Models": [
            "Role of nominal rigidities and aggregate demand"
        ],
        "Basic MIU Model with Nominal Rigidities": [
            "Households, firms, and central bank",
            "Optimization problems and equilibrium conditions"
        ],
        "A Linearized New Keynesian Model": [
            "New Keynesian Phillips curve",
            "Linearized IS curve"
        ],
        "Uniqueness of the Equilibrium": [
            "Taylor principle and interest rate rules"
        ],
        "Monetary Policy and Its Transmission": [],
        "Monetary Policy Analysis in New Keynesian Models": [
            "Objectives of the central bank",
            "Welfare criterion and quadratic loss functions"
        ],
        "Monetary Policy in the Open Economy": [
            "Exchange rate movements and their impact",
            "Two-country open-economy model (Clarida, Galf, and Gertler)",
            "Model of the small open economy (Gali and Monacelli)",
            "Equilibrium dynamics and policy analysis",
            "Evaluation of alternative policies"
        ]
    }
}


blank_comments = {
    topic: {subtopic: {task: {"done": False, "comment": ""} for task in tasks}
            for subtopic, tasks in subtopics.items()}
    for topic, subtopics in default_data.items()
}

# Load data from JSON file
def load_json(file_path, default_data=None):
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            return json.load(f)
    return default_data if default_data else {}

# Save data to JSON file
def save_json(file_path, data):
    with open(file_path, "w") as f:
        json.dump(data, f, indent=4)

# Load tasks and comments
tasks_data = load_json(TASKS_FILE, default_data)
comments_data = load_json(COMMENTS_FILE, blank_comments)

# Helper function to calculate text box height based on text length
def calculate_text_area_height(text, line_height=20, base_height=68, max_height=800):
    lines = len(text.splitlines())
    height = base_height + lines * line_height
    return min(height, max_height)  # Cap the height to prevent excessive growth

# Title and description
st.title("Interactive To-Do List")
st.markdown(""" 
    *Organize your tasks efficiently!*
    - Click checkboxes to mark tasks as done.
    - Edit tasks and add comments easily.
    - View progress for subtopics and topics.
""")

# Display the tasks as a list (expanded view of all topics, subtopics, and tasks)
for topic, subtopics in tasks_data.items():
    with st.expander(f"### {topic}", expanded=True):  # Collapsible topic section
        # Calculate progress for the entire topic
        total_tasks = sum(len(tasks) for tasks in subtopics.values())
        completed_tasks = sum(
            len([task for task in tasks if comments_data.get(topic, {}).get(subtopic, {}).get(task, {}).get("done", False)])
            for subtopic, tasks in subtopics.items()
        )
        progress = completed_tasks / total_tasks if total_tasks > 0 else 0

        # Display progress bar
        st.progress(progress)

        for subtopic, tasks in subtopics.items():
            st.markdown(f"#### {subtopic}")

            # Display task completion details
            subtopic_completed = len(
                [task for task in tasks if comments_data.get(topic, {}).get(subtopic, {}).get(task, {}).get("done", False)]
            )
            st.write(
                f"{subtopic_completed}/{len(tasks)} tasks completed"
            )

            # Tasks
            for i, task in enumerate(tasks):
                task_done = comments_data.get(topic, {}).get(subtopic, {}).get(task, {}).get("done", False)
                existing_comment = comments_data.get(topic, {}).get(subtopic, {}).get(task, {}).get("comment", "")

                # Compact layout for each task
                col1, col2, col3 = st.columns([0.1, 0.6, 0.3])

                with col1:
                    # Task Completion Checkbox
                    if st.checkbox("", value=task_done, key=f"{topic}-{subtopic}-{i}-checkbox"):
                        comments_data.setdefault(topic, {}).setdefault(subtopic, {}).setdefault(task, {})["done"] = not task_done
                        save_json(COMMENTS_FILE, comments_data)

                with col2:
                    # Inline editable task name
                    new_task_name = st.text_input(
                        "",
                        value=task,
                        key=f"{topic}-{subtopic}-{i}-task_name",
                        label_visibility="collapsed",
                    )
                    if new_task_name != task:
                        tasks_data[topic][subtopic][i] = new_task_name
                        save_json(TASKS_FILE, tasks_data)

                with col3:
                    # Dynamically resize comment box
                    height = calculate_text_area_height(existing_comment)
                    new_comment = st.text_area(
                        "Add/Edit Comment",
                        value=existing_comment,
                        height=height,
                        key=f"{topic}-{subtopic}-{i}-comment",
                        label_visibility="collapsed",
                    )
                    if new_comment != existing_comment:
                        comments_data.setdefault(topic, {}).setdefault(subtopic, {}).setdefault(task, {})["comment"] = new_comment
                        save_json(COMMENTS_FILE, comments_data)

# Sidebar for adding new tasks (optional, for adding new tasks directly)
with st.sidebar:
    st.title("Add New Task")
    new_topic = st.text_input("Topic", placeholder="e.g., Monetary Policy")
    new_subtopic = st.text_input("Subtopic", placeholder="e.g., Inflation Effects")
    new_task = st.text_input("Task", placeholder="e.g., Study inflation theories")
    if st.button("Add Task"):
        if new_topic and new_subtopic and new_task:
            tasks_data.setdefault(new_topic, {}).setdefault(new_subtopic, []).append(new_task)
            save_json(TASKS_FILE, tasks_data)
            st.experimental_rerun()

# Footer
st.markdown("---")
st.markdown(
    "<small style='font-size: 12px;'>Developed by [Your Name]</small>",
    unsafe_allow_html=True,
)
