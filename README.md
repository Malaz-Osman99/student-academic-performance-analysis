📊 Student Academic Performance Analysis

An end-to-end data analysis project exploring the factors that may influence student academic performance using Python for data cleaning and Excel for exploratory analysis and visualization.

This project investigates whether demographic characteristics, lifestyle habits, and study behaviors have a measurable relationship with student grades.

🎯 Project Objective

The goal of this project is to analyze student performance data to understand how different factors may affect academic achievement.

The analysis focuses on identifying patterns and answering key analytical questions such as:

Do male and female students perform differently?

Does parental education influence student achievement?

Does study time impact academic performance?

Is there a relationship between sleep duration and grades?

Does internet access affect student results?

Are there differences between school types?

📂 Dataset Description

The dataset contains information about 7,000 students and includes demographic, lifestyle, and academic variables.

Key Variables

Demographic Information

Gender

Race / Ethnicity

Parental Education

Socioeconomic Indicators

Lunch Type

Internet Access

Lifestyle Factors

Study Time per Week

Daily Sleep Duration

School Environment

School Type

Test Preparation

Academic Performance

Math Score

Reading Score

Writing Score

A new feature called Average Score was created to represent the overall academic performance of each student.

⚙️ Tools and Technologies

This project uses a combination of programming and spreadsheet tools:

Python

Pandas (data cleaning and preprocessing)

Microsoft Excel

Pivot Tables

Charts and Data Visualization

Comparative Analysis

🧹 Data Cleaning Process (Python)

The dataset was cleaned and prepared using Python and Pandas.
Key preprocessing steps included:

Handling missing values

Converting columns to appropriate data types

Removing unrealistic values

Replacing outliers

Creating a new feature: Average Score

Standardizing categorical variables

The cleaned dataset was exported for further analysis in Excel.

🔎 Exploratory Data Analysis

After cleaning the dataset, exploratory analysis was conducted using Excel Pivot Tables and charts to examine relationships between variables.

The analysis focused on comparing average scores across different categories.

📊 Key Analysis Questions

The following questions guided the analysis:

1️⃣ Gender Differences

Is there a difference in academic performance between male and female students?

2️⃣ Ethnic Group Comparison

Do students from different racial/ethnic groups show differences in average grades?

3️⃣ Parental Education

Does the level of parental education influence student performance?

4️⃣ Economic Indicator (Lunch Type)

Do students receiving free/reduced lunch perform differently from those with standard lunch?

5️⃣ School Type

Does the type of school (public, private, international) affect academic performance?

6️⃣ Internet Access

Does having internet access at home improve academic results?

7️⃣ Sleep Duration

Is there a relationship between daily sleep duration and academic performance?

8️⃣ Study Time

Do students who study more hours per week achieve higher grades?

📈 Key Findings
Gender

Male students had a slightly higher average score than female students.

However, the difference was very small, suggesting that gender does not significantly affect academic performance.

Race / Ethnicity

Average scores across different ethnic groups were very similar, indicating no strong performance gap between groups.

Parental Education

Students whose parents had higher education levels showed slightly higher average scores, but the differences remained relatively small.

Lunch Type

Students with standard lunch had a marginally higher average score compared to those receiving free or reduced lunch.

This may reflect minor socioeconomic differences.

School Type

Students from international schools had slightly higher average scores compared to public and private schools, though the difference was not large.

Internet Access

Students with and without internet access had almost identical average scores, indicating no clear relationship in this dataset.

Sleep Duration

Students across different sleep categories showed very similar average grades, suggesting sleep duration did not strongly impact performance in this data.

Study Time per Week

Students studying between 5 and 15 hours per week represented the majority of the dataset.

Despite variations in study time, average scores remained fairly consistent across groups.

📊 Data Visualization

Charts and Pivot Tables were used to visually compare average scores across different categories, including:

Gender comparison

Study time vs grades

Sleep duration vs grades

School type comparison

Internet access impact

These visualizations help highlight patterns and simplify interpretation of the data.

💡 Overall Insights

The analysis revealed that most demographic and lifestyle factors had only minor differences in average academic performance.

Average scores across nearly all groups remained close to the overall mean of approximately 70 points.

This suggests that student performance in this dataset may be influenced by factors not strongly represented in the available variables, or that the effects of these factors are relatively small.

🚀 Project Structure
student-performance-analysis

data
 ├─ student_academic_performance.xlsx
 └─ student_academic_performance_cleaned.xlsx

python
 └─ data_cleaning.py

excel_analysis
 └─ pivot_tables_analysis.xlsx

charts
 ├─ gender_analysis.png
 ├─ study_time_analysis.png
 ├─ sleep_analysis.png
 ├─ internet_access_analysis.png
 └─ school_type_analysis.png

 Future Improvements

Potential next steps for improving this analysis include:
Applying statistical testing to validate differences between groups
Using machine learning models to predict student performance
Performing correlation analysis
Building an interactive dashboard using tools like Power BI or Tableau


والفرق سيكون كبير جدًا في شكل المشروع.
