import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data=pd.read_csv("student_performance.csv")
df=pd.DataFrame(data)
print(df.isnull().sum())
print(df.head())

print(df.describe())

print("Average Examscore by Grade")
print(df.groupby("FinalGrade")["ExamScore"].mean())

print("Average Examscore by Gender")
print(df.groupby("Gender")["ExamScore"].mean())

print("Average Attendance by Grade")
print(df.groupby("FinalGrade")["Attendance"].mean())




sns.histplot(df["StudyHours"],kde=True)
plt.title("Study Hours Distribution with KDE")
plt.savefig("images/Studyhour_histkde.png")
plt.show()

plt.hexbin(data=df,x="StudyHours",y="ExamScore",gridsize=30,cmap="Blues",mincnt=1)
plt.colorbar(label="Count of Student")
plt.title("Studyhours by Examscore")
plt.xlabel("StudyHours")
plt.ylabel("ExamScore")
plt.savefig("images/examscore_hexbin.png")
plt.show()

plt.hexbin(data=df,x="Attendance",y="ExamScore",gridsize=30,cmap="Greens",mincnt=1)
plt.colorbar(label="Count Of Student")
plt.title("Attendance vs Examscore")
plt.xlabel("Attendance")
plt.ylabel("ExamScore")
plt.savefig("images/Attendance_hexbin.png")
plt.show()

plt.hexbin(data=df,x="OnlineCourses",y="ExamScore",gridsize=30,cmap="Purples",mincnt=2)
plt.colorbar(label="Count of student")
plt.title(" Onlinecourse vs Examscore")
plt.xlabel("Online Course")
plt.ylabel("ExamScore")
plt.savefig("images/OnlineCourses_hexbin.png")
plt.show()

sns.boxplot(data=df,x="Internet",y="ExamScore",hue="Internet"
            
)
plt.title(" InternetAccess vs Examscore")
plt.xlabel("Internet Access")
plt.ylabel("ExamScore")
plt.savefig("images/internetaccess_boxplt.png")
plt.show()

sns.boxplot(data=df,x="StressLevel",y="ExamScore",hue="StressLevel"
)
plt.title(" Stressslevel vs Examscore")
plt.xlabel("Stress Level")
plt.ylabel("ExamScore")
plt.savefig("images/stresslevel_boxplt.png")
plt.show()


sns.countplot(data=df, x="FinalGrade")
plt.title(" Counting Of Final grade")
plt.savefig("images/finalgrade_countplt.png")
plt.show()

sns.heatmap(df.corr(numeric_only=True),
             annot=True,
             fmt=".2f", 
             cmap="rocket", 
             linewidths=0.5,     
             annot_kws={"size": 9})
plt.title(" Correlation  between the numeric values")
plt.savefig("images/correlation_hist.png")
plt.show()

