from app import db
from mongoengine.queryset import queryset_manager

class Story(db.Document):
    title          = db.StringField(required = True)
    url            = db.StringField()
    points         = db.StringField()
    comments       = db.StringField()
    short_url      = db.StringField()
    comments_url   = db.StringField()
    user_name      = db.StringField()
    since          = db.StringField()
    post_time = db.DateTimeField(required = True)
    #http://stackoverflow.com/questions/25466966/mongoengine-link-to-existing-collection
    meta = {
        'collection': 'news'
    }
    @queryset_manager
    def newest_posts(doc_cls, queryset, page = 1, stories_per_page = 20):
        start = (page - 1) * stories_per_page
        end = page * stories_per_page + 1
        return queryset.order_by('url')[start:end]
    def __repr__(self):
        return "<Story(%s,%s,%s)>" % (self.id, self.title, self.post_time)