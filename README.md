# MLOPS GOLD PRICE PREDICTION


## INTRODUCTION
  
<p align="justify"> The Spotify dataset offers a comprehensive view into the world of music streaming, providing valuable insights into user preferences, popular trends, and artist dynamics within the platform. With its vast repository of anonymized user data, encompassing diverse genres, artists, albums, and tracks, the dataset serves as a goldmine for researchers, analysts, and music enthusiasts alike. By delving into this rich dataset, analysts can uncover intriguing patterns, identify emerging trends, and gain a deeper understanding of the ever-evolving landscape of music consumption. </p>
  <p align="justify"> Spotify dataset provides a wealth of information that can be leveraged to gain valuable insights into music consumption behavior, user preferences, and industry trends. Through careful analysis and interpretation, researchers and stakeholders can unlock actionable insights to inform decision-making, drive innovation, and enhance the overall music streaming experience for listeners worldwide. </p>

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
- Azure container instances - for run mage in cloud;
- Azure Blob Storage - for storing model files;
- Azure machine learning - for monitoring model;

## DATASET
Dataset for this project source from : https://huggingface.co/datasets/maharshipandya/spotify-tracks-dataset/blob/c4609440b24ac4075899f6e60b33775acbe00827/dataset.csv 

Here the DAG from mage :

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/c91c33dd-ca6b-4d11-a085-a3aadaec7bc9)

Here the dbt lineage graph :

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/c7cb963a-7f08-4a84-8c6b-08344b859595)

Due to this dataset doesn't have datetime or timestamp this data cannot be partitioned.

Clustered by genre column to improve performance.

## DATA ARCHITECTURE & WORKFLOW

![Work Flow](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/772944b3-e0f3-468f-87a5-8f24260d4a9e)

**1. Data Ingestion from Web API:**
     Utilize Cloud Run to create a scalable and serverless solution for fetching data from the Web API using Mage. Store the extracted data in a Cloud Storage

**2. Extract, Transform, Load (ETL) using Mage:**
     Use Mage to perform ETL operations on the raw data fetched from the Web API. Implement data transformations to cleaning data from null data, converted to minute and rename column name. Load data into a Cloud Storage.

**3. Save Data in Google Cloud Storage as Data Lake:**
     Store the transformed data in Google Cloud Storage as a data warehouse for long-term storage and analysis.

**4. Data Transformation using dbt:**
     Set up a dbt to orchestrate and define transformation logic such as aggregations, joins, and calculations within dbt models to generate analytical datasets. Execute dbt jobs to build and run the defined transformations and generate output datasets in the data warehouse for using in looker studio.

**5. Data Visualization using Looker Studio:**
     Connect Looker to the data warehouse or BigQuery where the transformed datasets reside. Create dashboards, reports, and visualizations using Looker's drag-and-drop interface to giving insights effectively.

## INSIGHTS DASHBOARD

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/e982d182-d4a7-4bde-baa3-bd32b2cde8a8)

Click [here](https://lookerstudio.google.com/reporting/f562671f-beab-47db-b706-5e864ffa0726) to look a dashboard

## Reproduce

## 1. Installation Terraform

I used Windows OS so for installation you can read the documentation in here :
> https://phoenixnap.com/kb/how-to-install-terraform

If you're successfully installed you can check with 
`terraform --version`

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/43710fc5-4cf3-4639-8b92-c8f00e411d14)

## 2. Installation Mage - Orchestration Tool using Terraform in GCP

If you're confused with the installation Mage in GCP I recommend using official Mage documentation and downloading all files :

> https://github.com/mage-ai/mage-ai-terraform-templates/tree/master/gcp

Save in your local folder
Open terminal or visual studio code
Enter to terraform folder

Open `variables.tf` file, fill and setting as you wish

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/ecde3fc4-3c82-471a-8683-7abdbd5beb7d)

Run `terraform init` The terraform init command initializes a working directory containing configuration files and installs plugins for required providers.

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/5b3adbc5-a331-4649-98e5-b4feba8fc1c9)

Run `terraform plan` The terraform plan command creates an execution plan, which lets you preview the changes that Terraform plans to make to your infrastructure.

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/d65da367-bdbe-463f-bfec-459ea253d92e)

Check if everything is correct, if there are error fix an error

Run command `terraform apply` Type "yes" then press Enter. You can check into GCP

![image](https://github.com/SofyanAkbar94/Project-DE-Zoomcamp-2024/assets/136363515/8f7e3783-341b-4797-9d11-4de427b451a8)

## 3. Installation DBT Cloud :

For further information setup DBT Cloud. Follow this tutorial from datatalksclub. Thanks for providing this tutorial.

> https://github.com/DataTalksClub/data-engineering-zoomcamp/blob/main/04-analytics-engineering/dbt_cloud_setup.md

## Acknowledgments

<p align="justify">I would like to extend my heartfelt gratitude to Alexey and the entire DataTalks.Club community for their invaluable contribution in organizing and hosting the Zoom camp, and generously sharing knowledge and expertise with participants, all free of charge.</p>

<p align="justify">Your dedication to fostering learning and professional development within the data community is truly commendable. Through the Zoom camp sessions, you have provided an invaluable platform for individuals to expand their skills, explore new technologies, and engage with industry experts in a supportive and collaborative environment.</p>
<p align="justify">Thank you, Alexey, and everyone at DataTalks.Club, for your unwavering dedication to education, collaboration, and community building. We look forward to continuing our journey of learning and discovery together.</p>
