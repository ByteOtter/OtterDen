# Copyright ByteOtter (c) 2023

import re
from flask import current_app, abort, flash
from flask_login import current_user
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
  search_string = query;
  is_user_query = re.search("\buser:[\S]+", query)
  only_with_images = re.search("\bimage:true", query)
  topic_filter = re.search("\btopic:[\S]+", query)

  if is_user_query:
    # is_user_query.group() returns the string "user:<username>". Split and take 2nd element <username>
    username = is_user_query.group().split(":")[1]
    user = User.query.filter_by(username=username)
    posts = Post.query.filter_by(author=username)
    return user, posts
