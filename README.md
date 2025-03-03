"AI Resume Screening & Candidate Ranking System " 

This is an **AI-powered resume screening application** built with **Streamlit**.
It ranks resumes based on their similarity to a given job description using **TF-IDF vectorization** and **cosine similarity**.  

## Features  

Upload multiple PDF resumes  
Extracts text automatically from resumes  
Ranks resumes based on job description relevance  
Displays sorted ranking results in a table  

## Installation  
1. Clone the repository:  
   git clone https://github.com/your-repo/resume-screening.git
   cd resume-screening
  
2. Install dependencies:  
   pip install streamlit PyPDF2 scikit-learn pandas
   
3. Run the application:
   Run following statement In Terminal 
   "streamlit run app.py"
   
## How It Works  

1. **Enter the Job Description** in the text box.  
2. **Upload Resumes** in PDF format.  
3. **AI-powered ranking** is performed:  
   - Extracts text from resumes.  
   - Converts text into numerical vectors using **TF-IDF**.  
   - Calculates **cosine similarity** between the job description and resumes.  
   - Displays resumes in **ranked order** based on relevance.  
4. **View Results** in a table with similarity scores.  

## Troubleshooting  

If you encounter the warning:  
"Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode."

Simply ignore it—it does not affect the functionality of the app.
 
Developed by **Dev Singh** 
