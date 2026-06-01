from bs4 import BeautifulSoup
import sqlite3

html = """
<div class='job'>
<h2>Python Developer</h2>
<p>Infosys</p>
<span>Python</span>
<span>6 LPA</span>
</div>

<div class='job'>
<h2>Data Analyst</h2>
<p>TCS</p>
<span>SQL</span>
<span>5 LPA</span>
</div>

<div class='job'>
<h2>Backend Engineer</h2>
<p>Wipro</p>
<span>Python</span>
<span>8 LPA</span>
</div>
"""

soup = BeautifulSoup(html, "html.parser")

conn = sqlite3.connect("jobs.db")

cursor = conn.cursor()

jobs = soup.find_all("div", class_="job")

for job in jobs:

    title = job.find("h2").text
    company = job.find("p").text

    spans = job.find_all("span")

    skill = spans[0].text
    salary = spans[1].text

    cursor.execute(
        "INSERT INTO jobs(title,company,skill,salary) VALUES(?,?,?,?)",
        (title, company, skill, salary)
    )

conn.commit()
conn.close()

print("Jobs Inserted Successfully")
