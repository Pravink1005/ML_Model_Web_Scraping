from ml_predictor import predict_job_details


job_description = """About the job
We are looking for a seasoned Lead/Senior Domino Data Lab Engineer with solid Python expertise to architect, build, and roll out scalable data science applications and machine learning solutions. In this position, you will use the Domino Data Lab platform to create production-ready models, partner with cross-functional teams, and champion best practices throughout the ML lifecycle.

Responsibilities

Architect, build, and roll out applications and machine learning models on the Domino Data Lab platform
Create and maintain Python-based solutions using modern frameworks and libraries
Build REST APIs to expose models and services for enterprise consumption
Oversee Domino Projects, Workspaces, Jobs, and Environments to support data science workflows
Apply MLOps practices covering model deployment, monitoring, and productionization
Partner with data scientists, engineers, and stakeholders to translate business needs into technical solutions
Connect applications with various databases and data sources
Set up CI/CD pipelines and containerization strategies for reliable delivery
Guide junior team members and promote software development best practices
Maintain the reliability, scalability, and performance of deployed models and services

Requirements

5-14 years of professional software/data engineering experience
Expertise in Domino Data Lab, including Projects, Workspaces, Jobs, and Environments
Proficiency in Python development and scripting
Skills in Pandas, NumPy, and Scikit-learn or similar Python libraries
Background in developing REST APIs with FastAPI, Flask, or Django
Understanding of MLOps principles and the end-to-end ML model lifecycle
Knowledge of Git, Docker, and CI/CD workflows
Familiarity with cloud platforms such as AWS, Azure, or GCP
Background in model deployment, monitoring, and productionization
Capability to work with databases and data integration solutions
Understanding of software development best practices

Nice to have

Background in Node.js
Familiarity with Kubernetes for orchestration
Knowledge of MLOps or Machine Learning platform tooling
Proficiency in Jupyter or similar Data Science environments
Competency in enterprise application integration"""


result = predict_job_details(job_description)


print("================================")
print("ML MODEL TEST")
print("================================")

print("Predicted Degree:",
      result["predicted_degree"])

print("Predicted Specialization:",
      result["predicted_specialization"])
