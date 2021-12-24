from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta # dbspart라는 이름으로 접속할 것

db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'9.39'}})
# 영화제목 '매트릭스'의 평점 가져오기
rank_matrix = db.movies.find_one({'title':'매트릭스'})
print(rank_matrix['star'])
# '매트릭스'의 평점과 같은 평점의 영화 제목들 가져오기
target_star = rank_matrix['star']
same_matrix_rank = list(db.movies.find({'star':target_star}))
for target in same_matrix_rank:
    print(target['title'])
# '매트릭스'의 평점을 0으로 만들기
db.movies.update_one({'title':'매트릭스'},{'$set':{'star':'0'}})
rank_matrix = db.movies.find_one({'title':'매트릭스'})
print(rank_matrix['star'])