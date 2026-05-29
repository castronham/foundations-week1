import json
import sys  # sys lets us look at commands typed into the terminal

print("Reading posts.json file...")
with open('posts.json', 'r') as file:
    posts = json.load(file)

# 1. Total Posts Count
total_posts = len(posts)

# 2. Tracking variables
total_words = 0
oldest_date = posts[0]['date']
oldest_title = posts[0]['title']
category_counts = {}

# Loop through every post
for post in posts:
    total_words = total_words + post['wordCount']
    
    if post['date'] < oldest_date:
        oldest_date = post['date']
        oldest_title = post['title']
        
    cat = post['category']
    if cat in category_counts:
        category_counts[cat] = category_counts[cat] + 1
    else:
        category_counts[cat] = 1

# 3. Calculations
average_words = total_words / total_posts
top_category = max(category_counts, key=category_counts.get)

# 4. Check for Terminal Flags
# sys.argv is a list of words we typed in the terminal
arguments = sys.argv

if "--summary" in arguments:
    # If the user typed --summary, give them the brief 1-line view
    print("\n--- QUICK SUMMARY ---")
    print(f"Stats: {total_posts} posts | Top Cat: {top_category} | Avg Words: {average_words}")
else:
    # Otherwise, show the full beautiful report
    print("\n--- UPGRADED RESULTS ---")
    print(f"Total Posts: {total_posts}")
    print(f"Average Words Per Post: {average_words}")
    print(f"Top Category: {top_category}")
    print(f"Oldest Post: '{oldest_title}' (Published: {oldest_date})")