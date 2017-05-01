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
##### Request
```
GET /api/posts/post-slug/  
```
##### Response
```
{
    "url": "http://mendozadaniel.tk/api/posts/post-slug/",
    "id": 4,
    "user": {
        "username": "username"
    },
    "title": "title",
    "slug": "slug",
    "content": "content",
    "html": "html-markup-content",
    "publish": "2017-04-19",
    "image": null,
    "comments": [
        {
            "id": 1,
            "content_type": 8,
            "object_id": 1,
            "parent": null,
            "content": "This is a comment to the post.",
            "reply_count": 1,
            "timestamp": "2017-02-16T22:08:22.330982Z"
        }
    ]
}
```
##### Input values
```
url         : Post url
id          : Post id
user        : User owner
title       : Post title
content     : Post content
html        : Post content in html format
publish     : Publish Date, format YYYY-MM-DD
image       : Linked images
comments    : Array of comments
comments.id           : Comment id
comments.content_type : 
comments.object_id    : 
comments.parent       : The id of the parent comment, used for replying to a comment
comments.reply_count  : Number of replies to this particular comment
comments.timestamp    : Timestamp in UTC
```

#### Edit a post   
##### Request
```
POST /api/posts/post-slug/edit/ 
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

#### Delete a post   
##### Request
```
POST /api/posts/post-slug/delete/ 
```
##### Response
```
```
##### Input values
```
```

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
