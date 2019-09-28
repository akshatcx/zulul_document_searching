import arxiv
import os

query = "iot"
max_results = 500

os.mkdir("test_papers")
os.chdir("test_papers")

papers = arxiv.query(query = query, max_results = max_results)

cnt = 0;
for paper in papers:
    print("downloading ", cnt);
    cnt += 1;
    arxiv.download(paper)
