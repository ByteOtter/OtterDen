# Copyright ByteOtter (c) 2023

import re
from otter_den import db
from otter_den.models import Post, User

"""
1. get search phrase by excluding image:true and user:<username> blocks from search string
2. [x] match if there is a block called user:<username> or image:true or topic:<topic>
3. if is_user_query: return the user aswell as all posts from that user which contain the search string
4. if only_with_images retrurn only the users posts with images
5. if topic, filter returned posts by topic
"""
def search_db(query):
  print("Your original query:" + query)
  is_user_query = re.search("\buser:[\S]+", query)
  only_with_images = re.search("\bimage:true", query)
  topic_filter = re.search("\btopic:[\S]+", query)
  # get the searchphrase itself without the flags to compare to posts if there are any flags that is
  if is_user_query | only_with_images | topic_filter:
    search_phrase = re.sub()
  else:
    search_phrase = query

  if not is_user_query and not only_with_images and not topic_filter:
    posts = Post.query()
    results = []
    for post in posts:
      if search_phrase in post.content:
        results.append(post)
      elif search_phrase in post.title:
        results.append(post)
  elif is_user_query:
    # is_user_query.group() returns the string "user:<username>". Split and take 2nd element <username>
    username = is_user_query.group().split(":")[1]
    user = User.query.filter_by(username=username)
    posts = Post.query.filter_by(author=username)
    return user, posts
