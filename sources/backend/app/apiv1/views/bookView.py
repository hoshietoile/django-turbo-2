from rest_framework import serializers, views
from utils.decorators import handle_request

from apiv1.models.book import Book

request = handle_request(["books"])


class BookCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["title", "price"]


class BookRequestSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    price = serializers.IntegerField()


class BookView(views.APIView):
    @request(res=BookCreateSerializer(many=True))
    def get(self, request, *args, **kwargs):
        pass

    # TODO: passならNginxで404になりそうなので、そんな時はモックにリダイレクトするとか
    @request(req=BookCreateSerializer, res=BookCreateSerializer)
    def post(self, request, *args, **kwargs):
        pass
