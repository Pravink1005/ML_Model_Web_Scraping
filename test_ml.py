from ml_predictor import predict_job_details


job_description = """Only immediate joiners please.

Experience: 10+ Years

Position: 1 Lead

Location: Multiple Locations

Employment Type: Full-Time

Role Overview

We are looking for an experienced SAP SAC Planning Lead with strong hands-on expertise in SAP Analytics Cloud (SAC) Planning. The ideal candidate should have experience in planning model development, data integration, forecasting, budgeting, and working closely with business/end users.

Must-Have Skills

10+ years of overall experience with strong hands-on experience in SAP SAC Planning.
Strong expertise in SAC Planning functionalities.
Hands-on experience in:
Planning Models
Data Actions
Allocations
Forecasting
Budgeting
Simulation Models
Strong experience in end-user planning processes.
Experience in designing and developing interactive dashboards, Stories, and visualizations in SAC.
Experience integrating SAP SAC with SAP BW and other data sources.
Strong understanding of SAP Analytics Cloud – BI and Planning.
Ability to gather requirements from business users and translate them into effective technical solutions.
Strong analytical and problem-solving skills.
Excellent communication and stakeholder management skills.
Good-to-Have Skills

Familiarity with SAP BW.
Experience working with SAP R/3 or other enterprise data sources.
Basic scripting knowledge; JavaScript for SAC scripting is an advantage.
Experience in performance optimization and data accuracy.
Experience providing end-user training and preparing technical/user documentation.
Exposure to advanced SAC planning and simulation capabilities.

Key Responsibilities

Design, develop, and maintain SAC dashboards, Stories, visualizations, and planning solutions.
Develop and maintain planning models, data actions, allocations, forecasting, and budgeting solutions.
Integrate SAC with SAP BW and other data sources.
Support business users in end-to-end planning and forecasting processes.
Collaborate with stakeholders to understand business requirements and deliver scalable technical solutions.
Ensure data accuracy, performance, and an intuitive end-user experience.
Provide training, knowledge transfer, and documentation to end users.
Participate in solution design, troubleshooting, and continuous improvement initiatives

Skills: forecasting,stories,sac dashboards,planning models,allocations,sap sac planning,simulation models,javascript,budgeting,stakeholder management,sap bw,sap analytics cloud,data actions,visualizations,interactive dashboards"""


result = predict_job_details(job_description)


print("================================")
print("ML MODEL TEST")
print("================================")

print("Predicted Degree:",
      result["predicted_degree"])

print("Predicted Specialization:",
      result["predicted_specialization"])
