# MLOPS GOLD PRICE PREDICTION


## INTRODUCTION
  
<p align="justify"> Gold price prediction is a critical task for investors, financial analysts, and policymakers due to gold's significance as a hedge against inflation and currency fluctuations. Accurate forecasting of gold prices can lead to more informed decision-making and better risk management. To achieve reliable predictions, we leverage advanced machine learning models and MLOps practices to create a robust, scalable, and automated gold price prediction system. </p>
<p align="justify">
This project aims to build an end-to-end MLOps pipeline for predicting gold prices. It encompasses data collection, preprocessing, model training, deployment, and monitoring using Azure Machine Learning services. The goal is to ensure that our model remains accurate, reliable, and continuously improving with minimal manual intervention. </p>

## PROBLEMS IN THIS PROJECT

### - Problem in terraform in main.tf file

  ![alt text](image.png)

  ![alt text](image-1.png)
  
  ### Solution :
  
  Change name and add suffix number
  
### - Problem in authorization mage with azure
  
  ![alt text](image-2.png)
  
  ### Solution :
  
  Give secret key connection string
  
  ![alt text](image-3.png)

## USED TECHNOLOGIES
- Terraform - as Infrastructure-as-Code (IaC) provide setup gcp services;
- MLFlow - for experiment tracking and model registry
- MageAI - for orchestration load, transform, train, inference, export;
- Azure container instances - for run mage and run model in cloud;
- Azure container registry - for storing registry image or model;
- Azure Blob Storage - for storing model files;
- Azure machine learning - for monitoring model;

## EXPERIMENT TRACKING AND MODEL REGISTRY 


## DATASET & WORKFLOW ORCHESTRATION
Dataset for this project source using yfinance api and i clean and convert the data into csv file and i upload to azure blob storage

![alt text](image-4.png)

Here the orchestration from mage :

![alt text](image-5.png)

## MODEL DEPLOYMENT

## MODEL MONITORING

## Reproduce

## 1. Installation Terraform

I used Windows OS so for installation you can read the documentation in here :
> https://phoenixnap.com/kb/how-to-install-terraform

If you're successfully installed you can check with 
`terraform --version`

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/43710fc5-4cf3-4639-8b92-c8f00e411d14)

## 2. Installation Mage - Orchestration Tool using Terraform in Azure

If you're confused with the installation Mage in GCP I recommend using official Mage documentation and downloading all files :

> https://github.com/mage-ai/mage-ai-terraform-templates/tree/master/gcp

Save in your local folder
Open terminal or visual studio code
Enter to terraform folder

Open `variables.tf` file, fill and setting as you wish

![alt text](image-6.png)

Run `terraform init` The terraform init command initializes a working directory containing configuration files and installs plugins for required providers.

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/5b3adbc5-a331-4649-98e5-b4feba8fc1c9)

Run `terraform plan` The terraform plan command creates an execution plan, which lets you preview the changes that Terraform plans to make to your infrastructure.

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/d65da367-bdbe-463f-bfec-459ea253d92e)

Check if everything is correct, if there are error fix an error

Run command `terraform apply` Type "yes" then press Enter. You can check into GCP

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/8f7e3783-341b-4797-9d11-4de427b451a8)

## Acknowledgments

<p align="justify">I would like to extend my heartfelt gratitude to Alexey and the entire DataTalks.Club community for their invaluable contribution in organizing and hosting the Zoom camp, and generously sharing knowledge and expertise with participants, all free of charge.</p>
<p align="justify">Your dedication to fostering learning and professional development within the data community is truly commendable. Through the Zoom camp sessions, you have provided an invaluable platform for individuals to expand their skills, explore new technologies, and engage with industry experts in a supportive and collaborative environment.</p>
<p align="justify">Thank you, Alexey, and everyone at DataTalks.Club, for your unwavering dedication to education, collaboration, and community building. We look forward to continuing our journey of learning and discovery together.</p>
