# blog

Stack: Django/Python/Postgres

## Introduction
This blog is designed for only one user, the superuser, to write about their daily thoughts and/or events. 

Other users can create an account so that they can comment on various blog posts.

## REST API Functionality
### Posts API
| Resource                                  | Description            |
| ----------------------------------------- |:----------------------:|
| GET /api/posts/                           | Retrieve all posts     |
| POST /api/posts/create/                   | Create a post          |
| GET /api/posts/post-slug/                 | View a particular post |
| POST /api/posts/post-slug/edit/           | Edit a post            |
| POST /api/posts/post-slug/delete/         | Delete a post          |

#### Retreive all posts
##### Request
```
GET /api/posts/
```
##### Response
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "url/api/posts/post-slug/",
            "user": {
                "username": "username"
            },
            "title": "Title",
            "content": "This is content to the post.",
            "publish": "2017-04-19"
        }]
}
```
##### Return values
```
count   : The number of total posts
next    : The next page
previous: The previous page
results : A list containing on the posts
url     : Post url
user    : User owner
title   : Post Title
content : Post Content
publish : Publish Date, format YYYY-MM-DD
```

#### Create a post  
##### Request
```
POST /api/posts/create/ 
```
##### Response
```
```
##### Input values
```
title   : Post Title
content : Post Content
publish : Publish Date, format MM-DD-YYYY
```

#### View a particular post

#### Edit a post  

#### Delete a post   

### Comments API
| Resource                                                         | Description               |
| --------------------------------------------------------------   |:-------------------------:|
| GET /api/comments/                                               | Retrieve all comments     |
| POST /api/comments/create/?type=post&slug=post-slug&parent_id=16 | Create a comment          |
| GET /api/comments/comment-id/                                    | View a particular comment |


### Retrieve all posts



#### To view a particular comment:
/api/comments/comment-id/
ex. /api/comments/26/
