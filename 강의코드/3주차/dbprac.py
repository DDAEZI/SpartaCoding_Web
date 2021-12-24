from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbsparta # dbspart라는 이름으로 접속할 것

# insert / find / update / delete
# insert
#doc = {'name':'jane','age':21}
#db.users.insert_one(doc) # 딕셔너리를 user에 넣기

# find
# _id:False : id값 가져오지 말아라
same_ages = list(db.users.find({'age':21},{'_id':False}))


user = db.users.find_one({'name':'bobby'},{'_id':False})
print(user)

# update
# update_many : 여러 개 바꾸기
db.users.update_one({'name':'bobby'},{'$set':{'age':19}})

# delete
db.users.delete_one({'name':'jane'})