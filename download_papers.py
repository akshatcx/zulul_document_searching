import arxiv
import os

query = "chemistry"
max_results = 500

os.mkdir("test_papers")
os.chdir("test_papers")

papers = arvix.query(query = query, max_results = max_results)

for paper in papers:
    arxiv.download(paper)

