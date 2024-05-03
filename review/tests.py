# # from django.test import TestCase
# from django.test import TestCase
# from  collections import OrderedDict
# from rest_framework.test import APIRequestFactory,force_authenticate
# from rest_framework.utils.serializer_helpers import ReturnDict,ReturnList
# from rest_framework_simplejwt.views import TokenObtainPairView
# from .views import PostViewSet
# from .models import Post
# from account.models import User

# # Create your tests here.

# class PostTest(TestCase):
#     def setUp(self):
#         self.factory=APIRequestFactory()
#         user=User.objects.create_user(email='admin2@admin.com',password='1')
#         post=[
#             Post(author=user,title='new post'),
#             Post(author=use,title='hello'),
#             Post(author=user,title='hello world')
#         ]
#         Post.objects.bulk_create(posts)

#         def test_list(self):
#             request=self.factory.get('/posts/')

#             view=PostViewSet.as_view({'get':'list'})
#             response=view(request)
#             assert response.status_code==200
#             assert type(response.data)==ReturnList
#             assert response.data[0]['title']=='new post'

#         def test_retrieve(self):
#             id=Post.objects.all()[0].id 
#             request=self.factory.get(f'/posts/{id}/')
#             view=PostViewSet.as_view({'get':'retrieve'})
#             response=view(request,id)
#             assert response.status_code==200
#             assert type(response.data)==ReturnDict
#             assert response.data['title']=='new post'
        

#         def test_auth(self):
#             data={
#                 'title':'new new new post'
#             }
#             request=self.factory.post('/post/',data,format='json')
#             view=PostViewSet.as_view({'post':'create'})
#             response=view(request)
#             assert response.status_code==401

#         def test_creste(self):
#             user=User.objects.all()[0]
#             data={'title':'hihihi'}
#             request=self.factory.post('/posts/',data,format='json')
#             view=PostViewSet.as_view({'post':'create'})
#             response=view(request)
#             assert response.status_code==201
#             assert response.data['title']==data['title']
#             assert response.data['author']==user.id 
#             assert Post.objects.filter(author=user,title=data['title'].exists())

#         def test_update(self):
#             user=User.objects.all()[0]
#             data={'title':'HELLO HELLO'}
#             post=Post.objects.all()[2]
#             request=self.factory.patch(f'/posts/{post.id}',data,format='json')
#             force_authenticate(request,user)
#             view=PostViewSet.as_view({'patch':'partial_update'})
#             response=view(request,post.id)

#             assert response.status_code==200
        

#         def test_delete(self):
#             user=User.objects.all()[0]
#             post=Post.objects.all()[2]
#             request=self.factory.delete(f'/posts/{post.id}/')
#             force_authenticate(request,user)
#             view=PostViewSet.as_view({'delete':'destroy'})
#             response=view(request,pk=post.id)
#             assert response.status_code==204
#             assert  not  Post.objects.filter(id=post.id).exists()



