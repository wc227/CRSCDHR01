import datetime
from haystack import indexes
from position.models import Position


class PostIndex(indexes.SearchIndex, indexes.Indexable):  # 类名必须为需要检索的Model_name+Index，这里需要检索Note，所以创建NoteIndex
    text = indexes.CharField(document=True, use_template=True)  # 创建一个text字段

    apply_type = indexes.CharField(model_attr='apply_type')  # 创建一个author字段

    # pub_date = indexes.DateTimeField(model_attr='pub_date')  # 创建一个pub_date字段

    def get_model(self):  # 重载get_model方法，必须要有！
        return Position

    def index_queryset(self, using=None):  # 重载index_..函数
        """Used when the entire index for model is updated."""
        return self.get_model().objects.filter(pub_date__lte=datetime.datetime.now())

