# blog

Stack: Django/Python/Postgres

## Introduction
This blog is designed for only one user, the superuser, to write about their daily thoughts and/or events. 

Other users can create an account so that they can comment on various blog posts.

## REST API Functionality
### Posts API
| Resource                                  | Description            |
| ----------------------------------------- |:----------------------:|
| GET  /api/posts/                          | Retrieve all posts     |
| GET  /api/posts/post-slug/                | View a particular post |
| POST /api/posts/create/                   | Create a post          |
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
results : A list containing all the posts
url     : Post url
user    : User owner
title   : Post Title
content : Post Content
publish : Publish Date, format YYYY-MM-DD
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
| GET  /api/comments/                                              | Retrieve all comments     |
| GET  /api/comments/comment-id/                                   | Comment Detail API        |
| POST /api/comments/create/?type=post&slug=post-slug&parent_id=16 | Create a comment          |


#### Retreive all comments
##### Request
```
GET /api/comments/
```
##### Response
```
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "url": "http://mendozadaniel.tk/api/comments/2/",
            "id": 2,
            "content": "It's even more awesome that you can reply to a comment, that creates it's own thread.",
            "reply_count": 0,
            "timestamp": "2017-02-16T22:09:11.589818Z"
        },
        {
            "url": "http://mendozadaniel.tk/api/comments/1/",
            "id": 1,
            "content": "That's awesome that you can style your post.",
            "reply_count": 1,
            "timestamp": "2017-02-16T22:08:22.330982Z"
        }]
}
```
##### Return values
```
count               : The number of total comments
next                : The next page of comments
previous            : The previous page of comments
results             : A list containing all the comments
results.url         : Post url
results.id          : Comment id
results.content     : Comment content
results.reply_count : Replies to that particular comment
results.timestamp   : Timestamp in UTC
```

#### Comment Detail API
##### Request
```
GET /api/comments/comment-id/ 
ex. /api/comments/1/ 
```
##### Response
```
{
    "id": 1,
    "user": {
        "username": "username"
    },
    "content": "That's awesome that you can style your post.",
    "timestamp": "2017-02-16T22:08:22.330982Z",
    "reply_count": 1,
    "replies": [
        {
            "id": 2,
            "user": {
                "username": "username"
            },
            "content": "It's even more awesome that you can reply to a comment, that creates it's own thread.",
            "timestamp": "2017-02-16T22:09:11.589818Z"
        }
    ],
    "content_object_url": "/api/posts/title-what-can-this-blog-do/"
}
```
##### Return values
```
id                 : Comment ID
user.username      : The user who posted the comment
content            : Comment content
timestamp          : Comment timestamp in UTC
reply count        : Number of replies to that particular comment
replies            : An array of all the comment replies
replies.id         : Comment reply id
replies.user       : Comment reply owner
replies.content    : Comment reply content
replies.timestamp  : Comment reply timestamp
content_object_url : The post url this comment belongs to
```

#### Create a comment
##### Request
```
POST /api/comments/create/?type=post&slug=post-slug&parent_id=16
```
##### Response
```
```
##### Return values
```
type      : post
slug      : post slug
parent_id : post id it belongs to
```
