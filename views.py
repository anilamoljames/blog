
from blog2.models import users,posts

session={}


def SigninRequird(fn):
    def wrapper(*args,**kwargs):
        if "user " in session:
            return fn(*args,**kwargs)
        else:
            print(("U must Login "))
    return wrapper
def autenticate(**kwargs):
    username=kwargs.get("username")
    password=kwargs.get("password")
    user = [user for user in users if user["username"] == username and user["password"] ==password]
    return user


class Signinview:
    username:str
    password:str
    def post(self, *args,**kwargs):
        print( autenticate(username="anu",password="Password@123"))
        username = kwargs.get("username")
        password = kwargs.get("password")
        user = [user for user in users if user["username"] == username and user["password"] == password]
        if user:
            session["user"]=user[0]
            print("Success")
        else:
            print("Invalid")
class Postview:
    def get(self,*args,**kwargs):
        return posts
    def post(self,*args,**kwargs):
        print(kwargs)
        userId=session["user"]["id"]
        kwargs["userId"]=userId
        print(kwargs)
        posts.append(kwargs)
        print("post added")
        print(posts)

class MypostlistView:
    @SigninRequird
    def get(self,*args,**kwargs):
        print(session)
        userId=session["user"]["id"]
        my_posts=[post for post in posts if post["userId"]==userId]
        return my_posts



class PostdetailsView:

    def get_object(self,id):
        post=[post for post in posts if post["postId"]==id]
        return post

    def delete(self,*args,**kwargs):
        post_id=kwargs.get("post_id")
        data=self.get_object(post_id)
        if data:
            post=data[0]
            posts.remove(post)
            print("post removed")
            print(len(posts))

    def put(self, *args,**kwargs):
        post_id=kwargs.get("post_id")
        instance=self.get_object(post_id)
        data=kwargs.get("data")
        if instance:
            post_obj=instance[0]
            post_obj.update(data)
            return post_obj


class Likeview:
    def  get(self,*args,**kwargs):

        postid=kwargs.get("postid")
        post=[post for post in posts if post["postId"]==postid]
        userid=session["user"]["id"]
        if post:
            post=post[0]
            post["liked_by"].append(userid)
            print(post["liked_by"])




log=Signinview()
log.post(username="anu",password="Password@123")
# print(session)
# data=Postview()
# print(data.get())
# data.post(postid=9,title="hello there",contain="hkjkj",liked_by=[])
mypost=MypostlistView()
print(mypost.get())
# post_det=PostdetailsView()
# post_det.delete(post_id=6)
#
# data={
#     "title":"nertitle"
# }
# det=PostdetailsView()
# print(det.put(post_id=4,data=data))


like=Likeview()
like.get(postid=6)