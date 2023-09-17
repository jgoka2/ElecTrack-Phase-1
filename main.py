import matplotlib.pyplot as plt

# Sample data
age_data = {'18-25': 150, '26-35': 200, '36-45': 180, '46-55': 120, '56+': 90}
gender_data = {'Male': 477, 'Female': 450}
community_data = {'General': 150, 'OBC': 350, 'SC': 280, 'ST': 147}
party_data = {'Party A': 500, 'Party B': 280, 'Party C': 110, 'Independent/others': 37}
voting_data = {'Voted': 720, 'Did not vote': 207}

# Bar graph for age data
plt.figure(figsize=(8, 6))
plt.bar(age_data.keys(), age_data.values())
plt.xlabel('Age Group')
plt.ylabel('Number of Voters')
plt.title('Voters by Age Group')
plt.show()

# Pie chart for gender data
plt.figure(figsize=(8, 6))
plt.pie(gender_data.values(), labels=gender_data.keys(), autopct='%1.1f%%')
plt.title('Voters by Gender')
plt.show()

# Bar graph for community data
plt.figure(figsize=(8, 6))
plt.bar(community_data.keys(), community_data.values())
plt.xlabel('Community')
plt.ylabel('Number of Voters')
plt.title('Voters by Community')
plt.show()

# Pie chart for party affiliation data
plt.figure(figsize=(8, 6))
plt.pie(party_data.values(), labels=party_data.keys(), autopct='%1.1f%%')
plt.title('Party Inclination of Voters')
plt.show()

# Pie chart for voting history data
plt.figure(figsize=(8, 6))
plt.pie(voting_data.values(), labels=voting_data.keys(), autopct='%1.1f%%')
plt.title('Voting History of Voters')
plt.show()